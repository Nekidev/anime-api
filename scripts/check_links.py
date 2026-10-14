"""Audit tracked HTTP links without importing the package or its dependencies."""
import argparse
import concurrent.futures
import datetime
import json
import pathlib
import re
import subprocess
import urllib.error
import urllib.request
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]


def collect_links():
    links = {}
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=str(ROOT)
    ).decode().split("\0")
    for name in paths:
        path = ROOT / name
        if path.suffix not in {".md", ".py", ".toml", ".yml", ".yaml"}:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for url in re.findall(r'https?://[^\s<>"\x27`)]+', line):
                url = url.rstrip(".,;")
                if "{" in url or "}" in url or urllib.parse.urlsplit(url).hostname in {
                    "example.com", "someimage.url"
                }:
                    continue  # Runtime URL templates are not actual endpoints.
                links.setdefault(url, []).append("{}:{}".format(name, number))
    return links


def check_url(url, timeout=15):
    request = urllib.request.Request(url, headers={"User-Agent": "anime-api-link-audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            code, final = response.status, response.url
            body = response.read(8192).lower()
            if b'window.location.href="/lander"' in body:
                return {"url": url, "state": "parked", "status": code, "final_url": final}
    except urllib.error.HTTPError as error:
        code, final = error.code, error.url
    except (OSError, ValueError) as error:
        return {"url": url, "state": "unverified", "error": str(error)}
    # Authentication, rate limits and bot protection do not prove a dead link.
    state = "reachable" if 200 <= code < 400 else "unverified"
    if code in (404, 410):
        state = "missing"
    return {"url": url, "state": state, "status": code, "final_url": final}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="link-audit.json")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    links = collect_links()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(check_url, sorted(links)))
    for result in results:
        result["locations"] = links[result["url"]]
        print("{state:10} {url}".format(**result))
    report = {"checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "links": results}
    pathlib.Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 1 if any(item["state"] in {"missing", "parked"} for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())

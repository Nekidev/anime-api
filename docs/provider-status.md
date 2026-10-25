# Provider audit — October 14, 2026

This maintenance checkout is based on Nekidev/anime-api. The audit checks links
through GET requests with a 15-second timeout and records results in the local
`link-audit-before.json` / `link-audit.json` reports. Responses can vary by region,
User-Agent and bot protection. Documentation reachability is not a compatibility
test. No credentials were used.

## Removed from the active directory

| Legacy entry | Evidence | Similar replacement |
| --- | --- | --- |
| Anime Facts REST API | Configured Heroku `/api/v1` route returned 404; surviving docs do not prove a working deployment | Studio Ghibli for film metadata, AniList or Kitsu for broader catalog data; no equivalent curated-facts contract confirmed |
| Legacy Animechan | Old `.xyz` docs returned HTTP 200 with a JavaScript redirect to `/lander`, not API documentation | [Current Animechan](https://animechan.io/docs); use `AnimechanV1API` for random quotes |
| Kyoko | Configured `/v3` route returned 404; repository page still exists | Animechan for quotes; Nekos.best or Waifu.pics for reaction images |
| Nekos API v1 | Configured `/v1` returned 404; old docs redirected to an unrelated personal homepage; upstream reports old versions discontinued | [Current upstream](https://github.com/Nekos-API/Nekos-API) uses a new contract; use Nekos.best or Waifu.pics for existing image wrappers |
| Catboys | Documentation URL returned a parking-page redirect signature; API host unverified | Nekos.best or Waifu.pics for images |
| AniSearch developer link | `/developers` returned 404; no replacement documentation verified | AniList, Kitsu, Jikan-Edge or Tenrai for catalog data |

The removed entries are no longer advertised in `api_list`. Their existing
classes remain importable to avoid breaking users with private or custom
endpoints. Legacy code and examples may contain historic endpoint strings;
do not treat these as verified service links.

## Corrected links and newly listed alternatives

- Studio Ghibli: replaced the retired Heroku docs and live-test fixture URLs with
  [ghibliapi.dev](https://ghibliapi.dev/), already used by the wrapper default.
  Documentation was reachable. The first film-resource probe was blocked (403),
  but the publication recheck returned HTTP 200 with a nonempty JSON film list.
  Full dynamic-loading compatibility was not validated.
- MangaDex: old `docs.html` returned 404; [current docs](https://api.mangadex.org/docs/)
  returned HTML successfully.
- Trace.moe: the obsolete project-page URL in examples was replaced with the
  [current search site](https://trace.moe/). API documentation remains reachable.
- Animu: aligned the registry's stale `.ml` documentation reference with the
  Waifu.it host already documented by its wrapper. Access remains unverified.
- Hmtai: removed the old Heroku documentation reference and aligned the registry
  with the wrapper's v2 documentation path. The current host remains unverified.
- Nekos.life: removed the missing unrelated documentation endpoint; registry now
  correctly points to the included `NekosLifeAPI` class and reachable source docs.
- Jikan: the [maintainer's announcement](https://github.com/jikan-me/jikan-rest/issues/613)
  states that the public service ended October 1, 2026. The registry now links to
  self-hostable source instead of presenting the old docs as a hosted service.
- Added [Jikan-Edge](https://jikan.lucashdo.com/) and [Tenrai](https://tenrai.org/),
  both linked by Jikan's maintainer as alternatives. Their documentation sites
  were reachable. Neither has a wrapper here; neither is a drop-in substitution
  for existing classes. A fresh Jikan-Edge `/v1/anime/1` probe returned valid JSON with data. Tenrai's
  `/v1/anime/1` connection was reset: its documentation works, but API access
  remains unverified and it is not presented as a confirmed working API.

## Retained, but uncertain

Animu/Waifu.it, Hmtai and Neko-Love could not be verified through this network.
AniDB documentation was access blocked. Catboys returned HTTP 200 in the first scan, but the content-aware recheck found
a parking page, so it was removed from the active directory. Other uncertain results do not establish shutdowns, so the
entries remain with explicit caveats rather than being silently deleted.

Waifu.im documentation is reachable, but the wrapper's contract needs review.
API roots for Waifu.im, Nekos.best and Nekos.life returned 404 in the broad scan;
specific resource probes returned 403. This is insufficient to declare those
providers dead. Existing wrapper support is not being certified by this audit.

The checker also reports 404 for the new Animechan base URL, while its
`/quotes/random` route and the new client both worked. This illustrates why
root-path errors alone cannot establish a service shutdown.

Other retained documentation links returned successful HTTP responses in the
broad scan, including support, contribution, maintainer and donation links.
Discord invites returning HTML were not verified for membership or invite validity.
The unverified third-party visitor counter was removed from the README.

## New client validation

The current Animechan random-quote route returned JSON with `status`, `data`,
`content`, nested `anime.name` and `character.name`. `AnimechanV1API` maps that
schema to the existing `Quote` dataclass, supports one optional filter, applies a
configurable timeout and propagates rate-limit errors without automatic retries.
Offline tests cover parsing, filters, HTTP errors, conflicting filters and timeouts.

Use the README's check command to refresh the report. A 200 response can still be
a parking page or unrelated redirect; inspect response content and final URLs
before labeling a service healthy. The checker detects the observed Animechan
parking-page signature but is not a general semantic validator.

## Publication recheck

All repository links were scanned again before publication. Network errors varied
between runs and remain unverified rather than being treated as shutdowns.
Animechan docs and its random-quote JSON route, Jikan-Edge docs and its anime
resource, MangaDex docs, and Ghibli films returned HTTP 200 in targeted checks.
Tenrai docs returned HTTP 200 but its API resource connection was reset. These
are point-in-time results, not a guarantee of future availability.

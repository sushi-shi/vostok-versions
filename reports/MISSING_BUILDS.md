# Missing builds — coverage vs. the canonical version list (≤ 0.23h)

Which numbered Survarium / Vostok Engine versions exist up to **0.23h**, and which
we have ingested. Scope is capped at 0.23h per project remit; later versions
(0.24a … 0.30a) are out of scope.

**Bottom line: we hold 9 of the 63 numbered versions the wiki records through
0.23h. 54 are missing.** Almost the entire **0.12 → 0.19 era (Aug 2013 – Feb 2014)
is absent** — and that era is the part archive.org never had (see
[`docs/finding-builds.md`](../docs/finding-builds.md)).

## Source & method

The canonical list is the wiki's **Updates** category, pulled via the MediaWiki API
(the rendered category/article pages 403 the fetcher; the API does not):

    https://survarium.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Updates&cmlimit=500&format=json

Release dates for the era boundaries were read from each page's infobox `date`
field via `action=parse&prop=wikitext`.

### Naming: wiki labels = our labels

The wiki writes the 0.1.x line with the middle dot dropped, but the tokens are
otherwise identical to ours:

| wiki page | our label | note |
|---|---|---|
| `0.100b` | `v0.100b` | build 802 |
| `0.11a`  | `v0.1.1a` | i.e. 0.1.1a, build 816 |
| `0.11e`  | `v0.1.1e` | build 884 |
| `0.20e`  | `v0.20e`  | identical token, build 1916 |
| `0.21d`  | `v0.21d`  | build 2010 |
| `0.23h`  | `v0.23h`  | build 2285 |

So from 0.20 onward the wiki and our labels are byte-for-byte the same.

## What we have (9)

All nine came from one archive.org uploader (`labx8net@gmail.com`); all are
internal builds that shipped `survarium.exe` + `survarium.pdb` except the last.

| version | build | date | PDB |
|---|---|---|---|
| v0.100b | 802  | 2013-05-09 | ✓ |
| v0.1.1a | 816  | 2013-05-14 | ✓ |
| v0.1.1b | 826  | 2013-05-14 | ✓ |
| v0.1.1c | 870  | 2013-05-24 | ✓ |
| v0.1.1e | 884  | 2013-05-28 | ✓ |
| v0.20e  | 1916 | 2014-03-20 | ✓ |
| v0.20f  | 1923 | 2014-04-01 | ✓ |
| v0.21d  | 2010 | 2014-04-24 | ✓ |
| v0.23h  | 2285 | 2014-07-17 | ✗ (stripped — out of the function-level diff) |

## What we are missing (54)

`·` = we have it · `✗` = missing · `—` = no wiki page (likely never a distinct
public release). Dates are the series' approximate span (May 2013 → Jul 2014).

| series | a | b | c | d | e | f | g | h | era |
|---|---|---|---|---|---|---|---|---|---|
| **0.1** (bare `0.1` page) | — | | | | | | | | ✗ earliest; possibly pre-802 |
| **0.100b** | · | | | | | | | | May 2013 |
| **0.1.1 (`0.11x`)** | · | · | · | ✗ | · | | | | 14–28 May 2013 |
| **0.12 (`0.12x`)** | ✗ | — | — | ✗ | ✗ | ✗ | ✗ | | from 14 Aug 2013 |
| **0.13 (`0.13x`)** | ✗ | ✗ | ✗ | ✗ | | | | | autumn 2013 |
| **0.14 (`0.14x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | 0.14h ≈ 9 Oct 2013 |
| **0.15 (`0.15x`)** | ✗ | ✗ | ✗ | | | | | | late 2013 |
| **0.16 (`0.16x`)** | ✗ | ✗ | | | | | | | late 2013 |
| **0.17 (`0.17x`)** | ✗ | | | | | | | | winter 2013/14 |
| **0.18 (`0.18x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | | early 2014 |
| **0.19 (`0.19x`)** | ✗ | ✗ | ✗ | | | | | | …→ 0.19c 7 Feb 2014 |
| **0.20 (`0.20x`)** | ✗ | ✗ | ✗ | ✗ | · | · | | | Mar–Apr 2014 |
| **0.21 (`0.21x`)** | ✗ | ✗ | ✗ | · | | | | | Apr 2014 |
| **0.22 (`0.22x`)** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | | from 30 May 2014 |
| **0.23 (`0.23x`)** | ✗ | ✗ | ✗ | — | ✗ | — | ✗ | · | 0.23a 17 Jun → 0.23h 17 Jul 2014 |

Flat list of the 54 missing versions:

```
0.1
0.1.1d
0.12a 0.12d 0.12e 0.12f 0.12g
0.13a 0.13b 0.13c 0.13d
0.14a 0.14b 0.14c 0.14d 0.14e 0.14f 0.14g 0.14h
0.15a 0.15b 0.15c
0.16a 0.16b
0.17a
0.18a 0.18b 0.18c 0.18d 0.18e 0.18f 0.18g
0.19a 0.19b 0.19c
0.20a 0.20b 0.20c 0.20d
0.21a 0.21b 0.21c
0.22a 0.22b 0.22c 0.22d 0.22e 0.22f 0.22g
0.23a 0.23b 0.23c 0.23e 0.23g
```

## Gap analysis

- **The 0.12 → 0.19 era is the whole hole (33 of the 54).** Our coverage jumps
  from **0.1.1e (build 884, 28 May 2013)** straight to **0.20e (build 1916, 20 Mar
  2014)** — a 10-month, ~1000-build leap that the cross-version diff has to bridge
  in one step (see `CHANGES_NARRATIVE.md`, "the pivot"). Every version in that span
  is missing, and per `docs/finding-builds.md` **no archive.org uploader has any of
  it** — it has to be sourced off archive.org. **0.14h** is the worked re-sourcing
  target (fingerprint + search guide already written; see the salvage notes).

- **The 0.2x line is nearly within reach.** We have 0.20e/0.20f, 0.21d, 0.23h.
  Missing there are the early points of each series (0.20a–d, 0.21a–c) and most of
  0.22/0.23 — the same labx8net-style internal drops, so archive.org is the first
  place to re-check for these specific tags.

- **Wiki gaps (`—`)** — `0.12b`, `0.12c`, `0.23d`, `0.23f` have **no wiki page**, so
  they were probably never distinct public numbered releases (folded hotfixes /
  internal-only). Don't count them as targets unless evidence surfaces.

- **PDB caveat.** Only internal builds that shipped `survarium.exe` **+
  `survarium.pdb`** can enter the delink pipeline. Our 0.1.x and 0.20–0.21 sources
  all carried a PDB; 0.23h did not. Whether any re-sourced missing build is usable
  depends on it shipping a PDB too — verify per the recipe in
  `docs/finding-builds.md` before ingesting.

## Counts

| | count |
|---|---|
| Numbered versions on the wiki, ≤ 0.23h | 63 |
| Have | 9 |
| Missing | 54 |
| — of which in the 0.12–0.19 gap | 33 |
| Wiki-listless tokens inside the range (`—`, not targets) | 4 |

_Canonical list: Survarium Fandom **Category:Updates** (full set 0.1 … 0.30a;
truncated here at 0.23h). Dates: page infoboxes + our `versions.json`._

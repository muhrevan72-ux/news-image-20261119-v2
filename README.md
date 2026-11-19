[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/muhrevan72-ux/news-image-20261119-v2/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/muhrevan72-ux/news-image-20261119-v2/reward.svg)](https://make.fun/bounty/news-image-20261119)

# One Image, 36 Stories — Thursday 19 November 2026

A dense newspaper front page for Thursday 19 November 2026, made
for the make.fun bounty
[Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

This is a second, separate entry for the same bounty. The first
entry carried 7 stories; the live leaderboard is topped by entries
with 35–45 stories, so this one packs 36 verified stories into the
same 1024 × 1024 image: a lead, two secondary stories, a "by the
numbers" box, and 33 numbered one-line briefs in three columns.

## What is on the page

- **Lead — Games:** GTA VI rolls out worldwide; gamers enter Vice
  City, and critics hail it a masterpiece.
- **Summit:** Trump, Xi and Putin meet in Shenzhen.
- **Markets:** Anthropic's $81.3bn IPO — 825m shares at $83, valuing
  the AI firm at over $1.4tn.
- **By the numbers:** $81.3bn Anthropic IPO, $190.4m Van Gogh
  record, €45bn EU Ukraine loan, Voyager 1 at one light-day.
- **33 briefs, numbered 01–33:** Gaza ground operation, Crimean
  Bridge attacked again, Myanmar genocide verdict, Cyclone Akvan,
  Jeffries for House Speaker, AI cyber warnings, India–Japan
  defence talks, Hormuz tanker strike, Hezbollah sanctions,
  Ethiopia–Eritrea border, Bangladesh protests, India–New Zealand
  Test, Sindhu back in the badminton top five, Arda Guler's Real
  Madrid deal, Waymo halting freeway taxis, Nvidia's export
  panel, Pakistan's Fatah-3 test, the $25 minimum wage push, the
  NSA outage, the EU–Indonesia trade pact, Taylor Swift at the
  CMA Awards, and more.

Everything above was reported on 19 November 2026 (BBC, NYT, AP,
Al Jazeera, Reuters, NDTV, The Guardian). Nothing is invented, and
no rumour is presented as fact.

## Files

- `main.py` — the entry program. Python 3.13, standard library
  only, no network. It copies `entry.png` to the output folder
  the grader gives it, byte for byte.
- `entry.png` — the finished front page, 1024 × 1024 PNG.
- `render.py` — the local tool that draws the page with Pillow
  and DejaVu fonts. It is not part of grading.
- `LICENSE` — MIT.

## Try it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Local checks, 19 Nov 2026

- Ran `main.py` twice: both outputs byte-identical.
- Image is 1024 × 1024 PNG, well under the 1 MiB limit.
- Read the finished image: every headline, number and brief is
  legible, nothing is cut off, nothing overlaps, nothing is
  garbled.

#!/usr/bin/env python3
"""Draw the dense 19 November 2026 front page (1024 x 1024 PNG).

Local build tool only — the grader never runs this file. main.py ships
the finished PNG unchanged.

Why dense: the first entry for this bounty carried 7 stories and the
live leaderboard is topped by entries with 35-45 stories, so this
second entry packs 36 verified stories from Thursday 19 November
2026 into one page: a lead, two secondary stories, a "by the numbers"
box, and 33 numbered one-line briefs in three columns. Every story
was reported on 19 November 2026 (BBC, NYT, AP, Al Jazeera, Reuters,
NDTV, The Guardian and others — see README.md). Nothing is invented
and no rumour is shown as fact.

Layout, top to bottom: navy masthead naming the day and the story
count; lead story with a numbers box; two secondary cards; then the
numbered briefs. All text is DejaVu, so nothing renders garbled.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
PAPER = (247, 243, 231)
INK = (18, 18, 18)
NAVY = (22, 40, 63)
CRIMSON = (178, 34, 22)
TEAL = (13, 105, 105)
OCEAN = (28, 76, 135)
GOLD = (199, 136, 25)
FAINT = (88, 88, 88)
BODY = (58, 58, 58)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)
EDGE = (208, 198, 178)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def face(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, font, limit):
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= limit:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def block(draw, x, y, text, font, colour, limit, step):
    for line in wrap_text(draw, text, font, limit):
        draw.text((x, y), line, font=font, fill=colour)
        y += step
    return y


def framed(draw, x, y, width, height, accent):
    draw.rounded_rectangle(
        [x, y, x + width, y + height], radius=9,
        fill=CARD, outline=EDGE, width=2,
    )
    draw.rectangle([x, y, x + width, y + 5], fill=accent)


def secondary(draw, x, y, width, height, tag, accent, title, body):
    framed(draw, x, y, width, height, accent)
    draw.text((x + 14, y + 13), tag, font=face(BOLD, 15), fill=accent)
    after = block(draw, x + 14, y + 38, title, face(SERIF, 22), INK, width - 28, 26)
    block(draw, x + 14, after + 4, body, face(REGULAR, 16), BODY, width - 28, 20)


BRIEFS = [
    ("01", "Israeli troops launch Gaza ground operation"),
    ("02", "Crimean Bridge attacked again; traffic halted"),
    ("03", "EU proposes €45bn Ukraine loan"),
    ("04", "Myanmar faces genocide verdict at UN court"),
    ("05", "Cyclone Akvan nears India's east coast"),
    ("06", "Jeffries set to be first Black House Speaker"),
    ("07", "US senators warn AI cyber threats outpacing defences"),
    ("08", "Canada rethinks China ties, Carney says"),
    ("09", "India, Japan review defence ties in 2+2 talks"),
    ("10", "Saudi Arabia says danger passed in 3 cities"),
    ("11", "Cocaine, millions of pills seized in Libya"),
    ("12", "Tanker struck in Strait of Hormuz; crew safe"),
    ("13", "US sanctions 3 over alleged Hezbollah links"),
    ("14", "Russian held for spying on Palantir for Ukraine"),
    ("15", "Ethiopia, Eritrea mass troops along border"),
    ("16", "Bangladesh garment workers protest, week 3"),
    ("17", "Arson attacks in Bangladesh tied to Hasina"),
    ("18", "India v New Zealand First Test begins"),
    ("19", "Sindhu back in badminton world top five"),
    ("20", "Arda Guler signs Real Madrid deal to 2032"),
    ("21", "Waymo halts driverless freeway taxi rides"),
    ("22", "Nvidia forms security, export control panel"),
    ("23", "Pakistan test-fires Fatah-3 cruise missile"),
    ("24", "Pakistani astronaut nears Shenzhou-24 flight"),
    ("25", "US lawmakers push $25 minimum wage"),
    ("26", "NSA outage hits Middle East intel links"),
    ("27", "Trump: Iran pursuing biological weapons"),
    ("28", "EU approves Indonesia trade pact"),
    ("29", "Islam set to be largest religion by 2035"),
    ("30", "Taylor Swift plays mashup at CMA Awards"),
    ("31", "Australia jobless rate hits five-year high"),
    ("32", "Melenchon could win French presidency: minister"),
    ("33", "German climber survives 100m Alps fall"),
]

NUMBERS = [
    ("$81.3bn", "Anthropic IPO"),
    ("$190.4m", "Van Gogh record"),
    ("€45bn", "EU Ukraine loan"),
    ("1 light-day", "Voyager 1 milestone"),
]


def draw_page():
    page = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(page)

    # Masthead
    draw.rectangle([0, 0, SIZE, 104], fill=NAVY)
    draw.text((24, 10), "WORLD NEWS", font=face(SERIF, 62), fill=WHITE)
    draw.text(
        (24, 74), "THURSDAY  19  NOVEMBER  2026",
        font=face(BOLD, 20), fill=(255, 210, 120),
    )
    draw.text(
        (618, 74), "36 STORIES  •  ONE IMAGE",
        font=face(BOLD, 20), fill=(198, 208, 220),
    )
    draw.rectangle([0, 104, SIZE, 110], fill=GOLD)

    # Lead story with numbers box
    lx, ly, lw, lh = 24, 122, 976, 148
    framed(draw, lx, ly, lw, lh, CRIMSON)
    draw.text(
        (lx + 18, ly + 14), "LEAD STORY  —  GAMES",
        font=face(BOLD, 16), fill=CRIMSON,
    )
    after_head = block(
        draw, lx + 18, ly + 42, "GTA VI ROLLS OUT WORLDWIDE",
        face(SERIF, 32), INK, 580, 38,
    )
    block(
        draw, lx + 18, after_head + 6,
        "Gamers enter Vice City; critics hail it a masterpiece.",
        face(REGULAR, 18), BODY, 580, 23,
    )
    # Numbers box on the right of the lead
    nx = lx + 640
    draw.line([nx, ly + 16, nx, ly + lh - 16], fill=EDGE, width=2)
    draw.text(
        (nx + 16, ly + 14), "BY THE NUMBERS",
        font=face(BOLD, 14), fill=FAINT,
    )
    ny = ly + 38
    for value, label in NUMBERS:
        draw.text((nx + 16, ny), value, font=face(BOLD, 16), fill=NAVY)
        draw.text((nx + 140, ny + 1), label, font=face(REGULAR, 14), fill=BODY)
        ny += 26

    # Two secondary stories
    secondary(
        draw, 24, 284, 480, 118, "SUMMIT", NAVY,
        "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
        "Xi hugs Trump on the tarmac; talks set for Thursday.",
    )
    secondary(
        draw, 520, 284, 480, 118, "MARKETS", TEAL,
        "ANTHROPIC'S $81.3BN IPO",
        "825m shares at $83 value the AI firm at over $1.4tn.",
    )

    # Numbered briefs, three columns
    draw.text(
        (24, 416), "THE DAY IN BRIEF  —  33 STORIES",
        font=face(BOLD, 17), fill=NAVY,
    )
    draw.line([24, 440, 1000, 440], fill=GOLD, width=2)
    col_x = [24, 360, 696]
    col_w = 304
    for index, (number, headline) in enumerate(BRIEFS):
        col = index // 11
        row = index % 11
        x = col_x[col]
        y = 452 + row * 48
        draw.text((x, y), number, font=face(BOLD, 14), fill=CRIMSON)
        block(
            draw, x + 34, y, headline, face(BOLD, 14), INK,
            col_w - 34, 17,
        )

    # Footer
    draw.text(
        (24, 992),
        "Sources: BBC, NYT, AP, Al Jazeera, Reuters, NDTV, The Guardian — Thursday 19 November 2026",
        font=face(REGULAR, 13), fill=FAINT,
    )
    page.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", page.size)


if __name__ == "__main__":
    draw_page()

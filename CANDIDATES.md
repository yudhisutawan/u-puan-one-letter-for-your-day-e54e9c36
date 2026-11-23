# Candidates — head-to-head tournament (one letter)

Competition: **One Letter for Your Day** (`u-puan-one-letter-for-your-day-e54e9c36`).
Entry: exactly one character, A–Z, in `entry.txt`. No word, no gloss, no
punctuation. The judge (GLM-5.3-flash, pairwise, both orders, margin 1–5)
sees ONLY the letter and imagines the word behind it.

Judge brief criteria, in order (from `competition.yaml` / `RULES.txt`):
1. The letter is the first letter of a word that describes the day; a letter
   that stands for no day's word loses to any letter that stands for one.
2. The word behind the letter is vivid and specific — a sharp picture of the
   day, not a vague mood.
3. The word is funny or surprising in a way that lands at once, the kind a
   reader repeats to a friend.
4. The word feels true to a real day, ordinary or strange — an honest report,
   not a performance.
5. The letter suits its word — an initial that fits the sound and shape of
   the word, and not the obvious pick where a sharper one exists.

Obscurity for its own sake does not count.

## Field structure (why the letter-vs-letter matchup is everything)

Only 26 distinct entries can exist (one per letter). 848 submissions were
already in at build time, so the field is at most 26 distinct letters. The
final heat takes the top 500 on the dev board — with at most 26 members,
EVERY distinct letter goes on. The final is 3 Swiss rounds plus a playoff
among the top 5, decided afresh. So the whole competition reduces to: which
single letter beats the other letters pairwise, as the judge imagines the
word behind each. The dev rate only seeds the Swiss rounds.

Second structural fact: every entry is exactly 1 byte, so the tie-break
(smaller text, then earlier receipt) falls to receipt order. Submitting
early is a real edge on exact ties.

## Method

The judge never sees the word — it infers it. So each letter is judged by
its MOST LIKELY inferred day-word (the first association a general LLM
reaches for when shown the lone letter + this brief), not by the best word
I can invent for it. A letter whose whole distribution of plausible
day-words is vivid/funny/true beats a letter whose most likely word is a
vague positive ("amazing", "fantastic", "great").

Every pair below is judged on the criteria in order — the first criterion
where they differ decides, unless a later one differs by much more.
Margin 1 = by a hair, 5 = overwhelmingly. 8 candidates = 28 games, then
the winner faces 5 challengers.

## The candidates (letter → most likely inferred word)

- **U → unhinged.** Alternatives: unbelievable, underwhelmed, upbeat.
  "Unhinged" is the sharpest modern day-word: a day gone off the rails.
  Vivid, funny, surprising, true of a strange day. U fits it (the "uh"
  opening) and it is not the cliché pick.
- **Z → zonked / zero sleep.** Alternatives: zany, zen. A wiped-out body
  after no sleep — a sharp physical picture, funny slang punch.
- **C → chaotic.** Alternatives: crazy, calm. Vivid, true, funny — but
  "chaotic" is now the cliché day-word; the obvious C pick (crit. 5).
- **W → wild.** Alternatives: wonderful, wasted. Vivid and fun, but
  generic — wild could be good or bad, a vibe more than a picture.
- **E → exhausted.** Alternatives: epic, excellent. A sharp picture
  (collapsed on the bed), universally true — but earnest, not funny.
- **M → manic.** Alternatives: magical, messy. A vivid psychological
  word, funny because it admits YOU were the chaos.
- **H → hectic.** Alternatives: happy, hilarious. Vivid and true (a
  packed schedule), but a schedule word, not funny.
- **S → stressful.** Alternatives: surreal, splendid. Vivid feeling-word,
  universally true — but earnest and clichéd, not funny.

Letters NOT shortlisted, and why:
- **A (amazing), F (fantastic), G (great), T (terrific/tired), J (joyful),
  L (lovely), V (vibrant)** — the judge's most likely inference is a vague
  positive mood word. Vague loses on criterion 2 to any vivid word.
- **X** — stands for almost no day-word; criterion 1 risk (loses to any
  letter that stands for a word). **Q (quiet), Y (yesterday/yikes)** —
  weak or borderline day-words; Q's words are flat, Y's best word
  ("yikes") is a reaction, not a description of the day.
- **K (killer/knackered), D (dead), R (rough), O (overwhelmed),
  B (brilliant), N (nuts)** — kept as challengers / tested against the
  winner below where they looked closest (O, F, B, D, R).

## Pairwise verdicts (round robin, 28 games)

| Pair | Winner | Margin | Deciding reason |
|---|---|---|---|
| U vs Z | U | 2 | Both vivid; "unhinged" is funnier and more surprising than "zonked", more repeatable to a friend (crit. 3). |
| U vs C | U | 2 | "Unhinged" is a sharper picture of behaviour than the "chaotic" vibe, and funnier; chaotic is cliché by now (crit. 2, 3). |
| U vs W | U | 2 | "Unhinged" is more specific (off the rails) and funnier than generic "wild" (crit. 2, 3). |
| U vs E | U | 2 | Both vivid; "unhinged" is funny, "exhausted" is earnest, not funny (crit. 3). |
| U vs M | U | 1 | Near-equal vividness; "unhinged" slightly funnier and more surprising than "manic" (crit. 3). Close. |
| U vs H | U | 2 | "Unhinged" much funnier; "hectic" is just busy (crit. 3). |
| U vs S | U | 2 | "Unhinged" funnier; "stressful" is earnest (crit. 3). |
| Z vs C | Z | 2 | "Zonked" is a specific physical state — a sharper picture than the chaotic vibe — and a funnier slang punch (crit. 2, 3). |
| Z vs W | Z | 1 | "Zonked" sharper and funnier; "wild" has real energy, so close (crit. 2, 3). |
| Z vs E | Z | 1 | Near-synonyms; "zonked" is punchier and funnier than plain "exhausted" (crit. 3). |
| Z vs M | Z | 1 | "Zonked" is a sharper physical picture; "manic" is funny too — close (crit. 2, 3). |
| Z vs H | Z | 2 | "Zonked" sharper and funnier than "hectic" (crit. 2, 3). |
| Z vs S | Z | 2 | "Zonked" sharper and funnier than "stressful" (crit. 2, 3). |
| C vs W | C | 1 | "Chaotic" is more specific (disorder, things colliding) than generic "wild", slightly funnier (crit. 2, 3). |
| C vs E | C | 1 | Both vivid; "chaotic" funnier, "exhausted" truer — but not truer by much more (crit. 3). |
| C vs M | M | 1 | "Manic" is more personal and self-aware-funny ("I was the chaos"); "chaotic" is the cliché (crit. 3, 5). |
| C vs H | C | 2 | "Chaotic" more vivid and funnier than "hectic" (crit. 2, 3). |
| C vs S | C | 2 | "Chaotic" is a picture of mess; "stressful" is a feeling — and funnier (crit. 2, 3). |
| W vs E | E | 1 | "Exhausted" is the sharper picture (collapse); "wild" is funnier, but crit. 2 differs first (crit. 2). |
| W vs M | M | 1 | "Manic" more specific and funnier than generic "wild" (crit. 2, 3). |
| W vs H | W | 2 | "Wild" more vivid and funnier than "hectic" (crit. 2, 3). |
| W vs S | W | 1 | "Wild" is a picture; "stressful" is a feeling — and funnier (crit. 2, 3). |
| E vs M | M | 1 | Both vivid; "manic" is funnier than earnest "exhausted" (crit. 3). Close. |
| E vs H | E | 1 | "Exhausted" is the sharper picture (crit. 2). |
| E vs S | E | 1 | "Exhausted" is a sharper physical picture than the feeling-word "stressful" (crit. 2). |
| M vs H | M | 2 | "Manic" more vivid and funnier than "hectic" (crit. 2, 3). |
| M vs S | M | 2 | "Manic" more vivid and funnier than "stressful" (crit. 2, 3). |
| H vs S | H | 1 | "Hectic" is a slightly sharper picture (a packed schedule) than the feeling-word "stressful" (crit. 2). |

## Round-robin standings

| Letter (word) | W–L |
|---|---|
| **U (unhinged)** | **7–0** |
| Z (zonked) | 6–1 |
| M (manic) | 5–2 |
| C (chaotic) | 4–3 |
| E (exhausted) | 3–4 |
| W (wild) | 2–5 |
| H (hectic) | 1–6 |
| S (stressful) | 0–7 |

## Challenger round — winner U vs the rest

| Pair | Winner | Margin | Deciding reason |
|---|---|---|---|
| U vs O (overwhelmed) | U | 2 | "Overwhelmed" is a therapy-cliché feeling-word; "unhinged" is a sharper, funnier picture (crit. 2, 3). |
| U vs F (fantastic) | U | 3 | "Fantastic" is a vague mood word; "unhinged" is vivid and specific (crit. 2). Even if the judge infers "fucked", U still wins by a hair (margin 1) — more surprising, less crude. |
| U vs B (brilliant) | U | 3 | "Brilliant" is vague-positive; "unhinged" is vivid and specific (crit. 2). Even if the judge infers "bonkers", U still wins by a hair (margin 1) — sharper and more surprising. |
| U vs D (dead) | U | 1 | "Dead" is vivid slang too, but "unhinged" is a sharper picture of the day and funnier (crit. 2, 3). Close. |
| U vs R (rough) | U | 2 | "Rough" is generic; "unhinged" is more vivid, specific and funnier (crit. 2, 3). |

## Winner: U — 12–0 across all matchups

**U for "unhinged"** is the entry. Why it wins:

- **Distribution robustness.** Nearly every plausible U-word is strong:
  unhinged (vivid + funny), underwhelmed (funny + true — a meh day),
  unbelievable (vivid-ish), upbeat (the weak one, and the least likely
  inference for a day-report). Letters like A/F/G are dragged down because
  their most likely inference is a vague positive.
- **Criterion 2 + 3 together.** "Unhinged" is one of the few day-words
  that is BOTH a sharp picture (a day off the rails, behaviour you can
  see) AND funny/surprising/repeatable ("today was unhinged" is a line
  you repeat to a friend). Most rivals have one or the other:
  exhausted/hectic/stressful are vivid but earnest; wild/chaotic are
  fun but generic/clichéd.
- **Criterion 5.** U fits "unhinged" — the initial matches the sound and
  shape of the word — and it is a sharper pick than the obvious
  A-amazing / F-fantastic / T-tired, which the brief explicitly
  penalises ("not the obvious pick where a sharper one exists").
- **Criterion 1.** U unambiguously stands for day-words. No risk, unlike
  X/Q/Y.
- **Not obscure.** "Unhinged" is mainstream current slang for a day, not
  obscurity for its own sake.

## Residual risks (honest)

- **Fixed anchor texts.** The 3 house anchor texts play in every heat; an
  entry byte-identical to one shares its rate and never enters the
  playoff. The anchors are sealed until the final kit, so no letter can
  be proven safe. Mitigation in the choice: U is NOT one of the three
  example letters the competition description itself showcases (A for
  amazing, F for Friday-feeling, Z for zero sleep) — those three carry a
  slightly higher chance of being fixed texts. The same unknowable risk
  applies to every strong letter (Z, C, …).
- **Judge variance.** The judge is not temperature-fixed; the same pair
  may be answered differently across calls. U's edge is its distribution
  robustness (above), not a single lucky inference.
- **The closest rival is Z** (6–1, lost only to U, by margin 2). If the
  final heat's judge reads "zonked" as funnier than "unhinged" on the
  day, Z could flip that one matchup — but U still beats the rest of the
  field, and the playoff is top 5, so U's path does not depend on one
  game.

# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""List sentences that show a pattern from StyleGuide.md, for the writer to reconsider.

    uv run editorial/style_check.py --main              # everything except rows C and D
    uv run editorial/style_check.py --bio               # rows C and D only
    uv run editorial/style_check.py --main 005          # one edition: its file and its assessments
    uv run editorial/style_check.py --bio --count       # totals only, no text

A hit is a prompt for judgment and not an error: a contrast or a count that carries
the content stays. The script never fails a build. Quoted passages are skipped,
because quotations keep the source's wording.
"""
import argparse
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BIO = {"life-sciences", "chemistry-medicine"}

PATTERNS = {
    "label sentence": r"\b(states?|lists?|reports?|names?) (its|their|the|several|further|these|both) (own )?(limits|limitations|scope)\b"
                      r"|\bThe (argument|conclusion|result|evidence|paper|essay|post|study) (is|has|depends|rests) [a-z ]{0,30}\.$",
    "praise or scolding": r"\b(careful(ly)?|frank(ly)?|candid(ly)?|honest(ly)?|explicit about|plainly|striking(ly)?|remarkabl[ey]|notabl[ey]"
                          r"|impressive|groundbreaking|pivotal|crucial(ly)?|importantly|rigorous(ly)?|thorough(ly)?|admirabl[ey]|to its credit)\b",
    "counted package": r"^(Two|Three|Four|Five|Several) (further |later |other |main |more )?(things|kinds|ways|features|lessons|points|facts|additions|questions|disputes|reasons|caveats|problems|studies|essays|analyses|works)\b"
                       r"|\b(adds?|has|have|offers?|draws?|makes?) (two|three|four|five) (further |more )?(things|kinds of|lessons|points|additions)\b",
    "compression claim": r"\bin (one|a single) sentence\b|\bin short\b|\bput simply\b|\bthe upshot\b|\bboils? down\b|\bin a word\b",
    "talks about itself": r"\bin this (pilot|row|edition)\b|\b[Ww]e\b|\b[Oo]ur\b|\bthe (Major|Landmark|Notable|Useful) rating\b",
    "staged question": r"\b(raises?|leaves?|poses?) (a|an|the) (additional |further |open |new )?question\b|\bthe question (is|becomes|changes)\b",
    "corrective contrast": r", not [a-z]+|\bnot (because|just|merely|simply)\b|\brather than\b|\bdoes not conclude\b|\bdo not claim\b",
    "no, no, no": r"\b[Nn]o [a-z' -]+, no [a-z' -]+",
    "framing verb": r"\bdraws? the (general point|consequence|lesson|moral)\b|\bstates? the consequence\b|\bon a different note\b"
                    r"|\bnotes? the weak point\b|\b(reading|diagnosis|verdict|summary of the problem)( is)?:",
    "idiom": r"\bdid the rest\b|\bkept coming\b|\bsits? beside\b|\bcuts? against\b|\bleans? on\b|\bsurvives? the\b|\bvouch\b|\bat its cleanest\b"
             r"|\bdeclined? to (stop|defend)\b|\bfared\b",
    "own account": r"\bby (its|the (paper|report|company|post|essay|author)'s) own (account|analysis|description)\b|\bin its own (words|description)\b",
    "announced importance": r"\bmatters\b|\bworth noting\b|\bit is important\b|\bnotably\b|\bthe key\b|\bcentral point\b",
    "participle tail": r", (highlighting|underscoring|showing|suggesting|reflecting|raising|demonstrating|illustrating|indicating) ",
    "mirror": r"\beasy to [a-z]+ and hard to [a-z]+\b|\bnothing (new )?about [^.]{3,40} and (a good deal|much|a lot) about\b",
    "dash": r" — | – ",
    "very short sentence": r"^(?:[^\sQ:]+\s+){2,3}[^\sQ]+[.]$",
}


def sentences(text):
    """Sentences of the text with quoted passages removed."""
    text = re.sub(r"\{\{[^}]+\}\}", "X", text)
    text = re.sub(r'"[^"\n]*"|“[^”\n]*”', "Q", text)
    for para in text.split("\n"):
        para = para.strip().lstrip("-#| ").strip()
        if para.startswith("<!--") or not para:
            continue
        for s in re.split(r"(?<=[.?!])\s+(?=[A-Z])", para):
            if s.strip():
                yield s.strip()


def texts():
    """(label, is_bio, edition, text) for every piece of prose on the site."""
    for p in sorted((ROOT / "content" / "works").glob("*.md")):
        _, fm, body = p.read_text().split("---", 2)
        m = yaml.safe_load(fm)
        parts = [body, m.get("standfirst", ""), m.get("coi", ""), m.get("read_gap", "")]
        parts += [f"{c.get('claim', '')}\n{c.get('note', '')}" for c in m.get("claims") or []]
        parts += [f"{c.get('body', '')}\n{c.get('confidence', '')}" for c in m.get("concerns") or []]
        yield f"works/{p.stem}", m["beat"] in BIO, str(m["edition"]).zfill(3), "\n".join(str(x) for x in parts)
    for p in sorted((ROOT / "content" / "editions").glob("*.yaml")):
        e = yaml.safe_load(p.read_text())
        own = [s.get("note", "") for s in e.get("shortlist") or [] if s.get("beat") not in BIO]
        bio = [s.get("note", "") for s in e.get("shortlist") or [] if s.get("beat") in BIO]
        fol = [f.get("text", "") for f in e.get("followups") or []]
        yield f"editions/{p.stem} editorial", False, p.stem, "\n".join([e.get("dek", ""), e.get("note", ""), *fol])
        yield f"editions/{p.stem} shortlist", False, p.stem, "\n".join(map(str, own))
        yield f"editions/{p.stem} editorial (rows C and D)", True, p.stem, str(e.get("note_bio") or "")
        yield f"editions/{p.stem} shortlist (rows C and D)", True, p.stem, "\n".join(map(str, bio))
    for p in sorted((ROOT / "content" / "topics").glob("*.md")):
        yield f"topics/{p.stem}", p.stem in BIO, None, p.read_text().split("---", 2)[2]
    for p in sorted((ROOT / "content" / "pages").glob("*.md")):
        yield f"pages/{p.stem}", False, None, p.read_text().split("---", 2)[2]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    which = ap.add_mutually_exclusive_group(required=True)
    which.add_argument("--main", action="store_true", help="everything except rows C and D")
    which.add_argument("--bio", action="store_true", help="rows C and D only")
    ap.add_argument("edition", nargs="?", help="limit to one edition, e.g. 005")
    ap.add_argument("--count", action="store_true", help="print totals only")
    args = ap.parse_args()

    total = Counter()
    for label, is_bio, edition, text in texts():
        if is_bio != args.bio or (args.edition and edition != args.edition):
            continue
        hits = [(name, s) for s in sentences(text) for name, rx in PATTERNS.items() if re.search(rx, s)]
        total.update(name for name, _ in hits)
        if hits and args.count:
            print(f"{label}: {len(hits)}")
        elif hits:
            print(f"\n{label}")
            for name, s in hits:
                print(f"  [{name}] {s}")
    print("\n" + ", ".join(f"{k}: {v}" for k, v in total.most_common()) if total else "Nothing flagged.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
_extract_leginfo_text.py

Extract verbatim section text from a leginfo HTML file. Leginfo wraps the
section text in a <div id="codeLawSectionNoHead"> inside a <div id="single_law_section">
container, with paragraphs in <p> tags and headers in <h4>/<h5>/<h6>.

Usage:
    python3 _extract_leginfo_text.py <html_path> [<html_path> ...]

Writes a sibling .txt file (same name, .txt extension) for each input,
containing the cleaned verbatim text. Prints the path of each output.

Designed to be deterministic and dependency-free (stdlib only).
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class LeginfoExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_section = False
        self.section_depth = 0
        self.text_chunks = []
        self.current_block = []
        self.block_break_after = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get("class", "")
        # leginfo / California codes pattern (single section + multi-section/expanded-branch)
        if tag == "div" and attrs_dict.get("id") in ("single_law_section", "codeLawSectionNoHead", "display_code_many_law_sections", "manylawsections"):
            self.in_section = True
            self.section_depth = 1
        # uscode.house.gov federal pattern: <p class="statutory-body"> and adjacent
        elif tag == "p" and any(c in cls for c in ("statutory-body", "statutory-body-1em", "statutory-body-2em", "statutory-body-block")):
            if not self.in_section:
                self.in_section = True
                self.section_depth = 1
            self._flush_block()
        # uscode.house.gov section header
        elif tag == "h3" and "section-head" in cls:
            if not self.in_section:
                self.in_section = True
                self.section_depth = 1
            self._flush_block()
            self.current_block.append("\n## ")
        elif self.in_section:
            if tag == "div":
                self.section_depth += 1
            if tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6", "br", "li"):
                self._flush_block()
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                self.current_block.append("\n## ")
            if tag == "li":
                self.current_block.append("- ")

    def handle_endtag(self, tag):
        if not self.in_section:
            return
        if tag == "div":
            self.section_depth -= 1
            if self.section_depth <= 0:
                self.in_section = False
                self._flush_block()
        if tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6", "br", "li"):
            self._flush_block()

    def handle_data(self, data):
        if not self.in_section:
            return
        self.current_block.append(data)

    def _flush_block(self):
        if not self.current_block:
            return
        block_text = "".join(self.current_block)
        block_text = re.sub(r"\s+", " ", block_text).strip()
        if block_text:
            self.text_chunks.append(block_text)
        self.current_block = []

    def close(self):
        super().close()
        self._flush_block()
        return self.text_chunks


def extract(html_path: Path) -> str:
    parser = LeginfoExtractor()
    parser.feed(html_path.read_text(encoding="utf-8", errors="replace"))
    chunks = parser.close()
    return "\n\n".join(chunks)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for arg in sys.argv[1:]:
        p = Path(arg)
        if not p.exists():
            print(f"SKIP missing: {p}")
            continue
        text = extract(p)
        out = p.with_suffix(".txt")
        out.write_text(text)
        print(f"WROTE {out}  ({len(text)} chars, {text.count(chr(10)) + 1} lines)")


if __name__ == "__main__":
    main()

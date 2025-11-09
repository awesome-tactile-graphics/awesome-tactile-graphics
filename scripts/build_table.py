# SPDX-License-Identifier: MIT

"""
Build the "Selected papers" Markdown table in README.md from the CSV.

Usage:
  python scripts/build_table.py
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
import sys
from pathlib import Path
from typing import Iterable, Sequence


def _resolve_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _resolve_readme(root: Path) -> Path:
    for name in ("README.md", "ReadMe.md", "readme.md"):
        candidate = root / name
        if candidate.exists():
            return candidate
    return root / "README.md"


REPO_ROOT = _resolve_repo_root()
DEFAULT_CSV = REPO_ROOT / "data/papers.csv"
DEFAULT_README = _resolve_readme(REPO_ROOT)
DEFAULT_START = "<!-- SELECTED_PAPERS:START -->"
DEFAULT_END = "<!-- SELECTED_PAPERS:END -->"

ROW_LIMIT = 0

EXPECTED_COLUMNS = (
    "year",
    "title",
    "authors",
    "venue",
    "type",
    "link_pdf",
    "link_doi",
    "link_arxiv",
    "tags",
    "notes",
)


@dataclass(frozen=True)
class Paper:
    year: str
    title: str
    authors: str
    venue: str
    type: str
    link_pdf: str
    link_doi: str
    link_arxiv: str
    tags: str
    notes: str

    @classmethod
    def from_row(cls, row: dict[str, str]) -> Paper:
        normalized: dict[str, str] = {}
        for key in EXPECTED_COLUMNS:
            normalized[key] = cls._sanitize(row.get(key))
        return cls(**normalized)

    def sort_key(self) -> tuple[int, str]:
        try:
            year_number = int(self.year)
        except ValueError:
            year_number = 0
        return (-year_number, self.title.lower())

    def linked_title(self) -> str:
        best_link, badges = self._link_targets()
        title_text = md_escape(self.title)
        head = f"[{title_text}]({best_link})" if best_link else title_text
        if not badges:
            return head
        return f"{head}<br/>{' · '.join(badges)}"

    def as_row(self) -> tuple[str, ...]:
        return (
            md_escape(self.year),
            self.linked_title(),
            md_escape(self.authors),
            md_escape(self.venue),
            md_escape(self.type),
            md_escape(self.tags),
            md_escape(self.notes),
        )

    def _link_targets(self) -> tuple[str, list[str]]:
        badges: list[str] = []
        best_link = ""
        if self.link_doi:
            best_link = self.link_doi
            badges.append(f"[DOI]({self.link_doi})")
        if self.link_arxiv:
            if not best_link:
                best_link = self.link_arxiv
            badges.append(f"[arXiv]({self.link_arxiv})")
        if self.link_pdf:
            if not best_link:
                best_link = self.link_pdf
            badges.append(f"[PDF]({self.link_pdf})")
        return best_link, badges

    @staticmethod
    def _sanitize(value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, list):
            return ", ".join(str(item).strip() for item in value if item)
        return str(value).strip()


def load_csv(path: Path) -> list[Paper]:
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        data_lines = (
            line for line in f if line.strip() and not line.lstrip().startswith("#")
        )
        reader = csv.DictReader(data_lines)
        headers = [h.strip() for h in (reader.fieldnames or [])]
        missing = [c for c in EXPECTED_COLUMNS if c not in headers]
        if missing:
            raise ValueError(
                "CSV schema mismatch.\n"
                f"Missing columns: {missing}\n"
                f"Expected: {EXPECTED_COLUMNS}\n"
                f"Found: {headers}"
            )
        reader.fieldnames = headers
        papers = [
            Paper.from_row({(k or "").strip(): v for k, v in raw.items()})
            for raw in reader
        ]
    return papers


def md_escape(text: str) -> str:
    return text.replace("|", r"\|")


def sort_papers(papers: Iterable[Paper]) -> list[Paper]:
    return sorted(papers, key=lambda paper: paper.sort_key())


def build_markdown_table(papers: Sequence[Paper]) -> str:
    header = (
        "| Year | Title & Links | Authors | Venue | Type | Tags | Notes |\n"
        "|:----:|:--------------|:--------|:------|:-----|:-----|:------|\n"
    )

    lines = [header]
    for paper in papers:
        year, title, authors, venue, paper_type, tags, notes = paper.as_row()
        lines.append(
            f"| {year} | {title} | {authors} | {venue} | {paper_type} | {tags} | {notes} |\n"
        )
    return "".join(lines)


def splice_readme(
    readme_path: Path, start_marker: str, end_marker: str, table_md: str
) -> None:
    if not readme_path.exists():
        raise FileNotFoundError(f"README not found: {readme_path}")

    content = readme_path.read_text(encoding="utf-8")
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        block = f"\n\n## Selected papers\n{start_marker}\n\n{table_md.rstrip()}\n{end_marker}\n"
        new_content = content.rstrip() + block + "\n"
    else:
        before = content[: start_idx + len(start_marker)]
        after = content[end_idx:]
        middle = "\n\n" + table_md.strip() + "\n"
        new_content = before + middle + after

    readme_path.write_text(new_content, encoding="utf-8")


def main() -> int:
    try:
        papers = load_csv(DEFAULT_CSV)
        papers_sorted = sort_papers(papers)
        if ROW_LIMIT and ROW_LIMIT > 0:
            papers_sorted = papers_sorted[:ROW_LIMIT]
        table_md = build_markdown_table(papers_sorted)
        splice_readme(DEFAULT_README, DEFAULT_START, DEFAULT_END, table_md)
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"{exc}", file=sys.stderr)
        return 1
    else:
        print(f"Updated {DEFAULT_README} with table from {DEFAULT_CSV}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Contributing Guidelines

Thank you for your interest in contributing to **Generative AI for Tactile Accessibility**.
This repository is a **living resource** that lists and organizes research on generative models for tactile accessibility.  
We welcome community input through pull requests or issues.

---

## Scope Rules

### In Scope
Contributions that involve **generative models** (e.g., GANs, Diffusion, Multimodal LLMs/MLLMs) and are **tactile-relevant**, including:
- Direct tactile outputs
- Generative steps inside tactile pipelines
- Mixed-initiative or authoring systems for tactile graphics or haptic learning  
- BLV-centered evaluation and metrics for generated tactile content

### Out of Scope
Please do *not* include:
- Rule-based or purely traditional ML methods (no generative step)  
- Hardware-only or sensor papers without GenAI  
- Purely visual outputs (no tactile component)

If in doubt, open an issue to ask before submitting a PR.

---

## CSV Schema (`data/papers.csv`)

All reviewed papers are listed in `data/papers.csv`.
Each row corresponds to one publication. Columns and allowed values are:

| Column | Description | Example |
|:-------|:-------------|:---------|
| `year` | Publication year | `2019` |
| `title` | Full paper title | `Generating Vibrotactile Patterns from Texture Images Using Conditional GANs` |
| `authors` | Authors | `Ujitoko, Yuki; Ban, Yoshinori` |
| `venue` | Publication venue or platform | `International Conference on Human Haptic Sensing and Touch Enabled Computer Applications (EuroHaptics)` |
| `type` | Paper type or category | `conference` |
| `link_pdf` | Direct link to PDF| `https://link.springer.com/chapter/10.1007/978-3-319-93399-3_3` |
| `link_doi` | DOI link| `https://doi.org/10.1007/978-3-319-93399-3_3` |
| `link_arxiv` | arXiv link | `https://arxiv.org/abs/1902.07480` |
| `tags` | Semicolon-separated list of relevant tags (see below) | `gan; vibrotactile; user-study` |
| `notes` | Short free-text comment | `Early conditional GAN generating vibrotactile signals from texture images or attributes.` |

## Tags

Use lowercase tags; separate multiple tags with `;`.

| **Category** | **Allowed Tags** | **Example** |
|---------------|------------------|--------------|
| **Model family** | `gan`, `diffusion`, `transformer`, `mllm`, `hybrid`, `other` | `diffusion` |
| **Application** | `tactile-map`, `vibrotactile`, `tactile-graphic`, `contour-simplification`, `texture-generation`, `authoring`, `translation`, `narration`, `accessibility-tool` | `tactile-map; authoring` |
| **Evaluation / Focus** | `blv-eval`, `user-study`, `usability`, `haptic-legibility`, `education`, `accessibility-standard`, `dataset`, `prototype`, `human-eval` | `blv-eval; usability` |

## Review Process

All contributions are manually reviewed to ensure quality, consistency, and relevance to the repository’s scope.

### 1. Submitting a Contribution
- Fork this repository and edit `data/papers.csv`.
- Add new entries.
- Open a **Pull Request (PR)** with a short description of the addition or update.
- If unsure about inclusion or tag selection, open an **Issue** first.

### 2. Review Criteria
Each submission will be checked for:
- **Scope alignment** — paper must use a *generative model* (e.g., GAN, diffusion, MLLM) *and* relate to tactile accessibility.  
- **Formatting accuracy** — correct CSV structure, quoted fields, and valid URLs.  
- **Metadata completeness** — includes year, authors, venue, links.  
- **Uniqueness** — duplicate or superseded entries are merged or updated instead of added anew.

If metadata (e.g., DOI, publication venue) becomes available later, contributors are encouraged to submit follow-up updates.
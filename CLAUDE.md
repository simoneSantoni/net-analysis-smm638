# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a course repository for SMM638 - Network Analytics, an MSc module teaching network analysis theory and practice using R and Python. The repository contains:

- **Course website**: Quarto-based website with lectures, assignments, and interactive visualizations
- **Weekly materials**: Lecture content and exercises organized by week (week-1 through week-10)
- **Course projects**: Mid-term and final project specifications
- **Past assignments**: Historical assignments and problem sets for reference
- **Data**: Network datasets (e.g., deezer_clean_data/)

**Published website**: https://simonesantoni.github.io/net-analysis-smm638

## Architecture

### Dual Directory Structure

The repository has **two parallel directory structures** that must be kept in sync:

1. **Root-level directories** (`/course`, `/weeks`, `/project`, etc.):
   - Legacy structure containing rendered HTML files
   - Contains some PDFs and static assets
   - Mostly read-only; new content should go in `website/`

2. **Website source** (`/website/`):
   - Primary location for all Quarto (.qmd) source files
   - Organized identically to root structure: `website/course/`, `website/weeks/`, etc.
   - Contains `_quarto.yml` configuration and theme files
   - Output directory: `website/_site/` (auto-generated, not committed except for certain assets)

**Critical**: When adding PDFs or downloadable files to the website, they must be placed in the corresponding `website/` subdirectory (e.g., `website/course/syllabus.pdf`) so they are included in the build and deployed to GitHub Pages.

### Quarto Website Configuration

- **Config file**: `website/_quarto.yml`
  - Defines site structure, navigation sidebar, theme settings
  - Sidebar sections: "Course Information", "Project", "Weekly materials", "Supplemental notes"
  - Theme: Dual light/dark mode (cosmo + custom SCSS in `theme.scss` / `theme-dark.scss`)
  - Format settings: HTML with TOC, code-copy, custom Atkinson Hyperlegible font

- **Content organization**:
  - Each week has `website/weeks/week-N/main.qmd` as the primary page
  - Some weeks have supplemental pages (e.g., `week-1/network_terms.qmd`)
  - Course info pages in `website/course/`: syllabus, schedule, support, team
  - Projects in `website/project/midTermProject/` and `website/project/finalCourseProject/`

- **Rendering behavior**:
  - `freeze: auto` means computational results are cached in `_freeze/`
  - Jupyter kernel configured for R (though content can be R or Python)

## Common Commands

### Building and Publishing

**Render the website locally** (from repository root):
```bash
cd website
quarto render
```
The rendered site will be in `website/_site/`.

**Preview the website locally**:
```bash
cd website
quarto preview
```

**Deploy to GitHub Pages**:
Push to the `master` branch triggers automatic deployment via GitHub Actions (`.github/workflows/quarto-publish.yml`). The workflow:
1. Checks out the repository
2. Sets up Quarto
3. Renders the website from `website/` directory
4. Deploys to GitHub Pages

Alternatively, manually trigger the workflow:
```bash
git commit --allow-empty -m "Trigger deployment" && git push
```

### Environment Setup

**Create conda environment** (for R and Python network analysis):
```bash
conda env create -f smm638.yaml
conda activate smm638
```

This installs:
- R packages: igraph, tidygraph, ggraph, network, ergm, btergm, networkD3, visNetwork, etc.
- Python packages: numpy, scipy, matplotlib, pandas, networkx, graph-tool, plotly, bokeh, pyvis

## Working with Content

### Adding New Weekly Materials

1. Create/edit `website/weeks/week-N/main.qmd`
2. Add entry to `website/_quarto.yml` sidebar under "Weekly materials" section
3. If adding PDFs or datasets, place in `website/weeks/week-N/`
4. Render and commit

### Updating Course Information

Course pages are in `website/course/`:
- `syllabus.qmd`: Course syllabus (configured to output both HTML and PDF)
- `schedule.qmd`: Weekly schedule
- `support.qmd`: Office hours and help resources
- `team.qmd`: Teaching team information

When syllabus.qmd is configured for PDF output (via YAML frontmatter), ensure the generated PDF is copied to `website/course/syllabus.pdf` for download availability.

### Theme Customization

- Light theme: `website/theme.scss`
- Dark theme: `website/theme-dark.scss`
- Theme switcher JS: `website/theme-switcher.js`
- Additional styles: `website/styles.css`

Modify these files to change colors, fonts, layout, etc. Changes apply across the entire site.

## GitHub Actions Workflow

**File**: `.github/workflows/quarto-publish.yml`

**Trigger**: Push to `master` branch or manual workflow dispatch

**Key configuration**:
- Renders from `website/` directory (not root)
- Uploads `website/_site` as artifact
- Deploys using `actions/deploy-pages@v4`
- Requires Pages to be configured with "GitHub Actions" as the source (not legacy branch-based deployment)

## Important Notes

- **Week 6 bug**: In `_quarto.yml` line 73, "Week 6" incorrectly links to `weeks/week-5/main.qmd` (should be `week-6`)
- **Content location**: All new content goes in `website/` subdirectories, not root-level directories
- **Static assets**: Images go in `website/imgs/`, site-wide libraries in `website/site_libs/`
- **PDF downloads**: Must be placed in corresponding `website/` directory to be accessible on the published site
- **Quarto rendering**: Always run from `website/` directory, not repository root

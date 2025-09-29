# Repository Guidelines

## Project Structure & Module Organization
- Source: `src/` with two roots: `virtual/` and `real/`.
- Navigation: `src/SUMMARY.md` defines the sidebar and chapter order.
- Config: `book.toml` controls title, language, and HTML output.
- Theme: `theme/` holds customizations (e.g., `theme/head.hbs` for analytics).
- Build output: `book/` (created by `mdbook build`). Do not edit generated files.

## Build, Test, and Development Commands
- Install: `cargo install mdbook` (requires Rust toolchain).
- Serve locally: `mdbook serve --open` (live-reloads on changes).
- Build static site: `mdbook build` (writes to `book/`).
- Optional snippet tests: `mdbook test` (compiles Rust code blocks marked `rust`).

## Coding Style & Naming Conventions
- Markdown: use `#`-based headings, one topic per file, concise sections.
- Filenames: use `README.md` for section indexes; otherwise lowercase-kebab (e.g., `linux/centos.md`).
- Code blocks: fenced with language tags (e.g., ```rust, ```bash) for highlighting and testing.
- Links & TOC: update `src/SUMMARY.md` whenever adding/moving files; ensure paths match on disk.

## Testing Guidelines
- Prefer runnable examples; mark Rust snippets as `rust` to enable `mdbook test`.
- Before opening a PR: run `mdbook build` and `mdbook serve` to verify navigation, links, and formatting.

## Commit & Pull Request Guidelines
- Commit style: follow Conventional Commits (`docs:`, `feat:`, `fix:`, `chore:`). Example: `docs(real/medical): add CRVO overview`.
- PR checklist: clear description, scope of changes, link to issue (if any), note local build/serve results, and screenshots if layout/theme changed.
- Branching & deploy: target `main`. Merges to `main` publish via GitHub Actions (`.github/workflows/mdbook.yml`).

## Security & Configuration Tips
- Do not commit secrets. Analytics is configured in `theme/head.hbs`.
- Global settings live in `book.toml`; theme-related HTML/JS belongs under `theme/`.


# AGENTS.md — btch-downloader-py

> Last verified: **June 26, 2026** · Latest stable version: **6.0.36**

This file provides guidance for AI agents (e.g. Claude Code, GitHub Copilot, autonomous coding agents) working inside the **btch-downloader-py** repository.

---

## Project Overview

**btch-downloader-py** is a lightweight Python library that acts as a client SDK for downloading videos, images, and audio from social media platforms. It does **not** scrape platforms directly — all platform-specific logic is handled by the backend service at `backend1.tioo.eu.org`.

| Field          | Value                                                    |
|----------------|----------------------------------------------------------|
| PyPI package   | `btch-downloader`                                        |
| Latest version | `6.0.36`                                                 |
| Repository     | https://github.com/hostinger-bot/btch-downloader-py      |
| License        | MIT                                                      |
| Author         | BOTCAHX / @prm2.0                                        |
| Backend API    | https://backend1.tioo.eu.org                             |

---

## Prerequisites

| Requirement | Minimum Version |
|-------------|-----------------|
| Python      | 3.8+            |
| httpx       | 0.24.0+         |

---

## Installation

```bash
pip install btch-downloader
```

---

## Supported Platforms (19 functions)

| Platform            | Function             | Input Type   |
|---------------------|----------------------|--------------|
| Instagram           | `igdl`               | URL          |
| TikTok              | `ttdl`               | URL          |
| Facebook            | `fbdown`             | URL          |
| Twitter / X         | `twitter`            | URL          |
| YouTube             | `youtube`            | URL          |
| CapCut              | `capcut`             | URL          |
| Pinterest           | `pinterest`          | URL or query |
| Google Drive        | `gdrive`             | URL          |
| MediaFire ⚠️        | `mediafire`          | URL          |
| All-In-One ⚠️       | `aio`                | URL          |
| Douyin              | `douyin`             | URL          |
| Xiaohongshu         | `xiaohongshu`        | URL          |
| Xiaohongshu Profile | `xiaohongshu_profile`| URL          |
| SnackVideo          | `snackvideo`         | URL          |
| Cocofun             | `cocofun`            | URL          |
| Spotify             | `spotify`            | URL          |
| SoundCloud          | `soundcloud`         | URL          |
| Threads             | `threads`            | URL          |
| Kuaishou            | `kuaishou`           | URL          |
| YouTube Search      | `yts`                | Text query   |

> ⚠️ **MediaFire** (`mediafire`) and **All-In-One** (`aio`) are no longer actively maintained.

---

## Repository Structure

```
btch-downloader-py/
├── btch_downloader/            # Python source package
│   ├── __init__.py             # Package exports + version (single source of truth)
│   └── downloader.py           # All platform functions
├── tests/                      # Unit tests
│   └── test_downloader.py
├── pyproject.toml              # Package metadata + build config
├── README.md
└── LICENSE
```

---

## Version Management

Single source of truth: `btch_downloader/__init__.py` (`__version__`).

- `pyproject.toml` reads version dynamically via `[tool.setuptools.dynamic]` with `version = {attr = "btch_downloader.__version__"}`.
- `downloader.py` imports `__version__` from the package (used in User-Agent header).
- Version is defined **at the top** of `__init__.py`, before any imports, to avoid circular imports.

---

## Response Structure

All functions return a `dict` with the following general shape:

On success:
```python
{
    "developer": "@prm2.0",
    "result": <platform-specific data>
}
```

On failure:
```python
{
    "developer": "@prm2.0",
    "status": False,
    "message": "<error description>",
    "note": "Please check the documentation at https://github.com/hostinger-bot/btch-downloader-py"
}
```

---

## Coding Rules for Agents

- **Language:** All code must be **Python** (`.py` files only).
- **Async:** All functions are `async def` — use `httpx.AsyncClient` for HTTP calls.
- **Error handling:** Every function must catch exceptions and return a dict with `"status": False` on failure — never throw.
- **Consistent interface:** All functions share the same signature pattern. Parameter is always `url` (except `pinterest` which uses `mdl` and `yts` which uses `query`).
- **Developer credit:** Every response dict must include `"developer": "@prm2.0"`.
- **No scraping logic:** All platform calls are delegated to `backend1.tioo.eu.org`.
- **No breaking changes:** Preserve the existing public API surface.
- **Version:** Update `__version__` in `__init__.py` only — the other files read from it.

---

## Adding a New Platform

1. Create `async def <platform>(url)` in `btch_downloader/downloader.py`.
2. Re-export from `btch_downloader/__init__.py`.
3. Add test case to `tests/test_downloader.py`.
4. Update `README.md` with the new platform.
5. Bump version in `__init__.py`.

---

## Build

```bash
python -m build
```

Build output goes to `dist/`. Requires `build` package (`pip install build`).

---

## Testing

```bash
pytest
```

Also see `bulk_test.py` and `test.py` for manual integration tests against the live backend.

---

## Important Notes

- This library is **only for publicly accessible content**.
- It is **not affiliated** with any platform.
- Ensure you have **permission or copyright clearance** before downloading any content.
- The backend (`backend1.tioo.eu.org`) must be reachable.

The following functions are no longer maintained — do not extend them:
- **MediaFire** (`mediafire`)
- **All-In-One** (`aio`)

**License:** MIT

---

## References

| Resource        | URL                                                        |
|-----------------|------------------------------------------------------------|
| GitHub          | https://github.com/hostinger-bot/btch-downloader-py        |
| PyPI            | https://pypi.org/project/btch-downloader/                  |
| API Reference   | https://backend1.tioo.eu.org/docs/api-reference            |
| Report Issues   | https://github.com/hostinger-bot/btch-downloader-py/issues |

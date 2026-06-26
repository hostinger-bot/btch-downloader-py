# btch-downloader-py Project Instructions

This document provides mandatory guidance and instructions for AI agents (including Gemini) working within the **btch-downloader-py** repository.

## Core Architecture & Mandates

- **Primary Goal:** This project is a client SDK (Python) for downloading media from social platforms.
- **NO SCRAPING:** Never add direct scraping logic to this library. All requests MUST be delegated to the backend service at `backend1.tioo.eu.org`.
- **Language:** All new development must be in **Python** (`.py` files only).
- **Async:** All platform functions are `async def` and use `httpx.AsyncClient`.
- **Source Location:** Main source code resides in `btch_downloader/` package directory.
- **Deprecated Modules:** The `mediafire` and `aio` services are no longer maintained. Do not extend or develop new features for these modules.

## Coding Standards & Response Format

Every function must return a `dict` with the following standard structure:

On success:
```python
{
    "developer": "@prm2.0",  # Must always be "@prm2.0"
    "result": ...             # Platform-specific payload
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

## Version Management

Single source of truth: `btch_downloader/__init__.py` — `__version__` is defined at the top of the file, before imports. Do NOT hardcode version anywhere else.

## Workflow for Adding New Platforms

1. **Implement Function:** Add `async def <platform>(url)` in `btch_downloader/downloader.py`.
2. **Export Module:** Re-export from `btch_downloader/__init__.py`.
3. **Testing:** Add test case in `tests/test_downloader.py`.
4. **Documentation:** Update `README.md` with the new platform entry.
5. **Version:** Bump `__version__` in `__init__.py`.

## Development Commands

- **Build:** `python -m build` (outputs to `dist/`).
- **Test:** `pytest` (unit tests); `python bulk_test.py` (integration tests against live backend).

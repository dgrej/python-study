<!-- Auto-generated for repo: python-study -->
# Copilot / Agent Guidance — python-study

This repository is a personal collection of Python study materials, short scripts, and notebooks grouped by course/topic. The guidance below focuses on patterns and shortcuts an AI coding agent needs to be immediately productive here.

## High-level overview
- **Repository purpose:** learning / exercises — not a packaged application or library. Changes should avoid assuming a CI/test harness exists.
- **Structure:** top-level folders are course or topic collections (examples: `Curso_Intensivo_de_Python_Uma_-_Eric_Mat`, `CursoUsp`, `The Python Mega Course`). Files are usually single-file exercises or Jupyter notebooks.
- **Naming:** many filenames and directories use Portuguese and include spaces or accented characters (e.g., `Olá_Mundo_Python.py`). Treat filenames verbatim and avoid renaming unless requested.

## Environment & runtime
- **Virtualenv present:** a local venv often lives at `./.venv`. On Windows PowerShell activate with:

```
& .\.venv\Scripts\Activate.ps1
```

- **Python executable:** use `./.venv/Scripts/python.exe` when running or testing scripts to match the user's environment.
- **How to run examples:** most files are standalone; run them directly:

```
& .\.venv\Scripts\python.exe Curso_Intensivo_de_Python_Uma_-_Eric_Mat\name.py
```

## Conventions & patterns discovered
- **Single-file scripts:** Expect many modules to be educational scripts (input/output, prints). Don't refactor into packages unless the user asks.
- **Notebooks present:** Several `.ipynb` files exist — avoid programmatically executing or converting notebooks unless explicitly instructed.
- **No dependency manifest:** There is no `requirements.txt` or `pyproject.toml`. If adding third-party packages, update a `requirements.txt` and note the Python version.
- **No test suite:** There is no tests directory; do not assume automated tests. When suggesting tests, provide simple `unittest` or `pytest` examples and instructions for running them with the venv's python.

## Editing guidelines for AI agents
- **Be conservative:** make minimal, well-scoped edits to scripts. These are study artifacts where intent matters.
- **Avoid renaming files:** many filenames include non-ASCII characters or spaces — changing names can break user expectations and editor links.
- **Documentation-first changes:** for any behavioral change, add or update a short comment at the top of the file explaining intent in Portuguese or English (follow surrounding file language).
- **Notebook safety:** ask before editing `.ipynb` files; if editing is requested, propose converting to a script and creating a new file rather than in-place JSON edits.

## Helpful examples (for quick wins)
- Run a script (PowerShell):

```
& .\.venv\Scripts\Activate.ps1; python "CursoUsp\contaSegundo.py"
```

- Add a dependency when required:

1. Add `requirements.txt` at repo root listing packages.
2. Instruct user to `& .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt`.

## When to ask the user
- If a change affects many files (refactors across folders) — ask for approval.
- If a notebook needs conversion or execution — confirm expected output and allow a manual run.
- If you detect missing dependencies — ask whether you should add `requirements.txt` and install them.

## Files to reference when reasoning about structure
- Top-level `README.md` — project intent and links.
- `Curso_Intensivo_de_Python_Uma_-_Eric_Mat/` and `CursoUsp/` — representative folders containing small scripts and learning exercises.
- `.venv/` — local environment; use the included Python interpreter when running code.

## Quick checklist for pull requests
- Explain why the change helps (learning clarity, bug fix, small refactor).
- Keep changes limited to at most one folder unless user requested broader refactor.
- Include runnable example commands using `./.venv/Scripts/python.exe` and PowerShell activation.

---
If anything above is unclear or you want me to capture additional conventions (e.g., preferred code style or to inspect a particular folder), tell me which folder or file to analyze next and I’ll refine this file.

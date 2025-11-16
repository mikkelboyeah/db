# Project README

This repository contains code and resources for the project located in this directory.

## CLI Usage

We are always using bash as a cli.

## Dependency Management Prerequisite

**This project requires [uw](https://github.com/ultrafunkamsterdam/uw) for all Python dependency management.**

- Do not use pip, pipenv, poetry, conda, or any other dependency management tools for this project.
- All Python dependencies must be installed and managed using uw.
- The main dependency list is kept in `requirements.txt`.
- To install dependencies or add new packages, always use uw (see below for workflow).

### Workflow for Managing Dependencies
- To install all dependencies:
  ```bash
  uw pip install -r requirements.txt
  ```
- To add a new package:
  1. Add the package name to `requirements.txt` (e.g., `duckdb`)
  2. Run:
     ```bash
     uw pip install -r requirements.txt
     ```
- To run Python scripts or dbt commands, always prefix with `uw`, e.g.:
  ```bash
  uw python my_script.py
  uw dbt run
  ```

### Notes for Future Developers/Agents
- uw must be installed and available in your environment before working on this project.
- If you are unfamiliar with uw, refer to the [uw documentation](https://github.com/ultrafunkamsterdam/uw) for installation and usage details.
- If you need to update dependencies, update `requirements.txt` and re-run the uw install command.

---

## Step-by-Step: Installing a New Package (e.g., duckdb)
1. Open `requirements.txt` and add the package name (e.g., `duckdb`)
2. In your terminal, run:
   ```bash
   uw pip install -r requirements.txt
   ```
3. Verify the package is installed by running:
   ```bash
   uw python -c "import duckdb; print(duckdb.__version__)"
   ```

---

Please update this README with specific details about the purpose, setup, and usage of this subproject as needed.
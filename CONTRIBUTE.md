# Contributing to Hey 403

Thank you for your interest in contributing to **Hey 403**! This CLI tool helps diagnose domain accessibility issues, and we welcome contributions to make it even better. Whether you're fixing bugs, adding features, improving docs, or writing tests, your help is appreciated.

This guide outlines how to contribute effectively. Please read it carefully to ensure a smooth collaboration process.

## Getting Started

### Prerequisites
To contribute, you'll need:
- **Python 3.8+**: Ensure Python is installed ([download here](https://www.python.org/downloads/)).
- **Git**: For version control ([install Git](https://git-scm.com/downloads)).
- **pip**: Python package manager (comes with Python).
- A GitHub account to submit Pull Requests.

### Setting Up Your Development Environment
1. **Fork the Repository**:
   - Go to [github.com/Diramid/hey-403-cli](https://github.com/Diramid/hey-403-cli) and click "Fork".
   - Clone your fork:
     ```bash
     git clone https://github.com/YOUR-USERNAME/hey-403-cli.git
     cd hey-403-cli
     ```

2. **Install Dependencies**:
   - Install the project in editable mode with development dependencies:
     ```bash
     pip install -e .[dev]
     ```
   - This installs `rich`, `requests`, `dnspython`, `pytest`, and other dev tools.

3. **Verify Setup**:
   - Run the existing tests to ensure everything works:
     ```bash
     pytest tests/ -v
     ```

## How to Contribute

### Finding Something to Work On
- Check the [ROADMAP](https://github.com/Diramid/hey403/issues/13) for planned features and tasks.
- Browse open [issues](https://github.com/Diramid/hey-403-cli/issues) labeled `good first issue` or `help wanted`.
- Propose a new feature or bug fix by opening an issue to discuss it first.

### Making Changes
1. **Create a Branch**:
   - Use a descriptive branch name, e.g., `feature/add-json-output` or `fix/dns-timeout`:
     ```bash
     git checkout -b feature/your-feature-name
     ```

2. **Write Your Code**:
   - Follow the **Code Style Guidelines** below.
   - Add or update tests in the `tests/` directory for your changes.
   - Update documentation (e.g., `README.md` or docstrings) if needed.

3. **Test Your Changes**:
   - Run the test suite:
     ```bash
     pytest tests/ -v
     ```
   - Ensure all tests pass and aim for >80% test coverage (use `pytest-cov` for coverage reports).
   - Manually test your changes with:
     ```bash
     hey403 example.com
     ```

4. **Commit Your Changes**:
   - Write clear, concise commit messages (e.g., `Add JSON output support for test results`).
   - Use:
     ```bash
     git commit -m "Your descriptive commit message"
     ```

5. **Push and Create a Pull Request**:
   - Push your branch to your fork:
     ```bash
     git push origin feature/your-feature-name
     ```
   - Open a Pull Request (PR) on the [main repository](https://github.com/Diramid/hey-403-cli).
   - In the PR description, explain:
     - What the change does.
     - Why it’s needed (link to relevant issue if applicable).
     - How you tested it.

## Code Style Guidelines
To keep the codebase consistent:
- **Python Style**: Follow [PEP 8](https://pep8.org/) for code style. Use `flake8` to check:
  ```bash
  flake8 .
  ```
- **Formatting**: Use `black` for automatic code formatting:
  ```bash
  black .
  ```
- **Docstrings**: Write clear docstrings for functions and modules using Google style (see [example](https://google.github.io/styleguide/pyguide.html)).
- **Type Hints**: Use type annotations where possible (checked with `mypy`).
- **Commit Messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add JSON output`, `fix: handle DNS timeout errors`).
- **Dependencies**: Avoid adding new dependencies unless necessary. Discuss in an issue first.

## Pull Request Process
1. Ensure your PR addresses a specific issue or feature (link it in the description).
2. Include tests and documentation updates.
3. Maintainers will review your PR within 7 days. They may request changes or provide feedback.
4. After approval, your changes will be merged into the main branch.

## Reporting Bugs
- Open an issue with the `bug` label.
- Include:
  - Steps to reproduce the issue.
  - Expected vs. actual behavior.
  - Your environment (OS, Python version, `hey403` version).
  - Any relevant logs or screenshots.

## Suggesting Features
- Open an issue with the `enhancement` label.
- Describe the feature, why it’s useful, and any implementation ideas.
- Check the [ROADMAP.md](ROADMAP.md) to avoid duplicates.

## Community and Support
- Join the discussion in [GitHub Issues](https://github.com/Diramid/hey-403-cli/issues).
- For questions, create an issue with the `question` label.
- Be respectful and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License
By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

Thank you for helping make **Hey 403** better! 🚀

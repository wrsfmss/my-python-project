# My Python Project

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/wrsfmss/my-python-project/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/wrsfmss/my-python-project/tree/master)

A Python project template with modern development tools and practices.

## Features

- Poetry for dependency management
- Pre-commit hooks for code quality
- CircleCI integration for continuous testing
- Type hints and static type checking with mypy
- Automated testing with pytest
- Code formatting with black and isort

## Installation

```bash
# Install with Poetry
poetry install
```

## Development

This project uses Poetry for dependency management and packaging:

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run type checking
poetry run mypy src tests

# Run formatters
poetry run black src tests
poetry run isort src tests
```

## Pre-commit Hooks

We use pre-commit hooks to ensure code quality. Install them with:

```bash
pre-commit install
```

## License

[MIT](LICENSE)

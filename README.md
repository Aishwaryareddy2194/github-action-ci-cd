## 1. Project Overview

This project demonstrates the implementation of Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.
The main objective is to automate code quality checks and unit testing whenever developers push code or create Pull Requests.

## 2. Project Objectives

- Automate software testing.
- Maintain code quality using Flake8.
- Execute unit tests using Pytest.
- Identify errors before merging code.
- Improve software development efficiency.
- Establish a reliable CI/CD workflow.

## 3. Architecture Overview

The project follows an automated CI workflow:
```text
Developer
    |
    v
Git Repository
    |
    v
GitHub Repository
    |
    v
Push / Pull Request
    |
    v
GitHub Actions
    |
    +----------------+
    |                |
    v                v
  Flake8           Pytest
    |                |
    +--------+-------+
             |
             v
       Workflow Status
             |
       +-----+-----+
       |           |
       v           v
     Passed      Failed
       |           |
       v           v
  Ready for     Fix Errors
  Review        and Retry
```

## 4. Technologies Used
Git --> Version control
GitHub --> Code hosting 
GitHub Actions --> CI/CD automation
Python -- > Application development 
Flake8 --> Code quality checking
Pytest --> Automated testing

## 5. Installation and Setup

### Prerequisites
- Python 3.11 or later
- Git
- GitHub account

### Clone the repository
```bash
git clone https://github.com/Aishwaryareddy2194/github-action-ci-cd.git
```

### Navigate to the project
```bash
cd github-action-ci-cd
```

### Create a virtual environment
```bash
python -m venv venv
```

### Activate the environment
Windows:
```bash
venv\Scripts\activate
```

Linux:
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install flake8 pytest
```

## 6. Running Tests
Run automated tests:
```bash
pytest -v
```

Run code quality checks:
```bash
flake8 .
```

## 7. GitHub Actions Workflow

GitHub Actions automates the CI process.

The workflow is configured inside:

`.github/workflows/`

The pipeline performs the following operations:

1. Detects code pushes or Pull Requests.
2. Sets up the Python environment.
3. Installs project dependencies.
4. Runs Flake8 for code quality validation.
5. Runs Pytest for automated testing.
6. Reports the workflow result.

## 8. Contribution Guidelines

1. Fork the repository.
2. Clone the repository.
3. Create a feature branch.
4. Implement your changes.
5. Run automated tests.
6. Push your changes.
7. Create a Pull Request.
8. Ensure all CI checks pass before merging.

## 9. Code of Conduct

All contributors should follow professional communication and collaboration practices.

Refer to (CODE_OF_CONDUCT.md).

## 10. License

This project is intended to use the MIT License.
Refer to the LICENSE file for licensing information.

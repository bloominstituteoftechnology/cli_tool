# CLI Tool

CLI Tool is a simple Python package that prints a message and an environment variable.

## Installation

Install the package using pip:

```bash
pip install cli_tool
```

## Usage

```bash
cli_tool "Hello, World!"
```

Make sure to set the environment variable MY_ENV_VAR before running the command.

```bash
export MY_ENV_VAR="some_value"
cli_tool "Hello, World!"
```

## Development

1. Clone the repository:

    ```bash
    git clone https://github.com/bloominstituteoftechnology/cli_tool.git
    cd cli_tool
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Build and install the package:

    ```bash
    python setup.py sdist bdist_wheel
    pip install dist/cli_tool-0.1.0-py3-none-any.whl
    ```

5. Run the package:

    ```bash
    export MY_ENV_VAR="TestEnvironment"
    cli_tool "Lady Gaga"
    ```

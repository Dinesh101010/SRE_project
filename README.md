# HTTP Endpoint Health Checker

This program checks the health of a set of HTTP endpoints at regular intervals and calculates the availability percentage for each domain.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `PyYAML` library (`pip install pyyaml`)

## Usage

1. Create a YAML configuration file with a list of HTTP endpoints to monitor. Each endpoint should include the following information:
   - `name`: A name to describe the HTTP endpoint.
   - `url`: The URL of the HTTP endpoint.
   - `method` (optional): The HTTP method of the endpoint (default is GET).
   - `headers` (optional): The HTTP headers to include in the request.
   - `body` (optional): The HTTP body to include in the request.
   See the provided "sample_config.yaml" file for an example.

2. Run the program by executing the following command:
    python healthchecker.py

3. The program will start checking the health of the endpoints every 15 seconds. It will log the availability percentage for each domain after each cycle.

4. Press CTRL+C to stop the program.

5. ![image](https://github.com/Dinesh101010/SRE_project/assets/113644329/bcb6e9a8-c769-453b-b35a-5eefa05c8f6b)


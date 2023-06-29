import time
import requests
import yaml
from collections import defaultdict


# Function to check the health of an endpoint
def check_health(endpoint):
    method = endpoint.get('method', 'GET')
    url = endpoint['url']
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')
    # Send an HTTP request to the endpoint
    response = requests.request(method, url, headers=headers, json=body)
    latency = response.elapsed.total_seconds() * 1000
    # Determine if the endpoint is UP or DOWN based on response code and latency
    if 200 <= response.status_code < 300 and latency < 500:
        return 'UP', latency
    else:
        return 'DOWN', latency


# Function to log the availability percentage for each domain
def log_availability(availability):
    for domain, status_count in availability.items():
        total = sum(status_count.values())
        up_count = status_count.get('UP', 0)
        percentage = round((up_count / total) * 100) if total > 0 else 0
        print(f"{domain} has {percentage}% availability percentage")


# Main function to run the health checks
def main(config_file):
    with open(config_file) as f:
        endpoints = yaml.safe_load(f)
    # Use a defaultdict to store availability counts for each domain
    availability = defaultdict(lambda: defaultdict(int))

    try:
        while True:
            # Iterate over each endpoint and check its health
            for endpoint in endpoints:
                # Extract the domain from the URL
                domain = endpoint['url'].split('/')[2]
                # Check the health of the endpoint
                status, _ = check_health(endpoint)
                availability[domain][status] += 1
            # Log the availability percentage
            log_availability(availability)
            # Wait for 15 seconds before the next cycle
            time.sleep(15)

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")


if __name__ == "__main__":
    config_file = "config_file.yaml"
    main(config_file)

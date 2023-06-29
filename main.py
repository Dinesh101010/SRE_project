import time
import requests
import yaml
from collections import defaultdict


def check_health(endpoint):
    method = endpoint.get('method', 'GET')
    url = endpoint['url']
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    response = requests.request(method, url, headers=headers, json=body)
    latency = response.elapsed.total_seconds() * 1000

    if 200 <= response.status_code < 300 and latency < 500:
        return 'UP', latency
    else:
        return 'DOWN', latency


def log_availability(availability):
    for domain, status_count in availability.items():
        total = sum(status_count.values())
        up_count = status_count.get('UP', 0)
        percentage = round((up_count / total) * 100) if total > 0 else 0
        print(f"{domain} has {percentage}% availability percentage")


def main(config_file):
    with open(config_file) as f:
        endpoints = yaml.safe_load(f)

    availability = defaultdict(lambda: defaultdict(int))

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint['url'].split('/')[2]
                status, _ = check_health(endpoint)
                availability[domain][status] += 1

            log_availability(availability)
            time.sleep(15)

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")


if __name__ == "__main__":
    config_file = "config_file.yaml"
    main(config_file)

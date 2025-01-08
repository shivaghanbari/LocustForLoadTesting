# Locust Load Testing for News API

This repository provides a load testing script for the [News API](https://newsapi.org/) using [Locust](https://locust.io/).

## Prerequisites

1. Python 3.x
2. Locust installed. If not, install it using:
   ```bash
   pip install locust
# Script Overview

The `NewsAPITest` class in the script performs a load test on the News API by sending requests to fetch Tesla news. The script simulates user activity with a random wait time between 1 to 2 seconds between requests.

### Key Parameters:
- **Host:** The base URL for the API is set to `https://newsapi.org`.
- **Wait time:** Random wait between 1 and 2 seconds between tasks.
- **Endpoint:** `/v2/everything?q=Tesla&from=2024-01-01&sortBy=popularity&apiKey=YOUR_API_KEY`.

## Running the Test

### 1. Headless Mode (Specify User Count, Spawn Rate, and Test Duration)

To run the load test in headless mode with a specific number of users, spawn rate, and test duration, use the following command:

```bash
locust -f SampleApi.py --headless -u 10 -r 2 -t 60s
```
This will run the test with 10 users, spawning 2 users per second for a duration of 60 seconds.

-f is followed by the path to the Python script that defines the load test behavior (in this case, SampleApi.py).

-u 10: Simulate 10 users.

-r 2: Spawn 2 users per second.

-t 60s: Run the test for 60 seconds.

from locust import HttpUser, task, between


class BamaAPITest(HttpUser):
    # Host that you will load test
    host = "https://int.bama.ir"

    # Wait time between tasks (in seconds)
    wait_time = between(1, 2)

    @task
    def search_vehicle(self):
        # Define the API endpoint you want to test
        endpoint = "/cad/api/search?vehicle=mg%2C3"

        # Make a GET request to the API endpoint
        response = self.client.get(endpoint)

        # Print the response status code and content (for debugging)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        assert "mg-3" in response.text.lower(), "hongqi not found in response"

        # Optionally, you can add assertions to validate response
        # For example:
        # assert response.status_code == 200, "Unexpected response code"

    @task
    def get_all_info(self):
        # Define the API endpoint for brands info
        endpoint = "/cad/api/filter/all?vehicle=mg%2C3"

        # Make a GET request to the brands info endpoint
        response = self.client.get(endpoint)

        # Print the response status code and content (for debugging)
        print(f"Brands Info - Response status code: {response.status_code}")
        print(f"Brands Info - Response content: {response.text}")

        # Optionally, you can add assertions to validate response
        # For example:
        assert response.status_code == 200, "expected response code"

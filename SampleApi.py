from locust import HttpUser, task, between

class NewsAPITest(HttpUser):
    # Host that you will load test
    host = "https://newsapi.org"
    
    # Wait time between tasks (in seconds)
    wait_time = between(1, 2)
    
    @task
    def get_tesla_news(self):
        # API endpoint and parameters
        endpoint = "/v2/everything?q=Tesla&from=2024-01-01&sortBy=popularity&apiKey=8281e2809bc04b338ca5c24f79d19f3e"
        
        # Send GET request
        response = self.client.get(endpoint)
        
        # Log and validate the response
        print(f"Tesla News - Response status code: {response.status_code}")
        print(f"Tesla News - Response content: {response.text}")
        assert response.status_code == 200, "Unexpected status code"

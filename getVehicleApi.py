from locust import HttpUser, task, between


class BamaAPITest(HttpUser):
    # Host that you will load test
    host = "https://bama.ir"

    # Wait time between tasks (in seconds)
    wait_time = between(1, 2)


    # @task
    # def get_vehicle_info(self):
    #     # Define the API endpoint you want to test
    #     endpoint = "/cad/api/BasicInfo/vehicles"
    #
    #     # Make a GET request to the API endpoint
    #     response = self.client.get(endpoint)
    #
    #     # Print the response status code and content (for debugging)
    #     print(f"Response status code: {response.status_code}")
    #     print(f"Response content: {response.text}")
    #     assert "هونگچی" in response.text.lower(), "hongqi not found in response"
    #
    #     # Optionally, you can add assertions to validate response
    #     # For example:
    #     # assert response.status_code == 200, "Unexpected response code"
    #
    # @task
    # def get_brands_info(self):
    #     # Define the API endpoint for brands info
    #     endpoint = "/cad/api/BasicInfo/brands"
    #
    #     # Make a GET request to the brands info endpoint
    #     response = self.client.get(endpoint)
    #
    #     # Print the response status code and content (for debugging)
    #     print(f"Brands Info - Response status code: {response.status_code}")
    #     print(f"Brands Info - Response content: {response.text}")
    #
    #     # Optionally, you can add assertions to validate response
    #     # For example:
    #     assert response.status_code == 200, "expected response code"

    @task
    def get_parking_info(self):
        endpoint = "/prf/api/Parking/3?PageIndex=0&PageSize=10"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNDOUJBRURGQkY2RjVBQUNCMUExMTBERjkwOEY0NTM4NzVGMDU4NTRSUzI1NiIsIng1dCI6IlBKdXUzNzl2V3F5eG9SRGZrSTlGT0hYd1dGUSIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2FjY291bnQuYmFtYS5pciIsIm5iZiI6MTcxNzMxNDg4NywiaWF0IjoxNzE3MzE0ODg3LCJleHAiOjE3MTczMTg0ODcsImF1ZCI6Imh0dHBzOi8vYWNjb3VudC5iYW1hLmlyL3Jlc291cmNlcyIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJlbWFpbCIsImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJwd2QiXSwiY2xpZW50X2lkIjoicG9wdXBsb2dpbiIsInN1YiI6IjIwNDQwNDgiLCJhdXRoX3RpbWUiOjE3MTYxMDg5MjksImlkcCI6ImxvY2FsIiwiY2VsbCI6IjA5MTI4MTY0Njk2Iiwic2lkIjoiM0MzMDc1QTJFMzk1RDIzMjhERDRFMDU0REFCMjFEQUIiLCJqdGkiOiJGNkNGRURBNzExRTk4RDEzRjVBNDBGQzQwNTg2QkY2MiJ9.sFsdy5EuwiohIf7LGGjgMoQDu2r_4MV5akEao1b1FprCoehk6GZpe6stpUQVbxOGzp9Bn_VgnhxysQqMwScCaCRgvEfAsAJpS5U0HDYz9IxoMIcwbU6hd3Pn15LLriekYszhvSVYxZCZL2y5pOzWNxL8_uM6xbnYGPwUNmk7UjJ4nAXJAaS03RTxUI03El-9UruHjuCC3g26HYCLJoEbTS1Wy2c0Cs8s1CYPbrObTdjP97v03wtQSV0p3ge9Ck5XIGxWpcN_Sa-VVuRFI6DilNOnWMbEaS3slLviE4PSmMXRD14TuxrwicMjWC26TEtZC_KSO1_ufY3_ULSLQ8KHUA"
        }
        response = self.client.get(endpoint, headers=headers)
        print(f"Parking Info - Response status code: {response.status_code}")
        print(f"Parking Info - Response content: {response.text}")
        assert response.status_code == 200, "Unexpected status code"

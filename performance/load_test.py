from locust import HttpUser, task, between

from performance.performance_page import BasePageLocust


class WebsiteUser(HttpUser):

    wait_time = between(1, 2)

    @task
    def test_flow(self):
        with self.client.get(BasePageLocust.home, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Fail! status code: {response.status_code}")

        with self.client.get(BasePageLocust.login, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Fail! status code: {response.status_code}")


# api/base_client.py
from playwright.sync_api import APIRequestContext

class BaseClient:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    def _get(self, endpoint: str, **kwargs):
        response = self.request.get(endpoint, **kwargs)
        return response

    def _post(self, endpoint: str, data: dict, **kwargs):
        response = self.request.post(endpoint, data=data, **kwargs)
        return response
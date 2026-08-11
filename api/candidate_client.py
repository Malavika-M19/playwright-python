# api/candidate_client.py
from api.base_client import BaseClient

class CandidateClient(BaseClient):
    ENDPOINT = "/web/index.php/api/v2/recruitment/candidates"

    def create_candidate(self, payload: dict):
        return self._post(self.ENDPOINT, data=payload)

    def get_candidate(self, candidate_id: int):
        return self._get(f"{self.ENDPOINT}/{candidate_id}")
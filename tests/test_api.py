
def test_api(playwright):
    request= playwright.request.new_context(base_url="https://opensource-demo.orangehrmlive.com")
    response = request.get("/web/index.php/auth/login")
    status_code = response.status
    assert status_code == 200, f"Expected status code 200, but got {status_code}"


def test_create_candidate_returns_success(candidate_client):
    payload = {
        "firstName": "Test",
        "lastName": "Candidate",
        "email": "test.candidate@example.com",
        "vacancyId": 1,
    }
    response = candidate_client.create_candidate(payload)

    assert response.ok
    body = response.json()
    assert body["data"]["firstName"] == "Test"
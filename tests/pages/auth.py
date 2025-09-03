
class AuthClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        self.auth_endpoint = f"{base_url}/tokens"
        self.token = None

    def get_token(self, email, password):
        body = {'email': email, 'password': password}
        response = self.session.post(self.auth_endpoint, json=body)
        if response.status_code == 200:
            self.token = response.json()['token']
            self.session.headers.update({'Authorization': f"Bearer {self.token}"})
        return response

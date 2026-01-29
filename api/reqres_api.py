from config.config import Config


class ReqResAPI:
    def __init__(self, request_context):
        self.request = request_context
        self.base_url = Config.API_BASE_URL

    def get_users(self):
        # JSONPlaceholder returns all users in one list
        return self.request.get(f"{self.base_url}/users")

    def get_single_user(self, user_id):
        return self.request.get(f"{self.base_url}/users/{user_id}")

    def create_user(self, name, username, email):
        payload = {
            "name": name,
            "username": username,
            "email": email
        }
        return self.request.post(f"{self.base_url}/users", data=payload)

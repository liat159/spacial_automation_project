import pytest
from jsonschema import validate


@pytest.mark.api
class TestReqResAPI:

    # Test 1: Positive - Create User
    def test_create_user(self, reqres_api):
        response = reqres_api.create_user(
            "Leanne Graham", "Leanne", "Sincere@april.biz")
        assert response.ok
        assert response.status == 201
        data = response.json()
        # JSONPlaceholder always returns id 11 for new creations
        assert data["name"] == "Leanne Graham"
        assert "id" in data

    # Test 2: Negative - User Not Found
    def test_get_user_not_found(self, reqres_api):
        response = reqres_api.get_single_user(99999)  # ID doesn't exist
        assert response.status == 404
        assert response.json() == {}

    # Test 3: Schema Validation (Contract)
    def test_get_users_list_schema(self, reqres_api):
        response = reqres_api.get_users()
        assert response.ok
        data = response.json()

        # Validate it is a list
        assert isinstance(data, list)
        assert len(data) > 0

        # Define schema for a single user object in the list
        user_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "address": {"type": "object"}
            },
            "required": ["id", "name", "email"]
        }

        # Validate the first item in the list against the schema
        validate(instance=data[0], schema=user_schema)

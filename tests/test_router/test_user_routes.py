
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_user_success(async_client: AsyncClient, admin_token, test_user):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.get(f"/users/{test_user.id}", headers=headers)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == str(test_user.id)
    assert response_json["email"] == test_user.email
    assert response_json["nickname"] == test_user.nickname

@pytest.mark.asyncio
async def test_update_user_email(async_client: AsyncClient, admin_token, test_user):
    updated_data = {"email": "updateduser@example.com","username":"tuwat"}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users/{test_user.id}", json=updated_data, headers=headers)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["email"] == updated_data["email"]
    assert response_json["id"] == str(test_user.id)
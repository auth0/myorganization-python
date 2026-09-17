from .conftest import get_client, verify_request_count


def test_organization_userStores_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.user_stores.list_.0"
    client = get_client(test_id)
    client.organization.user_stores.list(
        member_access_level=["none"],
        is_enabled=True,
    )
    verify_request_count(test_id, "GET", "/user-stores", {"member_access_level": "none", "is_enabled": "true"}, 1)

from .conftest import get_client, verify_request_count


def test_organization_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.roles.list_.0"
    client = get_client(test_id)
    client.organization.roles.list(
        from_="from",
        take=1,
        name="name",
    )
    verify_request_count(test_id, "GET", "/roles", {"from": "from", "take": "1", "name": "name"}, 1)

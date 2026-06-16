from .conftest import get_client, verify_request_count


def test_organization_members_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.members.list_.0"
    client = get_client(test_id)
    client.organization.members.list(
        fields="fields",
        include_fields=True,
        from_="from",
        take=1,
    )
    verify_request_count(
        test_id, "GET", "/members", {"fields": "fields", "include_fields": "true", "from": "from", "take": "1"}, 1
    )


def test_organization_members_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.members.get.0"
    client = get_client(test_id)
    client.organization.members.get(
        user_id="user_id",
        fields="fields",
        include_fields=True,
    )
    verify_request_count(test_id, "GET", "/members/user_id", {"fields": "fields", "include_fields": "true"}, 1)

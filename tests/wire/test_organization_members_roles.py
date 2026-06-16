from .conftest import get_client, verify_request_count


def test_organization_members_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.members.roles.list_.0"
    client = get_client(test_id)
    client.organization.members.roles.list(
        user_id="user_id",
        from_="from",
        take=1,
    )
    verify_request_count(test_id, "GET", "/members/user_id/roles", {"from": "from", "take": "1"}, 1)


def test_organization_members_roles_assign() -> None:
    """Test assign endpoint with WireMock"""
    test_id = "organization.members.roles.assign.0"
    client = get_client(test_id)
    client.organization.members.roles.assign(
        user_id="user_id",
        role_ids=["rol_SO2j0sFo9NFa3F9w"],
    )
    verify_request_count(test_id, "POST", "/members/user_id/roles", None, 1)


def test_organization_members_roles_unassign() -> None:
    """Test unassign endpoint with WireMock"""
    test_id = "organization.members.roles.unassign.0"
    client = get_client(test_id)
    client.organization.members.roles.unassign(
        user_id="user_id",
        role_ids=["rol_SO2j0sFo9NFa3F9w"],
    )
    verify_request_count(test_id, "DELETE", "/members/user_id/roles", None, 1)

from .conftest import get_client, verify_request_count


def test_organization_invitations_roles_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.invitations.roles.list_.0"
    client = get_client(test_id)
    client.organization.invitations.roles.list(
        invitation_id="invitation_id",
    )
    verify_request_count(test_id, "GET", "/member-invitations/invitation_id/roles", None, 1)

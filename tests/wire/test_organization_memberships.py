from .conftest import get_client, verify_request_count


def test_organization_memberships_delete_memberships() -> None:
    """Test deleteMemberships endpoint with WireMock"""
    test_id = "organization.memberships.delete_memberships.0"
    client = get_client(test_id)
    client.organization.memberships.delete_memberships(
        members=["auth0|1234567890"],
    )
    verify_request_count(test_id, "POST", "/delete-memberships", None, 1)

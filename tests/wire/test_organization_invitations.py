from .conftest import get_client, verify_request_count

from auth0.myorganization import CreateMemberInvitationInvitee, MemberInvitationInviter


def test_organization_invitations_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.invitations.list_.0"
    client = get_client(test_id)
    client.organization.invitations.list(
        fields="fields",
        include_fields=True,
        from_="from",
        take=1,
        sort="sort",
    )
    verify_request_count(
        test_id,
        "GET",
        "/member-invitations",
        {"fields": "fields", "include_fields": "true", "from": "from", "take": "1", "sort": "sort"},
        1,
    )


def test_organization_invitations_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.invitations.create.0"
    client = get_client(test_id)
    client.organization.invitations.create(
        invitees=[
            CreateMemberInvitationInvitee(
                email="user@example.com",
                roles=["rol_0000000000000001"],
            )
        ],
        inviter=MemberInvitationInviter(
            name="Allison the Admin",
        ),
        identity_provider_id="con_2CZPv6IY0gWzDaQJ",
        ttl_sec=3600,
    )
    verify_request_count(test_id, "POST", "/member-invitations", None, 1)


def test_organization_invitations_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.invitations.get.0"
    client = get_client(test_id)
    client.organization.invitations.get(
        invitation_id="invitation_id",
        fields="fields",
        include_fields=True,
    )
    verify_request_count(
        test_id, "GET", "/member-invitations/invitation_id", {"fields": "fields", "include_fields": "true"}, 1
    )


def test_organization_invitations_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.invitations.delete.0"
    client = get_client(test_id)
    client.organization.invitations.delete(
        invitation_id="invitation_id",
    )
    verify_request_count(test_id, "DELETE", "/member-invitations/invitation_id", None, 1)

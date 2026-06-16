from .conftest import get_client, verify_request_count

from auth0.myorganization import IdpOidcOptionsRequest, IdpOidcRequest, IdpOidcUpdateRequest


def test_organization_identityProviders_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.identity_providers.list_.0"
    client = get_client(test_id)
    client.organization.identity_providers.list()
    verify_request_count(test_id, "GET", "/identity-providers", None, 1)


def test_organization_identityProviders_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.identity_providers.create.0"
    client = get_client(test_id)
    client.organization.identity_providers.create(
        request=IdpOidcRequest(
            strategy="oidc",
            options=IdpOidcOptionsRequest(
                type="front_channel",
                client_id="a8f3b2e7-5d1c-4f9a-8b0d-2e1c3a5b6f7d",
                client_secret="KzQp2sVxR8nTgMjFhYcEWuLoIbDvUoC6A9B1zX7yWqFjHkGrP5sQdLmNp",
                discovery_url="https://{yourDomain}/.well-known/openid-configuration",
            ),
            name="oidcIdp",
            domains=["mydomain.com"],
            display_name="OIDC IdP",
            show_as_button=True,
            assign_membership_on_login=False,
            is_enabled=True,
        ),
    )
    verify_request_count(test_id, "POST", "/identity-providers", None, 1)


def test_organization_identityProviders_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.identity_providers.get.0"
    client = get_client(test_id)
    client.organization.identity_providers.get(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "GET", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.identity_providers.delete.0"
    client = get_client(test_id)
    client.organization.identity_providers.delete(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "DELETE", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organization.identity_providers.update.0"
    client = get_client(test_id)
    client.organization.identity_providers.update(
        idp_id="idp_id",
        request=IdpOidcUpdateRequest(
            display_name="OIDC IdP",
            show_as_button=True,
            assign_membership_on_login=False,
            is_enabled=True,
            options=IdpOidcOptionsRequest(
                type="front_channel",
                client_id="a8f3b2e7-5d1c-4f9a-8b0d-2e1c3a5b6f7d",
                client_secret="KzQp2sVxR8nTgMjFhYcEWuLoIbDvUoC6A9B1zX7yWqFjHkGrP5sQdLmNp",
                discovery_url="https://{yourDomain}/.well-known/openid-configuration",
            ),
        ),
    )
    verify_request_count(test_id, "PATCH", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_update_attributes() -> None:
    """Test updateAttributes endpoint with WireMock"""
    test_id = "organization.identity_providers.update_attributes.0"
    client = get_client(test_id)
    client.organization.identity_providers.update_attributes(
        idp_id="idp_id",
        request={"key": "value"},
    )
    verify_request_count(test_id, "PUT", "/identity-providers/idp_id/update-attributes", None, 1)


def test_organization_identityProviders_detach() -> None:
    """Test detach endpoint with WireMock"""
    test_id = "organization.identity_providers.detach.0"
    client = get_client(test_id)
    client.organization.identity_providers.detach(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "POST", "/identity-providers/idp_id/detach", None, 1)

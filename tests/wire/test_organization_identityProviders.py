from .conftest import get_client, verify_request_count


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
        request={
            "name": "oidcIdp",
            "domains": ["mydomain.com"],
            "display_name": "OIDC IdP",
            "show_as_button": True,
            "assign_membership_on_login": False,
            "is_enabled": True,
            "options": {},
        }
    )
    verify_request_count(test_id, "POST", "/identity-providers", None, 1)


def test_organization_identityProviders_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.identity_providers.get.0"
    client = get_client(test_id)
    client.organization.identity_providers.get(idp_id="idp_id")
    verify_request_count(test_id, "GET", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.identity_providers.delete.0"
    client = get_client(test_id)
    client.organization.identity_providers.delete(idp_id="idp_id")
    verify_request_count(test_id, "DELETE", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organization.identity_providers.update.0"
    client = get_client(test_id)
    client.organization.identity_providers.update(
        idp_id="idp_id",
        request={
            "display_name": "OIDC IdP",
            "show_as_button": True,
            "assign_membership_on_login": False,
            "is_enabled": True,
            "options": {},
        },
    )
    verify_request_count(test_id, "PATCH", "/identity-providers/idp_id", None, 1)


def test_organization_identityProviders_update_attributes() -> None:
    """Test updateAttributes endpoint with WireMock"""
    test_id = "organization.identity_providers.update_attributes.0"
    client = get_client(test_id)
    client.organization.identity_providers.update_attributes(idp_id="idp_id", request={"key": "value"})
    verify_request_count(test_id, "PUT", "/identity-providers/idp_id/update-attributes", None, 1)


def test_organization_identityProviders_detach() -> None:
    """Test detach endpoint with WireMock"""
    test_id = "organization.identity_providers.detach.0"
    client = get_client(test_id)
    client.organization.identity_providers.detach(idp_id="idp_id")
    verify_request_count(test_id, "POST", "/identity-providers/idp_id/detach", None, 1)

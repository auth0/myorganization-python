from .conftest import get_client, verify_request_count


def test_organization_identityProviders_provisioning_scimTokens_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.scim_tokens.list_.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.scim_tokens.list(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "GET", "/identity-providers/idp_id/provisioning/scim-tokens", None, 1)


def test_organization_identityProviders_provisioning_scimTokens_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.scim_tokens.create.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.scim_tokens.create(
        idp_id="idp_id",
        token_lifetime=86400,
    )
    verify_request_count(test_id, "POST", "/identity-providers/idp_id/provisioning/scim-tokens", None, 1)


def test_organization_identityProviders_provisioning_scimTokens_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.scim_tokens.delete.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.scim_tokens.delete(
        idp_id="idp_id",
        idp_scim_token_id="idp_scim_token_id",
    )
    verify_request_count(
        test_id, "DELETE", "/identity-providers/idp_id/provisioning/scim-tokens/idp_scim_token_id", None, 1
    )

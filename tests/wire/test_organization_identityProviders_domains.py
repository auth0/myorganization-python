from .conftest import get_client, verify_request_count


def test_organization_identityProviders_domains_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.identity_providers.domains.create.0"
    client = get_client(test_id)
    client.organization.identity_providers.domains.create(idp_id="idp_id", domain="my-domain.com")
    verify_request_count(test_id, "POST", "/identity-providers/idp_id/domains", None, 1)


def test_organization_identityProviders_domains_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.identity_providers.domains.delete.0"
    client = get_client(test_id)
    client.organization.identity_providers.domains.delete(idp_id="idp_id", domain="domain")
    verify_request_count(test_id, "DELETE", "/identity-providers/idp_id/domains/domain", None, 1)

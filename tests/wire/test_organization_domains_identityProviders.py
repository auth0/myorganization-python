from .conftest import get_client, verify_request_count


def test_organization_domains_identityProviders_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.domains.identity_providers.get.0"
    client = get_client(test_id)
    client.organization.domains.identity_providers.get(
        domain_id="domain_id",
    )
    verify_request_count(test_id, "GET", "/domains/domain_id/identity-providers", None, 1)

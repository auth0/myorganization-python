from .conftest import get_client, verify_request_count


def test_organization_domains_identityProviders_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.domains.identity_providers.list_.0"
    client = get_client(test_id)
    client.organization.domains.identity_providers.list(
        domain_id="domain_id",
    )
    verify_request_count(test_id, "GET", "/domains/domain_id/identity-providers", None, 1)

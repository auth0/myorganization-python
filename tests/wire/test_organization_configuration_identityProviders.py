from .conftest import get_client, verify_request_count


def test_organization_configuration_identityProviders_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.configuration.identity_providers.get.0"
    client = get_client(test_id)
    client.organization.configuration.identity_providers.get()
    verify_request_count(test_id, "GET", "/config/identity-providers", None, 1)

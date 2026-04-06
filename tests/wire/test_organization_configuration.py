from .conftest import get_client, verify_request_count


def test_organization_configuration_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.configuration.get.0"
    client = get_client(test_id)
    client.organization.configuration.get()
    verify_request_count(test_id, "GET", "/config", None, 1)

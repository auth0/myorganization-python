from .conftest import get_client, verify_request_count


def test_organization_domains_list_() -> None:
    """Test list endpoint with WireMock"""
    test_id = "organization.domains.list_.0"
    client = get_client(test_id)
    client.organization.domains.list()
    verify_request_count(test_id, "GET", "/domains", None, 1)


def test_organization_domains_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.domains.create.0"
    client = get_client(test_id)
    client.organization.domains.create(domain="acme.com")
    verify_request_count(test_id, "POST", "/domains", None, 1)


def test_organization_domains_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.domains.get.0"
    client = get_client(test_id)
    client.organization.domains.get(domain_id="domain_id")
    verify_request_count(test_id, "GET", "/domains/domain_id", None, 1)


def test_organization_domains_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.domains.delete.0"
    client = get_client(test_id)
    client.organization.domains.delete(domain_id="domain_id")
    verify_request_count(test_id, "DELETE", "/domains/domain_id", None, 1)

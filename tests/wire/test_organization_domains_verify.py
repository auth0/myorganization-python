from .conftest import get_client, verify_request_count


def test_organization_domains_verify_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.domains.verify.create.0"
    client = get_client(test_id)
    client.organization.domains.verify.create(
        domain_id="domain_id",
    )
    verify_request_count(test_id, "POST", "/domains/domain_id/verify", None, 1)

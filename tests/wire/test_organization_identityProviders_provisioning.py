from .conftest import get_client, verify_request_count


def test_organization_identityProviders_provisioning_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.get.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.get(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "GET", "/identity-providers/idp_id/provisioning", None, 1)


def test_organization_identityProviders_provisioning_create() -> None:
    """Test create endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.create.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.create(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "POST", "/identity-providers/idp_id/provisioning", None, 1)


def test_organization_identityProviders_provisioning_delete() -> None:
    """Test delete endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.delete.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.delete(
        idp_id="idp_id",
    )
    verify_request_count(test_id, "DELETE", "/identity-providers/idp_id/provisioning", None, 1)


def test_organization_identityProviders_provisioning_update_attributes() -> None:
    """Test updateAttributes endpoint with WireMock"""
    test_id = "organization.identity_providers.provisioning.update_attributes.0"
    client = get_client(test_id)
    client.organization.identity_providers.provisioning.update_attributes(
        idp_id="idp_id",
        request={"key": "value"},
    )
    verify_request_count(test_id, "PUT", "/identity-providers/idp_id/provisioning/update-attributes", None, 1)

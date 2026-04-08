from .conftest import get_client, verify_request_count

from auth0 import OrgBranding, OrgBrandingColors


def test_organizationDetails_get() -> None:
    """Test get endpoint with WireMock"""
    test_id = "organization_details.get.0"
    client = get_client(test_id)
    client.organization_details.get()
    verify_request_count(test_id, "GET", "/details", None, 1)


def test_organizationDetails_update() -> None:
    """Test update endpoint with WireMock"""
    test_id = "organization_details.update.0"
    client = get_client(test_id)
    client.organization_details.update(
        name="testorg",
        display_name="Test Organization",
        branding=OrgBranding(
            logo_url="https://example.com/logo.png",
            colors=OrgBrandingColors(
                primary="#000000",
                page_background="#FFFFFF",
            ),
        ),
    )
    verify_request_count(test_id, "PATCH", "/details", None, 1)

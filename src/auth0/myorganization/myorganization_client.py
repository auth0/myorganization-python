from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Dict, Optional, Union

import httpx
from .client import AsyncAuth0, Auth0
from .token_provider import TokenProvider

if TYPE_CHECKING:
    from .organization.client import AsyncOrganizationClient, OrganizationClient
    from .organization_details.client import AsyncOrganizationDetailsClient, OrganizationDetailsClient


class MyOrganizationClient:
    """
    Auth0 My Organization API client with automatic token management.

    Supports two initialization patterns:

    1. With an existing token:

        client = MyOrganizationClient(
            domain="tenant.auth0.com",
            token="your_token"
        )

    2. With client credentials (automatic token acquisition and refresh):

        client = MyOrganizationClient(
            domain="tenant.auth0.com",
            client_id="your_client_id",
            client_secret="your_client_secret",
            organization="org_123456789"
        )

    Parameters
    ----------
    domain : str
        Your Auth0 domain (e.g., "your-tenant.auth0.com").
    token : Optional[Union[str, Callable[[], str]]]
        A static token string or a callable that returns a token.
        Required if client_id/client_secret are not provided.
    client_id : Optional[str]
        Your Auth0 application client ID.
        Required along with client_secret for automatic token acquisition.
    client_secret : Optional[str]
        Your Auth0 application client secret.
        Required along with client_id for automatic token acquisition.
    organization : Optional[str]
        The Auth0 organization ID (e.g., "org_123456789").
        Included in the client credentials token request when provided.
    audience : Optional[str]
        The API audience. Defaults to https://{domain}/my-org/
    headers : Optional[Dict[str, str]]
        Additional headers to send with requests.
    timeout : Optional[float]
        Request timeout in seconds. Defaults to 60.
    httpx_client : Optional[httpx.Client]
        Custom httpx client for requests.

    Raises
    ------
    ValueError
        If neither token nor client_id/client_secret are provided.
    """

    def __init__(
        self,
        *,
        domain: str,
        token: Optional[Union[str, Callable[[], str]]] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        organization: Optional[str] = None,
        audience: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        httpx_client: Optional[httpx.Client] = None,
    ):
        # Validate auth options
        has_token = token is not None
        has_credentials = client_id is not None and client_secret is not None

        if not has_token and not has_credentials:
            raise ValueError("Either 'token' or both 'client_id' and 'client_secret' must be provided")

        # Create token supplier
        if has_credentials and not has_token:
            provider = TokenProvider(
                domain=domain,
                client_id=client_id,  # type: ignore[arg-type]
                client_secret=client_secret,  # type: ignore[arg-type]
                audience=audience,
                organization=organization,
            )
            resolved_token: Union[str, Callable[[], str]] = provider.get_token
        else:
            resolved_token = token  # type: ignore[assignment]

        # Create underlying client
        self._api = Auth0(
            base_url=f"https://{domain}/my-org",
            token=resolved_token,
            headers=headers,
            timeout=timeout,
            httpx_client=httpx_client,
        )

    # Forward sub-client properties
    @property
    def organization(self) -> "OrganizationClient":
        return self._api.organization

    @property
    def organization_details(self) -> "OrganizationDetailsClient":
        return self._api.organization_details


class AsyncMyOrganizationClient:
    """
    Async Auth0 My Organization API client with automatic token management.

    Supports two initialization patterns:

    1. With an existing token:

        client = AsyncMyOrganizationClient(
            domain="tenant.auth0.com",
            token="your_token"
        )

    2. With client credentials (automatic token acquisition and refresh):

        client = AsyncMyOrganizationClient(
            domain="tenant.auth0.com",
            client_id="your_client_id",
            client_secret="your_client_secret",
            organization="org_123456789"
        )

    Parameters
    ----------
    domain : str
        Your Auth0 domain (e.g., "your-tenant.auth0.com").
    token : Optional[Union[str, Callable[[], str]]]
        A static token string or a callable that returns a token.
        Required if client_id/client_secret are not provided.
    client_id : Optional[str]
        Your Auth0 application client ID.
        Required along with client_secret for automatic token acquisition.
    client_secret : Optional[str]
        Your Auth0 application client secret.
        Required along with client_id for automatic token acquisition.
    organization : Optional[str]
        The Auth0 organization ID (e.g., "org_123456789").
        Included in the client credentials token request when provided.
    audience : Optional[str]
        The API audience. Defaults to https://{domain}/my-org/
    headers : Optional[Dict[str, str]]
        Additional headers to send with requests.
    timeout : Optional[float]
        Request timeout in seconds. Defaults to 60.
    httpx_client : Optional[httpx.AsyncClient]
        Custom httpx async client for requests.

    Raises
    ------
    ValueError
        If neither token nor client_id/client_secret are provided.
    """

    def __init__(
        self,
        *,
        domain: str,
        token: Optional[Union[str, Callable[[], str]]] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        organization: Optional[str] = None,
        audience: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        httpx_client: Optional[httpx.AsyncClient] = None,
    ):
        # Validate auth options
        has_token = token is not None
        has_credentials = client_id is not None and client_secret is not None

        if not has_token and not has_credentials:
            raise ValueError("Either 'token' or both 'client_id' and 'client_secret' must be provided")

        # Create token supplier
        # Note: AsyncAuth0 expects a sync callable for token, so we use
        # the sync TokenProvider. This is safe because httpx sync calls work
        # in async contexts.
        if has_credentials and not has_token:
            provider = TokenProvider(
                domain=domain,
                client_id=client_id,  # type: ignore[arg-type]
                client_secret=client_secret,  # type: ignore[arg-type]
                audience=audience,
                organization=organization,
            )
            resolved_token: Union[str, Callable[[], str]] = provider.get_token
        else:
            resolved_token = token  # type: ignore[assignment]

        # Create underlying client
        self._api = AsyncAuth0(
            base_url=f"https://{domain}/my-org",
            token=resolved_token,
            headers=headers,
            timeout=timeout,
            httpx_client=httpx_client,
        )

    # Forward sub-client properties
    @property
    def organization(self) -> "AsyncOrganizationClient":
        return self._api.organization

    @property
    def organization_details(self) -> "AsyncOrganizationDetailsClient":
        return self._api.organization_details

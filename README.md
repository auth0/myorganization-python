![Python SDK for Auth0 MyOrganization](https://cdn.auth0.com/website/sdks/banners/myorganization-python-banner.png)

<div align="center">

[![pypi](https://img.shields.io/pypi/v/myorganization-python)](https://pypi.python.org/pypi/myorganization-python)
[![License](https://img.shields.io/:license-Apache%202.0-blue.svg?style=flat)](https://www.apache.org/licenses/LICENSE-2.0)
[![Build Status](https://img.shields.io/github/actions/workflow/status/auth0/myorganization-python/ci.yml?branch=main&style=flat-square)](https://github.com/auth0/myorganization-python/actions?query=branch%3Amain)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fauth0%2Fmyorganization-python)

📚 [Documentation](#documentation) • 🚀 [Getting Started](#getting-started) • 💬 [Feedback](#feedback)

</div>

---

## Documentation

- [Docs Site](https://auth0.com/docs) - explore our docs site and learn more about Auth0
- [API Reference](https://github.com/auth0/myorganization-python/blob/main/reference.md) - full reference for this library

## Getting Started

### Requirements

This library supports the following tooling versions:

- Python >= 3.8

### Installation

```sh
pip install myorganization-python
```

### Configure the SDK

The `MyOrganizationClient` is the recommended way to interact with the Auth0 My Organization API. It provides a simpler interface using just your Auth0 domain:

```python
from auth0.myorganization import MyOrganizationClient

# With an access token (from your authentication flow)
client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    token=user_access_token,
)
```

For backend scripts or admin tooling, you can use client credentials with automatic token management:

```python
# With client credentials (automatic token acquisition and refresh)
client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    organization="YOUR_ORG_ID",
)
```

Then use the client to interact with the API:

```python
# List organization domains
domains = client.organization.domains.list()

# Get organization details
details = client.organization_details.get()
```

### Using the Base Client

For more control, you can use the `Auth0` client directly with a full base URL:

```python
from auth0.myorganization import Auth0

client = Auth0(
    base_url="https://your-tenant.auth0.com/my-org",
    token="YOUR_TOKEN",
)
client.organization.domains.create(
    domain="acme.com",
)
```

## Async Client

The SDK also exports async clients so that you can make non-blocking calls to the API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from auth0.myorganization import AsyncMyOrganizationClient

client = AsyncMyOrganizationClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
)


async def main() -> None:
    details = await client.organization_details.get()
    print(details)


asyncio.run(main())
```

You can also use the base async client directly:

```python
import asyncio

from auth0.myorganization import AsyncAuth0

client = AsyncAuth0(
    base_url="https://your-tenant.auth0.com/my-org",
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.organization.domains.create(
        domain="acme.com",
    )


asyncio.run(main())
```

## Request and Response Types

The SDK exports all request and response types as Pydantic models. You can import them directly:

```python
from auth0.myorganization import MyOrganizationClient
from auth0.myorganization.types import GetOrganizationDetailsResponseContent

client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
)

details: GetOrganizationDetailsResponseContent = client.organization_details.get()
print(details.display_name)
```

## API Reference

- [Full Reference](./reference.md) - complete API reference guide

### Key Classes

- **MyOrganizationClient** - recommended client for managing organization details, domains, identity providers, and configuration
- **AsyncMyOrganizationClient** - async variant of the above
- **TokenProvider** - automatic token management via OAuth 2.0 client credentials grant

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from auth0.myorganization.core.api_error import ApiError

try:
    client.organization.domains.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from auth0.myorganization import Auth0

client = Auth0(
    base_url="https://your-tenant.auth0.com/my-org",
    token="YOUR_TOKEN",
)
response = client.organization.domains.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.organization.domains.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from auth0.myorganization import MyOrganizationClient

client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
    timeout=20.0,
)


# Override timeout for a specific method
client.organization.domains.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Additional Headers

If you would like to send additional headers as part of the request, use the `headers` parameter:

```python
client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
    headers={"X-Custom-Header": "custom value"},
)
```

### Logging

The SDK includes built-in logging that can help with debugging. You can enable it by passing a `logging` configuration when creating the client:

```python
from auth0.myorganization import Auth0

client = Auth0(
    base_url="https://your-tenant.auth0.com/my-org",
    token="YOUR_TOKEN",
    logging={"level": "debug"},
)
```

When enabled at `debug` level, the SDK logs HTTP request and response details including method, URL, status code, and headers. Sensitive information (authorization headers, API keys) is automatically redacted.

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from auth0.myorganization import MyOrganizationClient

client = MyOrganizationClient(
    domain="your-tenant.auth0.com",
    token="YOUR_TOKEN",
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Feedback

### Contributing

We appreciate feedback and contribution to this repo! Before you get started, please see the following:

- [Auth0's general contribution guidelines](https://github.com/auth0/open-source-template/blob/master/GENERAL-CONTRIBUTING.md)
- [Auth0's code of conduct guidelines](https://github.com/auth0/open-source-template/blob/master/CODE-OF-CONDUCT.md)

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

### Raise an issue

To provide feedback or report a bug, please [raise an issue on our issue tracker](https://github.com/auth0/myorganization-python/issues).

### Vulnerability Reporting

Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/responsible-disclosure-policy) details the procedure for disclosing security issues.

## What is Auth0?

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.auth0.com/website/sdks/logos/auth0_light_mode.png"   width="150">
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.auth0.com/website/sdks/logos/auth0_dark_mode.png" width="150">
    <img alt="Auth0 Logo" src="https://cdn.auth0.com/website/sdks/logos/auth0_light_mode.png" width="150">
  </picture>
</p>
<p align="center">Auth0 is an easy to implement, adaptable authentication and authorization platform. To learn more checkout <a href="https://auth0.com/why-auth0">Why Auth0</a></p>
<p align="center">
  Copyright 2026 Okta, Inc.<br>
  Licensed under the Apache License, Version 2.0 (the "License");<br>
  you may not use this file except in compliance with the License.<br>
  You may obtain a copy of the License at: <a href="https://www.apache.org/licenses/LICENSE-2.0">https://www.apache.org/licenses/LICENSE-2.0</a><br>
</p>

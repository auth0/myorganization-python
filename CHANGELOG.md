# Change Log

## [1.0.0b0](https://github.com/auth0/myorganization-python/tree/1.0.0b0) (2026-04-09)

`v1.0.0b0` is the first release of the **Auth0 My Organization Python SDK** — a Fern-generated SDK for the Auth0 My Organization API.

**Added**
- `MyOrganizationClient` and `AsyncMyOrganizationClient` high-level wrappers with domain-based URL derivation [\#4](https://github.com/auth0/myorganization-python/pull/4)
- `TokenProvider` and `AsyncTokenProvider` for automatic OAuth 2.0 client credentials token management with caching and auto-refresh [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Organization Details API — get and update org display name and branding [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Organization Domains API — list, create, get, delete, and verify custom domains with cursor-based pagination [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Organization Identity Providers API — create, get, list, update, delete, and detach IDPs; refresh attribute mappings [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Provisioning API — create, get, delete provisioning configs; refresh provisioning attribute mappings [\#4](https://github.com/auth0/myorganization-python/pull/4)
- SCIM Tokens API — list, create, and revoke SCIM tokens per IDP [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Configuration API — retrieve API configuration [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Raw HTTP response access via `.with_raw_response` for status codes, headers, and response data [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Automatic retries with exponential backoff on 408, 429, and 5XX responses [\#4](https://github.com/auth0/myorganization-python/pull/4)
- `Auth0-Client` telemetry header on every request [\#4](https://github.com/auth0/myorganization-python/pull/4)
- Configurable timeouts, retries, and custom headers at client and per-request level [\#4](https://github.com/auth0/myorganization-python/pull/4)

**Fixed**
- Use `AsyncTokenProvider` in async client to prevent event loop blocking [\#4](https://github.com/auth0/myorganization-python/pull/4)

### Installation

```sh
poetry add myorganization-python==1.0.0b0
```

### Requirements
- Python >= 3.9

# Change Log

## [1.0.0](https://github.com/auth0/myorganization-python/tree/1.0.0) (2026-06-16)

`v1.0.0` is the first stable release of the **Auth0 My Organization Python SDK** — a Fern-generated SDK for the Auth0 My Organization API. The API surface is now stable.

**Added**
- `MyOrganizationClient` and `AsyncMyOrganizationClient` high-level wrappers with domain-based URL derivation
- `TokenProvider` and `AsyncTokenProvider` for automatic OAuth 2.0 client credentials token management with caching and auto-refresh
- Organization Details API — get and update org display name and branding
- Organization Domains API — list, create, get, delete, and verify custom domains with cursor-based pagination
- Organization Identity Providers API — create, get, list, update, delete, and detach IDPs; refresh attribute mappings
- Organization Members API — list and get organization members [\#13](https://github.com/auth0/myorganization-python/pull/13)
- Organization Member Roles API — list, assign, and unassign roles for a member [\#13](https://github.com/auth0/myorganization-python/pull/13)
- Organization Memberships API — remove members from the organization [\#13](https://github.com/auth0/myorganization-python/pull/13)
- Organization Roles API — list roles available in the organization [\#13](https://github.com/auth0/myorganization-python/pull/13)
- Organization Member Invitations API — list, create, get, and delete invitations [\#13](https://github.com/auth0/myorganization-python/pull/13)
- Provisioning API — create, get, delete provisioning configs; refresh provisioning attribute mappings
- SCIM Tokens API — list, create, and revoke SCIM tokens per IDP
- Configuration API — retrieve API configuration
- Raw HTTP response access via `.with_raw_response` for status codes, headers, and response data
- Automatic retries with exponential backoff on 408, 429, and 5XX responses
- Configurable timeouts, retries, and custom headers at client and per-request level

**Changed**
- Dropped support for Python 3.9; the minimum supported version is now Python 3.10 [\#13](https://github.com/auth0/myorganization-python/pull/13)

### Installation

```sh
poetry add myorganization-python==1.0.0
```

### Requirements
- Python >= 3.10

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

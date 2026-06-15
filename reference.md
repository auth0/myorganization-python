# Reference
## OrganizationDetails
<details><summary><code>client.organization_details.<a href="src/auth0.myorganization/organization_details/client.py">get</a>() -> GetOrganizationDetailsResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for this Organization, including display name and branding options. To learn more about Auth0 Organizations, read [Organizations](https://auth0.com/docs/manage-users/organizations).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization_details.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization_details.<a href="src/auth0.myorganization/organization_details/client.py">update</a>(...) -> UpdateOrganizationDetailsResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update details for this Organization, such as display name and branding options. To learn more about Auth0 Organizations, read [Organizations](https://auth0.com/docs/manage-users/organizations).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0, OrgBranding, OrgBrandingColors
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateOrganizationDetailsRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Configuration
<details><summary><code>client.organization.configuration.<a href="src/auth0.myorganization/organization/configuration/client.py">get</a>() -> GetConfigurationResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the My Organization API configuration. Returns only the `connection_deletion_behavior` and `allowed_strategies`. Identifier attributes such as `user_attribute_profile_id` and `connection_profile_id` are not included. Cache this information, as it does not change frequently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.configuration.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Domains
<details><summary><code>client.organization.domains.<a href="src/auth0.myorganization/organization/domains/client.py">list</a>(...) -> ListOrganizationDomainsResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all pending and verified domains for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.list(
    from_="from",
    take=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.domains.<a href="src/auth0.myorganization/organization/domains/client.py">create</a>(...) -> CreateOrganizationDomainResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new domain for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.create(
    domain="acme.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `OrgDomainName` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.domains.<a href="src/auth0.myorganization/organization/domains/client.py">get</a>(...) -> GetOrganizationDomainResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a domain specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.get(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `OrgDomainId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.domains.<a href="src/auth0.myorganization/organization/domains/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a domain specified by ID from this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.delete(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `OrgDomainId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization IdentityProviders
<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">list</a>() -> ListIdentityProvidersResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all Identity Providers for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">create</a>(...) -> CreateIdentityProviderResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Identity Provider for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0, IdpOidcRequest, IdpOidcOptionsRequest
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.create(
    request=IdpOidcRequest(
        name="oidcIdp",
        strategy="oidc",
        domains=[
            "mydomain.com"
        ],
        display_name="OIDC IdP",
        show_as_button=True,
        assign_membership_on_login=False,
        is_enabled=True,
        options=IdpOidcOptionsRequest(
            type="front_channel",
            client_id="a8f3b2e7-5d1c-4f9a-8b0d-2e1c3a5b6f7d",
            client_secret="KzQp2sVxR8nTgMjFhYcEWuLoIbDvUoC6A9B1zX7yWqFjHkGrP5sQdLmNp",
            discovery_url="https://{yourDomain}/.well-known/openid-configuration",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateIdentityProviderRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">get</a>(...) -> GetIdentityProviderResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.get(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an Identity Provider specified by ID from this Organization. This will remove the association and delete the underlying Identity Provider. Members will no longer be able to authenticate using this Identity Provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.delete(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">update</a>(...) -> UpdateIdentityProviderResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0, IdpOidcUpdateRequest, IdpOidcOptionsRequest
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.update(
    idp_id="idp_id",
    request=IdpOidcUpdateRequest(
        display_name="OIDC IdP",
        show_as_button=True,
        assign_membership_on_login=False,
        is_enabled=True,
        options=IdpOidcOptionsRequest(
            type="front_channel",
            client_id="a8f3b2e7-5d1c-4f9a-8b0d-2e1c3a5b6f7d",
            client_secret="KzQp2sVxR8nTgMjFhYcEWuLoIbDvUoC6A9B1zX7yWqFjHkGrP5sQdLmNp",
            discovery_url="https://{yourDomain}/.well-known/openid-configuration",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateIdentityProviderRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">update_attributes</a>(...) -> GetIdentityProviderResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh the attribute mapping for an Identity Provider specified by ID for this Organization. Mappings are reset to the admin-defined defaults.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.update_attributes(
    idp_id="idp_id",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.<a href="src/auth0.myorganization/organization/identity_providers/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an Identity Provider specified by ID from this Organization. This only removes the association; the underlying Identity Provider is not deleted. Members will no longer be able to authenticate using this Identity Provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.detach(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Members
<details><summary><code>client.organization.members.<a href="src/auth0.myorganization/organization/members/client.py">list</a>(...) -> ListOrganizationMembersResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all members for this Organization. The `roles` field is only included for each member when the token also carries the `read:my_org:member_roles` scope; without that scope the `roles` field is omitted from the response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.members.list(
    fields="fields",
    include_fields=True,
    from_="from",
    take=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.members.<a href="src/auth0.myorganization/organization/members/client.py">get</a>(...) -> GetOrganizationMemberResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a member specified by user ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.members.get(
    user_id="user_id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `OrgMemberId` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Memberships
<details><summary><code>client.organization.memberships.<a href="src/auth0.myorganization/organization/memberships/client.py">delete_memberships</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one member from this Organization. The underlying user account is not deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.memberships.delete_memberships(
    members=[
        "auth0|1234567890"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**members:** `typing.List[OrgMemberId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Invitations
<details><summary><code>client.organization.invitations.<a href="src/auth0.myorganization/organization/invitations/client.py">list</a>(...) -> ListMembersInvitationsResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all member invitations for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.invitations.list(
    fields="fields",
    include_fields=True,
    from_="from",
    take=1,
    sort="sort",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields. Note: you cannot filter on ticket_id and this value will only be returned when fields are not filtered.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Field to sort by. Use field:order where order is 1 for ascending and -1 for descending. Defaults to created_at:-1
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.invitations.<a href="src/auth0.myorganization/organization/invitations/client.py">create</a>(...) -> CreateMemberInvitationResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one or more member invitations for this Organization. If an active invitation already exists for a user, generating a new invitation will automatically revoke any outstanding invitations for that user. Roles specified in the payload will be granted to the user upon acceptance of the invitation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0, CreateMemberInvitationInvitee, MemberInvitationInviter
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.invitations.create(
    invitees=[
        CreateMemberInvitationInvitee(
            email="user@example.com",
            roles=[
                "rol_0000000000000001"
            ],
        )
    ],
    inviter=MemberInvitationInviter(
        name="Allison the Admin",
    ),
    identity_provider_id="con_2CZPv6IY0gWzDaQJ",
    ttl_sec=3600,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitees:** `typing.List[CreateMemberInvitationInvitee]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_0_custom_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**inviter:** `typing.Optional[MemberInvitationInviter]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_provider_id:** `typing.Optional[str]` — Identity provider identifier.
    
</dd>
</dl>

<dl>
<dd>

**ttl_sec:** `typing.Optional[int]` — Number of seconds for which the invitation is valid before expiration. If unspecified or set to 0, this value defaults to 604800 seconds (7 days). Max value: 2592000 seconds (30 days).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.invitations.<a href="src/auth0.myorganization/organization/invitations/client.py">get</a>(...) -> GetMemberInvitationResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a member invitation specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.invitations.get(
    invitation_id="invitation_id",
    fields="fields",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitation_id:** `InvitationId` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include or exclude (based on value provided for include_fields) in the result. Leave empty to retrieve all fields. Note: you cannot filter on ticket_id and this value will only be returned when fields are not filtered.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — Whether specified fields are to be included (true) or excluded (false). Defaults to true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.invitations.<a href="src/auth0.myorganization/organization/invitations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a member invitation specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.invitations.delete(
    invitation_id="invitation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invitation_id:** `InvitationId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Roles
<details><summary><code>client.organization.roles.<a href="src/auth0.myorganization/organization/roles/client.py">list</a>(...) -> ListRolesResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of roles available for binding to members and invitations for this Organization. Only roles made visible to this Organization by the Tenant Admin are returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.roles.list(
    from_="from",
    take=1,
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — An optional filter on the name (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Configuration IdentityProviders
<details><summary><code>client.organization.configuration.identity_providers.<a href="src/auth0.myorganization/organization/configuration/identity_providers/client.py">get</a>() -> GetIdpConfigurationResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the [Connection Profile](https://auth0.com/docs/authenticate/enterprise-connections/connection-profile) for this application. You should cache this information as it does not change frequently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.configuration.identity_providers.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Domains Verify
<details><summary><code>client.organization.domains.verify.<a href="src/auth0.myorganization/organization/domains/verify/client.py">create</a>(...) -> StartOrganizationDomainVerificationResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate the verification process for a domain specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.verify.create(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `OrgDomainId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Domains IdentityProviders
<details><summary><code>client.organization.domains.identity_providers.<a href="src/auth0.myorganization/organization/domains/identity_providers/client.py">get</a>(...) -> ListDomainIdentityProvidersResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of Identity Providers associated with a domain specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.domains.identity_providers.get(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `OrgDomainId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization IdentityProviders Domains
<details><summary><code>client.organization.identity_providers.domains.<a href="src/auth0.myorganization/organization/identity_providers/domains/client.py">create</a>(...) -> CreateIdpDomainResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Associate a domain with an Identity Provider specified by ID for this Organization. The domain must be claimed and verified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.domains.create(
    idp_id="idp_id",
    domain="my-domain.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `OrgDomainName` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.domains.<a href="src/auth0.myorganization/organization/identity_providers/domains/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a domain specified by name from an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.domains.delete(
    idp_id="idp_id",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `OrgDomainName` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization IdentityProviders Provisioning
<details><summary><code>client.organization.identity_providers.provisioning.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/client.py">get</a>(...) -> GetIdPProvisioningConfigResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the Provisioning Configuration for an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.get(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.provisioning.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/client.py">create</a>(...) -> CreateIdPProvisioningConfigResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Provisioning Configuration for an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.create(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.provisioning.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the Provisioning Configuration for an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.delete(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.provisioning.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/client.py">update_attributes</a>(...) -> GetIdPProvisioningConfigResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh the attribute mapping for the Provisioning Configuration of an Identity Provider specified by ID for this Organization. Mappings are reset to the admin-defined defaults.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.update_attributes(
    idp_id="idp_id",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization IdentityProviders Provisioning ScimTokens
<details><summary><code>client.organization.identity_providers.provisioning.scim_tokens.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/scim_tokens/client.py">list</a>(...) -> ListIdpProvisioningScimTokensResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of [SCIM tokens](https://auth0.com/docs/authenticate/protocols/scim/configure-inbound-scim#scim-endpoints-and-tokens) for the Provisioning Configuration of an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.scim_tokens.list(
    idp_id="idp_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.provisioning.scim_tokens.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/scim_tokens/client.py">create</a>(...) -> CreateIdpProvisioningScimTokenResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new SCIM token for the Provisioning Configuration of an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.scim_tokens.create(
    idp_id="idp_id",
    token_lifetime=86400,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**token_lifetime:** `typing.Optional[int]` — Lifetime of the token in seconds. Do not set for non-expiring tokens.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.identity_providers.provisioning.scim_tokens.<a href="src/auth0.myorganization/organization/identity_providers/provisioning/scim_tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a SCIM token specified by token ID for the Provisioning Configuration of an Identity Provider specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.identity_providers.provisioning.scim_tokens.delete(
    idp_id="idp_id",
    idp_scim_token_id="idp_scim_token_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idp_id:** `IdpId` 
    
</dd>
</dl>

<dl>
<dd>

**idp_scim_token_id:** `IdpProvisioningScimTokenId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization Members Roles
<details><summary><code>client.organization.members.roles.<a href="src/auth0.myorganization/organization/members/roles/client.py">list</a>(...) -> GetOrganizationMemberRolesResponseContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of roles assigned to a member specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.members.roles.list(
    user_id="user_id",
    from_="from",
    take=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `OrgMemberId` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — An optional cursor from which to start the selection (exclusive).
    
</dd>
</dl>

<dl>
<dd>

**take:** `typing.Optional[int]` — Number of results per page. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.members.roles.<a href="src/auth0.myorganization/organization/members/roles/client.py">assign</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign roles to a member specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.members.roles.assign(
    user_id="user_id",
    role_ids=[
        "rol_SO2j0sFo9NFa3F9w"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `OrgMemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationMemberRolesChangeRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.members.roles.<a href="src/auth0.myorganization/organization/members/roles/client.py">unassign</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove roles from a member specified by ID for this Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from auth0.myorganization import Auth0
from auth0.myorganization.environment import Auth0Environment

client = Auth0(
    token="<token>",
    environment=Auth0Environment.DEFAULT,
)

client.organization.members.roles.unassign(
    user_id="user_id",
    role_ids=[
        "rol_SO2j0sFo9NFa3F9w"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `OrgMemberId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrganizationMemberRolesChangeRequestContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>


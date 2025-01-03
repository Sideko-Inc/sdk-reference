
### login <a name="login"></a>
Logs user into the system



**API Endpoint**: `GET /user/login`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.auth.login();
```

### logout <a name="logout"></a>
Logs out current logged in user session



**API Endpoint**: `GET /user/logout`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.auth.logout();
```

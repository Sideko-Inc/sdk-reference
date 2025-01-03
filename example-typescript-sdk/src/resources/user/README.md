
### delete <a name="delete"></a>
Delete user

This can only be done by the logged in user.

**API Endpoint**: `DELETE /user/{username}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.user.delete({ username: "string" });
```

### get <a name="get"></a>
Get user by user name



**API Endpoint**: `GET /user/{username}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.user.get({ username: "string" });
```

### create <a name="create"></a>
Create user

This can only be done by the logged in user.

**API Endpoint**: `POST /user`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.user.create();
```

### update <a name="update"></a>
Update user

This can only be done by the logged in user.

**API Endpoint**: `PUT /user/{username}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.user.update({ usernamePath: "string" });
```

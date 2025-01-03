
### create <a name="create"></a>
Creates list of users with given input array

Creates list of users with given input array

**API Endpoint**: `POST /user/createWithList`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.user.createWithList.create({ data: [{}] });
```

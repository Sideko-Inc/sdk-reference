
### list <a name="list"></a>
Finds Pets by status

Multiple status values can be provided with comma separated strings

**API Endpoint**: `GET /pet/findByStatus`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.status.list();
```

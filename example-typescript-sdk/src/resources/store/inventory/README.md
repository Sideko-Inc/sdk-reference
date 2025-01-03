
### get <a name="get"></a>
Returns pet inventories by status

Returns a map of status codes to quantities

**API Endpoint**: `GET /store/inventory`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.store.inventory.get();
```


### list <a name="list"></a>
Finds Pets by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

**API Endpoint**: `GET /pet/findByTags`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.tag.list();
```

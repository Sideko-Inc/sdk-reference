
### upload <a name="upload"></a>
uploads an image



**API Endpoint**: `POST /pet/{petId}/uploadImage`

#### Example Snippet

```typescript
import fs from "fs";
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});
const uploadFile = fs.createReadStream("uploads/file.pdf");
const res = await client.pet.image.upload({ data: uploadFile, petId: 123 });
```

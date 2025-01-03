
### delete <a name="delete"></a>
Deletes a pet



**API Endpoint**: `DELETE /pet/{petId}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.delete({ petId: 123 });
```

### get <a name="get"></a>
Find pet by ID

Returns a single pet

**API Endpoint**: `GET /pet/{petId}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.get({ petId: 123 });
```

### create <a name="create"></a>
Add a new pet to the store

Add a new pet to the store

**API Endpoint**: `POST /pet`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.create({ name: "doggie", photoUrls: ["string"] });
```

### update_form <a name="update_form"></a>
Updates a pet in the store with form data



**API Endpoint**: `POST /pet/{petId}`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.updateForm({ petId: 123 });
```

### update <a name="update"></a>
Update an existing pet

Update an existing pet by Id

**API Endpoint**: `PUT /pet`

#### Example Snippet

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});

const res = await client.pet.update({ name: "doggie", photoUrls: ["string"] });
```

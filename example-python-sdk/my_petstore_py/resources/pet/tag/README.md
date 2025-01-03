
### list <a name="list"></a>
Finds Pets by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

**API Endpoint**: `GET /pet/findByTags`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.tag.list()
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.tag.list()
```

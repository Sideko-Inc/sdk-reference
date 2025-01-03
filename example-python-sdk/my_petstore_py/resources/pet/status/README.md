
### list <a name="list"></a>
Finds Pets by status

Multiple status values can be provided with comma separated strings

**API Endpoint**: `GET /pet/findByStatus`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.status.list()
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.status.list()
```


### get <a name="get"></a>
Returns pet inventories by status

Returns a map of status codes to quantities

**API Endpoint**: `GET /store/inventory`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.store.inventory.get()
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.store.inventory.get()
```

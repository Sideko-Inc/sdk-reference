
### create <a name="create"></a>
Creates list of users with given input array

Creates list of users with given input array

**API Endpoint**: `POST /user/createWithList`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.user.create_with_list.create(data=[{}])
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.user.create_with_list.create(data=[{}])
```

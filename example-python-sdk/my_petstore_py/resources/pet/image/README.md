
### upload <a name="upload"></a>
uploads an image



**API Endpoint**: `POST /pet/{petId}/uploadImage`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.image.upload(data=open("uploads/file.pdf", "rb"), pet_id=123)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.image.upload(data=open("uploads/file.pdf", "rb"), pet_id=123)
```

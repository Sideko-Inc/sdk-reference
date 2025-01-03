
### delete <a name="delete"></a>
Deletes a pet



**API Endpoint**: `DELETE /pet/{petId}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.delete(pet_id=123)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.delete(pet_id=123)
```

### get <a name="get"></a>
Find pet by ID

Returns a single pet

**API Endpoint**: `GET /pet/{petId}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.get(pet_id=123)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.get(pet_id=123)
```

### create <a name="create"></a>
Add a new pet to the store

Add a new pet to the store

**API Endpoint**: `POST /pet`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.create(name="doggie", photo_urls=["string"], id=10)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.create(name="doggie", photo_urls=["string"], id=10)
```

### update_form <a name="update_form"></a>
Updates a pet in the store with form data



**API Endpoint**: `POST /pet/{petId}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.update_form(pet_id=123)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.update_form(pet_id=123)
```

### update <a name="update"></a>
Update an existing pet

Update an existing pet by Id

**API Endpoint**: `PUT /pet`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.pet.update(name="doggie", photo_urls=["string"], id=10)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.pet.update(name="doggie", photo_urls=["string"], id=10)
```

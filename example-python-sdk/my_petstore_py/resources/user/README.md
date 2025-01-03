
### delete <a name="delete"></a>
Delete user

This can only be done by the logged in user.

**API Endpoint**: `DELETE /user/{username}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.user.delete(username="string")
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.user.delete(username="string")
```

### get <a name="get"></a>
Get user by user name



**API Endpoint**: `GET /user/{username}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.user.get(username="string")
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.user.get(username="string")
```

### create <a name="create"></a>
Create user

This can only be done by the logged in user.

**API Endpoint**: `POST /user`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.user.create(
    email_field="john@email.com",
    first_name="John",
    id=10,
    last_name="James",
    password="12345",
    phone="12345",
    user_status=1,
    username="theUser",
)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.user.create(
    email_field="john@email.com",
    first_name="John",
    id=10,
    last_name="James",
    password="12345",
    phone="12345",
    user_status=1,
    username="theUser",
)
```

### update <a name="update"></a>
Update user

This can only be done by the logged in user.

**API Endpoint**: `PUT /user/{username}`

#### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = client.user.update(
    username_path="string",
    email_field="john@email.com",
    first_name="John",
    id=10,
    last_name="James",
    password="12345",
    phone="12345",
    user_status=1,
    username="theUser",
)
```

#### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
res = await client.user.update(
    username_path="string",
    email_field="john@email.com",
    first_name="John",
    id=10,
    last_name="James",
    password="12345",
    phone="12345",
    user_status=1,
    username="theUser",
)
```

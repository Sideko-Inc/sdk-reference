
# Sideko Generated SDK Swagger Petstore - OpenAPI 3.0 Python SDK
The purpose of this project is to view Sideko generated python code as a reference to understand how it might look for your APIs.

## Overview
This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:
- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

### Synchronous Client

```python
from my_petstore_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
```

### Asynchronous Client

```python
from my_petstore_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), oauth_token=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [auth](my_petstore_py/resources/auth/README.md)

* [login](my_petstore_py/resources/auth/README.md#login) - Logs user into the system
* [logout](my_petstore_py/resources/auth/README.md#logout) - Logs out current logged in user session

### [pet](my_petstore_py/resources/pet/README.md)

* [create](my_petstore_py/resources/pet/README.md#create) - Add a new pet to the store
* [delete](my_petstore_py/resources/pet/README.md#delete) - Deletes a pet
* [get](my_petstore_py/resources/pet/README.md#get) - Find pet by ID
* [update](my_petstore_py/resources/pet/README.md#update) - Update an existing pet
* [update_form](my_petstore_py/resources/pet/README.md#update_form) - Updates a pet in the store with form data

### [pet.image](my_petstore_py/resources/pet/image/README.md)

* [upload](my_petstore_py/resources/pet/image/README.md#upload) - uploads an image

### [pet.status](my_petstore_py/resources/pet/status/README.md)

* [list](my_petstore_py/resources/pet/status/README.md#list) - Finds Pets by status

### [pet.tag](my_petstore_py/resources/pet/tag/README.md)

* [list](my_petstore_py/resources/pet/tag/README.md#list) - Finds Pets by tags

### [store.inventory](my_petstore_py/resources/store/inventory/README.md)

* [get](my_petstore_py/resources/store/inventory/README.md#get) - Returns pet inventories by status

### [store.order](my_petstore_py/resources/store/order/README.md)

* [delete](my_petstore_py/resources/store/order/README.md#delete) - Delete purchase order by ID
* [get](my_petstore_py/resources/store/order/README.md#get) - Find purchase order by ID
* [place](my_petstore_py/resources/store/order/README.md#place) - Place an order for a pet

### [user](my_petstore_py/resources/user/README.md)

* [create](my_petstore_py/resources/user/README.md#create) - Create user
* [delete](my_petstore_py/resources/user/README.md#delete) - Delete user
* [get](my_petstore_py/resources/user/README.md#get) - Get user by user name
* [update](my_petstore_py/resources/user/README.md#update) - Update user

### [user.create_with_list](my_petstore_py/resources/user/create_with_list/README.md)

* [create](my_petstore_py/resources/user/create_with_list/README.md#create) - Creates list of users with given input array

<!-- MODULE DOCS END -->

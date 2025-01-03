
# Sideko Generated SDK Swagger Petstore - OpenAPI 3.0 Typescript SDK
The purpose of this project is to view Sideko generated python code as a reference to understand how it might look for your APIs.

## Overview
This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about
Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!
You can now help us improve the API whether it's by making changes to the definition itself or to the code.
That way, with time, we can improve the API in general, and expose some of the new features in OAS3.

Some useful links:
- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

### Example Client Initialization

```typescript
import Client from "my_petstore_ts";

const client = new Client({
  apiKey: process.env["API_KEY"]!!,
  oauthToken: process.env["API_TOKEN"]!!,
});
```

## Module Documentation and Snippets

### [auth](src/resources/auth/README.md)

* [login](src/resources/auth/README.md#login) - Logs user into the system
* [logout](src/resources/auth/README.md#logout) - Logs out current logged in user session

### [pet](src/resources/pet/README.md)

* [create](src/resources/pet/README.md#create) - Add a new pet to the store
* [delete](src/resources/pet/README.md#delete) - Deletes a pet
* [get](src/resources/pet/README.md#get) - Find pet by ID
* [update](src/resources/pet/README.md#update) - Update an existing pet
* [update_form](src/resources/pet/README.md#update_form) - Updates a pet in the store with form data

### [pet.image](src/resources/pet/image/README.md)

* [upload](src/resources/pet/image/README.md#upload) - uploads an image

### [pet.status](src/resources/pet/status/README.md)

* [list](src/resources/pet/status/README.md#list) - Finds Pets by status

### [pet.tag](src/resources/pet/tag/README.md)

* [list](src/resources/pet/tag/README.md#list) - Finds Pets by tags

### [store.inventory](src/resources/store/inventory/README.md)

* [get](src/resources/store/inventory/README.md#get) - Returns pet inventories by status

### [store.order](src/resources/store/order/README.md)

* [delete](src/resources/store/order/README.md#delete) - Delete purchase order by ID
* [get](src/resources/store/order/README.md#get) - Find purchase order by ID
* [place](src/resources/store/order/README.md#place) - Place an order for a pet

### [user](src/resources/user/README.md)

* [create](src/resources/user/README.md#create) - Create user
* [delete](src/resources/user/README.md#delete) - Delete user
* [get](src/resources/user/README.md#get) - Get user by user name
* [update](src/resources/user/README.md#update) - Update user

### [user.create_with_list](src/resources/user/create-with-list/README.md)

* [create](src/resources/user/create-with-list/README.md#create) - Creates list of users with given input array

<!-- MODULE DOCS END -->

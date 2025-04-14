import httpx
import typing
import typing_extensions

from my_petstore_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from my_petstore_py.resources.pet.image import AsyncImageClient, ImageClient
from my_petstore_py.resources.pet.status import AsyncStatusClient, StatusClient
from my_petstore_py.resources.pet.tag import AsyncTagClient, TagClient
from my_petstore_py.types import models, params


class PetClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.status = StatusClient(base_client=self._base_client)
        self.tag = TagClient(base_client=self._base_client)
        self.image = ImageClient(base_client=self._base_client)

    def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet



        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Generated default response

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.delete(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["petstore_auth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID

        Returns a single pet

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.get(pet_id=123)
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key", "petstore_auth"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store

        Add a new pet to the store

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["petstore_auth"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def update_form(
        self,
        *,
        pet_id: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Updates a pet in the store with form data



        POST /pet/{petId}

        Args:
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            petId: ID of pet that needs to be updated
            request_options: Additional options to customize the HTTP request

        Returns:
            Generated default response

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.update_form(pet_id=123)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet

        Update an existing pet by Id

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["petstore_auth"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncPetClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.status = AsyncStatusClient(base_client=self._base_client)
        self.tag = AsyncTagClient(base_client=self._base_client)
        self.image = AsyncImageClient(base_client=self._base_client)

    async def delete(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Deletes a pet



        DELETE /pet/{petId}

        Args:
            petId: Pet id to delete
            request_options: Additional options to customize the HTTP request

        Returns:
            Generated default response

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.delete(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/pet/{pet_id}",
            auth_names=["petstore_auth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, pet_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Find pet by ID

        Returns a single pet

        GET /pet/{petId}

        Args:
            petId: ID of pet to return
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.get(pet_id=123)
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/pet/{pet_id}",
            auth_names=["api_key", "petstore_auth"],
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Add a new pet to the store

        Add a new pet to the store

        POST /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.create(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="POST",
            path="/pet",
            auth_names=["petstore_auth"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def update_form(
        self,
        *,
        pet_id: int,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Updates a pet in the store with form data



        POST /pet/{petId}

        Args:
            name: Name of pet that needs to be updated
            status: Status of pet that needs to be updated
            petId: ID of pet that needs to be updated
            request_options: Additional options to customize the HTTP request

        Returns:
            Generated default response

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.update_form(pet_id=123)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "name",
                to_encodable(item=name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        name: str,
        photo_urls: typing.List[str],
        category: typing.Union[
            typing.Optional[params.Category], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[params.Tag]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Pet, BinaryResponse]:
        """
        Update an existing pet

        Update an existing pet by Id

        PUT /pet

        Args:
            category: Category
            id: int
            status: pet status in the store
            tags: typing.List[Tag]
            name: str
            photoUrls: typing.List[str]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.update(name="doggie", photo_urls=["string"], id=10)
        ```
        """
        _json = to_encodable(
            item={
                "category": category,
                "id": id,
                "status": status,
                "tags": tags,
                "name": name,
                "photo_urls": photo_urls,
            },
            dump_with=params._SerializerPet,
        )
        return await self._base_client.request(
            method="PUT",
            path="/pet",
            auth_names=["petstore_auth"],
            json=_json,
            cast_to=typing.Union[models.Pet, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

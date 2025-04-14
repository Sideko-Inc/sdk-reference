import typing

from my_petstore_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
)
from my_petstore_py.types import models, params


class CreateWithListClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: typing.List[params.User],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Creates list of users with given input array

        Creates list of users with given input array

        POST /user/createWithList

        Args:
            data: typing.List[User]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.create_with_list.create(
            data=[
                {
                    "email": "john@email.com",
                    "first_name": "John",
                    "id": 10,
                    "last_name": "James",
                    "password": "12345",
                    "phone": "12345",
                    "user_status": 1,
                    "username": "theUser",
                }
            ]
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.List[params._SerializerUser])
        return self._base_client.request(
            method="POST",
            path="/user/createWithList",
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncCreateWithListClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: typing.List[params.User],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, BinaryResponse]:
        """
        Creates list of users with given input array

        Creates list of users with given input array

        POST /user/createWithList

        Args:
            data: typing.List[User]
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.create_with_list.create(
            data=[
                {
                    "email": "john@email.com",
                    "first_name": "John",
                    "id": 10,
                    "last_name": "James",
                    "password": "12345",
                    "phone": "12345",
                    "user_status": 1,
                    "username": "theUser",
                }
            ]
        )
        ```
        """
        _json = to_encodable(item=data, dump_with=typing.List[params._SerializerUser])
        return await self._base_client.request(
            method="POST",
            path="/user/createWithList",
            json=_json,
            cast_to=typing.Union[models.User, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

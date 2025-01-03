import typing

from my_petstore_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from my_petstore_py.resources.user.create_with_list import (
    AsyncCreateWithListClient,
    CreateWithListClient,
)
from my_petstore_py import BinaryResponse
from my_petstore_py.types import models, params


class UserClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

        self.create_with_list = CreateWithListClient(base_client=self._base_client)

    def delete(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        This can only be done by the logged in user.

        DELETE /user/{username}

        Args:
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            None

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.delete(username="string")
        ```

        """
        return self._base_client.request(
            method="DELETE",
            path=f"/user/{username}",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.User, models.User]:
        """


        GET /user/{username}

        Args:
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.get(username="string")
        ```

        """
        return self._base_client.request(
            method="GET",
            path=f"/user/{username}",
            cast_to=typing.Union[models.User, models.User],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_status: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, models.User]:
        """
        This can only be done by the logged in user.

        POST /user

        Args:
            email: str
            firstName: str
            id: int
            lastName: str
            password: str
            phone: str
            userStatus: User Status
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.create(
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

        """
        _json = to_encodable(
            item={
                "email_field": email_field,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "password": password,
                "phone": phone,
                "user_status": user_status,
                "username": username,
            },
            dump_with=params._SerializerUser,
        )
        return self._base_client.request(
            method="POST",
            path="/user",
            json=_json,
            cast_to=typing.Union[models.User, models.User],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        username_path: str,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_status: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This can only be done by the logged in user.

        PUT /user/{username}

        Args:
            email: str
            firstName: str
            id: int
            lastName: str
            password: str
            phone: str
            userStatus: User Status
            username: str
            username_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.user.update(
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

        """
        _json = to_encodable(
            item={
                "email_field": email_field,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "password": password,
                "phone": phone,
                "user_status": user_status,
                "username": username,
            },
            dump_with=params._SerializerUser,
        )
        self._base_client.request(
            method="PUT",
            path=f"/user/{username_path}",
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncUserClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

        self.create_with_list = AsyncCreateWithListClient(base_client=self._base_client)

    async def delete(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        This can only be done by the logged in user.

        DELETE /user/{username}

        Args:
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            None

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.delete(username="string")
        ```

        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/user/{username}",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, username: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Union[models.User, models.User]:
        """


        GET /user/{username}

        Args:
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.get(username="string")
        ```

        """
        return await self._base_client.request(
            method="GET",
            path=f"/user/{username}",
            cast_to=typing.Union[models.User, models.User],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_status: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.User, models.User]:
        """
        This can only be done by the logged in user.

        POST /user

        Args:
            email: str
            firstName: str
            id: int
            lastName: str
            password: str
            phone: str
            userStatus: User Status
            username: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.create(
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

        """
        _json = to_encodable(
            item={
                "email_field": email_field,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "password": password,
                "phone": phone,
                "user_status": user_status,
                "username": username,
            },
            dump_with=params._SerializerUser,
        )
        return await self._base_client.request(
            method="POST",
            path="/user",
            json=_json,
            cast_to=typing.Union[models.User, models.User],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        username_path: str,
        email_field: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        phone: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_status: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This can only be done by the logged in user.

        PUT /user/{username}

        Args:
            email: str
            firstName: str
            id: int
            lastName: str
            password: str
            phone: str
            userStatus: User Status
            username: str
            username_path: str
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.user.update(
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

        """
        _json = to_encodable(
            item={
                "email_field": email_field,
                "first_name": first_name,
                "id": id,
                "last_name": last_name,
                "password": password,
                "phone": phone,
                "user_status": user_status,
                "username": username,
            },
            dump_with=params._SerializerUser,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/user/{username_path}",
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

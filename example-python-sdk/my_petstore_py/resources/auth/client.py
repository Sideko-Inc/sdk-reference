import httpx
import typing

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


class AuthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def login(
        self,
        *,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[str, BinaryResponse]:
        """
        Logs user into the system



        GET /user/login

        Args:
            password: The password for login in clear text
            username: The user name for login
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.auth.login()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(password, type_utils.NotGiven):
            encode_query_param(
                _query,
                "password",
                to_encodable(item=password, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/user/login",
            query_params=_query,
            cast_to=typing.Union[str, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Logs out current logged in user session



        GET /user/logout

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.auth.logout()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/user/logout",
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )


class AsyncAuthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def login(
        self,
        *,
        password: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        username: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[str, BinaryResponse]:
        """
        Logs user into the system



        GET /user/login

        Args:
            password: The password for login in clear text
            username: The user name for login
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.auth.login()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(password, type_utils.NotGiven):
            encode_query_param(
                _query,
                "password",
                to_encodable(item=password, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(username, type_utils.NotGiven):
            encode_query_param(
                _query,
                "username",
                to_encodable(item=username, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/user/login",
            query_params=_query,
            cast_to=typing.Union[str, BinaryResponse],
            request_options=request_options or default_request_options(),
        )

    async def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> httpx.Response:
        """
        Logs out current logged in user session



        GET /user/logout

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.auth.logout()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/user/logout",
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

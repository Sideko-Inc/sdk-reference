import typing

from my_petstore_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_param,
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
    ) -> typing.Union[str, str]:
        """


        GET /user/login

        Args:
            password: str
            username: str
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
            _query["password"] = encode_param(password, False)
        if not isinstance(username, type_utils.NotGiven):
            _query["username"] = encode_param(username, False)
        return self._base_client.request(
            method="GET",
            path="/user/login",
            query_params=_query,
            cast_to=typing.Union[str, str],
            request_options=request_options or default_request_options(),
        )

    def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


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
        self._base_client.request(
            method="GET",
            path="/user/logout",
            cast_to=type(None),
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
    ) -> typing.Union[str, str]:
        """


        GET /user/login

        Args:
            password: str
            username: str
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
            _query["password"] = encode_param(password, False)
        if not isinstance(username, type_utils.NotGiven):
            _query["username"] = encode_param(username, False)
        return await self._base_client.request(
            method="GET",
            path="/user/login",
            query_params=_query,
            cast_to=typing.Union[str, str],
            request_options=request_options or default_request_options(),
        )

    async def logout(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


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
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

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
from my_petstore_py.types import models


class StatusClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by status

        Multiple status values can be provided with comma separated strings

        GET /pet/findByStatus

        Args:
            status: Status values that need to be considered for filter
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.status.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["available", "pending", "sold"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/pet/findByStatus",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncStatusClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["available", "pending", "sold"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by status

        Multiple status values can be provided with comma separated strings

        GET /pet/findByStatus

        Args:
            status: Status values that need to be considered for filter
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.status.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["available", "pending", "sold"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/pet/findByStatus",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )

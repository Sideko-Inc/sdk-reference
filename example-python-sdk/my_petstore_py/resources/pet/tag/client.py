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
from my_petstore_py.types import models


class TagClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by tags

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        GET /pet/findByTags

        Args:
            tags: Tags to filter by
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.tag.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(tags, type_utils.NotGiven):
            encode_query_param(
                _query,
                "tags",
                to_encodable(item=tags, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/pet/findByTags",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )


class AsyncTagClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[typing.List[models.Pet], BinaryResponse]:
        """
        Finds Pets by tags

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        GET /pet/findByTags

        Args:
            tags: Tags to filter by
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.tag.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(tags, type_utils.NotGiven):
            encode_query_param(
                _query,
                "tags",
                to_encodable(item=tags, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/pet/findByTags",
            auth_names=["petstore_auth"],
            query_params=_query,
            cast_to=typing.Union[typing.List[models.Pet], BinaryResponse],
            request_options=request_options or default_request_options(),
        )

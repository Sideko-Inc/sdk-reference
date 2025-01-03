import typing

from my_petstore_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from my_petstore_py.types import models


class InventoryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetStoreInventoryResponse:
        """
        Returns a map of status codes to quantities

        GET /store/inventory

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.store.inventory.get()
        ```

        """
        return self._base_client.request(
            method="GET",
            path="/store/inventory",
            auth_names=["api_key"],
            cast_to=models.GetStoreInventoryResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncInventoryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GetStoreInventoryResponse:
        """
        Returns a map of status codes to quantities

        GET /store/inventory

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.store.inventory.get()
        ```

        """
        return await self._base_client.request(
            method="GET",
            path="/store/inventory",
            auth_names=["api_key"],
            cast_to=models.GetStoreInventoryResponse,
            request_options=request_options or default_request_options(),
        )

import typing
import io

from my_petstore_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_param,
    type_utils,
)
from my_petstore_py.types import models


class ImageClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def upload(
        self,
        *,
        data: typing.Union[typing.BinaryIO, io.BufferedReader],
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """


        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: str
            data: typing.Union[typing.BinaryIO, io.BufferedReader]
            petId: int
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.pet.image.upload(data=open("uploads/file.pdf", "rb"), pet_id=123)
        ```

        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            _query["additionalMetadata"] = encode_param(additional_metadata, False)
        _content = data.read()
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["petstore_auth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncImageClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def upload(
        self,
        *,
        data: typing.Union[typing.BinaryIO, io.BufferedReader],
        pet_id: int,
        additional_metadata: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApiResponse:
        """


        POST /pet/{petId}/uploadImage

        Args:
            additionalMetadata: str
            data: typing.Union[typing.BinaryIO, io.BufferedReader]
            petId: int
            request_options: Additional options to customize the HTTP request

        Returns:
            successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.pet.image.upload(data=open("uploads/file.pdf", "rb"), pet_id=123)
        ```

        """
        _query: QueryParams = {}
        if not isinstance(additional_metadata, type_utils.NotGiven):
            _query["additionalMetadata"] = encode_param(additional_metadata, False)
        _content = data.read()
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="POST",
            path=f"/pet/{pet_id}/uploadImage",
            auth_names=["petstore_auth"],
            query_params=_query,
            content=_content,
            content_type=_content_type,
            cast_to=models.ApiResponse,
            request_options=request_options or default_request_options(),
        )

import pytest
import pydantic

from my_petstore_py import AsyncClient, Client
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_upload_200_success_default():
    """Tests a POST request to the /pet/{petId}/uploadImage endpoint.

    Operation: upload
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : ApiResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        api_key="API_KEY", oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER
    )
    response = client.pet.image.upload(data=open("uploads/file.pdf", "rb"), pet_id=123)
    adapter = pydantic.TypeAdapter(models.ApiResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_upload_200_success_default():
    """Tests a POST request to the /pet/{petId}/uploadImage endpoint.

    Operation: upload
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : ApiResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        api_key="API_KEY", oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER
    )
    response = await client.pet.image.upload(
        data=open("uploads/file.pdf", "rb"), pet_id=123
    )
    adapter = pydantic.TypeAdapter(models.ApiResponse)
    adapter.validate_python(response)

import pytest
import typing
import pydantic

from my_petstore_py import AsyncClient, Client
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_list_200_generated_success():
    """Tests a GET request to the /pet/findByTags endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[typing.List[Pet], typing.List[Pet]]

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
    response = client.pet.tag.list()
    adapter = pydantic.TypeAdapter(
        typing.Union[typing.List[models.Pet], typing.List[models.Pet]]
    )
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Tests a GET request to the /pet/findByTags endpoint.

    Operation: list
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[typing.List[Pet], typing.List[Pet]]

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
    response = await client.pet.tag.list()
    adapter = pydantic.TypeAdapter(
        typing.Union[typing.List[models.Pet], typing.List[models.Pet]]
    )
    adapter.validate_python(response)

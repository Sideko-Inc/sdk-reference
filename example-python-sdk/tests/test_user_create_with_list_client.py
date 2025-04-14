import pydantic
import pytest

from my_petstore_py import AsyncClient, Client
from my_petstore_py.core import BinaryResponse
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_create_200_success_default():
    """Tests a POST request to the /user/createWithList endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.User, BinaryResponse]

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
    response = client.user.create_with_list.create(
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
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /user/createWithList endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.User, BinaryResponse]

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
    response = await client.user.create_with_list.create(
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
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"

import pytest
import typing
import pydantic

from my_petstore_py import AsyncClient, BinaryResponse, Client
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_update_default_success_default():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: default
    Mode: Synchronous execution

    Empty response expected

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
    response = client.user.update(
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
    adapter = pydantic.TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_update_default_success_default():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: default
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.user.update(
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
    adapter = pydantic.TypeAdapter(None)
    adapter.validate_python(response)


def test_create_default_success_default():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: default
    Mode: Synchronous execution

    Response : typing.Union[User, User]

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
    response = client.user.create(
        email_field="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    adapter = pydantic.TypeAdapter(typing.Union[models.User, models.User])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_default_success_default():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: default
    Mode: Asynchronous execution

    Response : typing.Union[User, User]

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
    response = await client.user.create(
        email_field="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    adapter = pydantic.TypeAdapter(typing.Union[models.User, models.User])
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[User, User]

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
    response = client.user.get(username="string")
    adapter = pydantic.TypeAdapter(typing.Union[models.User, models.User])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[User, User]

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
    response = await client.user.get(username="string")
    adapter = pydantic.TypeAdapter(typing.Union[models.User, models.User])
    adapter.validate_python(response)


def test_delete_2xx_generated_success():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 2xx
    Mode: Synchronous execution

    Response : typing.Union[typing.BinaryIO, io.BufferedReader]

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
    response = client.user.delete(username="string")
    assert isinstance(response, BinaryResponse)


@pytest.mark.asyncio
async def test_await_delete_2xx_generated_success():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 2xx
    Mode: Asynchronous execution

    Response : typing.Union[typing.BinaryIO, io.BufferedReader]

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
    response = await client.user.delete(username="string")
    assert isinstance(response, BinaryResponse)

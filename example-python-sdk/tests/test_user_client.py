import httpx
import pydantic
import pytest

from my_petstore_py import AsyncClient, Client
from my_petstore_py.core import BinaryResponse
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_update_default_success_default():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: default
    Mode: Synchronous execution

    Response : httpx.Response

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
        email="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_update_default_success_default():
    """Tests a PUT request to the /user/{username} endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: default
    Mode: Asynchronous execution

    Response : httpx.Response

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
        email="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    assert isinstance(response, httpx.Response)


def test_create_default_success_default():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: default
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
    response = client.user.create(
        email="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_default_success_default():
    """Tests a POST request to the /user endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: default
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
    response = await client.user.create(
        email="john@email.com",
        first_name="John",
        id=10,
        last_name="James",
        password="12345",
        phone="12345",
        user_status=1,
        username="theUser",
    )
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: generated_success
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
    response = client.user.get(username="string")
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /user/{username} endpoint.

    Operation: get
    Test Case ID: generated_success
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
    response = await client.user.get(username="string")
    try:
        pydantic.TypeAdapter(models.User).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


def test_delete_2xx_generated_success():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 2xx
    Mode: Synchronous execution

    Response : httpx.Response

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
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_2xx_generated_success():
    """Tests a DELETE request to the /user/{username} endpoint.

    Operation: delete
    Test Case ID: generated_success
    Expected Status: 2xx
    Mode: Asynchronous execution

    Response : httpx.Response

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
    assert isinstance(response, httpx.Response)

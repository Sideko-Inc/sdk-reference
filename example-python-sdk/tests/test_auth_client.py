import pytest
import typing
import pydantic

from my_petstore_py import AsyncClient, Client
from my_petstore_py.environment import Environment


def test_logout_default_generated_success():
    """Tests a GET request to the /user/logout endpoint.

    Operation: logout
    Test Case ID: generated_success
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
    response = client.auth.logout()
    adapter = pydantic.TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_logout_default_generated_success():
    """Tests a GET request to the /user/logout endpoint.

    Operation: logout
    Test Case ID: generated_success
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
    response = await client.auth.logout()
    adapter = pydantic.TypeAdapter(None)
    adapter.validate_python(response)


def test_login_200_generated_success():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[str, str]

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
    response = client.auth.login()
    adapter = pydantic.TypeAdapter(typing.Union[str, str])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_login_200_generated_success():
    """Tests a GET request to the /user/login endpoint.

    Operation: login
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[str, str]

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
    response = await client.auth.login()
    adapter = pydantic.TypeAdapter(typing.Union[str, str])
    adapter.validate_python(response)

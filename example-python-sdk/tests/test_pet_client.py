import pytest
import typing
import pydantic

from my_petstore_py import AsyncClient, BinaryResponse, Client
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_update_200_success_default():
    """Tests a PUT request to the /pet endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = client.pet.update(name="doggie", photo_urls=["string"], id=10)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_update_200_success_default():
    """Tests a PUT request to the /pet endpoint.

    Operation: update
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = await client.pet.update(name="doggie", photo_urls=["string"], id=10)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


def test_update_form_2xx_generated_success():
    """Tests a POST request to the /pet/{petId} endpoint.

    Operation: update_form
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
    response = client.pet.update_form(pet_id=123)
    assert isinstance(response, BinaryResponse)


@pytest.mark.asyncio
async def test_await_update_form_2xx_generated_success():
    """Tests a POST request to the /pet/{petId} endpoint.

    Operation: update_form
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
    response = await client.pet.update_form(pet_id=123)
    assert isinstance(response, BinaryResponse)


def test_create_200_success_default():
    """Tests a POST request to the /pet endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = client.pet.create(name="doggie", photo_urls=["string"], id=10)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_200_success_default():
    """Tests a POST request to the /pet endpoint.

    Operation: create
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = await client.pet.create(name="doggie", photo_urls=["string"], id=10)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Tests a GET request to the /pet/{petId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = client.pet.get(pet_id=123)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /pet/{petId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[Pet, Pet]

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
    response = await client.pet.get(pet_id=123)
    adapter = pydantic.TypeAdapter(typing.Union[models.Pet, models.Pet])
    adapter.validate_python(response)


def test_delete_2xx_generated_success():
    """Tests a DELETE request to the /pet/{petId} endpoint.

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
    response = client.pet.delete(pet_id=123)
    assert isinstance(response, BinaryResponse)


@pytest.mark.asyncio
async def test_await_delete_2xx_generated_success():
    """Tests a DELETE request to the /pet/{petId} endpoint.

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
    response = await client.pet.delete(pet_id=123)
    assert isinstance(response, BinaryResponse)

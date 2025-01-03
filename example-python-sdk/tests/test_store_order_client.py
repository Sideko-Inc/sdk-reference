import pytest
import typing
import pydantic

from my_petstore_py import AsyncClient, BinaryResponse, Client
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_place_200_success_default():
    """Tests a POST request to the /store/order endpoint.

    Operation: place
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : Order

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
    response = client.store.order.place(
        id=10, pet_id=198772, quantity=7, status="approved"
    )
    adapter = pydantic.TypeAdapter(models.Order)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_place_200_success_default():
    """Tests a POST request to the /store/order endpoint.

    Operation: place
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : Order

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
    response = await client.store.order.place(
        id=10, pet_id=198772, quantity=7, status="approved"
    )
    adapter = pydantic.TypeAdapter(models.Order)
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[Order, Order]

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
    response = client.store.order.get(order_id=123)
    adapter = pydantic.TypeAdapter(typing.Union[models.Order, models.Order])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[Order, Order]

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
    response = await client.store.order.get(order_id=123)
    adapter = pydantic.TypeAdapter(typing.Union[models.Order, models.Order])
    adapter.validate_python(response)


def test_delete_2xx_generated_success():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

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
    response = client.store.order.delete(order_id=123)
    assert isinstance(response, BinaryResponse)


@pytest.mark.asyncio
async def test_await_delete_2xx_generated_success():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

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
    response = await client.store.order.delete(order_id=123)
    assert isinstance(response, BinaryResponse)

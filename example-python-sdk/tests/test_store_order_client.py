import httpx
import pydantic
import pytest

from my_petstore_py import AsyncClient, Client
from my_petstore_py.core import BinaryResponse
from my_petstore_py.environment import Environment
from my_petstore_py.types import models


def test_place_200_success_default():
    """Tests a POST request to the /store/order endpoint.

    Operation: place
    Test Case ID: success_default
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Order

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
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_place_200_success_default():
    """Tests a POST request to the /store/order endpoint.

    Operation: place
    Test Case ID: success_default
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Order

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
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


def test_get_200_generated_success():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.Order, BinaryResponse]

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
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Tests a GET request to the /store/order/{orderId} endpoint.

    Operation: get
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.Order, BinaryResponse]

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
    try:
        pydantic.TypeAdapter(models.Order).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    is_binary = isinstance(response, BinaryResponse)
    assert any([is_json, is_binary]), "failed response type check"


def test_delete_2xx_generated_success():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

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
    response = client.store.order.delete(order_id=123)
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_delete_2xx_generated_success():
    """Tests a DELETE request to the /store/order/{orderId} endpoint.

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
    response = await client.store.order.delete(order_id=123)
    assert isinstance(response, httpx.Response)

import httpx
import typing

from my_petstore_py.core import (
    AsyncBaseClient,
    AuthBearer,
    AuthKeyHeader,
    SyncBaseClient,
)
from my_petstore_py.environment import Environment
from my_petstore_py.resources.pet import AsyncPetClient, PetClient
from my_petstore_py.resources.store import AsyncStoreClient, StoreClient
from my_petstore_py.resources.user import AsyncUserClient, UserClient
from my_petstore_py.resources.auth import AsyncAuthClient, AuthClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: Environment = Environment.ENVIRONMENT,
        api_key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )
        self._base_client.register_auth(
            "api_key", AuthKeyHeader(header_name="api_key", val=api_key)
        )

        self.pet = PetClient(base_client=self._base_client)

        self.store = StoreClient(base_client=self._base_client)

        self.user = UserClient(base_client=self._base_client)

        self.auth = AuthClient(base_client=self._base_client)
        self._base_client.register_auth("petstore_auth", AuthBearer(val=oauth_token))


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: Environment = Environment.ENVIRONMENT,
        api_key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )
        self._base_client.register_auth(
            "api_key", AuthKeyHeader(header_name="api_key", val=api_key)
        )

        self.pet = AsyncPetClient(base_client=self._base_client)

        self.store = AsyncStoreClient(base_client=self._base_client)

        self.user = AsyncUserClient(base_client=self._base_client)

        self.auth = AsyncAuthClient(base_client=self._base_client)
        self._base_client.register_auth("petstore_auth", AuthBearer(val=oauth_token))


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")

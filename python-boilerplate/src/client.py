class Sideko:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )


class AsyncSideko:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")

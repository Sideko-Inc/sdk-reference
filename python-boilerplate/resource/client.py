class SidekoResourceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client


class AsyncSidekoResourceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

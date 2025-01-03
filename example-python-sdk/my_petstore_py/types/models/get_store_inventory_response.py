import typing
import pydantic


class GetStoreInventoryResponse(pydantic.BaseModel):
    """
    GetStoreInventoryResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, int]

import typing
import typing_extensions
import pydantic


class User(typing_extensions.TypedDict):
    """
    User
    """

    email_field: typing_extensions.NotRequired[str]

    first_name: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[int]

    last_name: typing_extensions.NotRequired[str]

    password: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]

    user_status: typing_extensions.NotRequired[int]
    """
    User Status
    """

    username: typing_extensions.NotRequired[str]


class _SerializerUser(pydantic.BaseModel):
    """
    Serializer for User handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    first_name: typing.Optional[str] = pydantic.Field(alias="firstName", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="lastName", default=None)
    password: typing.Optional[str] = pydantic.Field(alias="password", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    user_status: typing.Optional[int] = pydantic.Field(alias="userStatus", default=None)
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)

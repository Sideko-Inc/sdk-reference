import typing
import pydantic


class User(pydantic.BaseModel):
    """
    User
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    first_name: typing.Optional[str] = pydantic.Field(alias="firstName", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="lastName", default=None)
    password: typing.Optional[str] = pydantic.Field(alias="password", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    user_status: typing.Optional[int] = pydantic.Field(alias="userStatus", default=None)
    """
    User Status
    """
    username: typing.Optional[str] = pydantic.Field(alias="username", default=None)

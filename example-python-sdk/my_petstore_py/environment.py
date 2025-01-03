import enum


class Environment(enum.Enum):
    ENVIRONMENT = "https://petstore3.swagger.io/api/v3"
    MOCK_SERVER = "https://petstore3.swagger.io/api/v3"  # in production, this would be a Sideko mock server URL

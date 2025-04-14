import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    PRODUCTION = "https://petstore3.swagger.io/api/v3"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/petstore/0.1.0"

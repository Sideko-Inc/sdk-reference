# Python SDK Boilerplate

This directory contains the boilerplate code used by Sideko to generate Python SDKs. The code here serves as a foundation that Sideko's generator builds upon to create complete, production-ready SDK clients.

## Directory Structure

### Core (`./core/`)
Contains utility code for core SDK functionality:
- Network request handling
- Authentication management
- Response parsing
- Error handling

### GitHub Actions (`./github_actions/`)
CI/CD workflow templates for:
- Running tests
- Type checking
- Publishing packages

### Package Configuration (`./pkg/`)
Files related to package management and git:
- Git configuration
- Distribution utilities

### Resource Templates (`./resource/`)
Boilerplate for individual API resource clients.

```python
class SidekoResourceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

class AsyncSidekoResourceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
```

These base classes are transformed during generation:
- Classes are renamed based on your configuration
- Methods are added based on API endpoints
- Type hints are generated from schemas

### Source (`./src/`)
Base SDK structure including:
- Client initialization
- Configuration handling
- Resource client registration
- Type definitions
- Constants like server URLs

## Code Generation

The code in this repository is intentionally incomplete. During generation:
1. Sideko analyzes your API specification
2. Classes and methods are renamed according to configuration
3. API-specific code is injected
4. Types are created and linked

### Customization Points

The boilerplate includes strategic points where Sideko injects generated code:
- Resource class names (e.g., `SidekoResourceClient` → `PetsClient`)
- Method signatures based on endpoints
- Type definitions from schemas
- Authentication method implementations
- API-specific configuration options

## Usage

This code is not meant to be used directly. Instead:
1. Use Sideko's API to generate your SDK
2. The generator will use this boilerplate as a foundation
3. Your API-specific code will be added automatically
4. The result will be a complete, typed SDK that is automatically maintained by Sideko as your APIs change

## Contributing

While this is primarily boilerplate code, we welcome:
- Improvements to utility functions
- Documentation enhancements
- Suggestions for better Python patterns

For more information about SDK generation, visit [sideko.dev](https://sideko.dev).
# Sideko SDK Generator Boilerplate and Examples

This repository contains the foundational boilerplate code used by [Sideko](https://sideko.dev) for generating SDK client libraries. Unlike traditional SDK generators that rely on templates, Sideko employs advanced syntax tree analysis to generate code that closely mirrors human-written code.

## Current Status

Currently, this repository includes boilerplate code for:
- [Python](./python-boilerplate/README.md)
- [Typescript](./typescript-boilerplate/README.md)

Sideko generates SDKs in many other languages, and those boilerplates will be added to this library in the future.

## How It Works

Sideko takes a unique approach to SDK generation:

1. The boilerplate code in this repository serves as the starting point
2. Sideko's analyzer, written in Rust, processes your API specification
3. Using syntax tree analysis, it augments the boilerplate with API-specific code
4. The result is a maintainable, high-quality SDK that can be modified
5. Currently, users of Sideko can add new files to the repos, modify the README, and add other dependencies, and annotate the generated files in a few specific files
6. In the future, most of SDK will be editable, unlocking ultimate flexibility in the SDKs

This approach offers several advantages over template-based generation:
- More natural, human-like code structure
- Better code quality and maintainability
- Safe manual editing without breaking regeneration capability
- Consistent coding patterns across different APIs

## Example

The repository includes example generated SDKs for the Swagger Petstore API (`./petstore-openapi.json`) to demonstrate the output structure and generated documentation.

## Technical Details

- The actual code generation is performed by Sideko's generation engine written in Rust
- Generated code is also formatted by the Rust generation engine
- Generation is executed via Sideko's API
- The boilerplate usually serves to help generated code utilize auth, make network requests, parse responses, stream data, ect. Each langauge is different, and sometimes the generated code has to do more work. For a language like Python, the boilerplate actually does a lot.
- Sideko SDKs are fully typed, but the type systems require no boilerplate, so there is no type-related code in this repo.

## Getting Started

To use Sideko for generating your own SDKs visit [Sideko's website](https://sideko.dev)

## Contributing

While this repository primarily serves as a reference for Sideko's boilerplate code, we welcome:
- Documentation improvements
- Boilerplate Code improvements
- SDK Generator improvements - tell us something you'd like to see changed referencing the example SDK

## License

[MIT License](./LICENSE)


## Contact

For more information about Sideko and our SDK generation capabilities, visit [sideko.dev](https://sideko.dev).
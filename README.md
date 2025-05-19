# Factorio Blueprint String JSON Schemas

This document is intended to be an open source public specification for the decoded JSON representation of Factorio blueprint strings. 

This place is intended to provide a centralized resource from which contributions and corrections to the blueprint string format can be made. By providing this specification in a standardized format (JSON schema) this allows for the potential of automatic integration of developed tools

## Organization

Each version of the blueprint string format is located in it's respective semantically versioned folder in the `schemas` master folder. "Global" schemas that are commonly used and reused throughout all specifications lie in the `schemas/common` folder.

## Specification

Each file is written as Draft 2020-compliant JSON schema. Titles and descriptions should also be provided, if a properties function is not immediately obvious.

To keep schemas concise and easy to maintain, large schemas are frequently split into multiple smaller schemas and `$ref`-erenced appropriately. `$defs` are also permitted if certain structures are reused often in *one* single schema; but if something is used in more than one place at once, referencing the schema is preferred.

In order to reduce the duplication of work, cross-referencing schemas between versions is not only permitted, but recommended if a schema is truly unchanged. In such cases, always prefer referencing schemas in earlier semantic versions; so schemas defined in folder `2.0.0` can reference schemas in defined in `1.0.0`, but not vise-versa.

## Usage

Individual schemas can be grabbed by taking their corresponding raw github URL
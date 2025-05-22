# Factorio Blueprint String JSON Schemas

This document is intended to be an open source public specification for the decoded JSON format of Factorio blueprint strings. 

This place is intended to provide a centralized resource from which contributions and corrections to the blueprint string format can be made. By providing this specification in a standardized format (JSON schema) this allows for the potential of automatic integration of developed tools.

If a JSON dictionary validates against the schemas defined here, it should import into Factorio without issue.

## Organization

Each file is written as Draft 2020-compliant JSON schema. In addition to required fields, documentation metadata `"title"` and `"description"` fields should also be provided (if a properties function is not immediately obvious), as well as comments for maintainers.

All schemas corresponding to a particular blueprint string format is located in it's respective semantically versioned subfolder in the `schemas` folder. A versioned schema is valid for all versions above until the next versioned schema; so the schemas in folder `1.0.0` will validate up to and excluding version `1.1.0` - and the `1.1.0` folder will validate for versions up until `2.0.0`, and so on.

"Global" schemas that are commonly used and reused throughout all specifications lie in the `common` folder.

## Specification

To keep schemas concise and easy to maintain, large schemas are frequently split into multiple smaller schemas and `"$ref"`-erenced appropriately. `$defs` are also permitted if certain structures are reused often in *one* single schema; but if something is used in more than one place at once, referencing the schema is preferred.

In an effort towards DRY, cross-referencing schemas *between* versions is not only permitted, but recommended in cases where schemas are exactly equivalent. In such cases, always prefer referencing schemas in earlier semantic versions; so schemas defined in folder `2.0.0` can reference schemas in defined in `1.0.0`, but not vise-versa.

## Usage

Here's a simple illustration of how to use the schemas to validate some JSON dictionary using Python and `jsonschema`:

```py
from referencing import Registry, Resource
from jsonschema import Draft202012Validator

import base64
import json
import os
import zlib

def grab_json_file(*path) -> dict:
    with open(os.path.join(*path), "r") as json_file:
        return json.load(json_file)

# Create a registry object which will search the `schemas` folder for references
# Schemas will only be grabbed if they are needed, and reused if needed more than once
def retrieve_from_path(uri: str) -> Resource:
    return Resource.from_contents(grab_json_file("schemas", uri))

registry = Registry(retrieve=retrieve_from_path)

# Create a validator for a 2.0 blueprint
validator = Draft202012Validator(
    grab_json_file("schemas", "2.0.0", "blueprint.json"),
    registry=registry
)

# Decode a blueprint string into a JSON dict we can validate
blueprint_string = "..."
blueprint_dict = json.loads(zlib.decompress(base64.b64decode(bp_string[1:])))

# Validate
validator.validate(bluprint_dict)
assert validator.is_valid(blueprint_dict)
```

This can be adapted to your chosen project/programming language as you see fit.

## Testing

To ensure correctness, this repo comes with a set of Python files in the `test` folder which can be run with `pytest`:

```
TODO
```

## Building HTML/Markdown representations of the Schemas using `json-schema-for-humans`


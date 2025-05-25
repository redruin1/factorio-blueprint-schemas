# Factorio Blueprint String JSON Schemas

This document is intended to be an open source public specification for the decoded JSON format of [Factorio](https://factorio.com/) blueprint strings. If you don't know what any of that that means, see [here](https://wiki.factorio.com/Blueprint_string_format).

The purpose of this repository is similar to that of the Factorio wiki page on the blueprint string format, but specified in a standardized, machine readable format - giving it the potential to used by software suites for validation purposes. In addition to providing rigorous technical description of the format, documentation and descriptions are also provided directly alongside each property, meaning that automatically generating accurate, readable documentation of these formats is not only possible, but eminently feasible. [For example, here's a convenient, navigatable digest of the entire 2.0 blueprint string format.](https://redruin1.github.io/factorio-blueprint-schemas/html/2.0.0/blueprintable.html)

## Validation

Here's a simple illustration of how to use the schemas to validate some JSON dictionary using Python and [`jsonschema`](https://github.com/python-jsonschema/jsonschema):

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

## Specification

Each file is written as Draft 2020-compliant JSON schema. In addition to required fields, documentation metadata `"title"` and `"description"` fields should also be provided (if a properties function is not immediately obvious), as well as comments for maintainers. Descriptions for properties are defined in Markdown, and as such can include things like _emphasis_, **bold**, `inline code`, as well as [hyperlinks](https://example.com/).

All schemas corresponding to a particular format are located in their respective semantically versioned directory inside of the `schemas` master folder. A versioned schema is valid for all versions above it until the next specified versioned schema; so the schemas in folder `1.0.0` will validate up to and excluding version `1.1.0` - and the `1.1.0` folder will validate for versions up until `2.0.0`, and so on. "Global" schemas that are not necessarily associated with a particular Factorio version (such as a specification for a `uint16`) lie in the topmost `common` folder next to the versioned schema folders. Inside of a version folder, this pattern continues; definitions that are reused throughout version `2.0.0` are defined in the `schemas/2.0.0/common` folder.

To keep schemas concise and easy to maintain, large schemas are frequently split into multiple smaller schemas and `"$ref"`-erenced appropriately. `$defs` are also permitted if certain structures are reused often in *one* single schema; but if something is used in more than one file at once, the definition is broken out into it's own file and referenced accordingly.

In an effort towards DRY, cross-referencing schemas *between* versions is not only permitted, but recommended. In such cases, always prefer referencing schemas in earlier semantic versions; so schemas defined in folder `2.0.0` can reference schemas defined in `1.0.0`, but not vise-versa. However, if cross referencing between versions in this manner would directly reduce readability/understandability of the schema, this recommendation can be ignored.

## Testing

To ensure correctness, this repo comes with a set of Python files in the `test` folder which can be simply run with [`pytest`](https://github.com/pytest-dev/pytest). This will collect and attempt to validate a set of blueprint string files located in the `test/examples` subdirectory. You can use these files located here as sample data to test your own validation suites against.

## Building HTML/Markdown Documentation Locally

If you have Python installed (in whatever virtual environment you prefer), you can `pip install json-schema-for-humans` and then run the `make.py` script in the `doc` folder:

```
python doc/make.py
```

This will make populate the `doc/html` folder. Alternatively, if you want to generate markdown documentation instead, you can use:

```
python doc/make.py md
```

Which will then populate the `doc/md` folder with the same structure.

Additionally, `doc/make.py` is specified as a pre-commit hook, so it should automatically run on `git commit` and keep the generated files up-to-date.

## Contributing

PRs of all types are of course welcome. It is suggested that any changes to the JSON schemas themselves abide by the specification outlined above, unless the purpose of the change is to tweak the conventions themselves.

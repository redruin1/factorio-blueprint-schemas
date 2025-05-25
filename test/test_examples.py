# test_examples.py

from referencing import Registry, Resource
from jsonschema import Draft202012Validator
import pytest

import base64
import json
import os
import zlib

def grab_json_file(*path) -> dict:
    with open(os.path.join(*path), "r") as json_file:
        return json.load(json_file)

def retrieve_from_path(uri: str):
    # print(uri)
    with open("schemas/" + uri, "r") as json_file:
        res = json.load(json_file)
    return Resource.from_contents(res)

test_reg = Registry(retrieve=retrieve_from_path)

def gather_examples(path, extension):
    return [os.path.join(path, item) for item in os.listdir(path) if item.endswith(extension)]
@pytest.mark.parametrize("filename", gather_examples(os.path.join("test", "examples"), ".bp"))
def test_example_blueprints(filename):
    # Decode the value to json
    print(filename)

    with open(filename, "r") as file:
        bp_string = file.read()

    json_dict = json.loads(zlib.decompress(base64.b64decode(bp_string[1:])))

    # We assume version 2.0
    validator = Draft202012Validator(
        grab_json_file("schemas", "2.0.0", "blueprint.json"),
        registry=test_reg
    )
    validator.validate(json_dict)

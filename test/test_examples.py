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

# def gather_json_schemas(path) -> dict:
#     res = {}
#     for dir_path, _, file_names in os.walk(path):
#         for file_name in file_names:
#             entry = grab_json_file(dir_path, file_name)
#             res[entry["$id"]] = entry
#     return res

# registry_2_0_0 = Registry().with_contents(gather_json_schemas(os.path.join("schemas", "common")).items())
# registry_2_0_0 = registry_2_0_0.with_contents(gather_json_schemas(os.path.join("schemas", "2.0.0")).items())



def retrieve_from_path(uri: str):
    print(uri)
    with open("schemas/" + uri, "r") as json_file:
        res = json.load(json_file)
    return Resource.from_contents(res)

test_reg = Registry(retrieve=retrieve_from_path)

from draftsman.entity import *

@pytest.mark.parametrize(
    "inst,filepath", 
    [
        (Accumulator(), "accumulator.json"),
        (AgriculturalTower(items=[]), "agricultural-tower.json"), 
        (AmmoTurret(), "ammo-turret.json"),
        (ArithmeticCombinator(player_description=""), "arithmetic-combinator.json"),
        (ArtilleryTurret(items=[]), "artillery-turret.json"),
        (ArtilleryWagon(), "artillery-wagon.json"),
        (AssemblingMachine(recipe_quality="normal"), "assembling-machine.json"),
        (AsteroidCollector(), "asteroid-collector.json"),
        # Beacon,
        # Boiler
    ]
)
def test_simple_entity(inst, filepath):
    json_dict = inst.to_dict(exclude_defaults=False, exclude_none=False)
    json_dict["entity_number"] = 1

    validator = Draft202012Validator(
        grab_json_file("schemas", "2.0.0", "entity", filepath),
        registry=test_reg
    )
    validator.validate(json_dict)


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

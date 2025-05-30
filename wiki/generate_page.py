# generate_page.py

"""
Creates a file of Media Wiki formatted text which can be pasted to the Factorio wiki.
"""

def make_collapsable_table(json_schema: dict[str, dict], indent: int=0) -> str:
    lines = [
        "{| class='mw-collapsible mw-collapsed wikitable'"
    ]
    lines.append(f"|+ style='white-space:nowrap; border:1px solid; padding:3px;' | {json_schema.get("title", "TODO")}")
    lines.append("|-")
    lines.append("! Key !! Description !! Data type !! Default")
    schema_type = json_schema.get("type", "object")
    if schema_type == "object":
        for property_name, property_value in json_schema.get("properties", {}).items():
            lines.append("|-")
            lines.append(f"| <code>{property_name}</code>")
            lines.append(f"| {property_value.get("description", "")}")
            if property_value.get("type", "object") == "object":
                lines.append(make_collapsable_table(property_value, indent=indent+2))
            lines.append(f"| {property_value.get("type", "")}")
            lines.append(f"| {property_value.get("default", "")}")
    lines.append("|}")
    return "\n".join(" " * indent + line for line in lines)


"""
{| class="mw-collapsible mw-collapsed wikitable"
|+ style="white-space:nowrap; border:1px solid; padding:3px;" | Blueprint Book
|-
! Key !! Description !! Data type !! Default
|-
| <code>"index"</code>
| Index of this blueprintable if it lives inside of another blueprint book, 0-based. If not, this field has no effect.
| uint16
| null
|-
| <code>"blueprint_book"</code>
| colspan="3" | <!--
-->
<div>
The actual contents of this blueprint book.
{| class="wikitable mw-collapsible mw-collapsed" style="width:100%; margin:0;"
|+ Blueprint Book Object
! Key !! Description !! Data type !! Default
|-
| <code>"item"</code>
| String, the name of the item that was saved ("blueprint-book" in vanilla).
| String
| "blueprint-book"
|-
| <code>"label"</code>
| String, the name of the blueprint set by the user.
| String
| ""
|-
| <code>"label_color"</code>
| The color of the label of this blueprint. Optional. [[#Color object]].
| Object
| null
|-
| <code>"blueprints"</code>
| The actual content of the blueprint book, array of objects containing an "index" key and 0-based value and a "blueprint" key with a [[#Blueprint object]] as the value.
| Array
| []
|-
| <code>"active_index"</code>
| Index of the currently selected blueprint, 0-based.
| Integer
| 0
|-
| <code>"icons"</code>
| The icons of the blueprint book set by the user, array of [[#Icon object]]s.
| Array
|
|-
| <code>"description"</code>
| The description of the blueprint book. Optional.
| String
| ""
|-
| <code>"version"</code>
| The map version of the map the blueprint was created in, see [[Version string format]].
| Integer (long)
|
|}
</div><!--
-->
|}

{| class="wikitable"
! Key !! Description !! Data type
|-
| item
| String, the name of the item that was saved ("blueprint-book" in vanilla).
| String
|-
| label
| String, the name of the blueprint set by the user.
| String
|-
| label_color
| The color of the label of this blueprint. Optional. [[#Color object]].
| Object
|-
| blueprints
| The actual content of the blueprint book, array of objects containing an "index" key and 0-based value and a "blueprint" key with a [[#Blueprint object]] as the value.
| Array
|-
| active_index
| Index of the currently selected blueprint, 0-based.
| Integer
|-
| icons
| The icons of the blueprint book set by the user, array of [[#Icon object]]s.
| Array
|-
| description
| The description of the blueprint book. Optional.
| String
|-
| version
| The map version of the map the blueprint was created in, see [[Version string format]].
| Integer (long)
|}
"""

import json

with open("schemas/2.0.0/blueprint-book.json") as file:
    blueprint_book_schema = json.load(file)

print(make_collapsable_table(blueprint_book_schema))
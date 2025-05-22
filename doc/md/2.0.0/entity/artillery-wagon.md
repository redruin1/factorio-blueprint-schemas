# Artillery Wagon

- [1. Property `Generic Entity`](#allOf_i0)
  - [1.1. Property `entity_number`](#allOf_i0_entity_number)
  - [1.2. Property `name`](#allOf_i0_name)
  - [1.3. Property `position`](#allOf_i0_position)
    - [1.3.1. Property `x`](#allOf_i0_position_x)
    - [1.3.2. Property `y`](#allOf_i0_position_y)
  - [1.4. Property `direction`](#allOf_i0_direction)
  - [1.5. Property `mirror`](#allOf_i0_mirror)
  - [1.6. Property `quality`](#allOf_i0_quality)
  - [1.7. Property `tags`](#allOf_i0_tags)
    - [1.7.1. Property `additionalProperties`](#allOf_i0_tags_additionalProperties)
      - [1.7.1.1. Property `item 0`](#allOf_i0_tags_additionalProperties_anyOf_i0)
      - [1.7.1.2. Property `item 1`](#allOf_i0_tags_additionalProperties_anyOf_i1)
      - [1.7.1.3. Property `item 2`](#allOf_i0_tags_additionalProperties_anyOf_i2)
      - [1.7.1.4. Property `object`](#allOf_i0_tags_additionalProperties_anyOf_i3)
- [2. Property `orientation.json`](#allOf_i1)
  - [2.1. Property `orientation`](#allOf_i1_orientation)
- [3. Property `item-requests.json`](#allOf_i2)
  - [3.1. Property `items`](#allOf_i2_items)
    - [3.1.1. urn:factorio:item-request](#allOf_i2_items_items)
- [4. Property `equipment-grid.json`](#allOf_i3)
  - [4.1. Property `enable_logistics_while_moving`](#allOf_i3_enable_logistics_while_moving)
  - [4.2. Property `grid`](#allOf_i3_grid)
    - [4.2.1. equipment-component](#allOf_i3_grid_items)
      - [4.2.1.1. Property `equipment`](#allOf_i3_grid_items_equipment)
        - [4.2.1.1.1. Property `name`](#allOf_i3_grid_items_equipment_name)
        - [4.2.1.1.2. Property `quality`](#allOf_i3_grid_items_equipment_quality)
      - [4.2.1.2. Property `position`](#allOf_i3_grid_items_position)
- [5. Property `artillery-auto-targeting.json`](#allOf_i4)
  - [5.1. Property `artillery_auto_targeting`](#allOf_i4_artillery_auto_targeting)

**Title:** Artillery Wagon

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Rolling stock with an attached artillery turret.

| All of(Requirement)                        |
| ------------------------------------------ |
| [Generic Entity](#allOf_i0)                |
| [orientation.json](#allOf_i1)              |
| [item-requests.json](#allOf_i2)            |
| [equipment-grid.json](#allOf_i3)           |
| [artillery-auto-targeting.json](#allOf_i4) |

## <a name="allOf_i0"></a>1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | ../entity.json   |

**Description:** A schema which contains the keys that all entities share.

| Property                                    | Pattern | Type              | Deprecated | Definition                  | Title/Description |
| ------------------------------------------- | ------- | ----------------- | ---------- | --------------------------- | ----------------- |
| + [entity_number](#allOf_i0_entity_number ) | No      | number            | No         | In ../common/uint64.json    | Entity Number     |
| + [name](#allOf_i0_name )                   | No      | string            | No         | -                           | Name              |
| + [position](#allOf_i0_position )           | No      | object            | No         | In ../common/position.json  | Position          |
| - [direction](#allOf_i0_direction )         | No      | enum (of integer) | No         | -                           | Direction         |
| - [mirror](#allOf_i0_mirror )               | No      | boolean           | No         | -                           | Mirror            |
| - [quality](#allOf_i0_quality )             | No      | enum (of string)  | No         | In common/quality-name.json | Quality           |
| - [tags](#allOf_i0_tags )                   | No      | object            | No         | -                           | Tags              |

### <a name="allOf_i0_entity_number"></a>1.1. Property `entity_number`

**Title:** Entity Number

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** A unique ID given to every entity contained within a blueprint. In practice, this value is the 1-indexed position of the entity inside it's parent blueprint's 'entities' list. This is not enforced however, so an entity's number can be specified with any value as long as it's unique inside that particular blueprint. This value is used for resolving associations between different entities, such as wire connections or schedule definitions.

### <a name="allOf_i0_name"></a>1.2. Property `name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the entity. If this name is not recognized by Factorio when importing the entity is omitted with a notification to the console.

### <a name="allOf_i0_position"></a>1.3. Property `position`

**Title:** Position

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | ../common/position.json |

**Description:** The position where the entity is located inside of it's parent blueprint. This position is (almost) always located at the spatial center of the entity. For grid-aligned entities, this position always lies either in the center of a tile or on its transition.

| Property                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#allOf_i0_position_x ) | No      | number | No         | -          | -                 |
| - [y](#allOf_i0_position_y ) | No      | number | No         | -          | -                 |

#### <a name="allOf_i0_position_x"></a>1.3.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="allOf_i0_position_y"></a>1.3.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

### <a name="allOf_i0_direction"></a>1.4. Property `direction`

**Title:** Direction

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | No                  |
| **Default**  | `0`                 |

**Description:** The direction of the entity, where 0 corresponds to north and incrementing spins clockwise. Not all entities can manipulate their direction, so setting this attribute may have no effect.

Must be one of:
* 0
* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15

### <a name="allOf_i0_mirror"></a>1.5. Property `mirror`

**Title:** Mirror

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not the input/output fluid boxes are mirrored on this particular entity.

### <a name="allOf_i0_quality"></a>1.6. Property `quality`

**Title:** Quality

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `enum (of string)`       |
| **Required**   | No                       |
| **Default**    | `"normal"`               |
| **Defined in** | common/quality-name.json |

**Description:** The quality of the entity itself.

Must be one of:
* "normal"
* "uncommon"
* "rare"
* "epic"
* "legendary"
* "quality-unknown"

### <a name="allOf_i0_tags"></a>1.7. Property `tags`

**Title:** Tags

|                           |                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                   |
| **Required**              | No                                                                                         |
| **Additional properties** | [Each additional property must conform to the schema](#allOf_i0_tags_additionalProperties) |

**Description:** Any additional metadata associated with this entity, mostly intended for including mod information inside exported blueprint strings. Each key must be a string, and each value can be either a string, a boolean, a number, or another JSON object.

| Property                                   | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [](#allOf_i0_tags_additionalProperties ) | No      | Combination | No         | -          | -                 |

#### <a name="allOf_i0_tags_additionalProperties"></a>1.7.1. Property `additionalProperties`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#allOf_i0_tags_additionalProperties_anyOf_i0) |
| [item 1](#allOf_i0_tags_additionalProperties_anyOf_i1) |
| [item 2](#allOf_i0_tags_additionalProperties_anyOf_i2) |
| [object](#allOf_i0_tags_additionalProperties_anyOf_i3) |

##### <a name="allOf_i0_tags_additionalProperties_anyOf_i0"></a>1.7.1.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

##### <a name="allOf_i0_tags_additionalProperties_anyOf_i1"></a>1.7.1.2. Property `item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

##### <a name="allOf_i0_tags_additionalProperties_anyOf_i2"></a>1.7.1.3. Property `item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

##### <a name="allOf_i0_tags_additionalProperties_anyOf_i3"></a>1.7.1.4. Property `object`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | object           |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

## <a name="allOf_i1"></a>2. Property `orientation.json`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | features/orientation.json |

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [orientation](#allOf_i1_orientation ) | No      | number | No         | -          | Orientation       |

### <a name="allOf_i1_orientation"></a>2.1. Property `orientation`

**Title:** Orientation

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0.0`    |

**Description:** A number in the range [0.0, 1.0] representing the direction this entity is facing. Any value specified out of this range is modulo'd back into this range.

## <a name="allOf_i2"></a>3. Property `item-requests.json`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | features/item-requests.json |

| Property                    | Pattern | Type  | Deprecated | Definition | Title/Description |
| --------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [items](#allOf_i2_items ) | No      | array | No         | -          | Item Requests     |

### <a name="allOf_i2_items"></a>3.1. Property `items`

**Title:** Item Requests

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of item requests objects, which contain the item name, it's quality, the amount to request, as well as exactly what inventories to request to and where inside those inventories.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                    | Description                                                                                                   |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:item-request](#allOf_i2_items_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

#### <a name="allOf_i2_items_items"></a>3.1.1. urn:factorio:item-request

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:item-request |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

## <a name="allOf_i3"></a>4. Property `equipment-grid.json`

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | features/equipment-grid.json |

| Property                                                                    | Pattern | Type    | Deprecated | Definition | Title/Description              |
| --------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------ |
| - [enable_logistics_while_moving](#allOf_i3_enable_logistics_while_moving ) | No      | boolean | No         | -          | Enable Logistics While Moving? |
| - [grid](#allOf_i3_grid )                                                   | No      | array   | No         | -          | Equipment Grid Components      |

### <a name="allOf_i3_enable_logistics_while_moving"></a>4.1. Property `enable_logistics_while_moving`

**Title:** Enable Logistics While Moving?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should try to fulfill it's logistic requests when it is in motion. Only has an effect if this entity is configured to have an equipment grid and that equipment grid contains personal roboports.

### <a name="allOf_i3_grid"></a>4.2. Property `grid`

**Title:** Equipment Grid Components

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The specification for where equipment should lie inside of this entity's equipment grid (if it has one).

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [equipment-component](#allOf_i3_grid_items) | -           |

#### <a name="allOf_i3_grid_items"></a>4.2.1. equipment-component

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/equipment-component |

| Property                                       | Pattern | Type   | Deprecated | Definition               | Title/Description                                                                                         |
| ---------------------------------------------- | ------- | ------ | ---------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| + [equipment](#allOf_i3_grid_items_equipment ) | No      | object | No         | In #/$defs/equipment-id  | Equipment ID                                                                                              |
| + [position](#allOf_i3_grid_items_position )   | No      | object | No         | In urn:factorio:position | The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies. |

##### <a name="allOf_i3_grid_items_equipment"></a>4.2.1.1. Property `equipment`

**Title:** Equipment ID

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/equipment-id |

**Description:** A particular type of equipment and its quality.

| Property                                             | Pattern | Type   | Deprecated | Definition                   | Title/Description                                                                                             |
| ---------------------------------------------------- | ------- | ------ | ---------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [name](#allOf_i3_grid_items_equipment_name )       | No      | string | No         | -                            | The name of a valid piece of equipment (that can fit inside this particular equipment grid).                  |
| - [quality](#allOf_i3_grid_items_equipment_quality ) | No      | object | No         | In urn:factorio:quality-name | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="allOf_i3_grid_items_equipment_name"></a>4.2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid piece of equipment (that can fit inside this particular equipment grid).

###### <a name="allOf_i3_grid_items_equipment_quality"></a>4.2.1.1.2. Property `quality`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:quality-name |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

##### <a name="allOf_i3_grid_items_position"></a>4.2.1.2. Property `position`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:position |

**Description:** The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies.

## <a name="allOf_i4"></a>5. Property `artillery-auto-targeting.json`

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | features/artillery-auto-targeting.json |

| Property                                                          | Pattern | Type    | Deprecated | Definition | Title/Description        |
| ----------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------ |
| - [artillery_auto_targeting](#allOf_i4_artillery_auto_targeting ) | No      | boolean | No         | -          | Artillery Auto Targeting |

### <a name="allOf_i4_artillery_auto_targeting"></a>5.1. Property `artillery_auto_targeting`

**Title:** Artillery Auto Targeting

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should automatically target enemies in range.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

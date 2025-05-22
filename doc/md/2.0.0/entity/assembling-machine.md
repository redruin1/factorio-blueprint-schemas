# Assembling Machine

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
- [2. Property `item-requests.json`](#allOf_i1)
  - [2.1. Property `items`](#allOf_i1_items)
    - [2.1.1. urn:factorio:item-request](#allOf_i1_items_items)
- [3. Property `circuit-enabled.json`](#allOf_i2)
  - [3.1. Property `control_behavior`](#allOf_i2_control_behavior)
    - [3.1.1. Property `circuit_enabled`](#allOf_i2_control_behavior_circuit_enabled)
- [4. Property `circuit-condition.json`](#allOf_i3)
  - [4.1. Property `control_behavior`](#allOf_i3_control_behavior)
    - [4.1.1. Property `circuit_condition`](#allOf_i3_control_behavior_circuit_condition)
      - [4.1.1.1. Property `first_signal`](#allOf_i3_control_behavior_circuit_condition_first_signal)
        - [4.1.1.1.1. Property `SignalID`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
          - [4.1.1.1.1.1. Property `name`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name)
          - [4.1.1.1.1.2. Property `type`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type)
          - [4.1.1.1.1.3. Property `quality`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality)
        - [4.1.1.1.2. Property `item 1`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
      - [4.1.1.2. Property `comparator`](#allOf_i3_control_behavior_circuit_condition_comparator)
      - [4.1.1.3. Property `constant`](#allOf_i3_control_behavior_circuit_condition_constant)
      - [4.1.1.4. Property `second_signal`](#allOf_i3_control_behavior_circuit_condition_second_signal)
        - [4.1.1.4.1. Property `SignalID`](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
        - [4.1.1.4.2. Property `item 1`](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
- [5. Property `logistic-condition.json`](#allOf_i4)
  - [5.1. Property `control_behavior`](#allOf_i4_control_behavior)
    - [5.1.1. Property `connect_to_logistic_network`](#allOf_i4_control_behavior_connect_to_logistic_network)
    - [5.1.2. Property `logistic_condition`](#allOf_i4_control_behavior_logistic_condition)
      - [5.1.2.1. Property `first_signal`](#allOf_i3_control_behavior_circuit_condition_first_signal)
        - [5.1.2.1.1. Property `SignalID`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
          - [5.1.2.1.1.1. Property `name`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name)
          - [5.1.2.1.1.2. Property `type`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type)
          - [5.1.2.1.1.3. Property `quality`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality)
        - [5.1.2.1.2. Property `item 1`](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
      - [5.1.2.2. Property `comparator`](#allOf_i3_control_behavior_circuit_condition_comparator)
      - [5.1.2.3. Property `constant`](#allOf_i3_control_behavior_circuit_condition_constant)
      - [5.1.2.4. Property `second_signal`](#allOf_i3_control_behavior_circuit_condition_second_signal)
        - [5.1.2.4.1. Property `SignalID`](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
        - [5.1.2.4.2. Property `item 1`](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
- [6. Property `recipe`](#recipe)
  - [6.1. Property `item 0`](#recipe_oneOf_i0)
  - [6.2. Property `item 1`](#recipe_oneOf_i1)
- [7. Property `recipe_quality`](#recipe_quality)
- [8. Property `control_behavior`](#control_behavior)
  - [8.1. Property `set_recipe`](#control_behavior_set_recipe)
  - [8.2. Property `read_contents`](#control_behavior_read_contents)
  - [8.3. Property `include_in_crafting`](#control_behavior_include_in_crafting)
  - [8.4. Property `read_recipe_finished`](#control_behavior_read_recipe_finished)
  - [8.5. Property `recipe_finished_signal`](#control_behavior_recipe_finished_signal)
    - [8.5.1. Property `urn:factorio:signal-id`](#control_behavior_recipe_finished_signal_anyOf_i0)
    - [8.5.2. Property `item 1`](#control_behavior_recipe_finished_signal_anyOf_i1)
  - [8.6. Property `read_working`](#control_behavior_read_working)
  - [8.7. Property `working_signal`](#control_behavior_working_signal)
    - [8.7.1. Property `urn:factorio:signal-id`](#control_behavior_working_signal_anyOf_i0)
    - [8.7.2. Property `item 1`](#control_behavior_working_signal_anyOf_i1)

**Title:** Assembling Machine

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An entity that can convert items and fluids into other items and fluids.

| Property                                 | Pattern | Type             | Deprecated | Definition                     | Title/Description |
| ---------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ----------------- |
| - [recipe](#recipe )                     | No      | Combination      | No         | -                              | Recipe            |
| - [recipe_quality](#recipe_quality )     | No      | enum (of string) | No         | In ../common/quality-name.json | Recipe Quality    |
| - [control_behavior](#control_behavior ) | No      | object           | No         | -                              | -                 |

| All of(Requirement)                  |
| ------------------------------------ |
| [Generic Entity](#allOf_i0)          |
| [item-requests.json](#allOf_i1)      |
| [circuit-enabled.json](#allOf_i2)    |
| [circuit-condition.json](#allOf_i3)  |
| [logistic-condition.json](#allOf_i4) |

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

## <a name="allOf_i1"></a>2. Property `item-requests.json`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | features/item-requests.json |

| Property                    | Pattern | Type  | Deprecated | Definition | Title/Description |
| --------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [items](#allOf_i1_items ) | No      | array | No         | -          | Item Requests     |

### <a name="allOf_i1_items"></a>2.1. Property `items`

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
| [urn:factorio:item-request](#allOf_i1_items_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

#### <a name="allOf_i1_items_items"></a>2.1.1. urn:factorio:item-request

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:item-request |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

## <a name="allOf_i2"></a>3. Property `circuit-enabled.json`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | features/circuit-enabled.json |

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#allOf_i2_control_behavior ) | No      | object | No         | -          | -                 |

### <a name="allOf_i2_control_behavior"></a>3.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                         | Pattern | Type    | Deprecated | Definition | Title/Description                                                                 |
| ---------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------------- |
| - [circuit_enabled](#allOf_i2_control_behavior_circuit_enabled ) | No      | boolean | No         | -          | Whether or not this entity should be controlled by a specified circuit condition. |

#### <a name="allOf_i2_control_behavior_circuit_enabled"></a>3.1.1. Property `circuit_enabled`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified circuit condition.

## <a name="allOf_i3"></a>4. Property `circuit-condition.json`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | features/circuit-condition.json |

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#allOf_i3_control_behavior ) | No      | object | No         | -          | -                 |

### <a name="allOf_i3_control_behavior"></a>4.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                             | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| -------------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [circuit_condition](#allOf_i3_control_behavior_circuit_condition ) | No      | object | No         | In ../../common/condition.json | Condition         |

#### <a name="allOf_i3_control_behavior_circuit_condition"></a>4.1.1. Property `circuit_condition`

**Title:** Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** A conditional statement between either 2 signals or 1 signal and 1 constant value.

| Property                                                                       | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ------------------------------------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

##### <a name="allOf_i3_control_behavior_circuit_condition_first_signal"></a>4.1.1.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [SignalID](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>4.1.1.1.1. Property `SignalID`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                                                                 | Pattern | Type             | Deprecated | Definition                            | Title/Description                                                                                 |
| ---------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name )       | No      | string           | No         | -                                     | -                                                                                                 |
| - [type](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type )       | No      | enum (of string) | No         | -                                     | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality ) | No      | enum (of string) | No         | Same as [quality](#allOf_i0_quality ) | Quality                                                                                           |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name"></a>4.1.1.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type"></a>4.1.1.1.1.2. Property `type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"item"`           |

**Description:** The category of the signal. There can be multiple signals with the same name but differing types.

Must be one of:
* "item"
* "fluid"
* "recipe"
* "entity"
* "space-location"
* "asteroid-chunk"
* "quality"
* "virtual"

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality"></a>4.1.1.1.1.3. Property `quality`

**Title:** Quality

|                        |                              |
| ---------------------- | ---------------------------- |
| **Type**               | `enum (of string)`           |
| **Required**           | No                           |
| **Default**            | `"normal"`                   |
| **Same definition as** | [quality](#allOf_i0_quality) |

**Description:** A type of quality.

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>4.1.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="allOf_i3_control_behavior_circuit_condition_comparator"></a>4.1.1.2. Property `comparator`

**Title:** Comparator

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `enum (of string)`           |
| **Required**   | No                           |
| **Default**    | `">"`                        |
| **Defined in** | ../../common/comparator.json |

**Description:** In/equality operation to use in conditions and item request filters.

Must be one of:
* ">"
* "<"
* "="
* "≥"
* "≤"
* "≠"

##### <a name="allOf_i3_control_behavior_circuit_condition_constant"></a>4.1.1.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

##### <a name="allOf_i3_control_behavior_circuit_condition_second_signal"></a>4.1.1.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [SignalID](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>4.1.1.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                                                                |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                       |
| **Required**              | No                                                                             |
| **Additional properties** | Any type allowed                                                               |
| **Same definition as**    | [SignalID](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

###### <a name="allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>4.1.1.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="allOf_i4"></a>5. Property `logistic-condition.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/logistic-condition.json |

| Property                                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#allOf_i4_control_behavior ) | No      | object | No         | -          | -                 |

### <a name="allOf_i4_control_behavior"></a>5.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                 | Pattern | Type    | Deprecated | Definition                     | Title/Description            |
| ---------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ------------------------------ | ---------------------------- |
| - [connect_to_logistic_network](#allOf_i4_control_behavior_connect_to_logistic_network ) | No      | boolean | No         | -                              | Connect to logistic network? |
| - [logistic_condition](#allOf_i4_control_behavior_logistic_condition )                   | No      | object  | No         | In ../../common/condition.json | Logistic Condition           |

#### <a name="allOf_i4_control_behavior_connect_to_logistic_network"></a>5.1.1. Property `connect_to_logistic_network`

**Title:** Connect to logistic network?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified logistic condition.

#### <a name="allOf_i4_control_behavior_logistic_condition"></a>5.1.2. Property `logistic_condition`

**Title:** Logistic Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** The logistic condition that the entity should be enabled with, if 'connect_to_logistic_network' is 'true'.

| Property                                                                       | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ------------------------------------------------------------------------------ | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

##### <a name="allOf_i3_control_behavior_circuit_condition_first_signal"></a>5.1.2.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [SignalID](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>5.1.2.1.1. Property `SignalID`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                                                                 | Pattern | Type             | Deprecated | Definition                            | Title/Description                                                                                 |
| ---------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name )       | No      | string           | No         | -                                     | -                                                                                                 |
| - [type](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type )       | No      | enum (of string) | No         | -                                     | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality ) | No      | enum (of string) | No         | Same as [quality](#allOf_i0_quality ) | Quality                                                                                           |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_name"></a>5.1.2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_type"></a>5.1.2.1.1.2. Property `type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"item"`           |

**Description:** The category of the signal. There can be multiple signals with the same name but differing types.

Must be one of:
* "item"
* "fluid"
* "recipe"
* "entity"
* "space-location"
* "asteroid-chunk"
* "quality"
* "virtual"

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0_quality"></a>5.1.2.1.1.3. Property `quality`

**Title:** Quality

|                        |                              |
| ---------------------- | ---------------------------- |
| **Type**               | `enum (of string)`           |
| **Required**           | No                           |
| **Default**            | `"normal"`                   |
| **Same definition as** | [quality](#allOf_i0_quality) |

**Description:** A type of quality.

###### <a name="allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>5.1.2.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="allOf_i3_control_behavior_circuit_condition_comparator"></a>5.1.2.2. Property `comparator`

**Title:** Comparator

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `enum (of string)`           |
| **Required**   | No                           |
| **Default**    | `">"`                        |
| **Defined in** | ../../common/comparator.json |

**Description:** In/equality operation to use in conditions and item request filters.

Must be one of:
* ">"
* "<"
* "="
* "≥"
* "≤"
* "≠"

##### <a name="allOf_i3_control_behavior_circuit_condition_constant"></a>5.1.2.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

##### <a name="allOf_i3_control_behavior_circuit_condition_second_signal"></a>5.1.2.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [SignalID](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>5.1.2.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                                                                |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                       |
| **Required**              | No                                                                             |
| **Additional properties** | Any type allowed                                                               |
| **Same definition as**    | [SignalID](#allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

###### <a name="allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>5.1.2.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="recipe"></a>6. Property `recipe`

**Title:** Recipe

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The recipe that this entity is configured to perform.

| One of(Option)             |
| -------------------------- |
| [item 0](#recipe_oneOf_i0) |
| [item 1](#recipe_oneOf_i1) |

### <a name="recipe_oneOf_i0"></a>6.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="recipe_oneOf_i1"></a>6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="recipe_quality"></a>7. Property `recipe_quality`

**Title:** Recipe Quality

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `enum (of string)`          |
| **Required**   | No                          |
| **Default**    | `"normal"`                  |
| **Defined in** | ../common/quality-name.json |

**Description:** The quality of the ingredients/output items that this machine should use.

Must be one of:
* "normal"
* "uncommon"
* "rare"
* "epic"
* "legendary"
* "quality-unknown"

## <a name="control_behavior"></a>8. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                              | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [set_recipe](#control_behavior_set_recipe )                         | No      | boolean     | No         | -          | -                 |
| - [read_contents](#control_behavior_read_contents )                   | No      | boolean     | No         | -          | -                 |
| - [include_in_crafting](#control_behavior_include_in_crafting )       | No      | boolean     | No         | -          | -                 |
| - [read_recipe_finished](#control_behavior_read_recipe_finished )     | No      | boolean     | No         | -          | -                 |
| - [recipe_finished_signal](#control_behavior_recipe_finished_signal ) | No      | Combination | No         | -          | -                 |
| - [read_working](#control_behavior_read_working )                     | No      | boolean     | No         | -          | -                 |
| - [working_signal](#control_behavior_working_signal )                 | No      | Combination | No         | -          | -                 |

### <a name="control_behavior_set_recipe"></a>8.1. Property `set_recipe`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

### <a name="control_behavior_read_contents"></a>8.2. Property `read_contents`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

### <a name="control_behavior_include_in_crafting"></a>8.3. Property `include_in_crafting`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"true"`  |

### <a name="control_behavior_read_recipe_finished"></a>8.4. Property `read_recipe_finished`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

### <a name="control_behavior_recipe_finished_signal"></a>8.5. Property `recipe_finished_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

| Any of(Option)                                                              |
| --------------------------------------------------------------------------- |
| [urn:factorio:signal-id](#control_behavior_recipe_finished_signal_anyOf_i0) |
| [item 1](#control_behavior_recipe_finished_signal_anyOf_i1)                 |

#### <a name="control_behavior_recipe_finished_signal_anyOf_i0"></a>8.5.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

#### <a name="control_behavior_recipe_finished_signal_anyOf_i1"></a>8.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="control_behavior_read_working"></a>8.6. Property `read_working`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

### <a name="control_behavior_working_signal"></a>8.7. Property `working_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                      |
| ------------------------------------------------------------------- |
| [urn:factorio:signal-id](#control_behavior_working_signal_anyOf_i0) |
| [item 1](#control_behavior_working_signal_anyOf_i1)                 |

#### <a name="control_behavior_working_signal_anyOf_i0"></a>8.7.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

#### <a name="control_behavior_working_signal_anyOf_i1"></a>8.7.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

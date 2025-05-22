# Arithmetic Combinator

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
- [2. Property `player-description.json`](#allOf_i1)
  - [2.1. Property `player_description`](#allOf_i1_player_description)
- [3. Property `control_behavior`](#control_behavior)
  - [3.1. Property `arithmetic_conditions`](#control_behavior_arithmetic_conditions)
    - [3.1.1. Property `first_constant`](#control_behavior_arithmetic_conditions_first_constant)
      - [3.1.1.1. Property `int32.json`](#control_behavior_arithmetic_conditions_first_constant_oneOf_i0)
      - [3.1.1.2. Property `item 1`](#control_behavior_arithmetic_conditions_first_constant_oneOf_i1)
    - [3.1.2. Property `first_signal`](#control_behavior_arithmetic_conditions_first_signal)
      - [3.1.2.1. Property `SignalID`](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0)
        - [3.1.2.1.1. Property `name`](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_name)
        - [3.1.2.1.2. Property `type`](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_type)
        - [3.1.2.1.3. Property `quality`](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_quality)
      - [3.1.2.2. Property `item 1`](#control_behavior_arithmetic_conditions_first_signal_oneOf_i1)
    - [3.1.3. Property `first_signal_networks`](#control_behavior_arithmetic_conditions_first_signal_networks)
      - [3.1.3.1. Property `red`](#control_behavior_arithmetic_conditions_first_signal_networks_red)
      - [3.1.3.2. Property `green`](#control_behavior_arithmetic_conditions_first_signal_networks_green)
    - [3.1.4. Property `operation`](#control_behavior_arithmetic_conditions_operation)
    - [3.1.5. Property `second_constant`](#control_behavior_arithmetic_conditions_second_constant)
      - [3.1.5.1. Property `int32.json`](#control_behavior_arithmetic_conditions_second_constant_oneOf_i0)
      - [3.1.5.2. Property `item 1`](#control_behavior_arithmetic_conditions_second_constant_oneOf_i1)
    - [3.1.6. Property `second_signal`](#control_behavior_arithmetic_conditions_second_signal)
      - [3.1.6.1. Property `SignalID`](#control_behavior_arithmetic_conditions_second_signal_oneOf_i0)
      - [3.1.6.2. Property `item 1`](#control_behavior_arithmetic_conditions_second_signal_oneOf_i1)
    - [3.1.7. Property `second_signal_networks`](#control_behavior_arithmetic_conditions_second_signal_networks)
      - [3.1.7.1. Property `red`](#control_behavior_arithmetic_conditions_first_signal_networks_red)
      - [3.1.7.2. Property `green`](#control_behavior_arithmetic_conditions_first_signal_networks_green)
    - [3.1.8. Property `output_signal`](#control_behavior_arithmetic_conditions_output_signal)
      - [3.1.8.1. Property `SignalID`](#control_behavior_arithmetic_conditions_output_signal_oneOf_i0)
      - [3.1.8.2. Property `item 1`](#control_behavior_arithmetic_conditions_output_signal_oneOf_i1)

**Title:** Arithmetic Combinator

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A combinator that can perform mathematical operations on one or more values.

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#control_behavior ) | No      | object | No         | -          | -                 |

| All of(Requirement)                  |
| ------------------------------------ |
| [Generic Entity](#allOf_i0)          |
| [player-description.json](#allOf_i1) |

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

## <a name="allOf_i1"></a>2. Property `player-description.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/player-description.json |

| Property                                              | Pattern | Type   | Deprecated | Definition | Title/Description  |
| ----------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------ |
| - [player_description](#allOf_i1_player_description ) | No      | string | No         | -          | Player Description |

### <a name="allOf_i1_player_description"></a>2.1. Property `player_description`

**Title:** Player Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** An attached string, intended for entity documentation.

## <a name="control_behavior"></a>3. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                            | Pattern | Type   | Deprecated | Definition | Title/Description     |
| ------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | --------------------- |
| - [arithmetic_conditions](#control_behavior_arithmetic_conditions ) | No      | object | No         | -          | Arithmetic Conditions |

### <a name="control_behavior_arithmetic_conditions"></a>3.1. Property `arithmetic_conditions`

**Title:** Arithmetic Conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Container for arithmetic combinator specific parameters.

| Property                                                                                    | Pattern | Type             | Deprecated | Definition                              | Title/Description      |
| ------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | --------------------------------------- | ---------------------- |
| - [first_constant](#control_behavior_arithmetic_conditions_first_constant )                 | No      | Combination      | No         | -                                       | First Constant         |
| - [first_signal](#control_behavior_arithmetic_conditions_first_signal )                     | No      | Combination      | No         | -                                       | First Signal           |
| - [first_signal_networks](#control_behavior_arithmetic_conditions_first_signal_networks )   | No      | object           | No         | In ../common/network-specification.json | First Signal Networks  |
| - [operation](#control_behavior_arithmetic_conditions_operation )                           | No      | enum (of string) | No         | -                                       | Operation              |
| - [second_constant](#control_behavior_arithmetic_conditions_second_constant )               | No      | Combination      | No         | -                                       | Second Constant        |
| - [second_signal](#control_behavior_arithmetic_conditions_second_signal )                   | No      | Combination      | No         | -                                       | Second Signal          |
| - [second_signal_networks](#control_behavior_arithmetic_conditions_second_signal_networks ) | No      | object           | No         | In ../common/network-specification.json | Second Signal Networks |
| - [output_signal](#control_behavior_arithmetic_conditions_output_signal )                   | No      | Combination      | No         | -                                       | Output Signal          |

#### <a name="control_behavior_arithmetic_conditions_first_constant"></a>3.1.1. Property `first_constant`

**Title:** First Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Constant value that goes in the leftmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                |
| ----------------------------------------------------------------------------- |
| [int32.json](#control_behavior_arithmetic_conditions_first_constant_oneOf_i0) |
| [item 1](#control_behavior_arithmetic_conditions_first_constant_oneOf_i1)     |

##### <a name="control_behavior_arithmetic_conditions_first_constant_oneOf_i0"></a>3.1.1.1. Property `int32.json`

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Defined in** | ../../common/int32.json |

**Description:** Signed 32-bit integer.

##### <a name="control_behavior_arithmetic_conditions_first_constant_oneOf_i1"></a>3.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="control_behavior_arithmetic_conditions_first_signal"></a>3.1.2. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the leftmost slot. Takes precedence over 'first_constant', if both happen to be specified.

| One of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [SignalID](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0) |
| [item 1](#control_behavior_arithmetic_conditions_first_signal_oneOf_i1)   |

##### <a name="control_behavior_arithmetic_conditions_first_signal_oneOf_i0"></a>3.1.2.1. Property `SignalID`

**Title:** SignalID

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | ../common/signal-id.json |

**Description:** An object which represents a valid signal.

| Property                                                                            | Pattern | Type             | Deprecated | Definition                            | Title/Description                                                                                 |
| ----------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_name )       | No      | string           | No         | -                                     | -                                                                                                 |
| - [type](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_type )       | No      | enum (of string) | No         | -                                     | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0_quality ) | No      | enum (of string) | No         | Same as [quality](#allOf_i0_quality ) | Quality                                                                                           |

###### <a name="control_behavior_arithmetic_conditions_first_signal_oneOf_i0_name"></a>3.1.2.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="control_behavior_arithmetic_conditions_first_signal_oneOf_i0_type"></a>3.1.2.1.2. Property `type`

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

###### <a name="control_behavior_arithmetic_conditions_first_signal_oneOf_i0_quality"></a>3.1.2.1.3. Property `quality`

**Title:** Quality

|                        |                              |
| ---------------------- | ---------------------------- |
| **Type**               | `enum (of string)`           |
| **Required**           | No                           |
| **Default**            | `"normal"`                   |
| **Same definition as** | [quality](#allOf_i0_quality) |

**Description:** A type of quality.

##### <a name="control_behavior_arithmetic_conditions_first_signal_oneOf_i1"></a>3.1.2.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="control_behavior_arithmetic_conditions_first_signal_networks"></a>3.1.3. Property `first_signal_networks`

**Title:** First Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the leftmost slot should consider for values. Only has an effect if the first slot is occupied by a signal.

| Property                                                                        | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

##### <a name="control_behavior_arithmetic_conditions_first_signal_networks_red"></a>3.1.3.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

##### <a name="control_behavior_arithmetic_conditions_first_signal_networks_green"></a>3.1.3.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

#### <a name="control_behavior_arithmetic_conditions_operation"></a>3.1.4. Property `operation`

**Title:** Operation

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"*"`              |

**Description:** The mathematical operation to perform.

Must be one of:
* "*"
* "/"
* "+"
* "-"
* "%"
* "^"
* "<<"
* ">>"
* "AND"
* "OR"
* "XOR"

#### <a name="control_behavior_arithmetic_conditions_second_constant"></a>3.1.5. Property `second_constant`

**Title:** Second Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `0`              |

**Description:** Constant value that goes in the rightmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [int32.json](#control_behavior_arithmetic_conditions_second_constant_oneOf_i0) |
| [item 1](#control_behavior_arithmetic_conditions_second_constant_oneOf_i1)     |

##### <a name="control_behavior_arithmetic_conditions_second_constant_oneOf_i0"></a>3.1.5.1. Property `int32.json`

|                        |                                                                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**               | `number`                                                                                                                          |
| **Required**           | No                                                                                                                                |
| **Same definition as** | [control_behavior_arithmetic_conditions_first_constant_oneOf_i0](#control_behavior_arithmetic_conditions_first_constant_oneOf_i0) |

**Description:** Signed 32-bit integer.

##### <a name="control_behavior_arithmetic_conditions_second_constant_oneOf_i1"></a>3.1.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="control_behavior_arithmetic_conditions_second_signal"></a>3.1.6. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the rightmost slot. Takes precedence over 'second_constant', if both happen to be specified.

| One of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [SignalID](#control_behavior_arithmetic_conditions_second_signal_oneOf_i0) |
| [item 1](#control_behavior_arithmetic_conditions_second_signal_oneOf_i1)   |

##### <a name="control_behavior_arithmetic_conditions_second_signal_oneOf_i0"></a>3.1.6.1. Property `SignalID`

**Title:** SignalID

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [SignalID](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

##### <a name="control_behavior_arithmetic_conditions_second_signal_oneOf_i1"></a>3.1.6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="control_behavior_arithmetic_conditions_second_signal_networks"></a>3.1.7. Property `second_signal_networks`

**Title:** Second Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the rightmost slot should consider for values. Only has an effect if the second slot is occupied by a signal.

| Property                                                                        | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

##### <a name="control_behavior_arithmetic_conditions_first_signal_networks_red"></a>3.1.7.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

##### <a name="control_behavior_arithmetic_conditions_first_signal_networks_green"></a>3.1.7.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

#### <a name="control_behavior_arithmetic_conditions_output_signal"></a>3.1.8. Property `output_signal`

**Title:** Output Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** What signal (or signals) should this combinator output.

| One of(Option)                                                             |
| -------------------------------------------------------------------------- |
| [SignalID](#control_behavior_arithmetic_conditions_output_signal_oneOf_i0) |
| [item 1](#control_behavior_arithmetic_conditions_output_signal_oneOf_i1)   |

##### <a name="control_behavior_arithmetic_conditions_output_signal_oneOf_i0"></a>3.1.8.1. Property `SignalID`

**Title:** SignalID

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | Any type allowed                                                          |
| **Same definition as**    | [SignalID](#control_behavior_arithmetic_conditions_first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

##### <a name="control_behavior_arithmetic_conditions_output_signal_oneOf_i1"></a>3.1.8.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

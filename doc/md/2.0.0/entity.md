# Generic Entity

- [1. Property `entity_number`](#entity_number)
- [2. Property `name`](#name)
- [3. Property `position`](#position)
  - [3.1. Property `x`](#position_x)
  - [3.2. Property `y`](#position_y)
- [4. Property `direction`](#direction)
- [5. Property `mirror`](#mirror)
- [6. Property `quality`](#quality)
- [7. Property `tags`](#tags)
  - [7.1. Property `additionalProperties`](#tags_additionalProperties)
    - [7.1.1. Property `item 0`](#tags_additionalProperties_anyOf_i0)
    - [7.1.2. Property `item 1`](#tags_additionalProperties_anyOf_i1)
    - [7.1.3. Property `item 2`](#tags_additionalProperties_anyOf_i2)
    - [7.1.4. Property `object`](#tags_additionalProperties_anyOf_i3)

**Title:** Generic Entity

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A schema which contains the keys that all entities share.

| Property                           | Pattern | Type              | Deprecated | Definition                  | Title/Description |
| ---------------------------------- | ------- | ----------------- | ---------- | --------------------------- | ----------------- |
| + [entity_number](#entity_number ) | No      | number            | No         | In ../common/uint64.json    | Entity Number     |
| + [name](#name )                   | No      | string            | No         | -                           | Name              |
| + [position](#position )           | No      | object            | No         | In ../common/position.json  | Position          |
| - [direction](#direction )         | No      | enum (of integer) | No         | -                           | Direction         |
| - [mirror](#mirror )               | No      | boolean           | No         | -                           | Mirror            |
| - [quality](#quality )             | No      | enum (of string)  | No         | In common/quality-name.json | Quality           |
| - [tags](#tags )                   | No      | object            | No         | -                           | Tags              |

## <a name="entity_number"></a>1. Property `entity_number`

**Title:** Entity Number

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** A unique ID given to every entity contained within a blueprint. In practice, this value is the 1-indexed position of the entity inside it's parent blueprint's 'entities' list. This is not enforced however, so an entity's number can be specified with any value as long as it's unique inside that particular blueprint. This value is used for resolving associations between different entities, such as wire connections or schedule definitions.

## <a name="name"></a>2. Property `name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the entity. If this name is not recognized by Factorio when importing the entity is omitted with a notification to the console.

## <a name="position"></a>3. Property `position`

**Title:** Position

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | ../common/position.json |

**Description:** The position where the entity is located inside of it's parent blueprint. This position is (almost) always located at the spatial center of the entity. For grid-aligned entities, this position always lies either in the center of a tile or on its transition.

| Property            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#position_x ) | No      | number | No         | -          | -                 |
| - [y](#position_y ) | No      | number | No         | -          | -                 |

### <a name="position_x"></a>3.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

### <a name="position_y"></a>3.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

## <a name="direction"></a>4. Property `direction`

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

## <a name="mirror"></a>5. Property `mirror`

**Title:** Mirror

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not the input/output fluid boxes are mirrored on this particular entity.

## <a name="quality"></a>6. Property `quality`

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

## <a name="tags"></a>7. Property `tags`

**Title:** Tags

|                           |                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                          |
| **Required**              | No                                                                                |
| **Additional properties** | [Each additional property must conform to the schema](#tags_additionalProperties) |

**Description:** Any additional metadata associated with this entity, mostly intended for including mod information inside exported blueprint strings. Each key must be a string, and each value can be either a string, a boolean, a number, or another JSON object.

| Property                          | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [](#tags_additionalProperties ) | No      | Combination | No         | -          | -                 |

### <a name="tags_additionalProperties"></a>7.1. Property `additionalProperties`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                |
| --------------------------------------------- |
| [item 0](#tags_additionalProperties_anyOf_i0) |
| [item 1](#tags_additionalProperties_anyOf_i1) |
| [item 2](#tags_additionalProperties_anyOf_i2) |
| [object](#tags_additionalProperties_anyOf_i3) |

#### <a name="tags_additionalProperties_anyOf_i0"></a>7.1.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="tags_additionalProperties_anyOf_i1"></a>7.1.2. Property `item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

#### <a name="tags_additionalProperties_anyOf_i2"></a>7.1.3. Property `item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="tags_additionalProperties_anyOf_i3"></a>7.1.4. Property `object`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | object           |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

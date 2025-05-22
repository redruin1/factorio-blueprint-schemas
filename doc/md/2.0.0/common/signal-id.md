# SignalID

- [1. Property `name`](#name)
- [2. Property `type`](#type)
- [3. Property `quality`](#quality)

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An object which represents a valid signal.

| Property               | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| ---------------------- | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

## <a name="name"></a>1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="type"></a>2. Property `type`

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

## <a name="quality"></a>3. Property `quality`

**Title:** Quality

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"normal"`         |
| **Defined in** | quality-name.json  |

**Description:** A type of quality.

Must be one of:
* "normal"
* "uncommon"
* "rare"
* "epic"
* "legendary"
* "quality-unknown"

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

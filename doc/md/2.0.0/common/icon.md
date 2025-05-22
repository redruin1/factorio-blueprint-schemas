# Schema Docs

- [1. Property `index`](#index)
- [2. Property `signal`](#signal)
  - [2.1. Property `name`](#signal_name)
  - [2.2. Property `type`](#signal_type)
  - [2.3. Property `quality`](#signal_quality)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property             | Pattern | Type   | Deprecated | Definition                 | Title/Description |
| -------------------- | ------- | ------ | ---------- | -------------------------- | ----------------- |
| - [index](#index )   | No      | number | No         | In ../../common/uint8.json | uint8             |
| - [signal](#signal ) | No      | object | No         | In signal-id.json          | SignalID          |

## <a name="index"></a>1. Property `index`

**Title:** uint8

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Defined in** | ../../common/uint8.json |

**Description:** An unsigned 8-bit integer.

## <a name="signal"></a>2. Property `signal`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                      | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| ----------------------------- | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#signal_name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#signal_type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#signal_quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

### <a name="signal_name"></a>2.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

### <a name="signal_type"></a>2.2. Property `type`

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

### <a name="signal_quality"></a>2.3. Property `quality`

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

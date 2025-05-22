# Schema Docs

- [1. Property `orientation`](#orientation)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [orientation](#orientation ) | No      | number | No         | -          | Orientation       |

## <a name="orientation"></a>1. Property `orientation`

**Title:** Orientation

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0.0`    |

**Description:** A number in the range [0.0, 1.0] representing the direction this entity is facing. Any value specified out of this range is modulo'd back into this range.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

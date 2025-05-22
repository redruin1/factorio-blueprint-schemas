# Schema Docs

- [1. Property `control_behavior`](#control_behavior)
  - [1.1. Property `circuit_enabled`](#control_behavior_circuit_enabled)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#control_behavior ) | No      | object | No         | -          | -                 |

## <a name="control_behavior"></a>1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                | Pattern | Type    | Deprecated | Definition | Title/Description                                                                 |
| ------------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------------- |
| - [circuit_enabled](#control_behavior_circuit_enabled ) | No      | boolean | No         | -          | Whether or not this entity should be controlled by a specified circuit condition. |

### <a name="control_behavior_circuit_enabled"></a>1.1. Property `circuit_enabled`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified circuit condition.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

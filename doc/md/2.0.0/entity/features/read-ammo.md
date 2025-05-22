# Schema Docs

- [1. Property `control_behavior`](#control_behavior)
  - [1.1. Property `read_ammo`](#control_behavior_read_ammo)

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

| Property                                    | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [read_ammo](#control_behavior_read_ammo ) | No      | boolean | No         | -          | Read Ammo         |

### <a name="control_behavior_read_ammo"></a>1.1. Property `read_ammo`

**Title:** Read Ammo

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not to broadcast the current amount of ammo in the turrets inventory to a connected circuit network.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

# Schema Docs

- [1. Property `enable_logistics_while_moving`](#enable_logistics_while_moving)
- [2. Property `grid`](#grid)
  - [2.1. equipment-component](#grid_items)
    - [2.1.1. Property `equipment`](#grid_items_equipment)
      - [2.1.1.1. Property `name`](#grid_items_equipment_name)
      - [2.1.1.2. Property `quality`](#grid_items_equipment_quality)
    - [2.1.2. Property `position`](#grid_items_position)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                           | Pattern | Type    | Deprecated | Definition | Title/Description              |
| ------------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | ------------------------------ |
| - [enable_logistics_while_moving](#enable_logistics_while_moving ) | No      | boolean | No         | -          | Enable Logistics While Moving? |
| - [grid](#grid )                                                   | No      | array   | No         | -          | Equipment Grid Components      |

## <a name="enable_logistics_while_moving"></a>1. Property `enable_logistics_while_moving`

**Title:** Enable Logistics While Moving?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should try to fulfill it's logistic requests when it is in motion. Only has an effect if this entity is configured to have an equipment grid and that equipment grid contains personal roboports.

## <a name="grid"></a>2. Property `grid`

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

| Each item of this array must be    | Description |
| ---------------------------------- | ----------- |
| [equipment-component](#grid_items) | -           |

### <a name="grid_items"></a>2.1. equipment-component

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/equipment-component |

| Property                              | Pattern | Type   | Deprecated | Definition               | Title/Description                                                                                         |
| ------------------------------------- | ------- | ------ | ---------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| + [equipment](#grid_items_equipment ) | No      | object | No         | In #/$defs/equipment-id  | Equipment ID                                                                                              |
| + [position](#grid_items_position )   | No      | object | No         | In urn:factorio:position | The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies. |

#### <a name="grid_items_equipment"></a>2.1.1. Property `equipment`

**Title:** Equipment ID

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/equipment-id |

**Description:** A particular type of equipment and its quality.

| Property                                    | Pattern | Type   | Deprecated | Definition                   | Title/Description                                                                                             |
| ------------------------------------------- | ------- | ------ | ---------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [name](#grid_items_equipment_name )       | No      | string | No         | -                            | The name of a valid piece of equipment (that can fit inside this particular equipment grid).                  |
| - [quality](#grid_items_equipment_quality ) | No      | object | No         | In urn:factorio:quality-name | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

##### <a name="grid_items_equipment_name"></a>2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid piece of equipment (that can fit inside this particular equipment grid).

##### <a name="grid_items_equipment_quality"></a>2.1.1.2. Property `quality`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:quality-name |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

#### <a name="grid_items_position"></a>2.1.2. Property `position`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:position |

**Description:** The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

# Schema Docs

- [1. Property `priority_list`](#priority_list)
  - [1.1. urn:factorio:target-id](#priority_list_items)
- [2. Property `ignore_unprioritized`](#ignore_unprioritized)
- [3. Property `set_priority_list`](#set_priority_list)
- [4. Property `set_ignore_unprioritized`](#set_ignore_unprioritized)
- [5. Property `ignore_unlisted_targets_condition`](#ignore_unlisted_targets_condition)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                   | Pattern | Type    | Deprecated | Definition                       | Title/Description                 |
| -------------------------------------------------------------------------- | ------- | ------- | ---------- | -------------------------------- | --------------------------------- |
| - [priority_list](#priority_list )                                         | No      | array   | No         | -                                | Priority List                     |
| - [ignore_unprioritized](#ignore_unprioritized )                           | No      | boolean | No         | -                                | Ignore Unprioritized              |
| - [set_priority_list](#set_priority_list )                                 | No      | boolean | No         | -                                | Set Priority List                 |
| - [set_ignore_unprioritized](#set_ignore_unprioritized )                   | No      | boolean | No         | -                                | Set Ignore Unprioritized          |
| - [ignore_unlisted_targets_condition](#ignore_unlisted_targets_condition ) | No      | object  | No         | In urn:factorio:simple-condition | Ignore Unlisted Targets Condition |

## <a name="priority_list"></a>1. Property `priority_list`

**Title:** Priority List

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |
| **Default**  | `[]`    |

**Description:** The (static) list of priority targets that this turret should aim for. Overwritten by circuit network signals if 'set_priority_list' is 'true'.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                | Description                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:target-id](#priority_list_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

### <a name="priority_list_items"></a>1.1. urn:factorio:target-id

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:target-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

## <a name="ignore_unprioritized"></a>2. Property `ignore_unprioritized`

**Title:** Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not to completely ignore enemies that do not lie in this turret's target priority lists.

## <a name="set_priority_list"></a>3. Property `set_priority_list`

**Title:** Set Priority List

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should set its target priorities via connected circuit network signals.

## <a name="set_ignore_unprioritized"></a>4. Property `set_ignore_unprioritized`

**Title:** Set Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should have it's ignore unprioritized behavior be set conditionally via 'ignore_unlisted_targets_condition'.

## <a name="ignore_unlisted_targets_condition"></a>5. Property `ignore_unlisted_targets_condition`

**Title:** Ignore Unlisted Targets Condition

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | urn:factorio:simple-condition |

**Description:** A condition which must be true in order for non-prioritized targets to be entirely ignored when this turret is targeting. Does nothing unless 'set_ignore_unprioritized' is 'true'.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

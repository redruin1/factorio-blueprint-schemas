# Schema Docs

- [1. Property `control_behavior`](#control_behavior)
  - [1.1. Property `connect_to_logistic_network`](#control_behavior_connect_to_logistic_network)
  - [1.2. Property `logistic_condition`](#control_behavior_logistic_condition)
    - [1.2.1. Property `first_signal`](#control_behavior_logistic_condition_first_signal)
      - [1.2.1.1. Property `SignalID`](#control_behavior_logistic_condition_first_signal_oneOf_i0)
        - [1.2.1.1.1. Property `name`](#control_behavior_logistic_condition_first_signal_oneOf_i0_name)
        - [1.2.1.1.2. Property `type`](#control_behavior_logistic_condition_first_signal_oneOf_i0_type)
        - [1.2.1.1.3. Property `quality`](#control_behavior_logistic_condition_first_signal_oneOf_i0_quality)
      - [1.2.1.2. Property `item 1`](#control_behavior_logistic_condition_first_signal_oneOf_i1)
    - [1.2.2. Property `comparator`](#control_behavior_logistic_condition_comparator)
    - [1.2.3. Property `constant`](#control_behavior_logistic_condition_constant)
    - [1.2.4. Property `second_signal`](#control_behavior_logistic_condition_second_signal)
      - [1.2.4.1. Property `SignalID`](#control_behavior_logistic_condition_second_signal_oneOf_i0)
      - [1.2.4.2. Property `item 1`](#control_behavior_logistic_condition_second_signal_oneOf_i1)

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

| Property                                                                        | Pattern | Type    | Deprecated | Definition                     | Title/Description            |
| ------------------------------------------------------------------------------- | ------- | ------- | ---------- | ------------------------------ | ---------------------------- |
| - [connect_to_logistic_network](#control_behavior_connect_to_logistic_network ) | No      | boolean | No         | -                              | Connect to logistic network? |
| - [logistic_condition](#control_behavior_logistic_condition )                   | No      | object  | No         | In ../../common/condition.json | Logistic Condition           |

### <a name="control_behavior_connect_to_logistic_network"></a>1.1. Property `connect_to_logistic_network`

**Title:** Connect to logistic network?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified logistic condition.

### <a name="control_behavior_logistic_condition"></a>1.2. Property `logistic_condition`

**Title:** Logistic Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** The logistic condition that the entity should be enabled with, if 'connect_to_logistic_network' is 'true'.

| Property                                                               | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ---------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#control_behavior_logistic_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#control_behavior_logistic_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#control_behavior_logistic_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#control_behavior_logistic_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

#### <a name="control_behavior_logistic_condition_first_signal"></a>1.2.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                         |
| ---------------------------------------------------------------------- |
| [SignalID](#control_behavior_logistic_condition_first_signal_oneOf_i0) |
| [item 1](#control_behavior_logistic_condition_first_signal_oneOf_i1)   |

##### <a name="control_behavior_logistic_condition_first_signal_oneOf_i0"></a>1.2.1.1. Property `SignalID`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                                                         | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| -------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#control_behavior_logistic_condition_first_signal_oneOf_i0_name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#control_behavior_logistic_condition_first_signal_oneOf_i0_type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#control_behavior_logistic_condition_first_signal_oneOf_i0_quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

###### <a name="control_behavior_logistic_condition_first_signal_oneOf_i0_name"></a>1.2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="control_behavior_logistic_condition_first_signal_oneOf_i0_type"></a>1.2.1.1.2. Property `type`

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

###### <a name="control_behavior_logistic_condition_first_signal_oneOf_i0_quality"></a>1.2.1.1.3. Property `quality`

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

##### <a name="control_behavior_logistic_condition_first_signal_oneOf_i1"></a>1.2.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="control_behavior_logistic_condition_comparator"></a>1.2.2. Property `comparator`

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

#### <a name="control_behavior_logistic_condition_constant"></a>1.2.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

#### <a name="control_behavior_logistic_condition_second_signal"></a>1.2.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                          |
| ----------------------------------------------------------------------- |
| [SignalID](#control_behavior_logistic_condition_second_signal_oneOf_i0) |
| [item 1](#control_behavior_logistic_condition_second_signal_oneOf_i1)   |

##### <a name="control_behavior_logistic_condition_second_signal_oneOf_i0"></a>1.2.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **Type**                  | `object`                                                               |
| **Required**              | No                                                                     |
| **Additional properties** | Any type allowed                                                       |
| **Same definition as**    | [SignalID](#control_behavior_logistic_condition_first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

##### <a name="control_behavior_logistic_condition_second_signal_oneOf_i1"></a>1.2.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

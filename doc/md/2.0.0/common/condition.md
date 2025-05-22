# Condition

- [1. Property `first_signal`](#first_signal)
  - [1.1. Property `SignalID`](#first_signal_oneOf_i0)
    - [1.1.1. Property `name`](#first_signal_oneOf_i0_name)
    - [1.1.2. Property `type`](#first_signal_oneOf_i0_type)
    - [1.1.3. Property `quality`](#first_signal_oneOf_i0_quality)
  - [1.2. Property `item 1`](#first_signal_oneOf_i1)
- [2. Property `comparator`](#comparator)
- [3. Property `constant`](#constant)
- [4. Property `second_signal`](#second_signal)
  - [4.1. Property `SignalID`](#second_signal_oneOf_i0)
  - [4.2. Property `item 1`](#second_signal_oneOf_i1)

**Title:** Condition

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A conditional statement between either 2 signals or 1 signal and 1 constant value.

| Property                           | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ---------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

## <a name="first_signal"></a>1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                     |
| ---------------------------------- |
| [SignalID](#first_signal_oneOf_i0) |
| [item 1](#first_signal_oneOf_i1)   |

### <a name="first_signal_oneOf_i0"></a>1.1. Property `SignalID`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                     | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| -------------------------------------------- | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#first_signal_oneOf_i0_name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#first_signal_oneOf_i0_type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#first_signal_oneOf_i0_quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

#### <a name="first_signal_oneOf_i0_name"></a>1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="first_signal_oneOf_i0_type"></a>1.1.2. Property `type`

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

#### <a name="first_signal_oneOf_i0_quality"></a>1.1.3. Property `quality`

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

### <a name="first_signal_oneOf_i1"></a>1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="comparator"></a>2. Property `comparator`

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

## <a name="constant"></a>3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

## <a name="second_signal"></a>4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                      |
| ----------------------------------- |
| [SignalID](#second_signal_oneOf_i0) |
| [item 1](#second_signal_oneOf_i1)   |

### <a name="second_signal_oneOf_i0"></a>4.1. Property `SignalID`

**Title:** SignalID

|                           |                                    |
| ------------------------- | ---------------------------------- |
| **Type**                  | `object`                           |
| **Required**              | No                                 |
| **Additional properties** | Any type allowed                   |
| **Same definition as**    | [SignalID](#first_signal_oneOf_i0) |

**Description:** An object which represents a valid signal.

### <a name="second_signal_oneOf_i1"></a>4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

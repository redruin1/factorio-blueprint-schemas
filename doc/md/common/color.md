# Color

- [1. Property `r`](#r)
- [2. Property `g`](#g)
- [3. Property `b`](#b)
- [4. Property `a`](#a)
  - [4.1. Property `color-component`](#a_oneOf_i0)
  - [4.2. Property `item 1`](#a_oneOf_i1)

**Title:** Color

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** An object which stores an RGBA color value. Each color component can be either specified as a float in the [0.0, 1.0] range, or as a integer in the [0, 255] range. If any of the given values exceeds 1, then the color is interpreted with the latter range, otherwise the former. Colors specified in the [0, 255] range are normalized to the [0.0, 1.0] range upon import/export cycle.

| Property   | Pattern | Type        | Deprecated | Definition                 | Title/Description |
| ---------- | ------- | ----------- | ---------- | -------------------------- | ----------------- |
| + [r](#r ) | No      | number      | No         | In #/$defs/color-component | Red               |
| + [g](#g ) | No      | number      | No         | In #/$defs/color-component | Green             |
| + [b](#b ) | No      | number      | No         | In #/$defs/color-component | Blue              |
| - [a](#a ) | No      | Combination | No         | -                          | Alpha             |

## <a name="r"></a>1. Property `r`

**Title:** Red

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

## <a name="g"></a>2. Property `g`

**Title:** Green

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

## <a name="b"></a>3. Property `b`

**Title:** Blue

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

## <a name="a"></a>4. Property `a`

**Title:** Alpha

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                 |
| ------------------------------ |
| [color-component](#a_oneOf_i0) |
| [item 1](#a_oneOf_i1)          |

### <a name="a_oneOf_i0"></a>4.1. Property `color-component`

|                        |          |
| ---------------------- | -------- |
| **Type**               | `number` |
| **Required**           | No       |
| **Same definition as** | [r](#r)  |

### <a name="a_oneOf_i1"></a>4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

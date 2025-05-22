# Blueprint Root

- [1. Property `index`](#index)
  - [1.1. Property `uint16`](#index_oneOf_i0)
  - [1.2. Property `Null`](#index_oneOf_i1)
- [2. Property `blueprint`](#blueprint)
  - [2.1. Property `item`](#blueprint_item)
  - [2.2. Property `label`](#blueprint_label)
  - [2.3. Property `label_color`](#blueprint_label_color)
    - [2.3.1. Property `r`](#blueprint_label_color_r)
    - [2.3.2. Property `g`](#blueprint_label_color_g)
    - [2.3.3. Property `b`](#blueprint_label_color_b)
    - [2.3.4. Property `a`](#blueprint_label_color_a)
      - [2.3.4.1. Property `color-component`](#blueprint_label_color_a_oneOf_i0)
      - [2.3.4.2. Property `item 1`](#blueprint_label_color_a_oneOf_i1)
  - [2.4. Property `description`](#blueprint_description)
  - [2.5. Property `icons`](#blueprint_icons)
    - [2.5.1. icon.json](#blueprint_icons_items)
      - [2.5.1.1. Property `index`](#blueprint_icons_items_index)
      - [2.5.1.2. Property `signal`](#blueprint_icons_items_signal)
        - [2.5.1.2.1. Property `name`](#blueprint_icons_items_signal_name)
        - [2.5.1.2.2. Property `type`](#blueprint_icons_items_signal_type)
        - [2.5.1.2.3. Property `quality`](#blueprint_icons_items_signal_quality)
  - [2.6. Property `version`](#blueprint_version)
  - [2.7. Property `snap-to-grid`](#blueprint_snap-to-grid)
  - [2.8. Property `absolute-snapping`](#blueprint_absolute-snapping)
  - [2.9. Property `position-relative-to-grid`](#blueprint_position-relative-to-grid)
    - [2.9.1. Property `x`](#blueprint_position-relative-to-grid_x)
    - [2.9.2. Property `y`](#blueprint_position-relative-to-grid_y)
  - [2.10. Property `entities`](#blueprint_entities)
    - [2.10.1. entities items](#blueprint_entities_items)
      - [2.10.1.1. Property `Accumulator`](#blueprint_entities_items_anyOf_i0)
        - [2.10.1.1.1. Property `entity_number`](#blueprint_entities_items_anyOf_i0_entity_number)
        - [2.10.1.1.2. Property `name`](#blueprint_entities_items_anyOf_i0_name)
        - [2.10.1.1.3. Property `position`](#blueprint_entities_items_anyOf_i0_position)
          - [2.10.1.1.3.1. Property `x`](#blueprint_position-relative-to-grid_x)
          - [2.10.1.1.3.2. Property `y`](#blueprint_position-relative-to-grid_y)
        - [2.10.1.1.4. Property `direction`](#blueprint_entities_items_anyOf_i0_direction)
        - [2.10.1.1.5. Property `mirror`](#blueprint_entities_items_anyOf_i0_mirror)
        - [2.10.1.1.6. Property `quality`](#blueprint_entities_items_anyOf_i0_quality)
        - [2.10.1.1.7. Property `tags`](#blueprint_entities_items_anyOf_i0_tags)
          - [2.10.1.1.7.1. Property `additionalProperties`](#blueprint_entities_items_anyOf_i0_tags_additionalProperties)
            - [2.10.1.1.7.1.1. Property `item 0`](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0)
            - [2.10.1.1.7.1.2. Property `item 1`](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1)
            - [2.10.1.1.7.1.3. Property `item 2`](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2)
            - [2.10.1.1.7.1.4. Property `object`](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3)
        - [2.10.1.1.8. Property `control_behavior`](#blueprint_entities_items_anyOf_i0_control_behavior)
          - [2.10.1.1.8.1. Property `output_signal`](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal)
            - [2.10.1.1.8.1.1. Property `SignalID`](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0)
            - [2.10.1.1.8.1.2. Property `item 1`](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1)
      - [2.10.1.2. Property `Agricultural Tower`](#blueprint_entities_items_anyOf_i1)
        - [2.10.1.2.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i1_allOf_i0)
        - [2.10.1.2.2. Property `item-requests.json`](#blueprint_entities_items_anyOf_i1_allOf_i1)
          - [2.10.1.2.2.1. Property `items`](#blueprint_entities_items_anyOf_i1_allOf_i1_items)
            - [2.10.1.2.2.1.1. urn:factorio:item-request](#blueprint_entities_items_anyOf_i1_allOf_i1_items_items)
        - [2.10.1.2.3. Property `circuit-enabled.json`](#blueprint_entities_items_anyOf_i1_allOf_i2)
          - [2.10.1.2.3.1. Property `control_behavior`](#blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior)
            - [2.10.1.2.3.1.1. Property `circuit_enabled`](#blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled)
        - [2.10.1.2.4. Property `circuit-condition.json`](#blueprint_entities_items_anyOf_i1_allOf_i3)
          - [2.10.1.2.4.1. Property `control_behavior`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior)
            - [2.10.1.2.4.1.1. Property `circuit_condition`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition)
              - [2.10.1.2.4.1.1.1. Property `first_signal`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal)
                - [2.10.1.2.4.1.1.1.1. Property `SignalID`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
                - [2.10.1.2.4.1.1.1.2. Property `item 1`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
              - [2.10.1.2.4.1.1.2. Property `comparator`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator)
              - [2.10.1.2.4.1.1.3. Property `constant`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant)
              - [2.10.1.2.4.1.1.4. Property `second_signal`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal)
                - [2.10.1.2.4.1.1.4.1. Property `SignalID`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
                - [2.10.1.2.4.1.1.4.2. Property `item 1`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
        - [2.10.1.2.5. Property `logistic-condition.json`](#blueprint_entities_items_anyOf_i1_allOf_i4)
          - [2.10.1.2.5.1. Property `control_behavior`](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior)
            - [2.10.1.2.5.1.1. Property `connect_to_logistic_network`](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network)
            - [2.10.1.2.5.1.2. Property `logistic_condition`](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition)
              - [2.10.1.2.5.1.2.1. Property `first_signal`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal)
                - [2.10.1.2.5.1.2.1.1. Property `SignalID`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
                - [2.10.1.2.5.1.2.1.2. Property `item 1`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
              - [2.10.1.2.5.1.2.2. Property `comparator`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator)
              - [2.10.1.2.5.1.2.3. Property `constant`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant)
              - [2.10.1.2.5.1.2.4. Property `second_signal`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal)
                - [2.10.1.2.5.1.2.4.1. Property `SignalID`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
                - [2.10.1.2.5.1.2.4.2. Property `item 1`](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
        - [2.10.1.2.6. Property `control_behavior`](#blueprint_entities_items_anyOf_i1_control_behavior)
          - [2.10.1.2.6.1. Property `read_contents`](#blueprint_entities_items_anyOf_i1_control_behavior_read_contents)
      - [2.10.1.3. Property `Ammo Turret`](#blueprint_entities_items_anyOf_i2)
        - [2.10.1.3.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i2_allOf_i0)
        - [2.10.1.3.2. Property `item-requests.json`](#blueprint_entities_items_anyOf_i2_allOf_i1)
        - [2.10.1.3.3. Property `circuit-enabled.json`](#blueprint_entities_items_anyOf_i2_allOf_i2)
        - [2.10.1.3.4. Property `circuit-condition.json`](#blueprint_entities_items_anyOf_i2_allOf_i3)
        - [2.10.1.3.5. Property `logistic-condition.json`](#blueprint_entities_items_anyOf_i2_allOf_i4)
        - [2.10.1.3.6. Property `turret-priorities.json`](#blueprint_entities_items_anyOf_i2_allOf_i5)
          - [2.10.1.3.6.1. Property `priority_list`](#blueprint_entities_items_anyOf_i2_allOf_i5_priority_list)
            - [2.10.1.3.6.1.1. urn:factorio:target-id](#blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items)
          - [2.10.1.3.6.2. Property `ignore_unprioritized`](#blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized)
          - [2.10.1.3.6.3. Property `set_priority_list`](#blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list)
          - [2.10.1.3.6.4. Property `set_ignore_unprioritized`](#blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized)
          - [2.10.1.3.6.5. Property `ignore_unlisted_targets_condition`](#blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition)
        - [2.10.1.3.7. Property `read-ammo.json`](#blueprint_entities_items_anyOf_i2_allOf_i6)
          - [2.10.1.3.7.1. Property `control_behavior`](#blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior)
            - [2.10.1.3.7.1.1. Property `read_ammo`](#blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo)
      - [2.10.1.4. Property `Arithmetic Combinator`](#blueprint_entities_items_anyOf_i3)
        - [2.10.1.4.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i3_allOf_i0)
        - [2.10.1.4.2. Property `player-description.json`](#blueprint_entities_items_anyOf_i3_allOf_i1)
          - [2.10.1.4.2.1. Property `player_description`](#blueprint_entities_items_anyOf_i3_allOf_i1_player_description)
        - [2.10.1.4.3. Property `control_behavior`](#blueprint_entities_items_anyOf_i3_control_behavior)
          - [2.10.1.4.3.1. Property `arithmetic_conditions`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions)
            - [2.10.1.4.3.1.1. Property `first_constant`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant)
              - [2.10.1.4.3.1.1.1. Property `int32.json`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0)
              - [2.10.1.4.3.1.1.2. Property `item 1`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1)
            - [2.10.1.4.3.1.2. Property `first_signal`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal)
              - [2.10.1.4.3.1.2.1. Property `SignalID`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0)
              - [2.10.1.4.3.1.2.2. Property `item 1`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1)
            - [2.10.1.4.3.1.3. Property `first_signal_networks`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks)
              - [2.10.1.4.3.1.3.1. Property `red`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red)
              - [2.10.1.4.3.1.3.2. Property `green`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green)
            - [2.10.1.4.3.1.4. Property `operation`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation)
            - [2.10.1.4.3.1.5. Property `second_constant`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant)
              - [2.10.1.4.3.1.5.1. Property `int32.json`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0)
              - [2.10.1.4.3.1.5.2. Property `item 1`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1)
            - [2.10.1.4.3.1.6. Property `second_signal`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal)
              - [2.10.1.4.3.1.6.1. Property `SignalID`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0)
              - [2.10.1.4.3.1.6.2. Property `item 1`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1)
            - [2.10.1.4.3.1.7. Property `second_signal_networks`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks)
              - [2.10.1.4.3.1.7.1. Property `red`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red)
              - [2.10.1.4.3.1.7.2. Property `green`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green)
            - [2.10.1.4.3.1.8. Property `output_signal`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal)
              - [2.10.1.4.3.1.8.1. Property `SignalID`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0)
              - [2.10.1.4.3.1.8.2. Property `item 1`](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1)
      - [2.10.1.5. Property `Artillery Turret`](#blueprint_entities_items_anyOf_i4)
        - [2.10.1.5.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i4_allOf_i0)
        - [2.10.1.5.2. Property `item-requests.json`](#blueprint_entities_items_anyOf_i4_allOf_i1)
        - [2.10.1.5.3. Property `circuit-enabled.json`](#blueprint_entities_items_anyOf_i4_allOf_i2)
        - [2.10.1.5.4. Property `circuit-condition.json`](#blueprint_entities_items_anyOf_i4_allOf_i3)
        - [2.10.1.5.5. Property `logistic-condition.json`](#blueprint_entities_items_anyOf_i4_allOf_i4)
        - [2.10.1.5.6. Property `read-ammo.json`](#blueprint_entities_items_anyOf_i4_allOf_i5)
        - [2.10.1.5.7. Property `artillery-auto-targeting.json`](#blueprint_entities_items_anyOf_i4_allOf_i6)
          - [2.10.1.5.7.1. Property `artillery_auto_targeting`](#blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting)
      - [2.10.1.6. Property `Artillery Wagon`](#blueprint_entities_items_anyOf_i5)
        - [2.10.1.6.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i5_allOf_i0)
        - [2.10.1.6.2. Property `orientation.json`](#blueprint_entities_items_anyOf_i5_allOf_i1)
          - [2.10.1.6.2.1. Property `orientation`](#blueprint_entities_items_anyOf_i5_allOf_i1_orientation)
        - [2.10.1.6.3. Property `item-requests.json`](#blueprint_entities_items_anyOf_i5_allOf_i2)
        - [2.10.1.6.4. Property `equipment-grid.json`](#blueprint_entities_items_anyOf_i5_allOf_i3)
          - [2.10.1.6.4.1. Property `enable_logistics_while_moving`](#blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving)
          - [2.10.1.6.4.2. Property `grid`](#blueprint_entities_items_anyOf_i5_allOf_i3_grid)
            - [2.10.1.6.4.2.1. equipment-component](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items)
              - [2.10.1.6.4.2.1.1. Property `equipment`](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment)
                - [2.10.1.6.4.2.1.1.1. Property `name`](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name)
                - [2.10.1.6.4.2.1.1.2. Property `quality`](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality)
              - [2.10.1.6.4.2.1.2. Property `position`](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position)
        - [2.10.1.6.5. Property `artillery-auto-targeting.json`](#blueprint_entities_items_anyOf_i5_allOf_i4)
      - [2.10.1.7. Property `Assembling Machine`](#blueprint_entities_items_anyOf_i6)
        - [2.10.1.7.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i6_allOf_i0)
        - [2.10.1.7.2. Property `item-requests.json`](#blueprint_entities_items_anyOf_i6_allOf_i1)
        - [2.10.1.7.3. Property `circuit-enabled.json`](#blueprint_entities_items_anyOf_i6_allOf_i2)
        - [2.10.1.7.4. Property `circuit-condition.json`](#blueprint_entities_items_anyOf_i6_allOf_i3)
        - [2.10.1.7.5. Property `logistic-condition.json`](#blueprint_entities_items_anyOf_i6_allOf_i4)
        - [2.10.1.7.6. Property `recipe`](#blueprint_entities_items_anyOf_i6_recipe)
          - [2.10.1.7.6.1. Property `item 0`](#blueprint_entities_items_anyOf_i6_recipe_oneOf_i0)
          - [2.10.1.7.6.2. Property `item 1`](#blueprint_entities_items_anyOf_i6_recipe_oneOf_i1)
        - [2.10.1.7.7. Property `recipe_quality`](#blueprint_entities_items_anyOf_i6_recipe_quality)
        - [2.10.1.7.8. Property `control_behavior`](#blueprint_entities_items_anyOf_i6_control_behavior)
          - [2.10.1.7.8.1. Property `set_recipe`](#blueprint_entities_items_anyOf_i6_control_behavior_set_recipe)
          - [2.10.1.7.8.2. Property `read_contents`](#blueprint_entities_items_anyOf_i6_control_behavior_read_contents)
          - [2.10.1.7.8.3. Property `include_in_crafting`](#blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting)
          - [2.10.1.7.8.4. Property `read_recipe_finished`](#blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished)
          - [2.10.1.7.8.5. Property `recipe_finished_signal`](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal)
            - [2.10.1.7.8.5.1. Property `urn:factorio:signal-id`](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0)
            - [2.10.1.7.8.5.2. Property `item 1`](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1)
          - [2.10.1.7.8.6. Property `read_working`](#blueprint_entities_items_anyOf_i6_control_behavior_read_working)
          - [2.10.1.7.8.7. Property `working_signal`](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal)
            - [2.10.1.7.8.7.1. Property `urn:factorio:signal-id`](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0)
            - [2.10.1.7.8.7.2. Property `item 1`](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1)
      - [2.10.1.8. Property `Asteroid Collector`](#blueprint_entities_items_anyOf_i7)
        - [2.10.1.8.1. Property `Generic Entity`](#blueprint_entities_items_anyOf_i7_allOf_i0)
        - [2.10.1.8.2. Property `item-requests.json`](#blueprint_entities_items_anyOf_i7_allOf_i1)
        - [2.10.1.8.3. Property `circuit-enabled.json`](#blueprint_entities_items_anyOf_i7_allOf_i2)
        - [2.10.1.8.4. Property `circuit-condition.json`](#blueprint_entities_items_anyOf_i7_allOf_i3)
        - [2.10.1.8.5. Property `result_inventory`](#blueprint_entities_items_anyOf_i7_result_inventory)
          - [2.10.1.8.5.1. Property `bar`](#blueprint_entities_items_anyOf_i7_result_inventory_bar)
        - [2.10.1.8.6. Property `chunk-filter`](#blueprint_entities_items_anyOf_i7_chunk-filter)
          - [2.10.1.8.6.1. asteroid-chunk-id](#blueprint_entities_items_anyOf_i7_chunk-filter_items)
            - [2.10.1.8.6.1.1. Property `index`](#blueprint_entities_items_anyOf_i7_chunk-filter_items_index)
            - [2.10.1.8.6.1.2. Property `name`](#blueprint_entities_items_anyOf_i7_chunk-filter_items_name)
        - [2.10.1.8.7. Property `control_behavior`](#blueprint_entities_items_anyOf_i7_control_behavior)
          - [2.10.1.8.7.1. Property `circuit_set_filters`](#blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters)
          - [2.10.1.8.7.2. Property `circuit_read_contents`](#blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents)
          - [2.10.1.8.7.3. Property `include_hands`](#blueprint_entities_items_anyOf_i7_control_behavior_include_hands)
  - [2.11. Property `tiles`](#blueprint_tiles)
    - [2.11.1. urn:factorio:tile](#blueprint_tiles_items)
  - [2.12. Property `wires`](#blueprint_wires)
    - [2.12.1. wires items](#blueprint_wires_items)
      - [2.12.1.1. uint64](#autogenerated_heading_2)
      - [2.12.1.2. wires items item 1](#autogenerated_heading_3)
      - [2.12.1.3. uint64](#autogenerated_heading_4)
      - [2.12.1.4. wires items item 3](#autogenerated_heading_5)
  - [2.13. Property `schedules`](#blueprint_schedules)
    - [2.13.1. urn:factorio:schedule](#blueprint_schedules_items)
  - [2.14. Property `stock_connections`](#blueprint_stock_connections)
    - [2.14.1. urn:factorio:stock-connection](#blueprint_stock_connections_items)

**Title:** Blueprint Root

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A regular blueprint, which can contain entities, tiles, schedules, wire connections, stock connections, in addition to additional metadata.

| Property                   | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [index](#index )         | No      | Combination | No         | -          | Index             |
| - [blueprint](#blueprint ) | No      | object      | No         | -          | Blueprint Object  |

## <a name="index"></a>1. Property `index`

**Title:** Index

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The unique index of the blueprint, if it lies inside of a parent blueprint book. If not inside of a blueprint book, this key has no effect.

| One of(Option)            |
| ------------------------- |
| [uint16](#index_oneOf_i0) |
| [Null](#index_oneOf_i1)   |

### <a name="index_oneOf_i0"></a>1.1. Property `uint16`

**Title:** uint16

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | No                    |
| **Defined in** | ../common/uint16.json |

**Description:** An unsigned 16-bit integer.

### <a name="index_oneOf_i1"></a>1.2. Property `Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

## <a name="blueprint"></a>2. Property `blueprint`

**Title:** Blueprint Object

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Main object of the blueprint, which actually contains the majority of its keys.

| Property                                                             | Pattern | Type           | Deprecated | Definition                 | Title/Description         |
| -------------------------------------------------------------------- | ------- | -------------- | ---------- | -------------------------- | ------------------------- |
| + [item](#blueprint_item )                                           | No      | const          | No         | -                          | Item                      |
| - [label](#blueprint_label )                                         | No      | string         | No         | -                          | Label                     |
| - [label_color](#blueprint_label_color )                             | No      | object         | No         | In ../common/color.json    | Label Color               |
| - [description](#blueprint_description )                             | No      | string         | No         | -                          | Description               |
| - [icons](#blueprint_icons )                                         | No      | array          | No         | -                          | Icons                     |
| + [version](#blueprint_version )                                     | No      | number         | No         | In ../common/uint64.json   | Version                   |
| - [snap-to-grid](#blueprint_snap-to-grid )                           | No      | object         | No         | In common/position.json    | Snap to Grid              |
| - [absolute-snapping](#blueprint_absolute-snapping )                 | No      | boolean        | No         | -                          | Absolute Snapping         |
| - [position-relative-to-grid](#blueprint_position-relative-to-grid ) | No      | object         | No         | In ../common/position.json | Position Relative to Grid |
| - [entities](#blueprint_entities )                                   | No      | array          | No         | -                          | Entities                  |
| - [tiles](#blueprint_tiles )                                         | No      | array          | No         | -                          | Tiles                     |
| - [wires](#blueprint_wires )                                         | No      | array of array | No         | -                          | Wires                     |
| - [schedules](#blueprint_schedules )                                 | No      | array          | No         | -                          | Wires                     |
| - [stock_connections](#blueprint_stock_connections )                 | No      | array          | No         | -                          | Stock Connections         |

### <a name="blueprint_item"></a>2.1. Property `item`

**Title:** Item

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** The name of the item associated with this blueprintable.

Specific value: `"blueprint"`

### <a name="blueprint_label"></a>2.2. Property `label`

**Title:** Label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** The player-given title of this blueprint. Can be specified with rich text colors and icons. If omitted or specified as an empty string, then the blueprint is given the default name 'Blueprint'.

### <a name="blueprint_label_color"></a>2.3. Property `label_color`

**Title:** Label Color

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | ../common/color.json |

**Description:** The color of the label. If omitted, this color defaults to a special hybrid color, where it is white in your inventory and black when being placed.

| Property                         | Pattern | Type        | Deprecated | Definition                 | Title/Description |
| -------------------------------- | ------- | ----------- | ---------- | -------------------------- | ----------------- |
| + [r](#blueprint_label_color_r ) | No      | number      | No         | In #/$defs/color-component | Red               |
| + [g](#blueprint_label_color_g ) | No      | number      | No         | In #/$defs/color-component | Green             |
| + [b](#blueprint_label_color_b ) | No      | number      | No         | In #/$defs/color-component | Blue              |
| - [a](#blueprint_label_color_a ) | No      | Combination | No         | -                          | Alpha             |

#### <a name="blueprint_label_color_r"></a>2.3.1. Property `r`

**Title:** Red

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

#### <a name="blueprint_label_color_g"></a>2.3.2. Property `g`

**Title:** Green

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

#### <a name="blueprint_label_color_b"></a>2.3.3. Property `b`

**Title:** Blue

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

#### <a name="blueprint_label_color_a"></a>2.3.4. Property `a`

**Title:** Alpha

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                       |
| ---------------------------------------------------- |
| [color-component](#blueprint_label_color_a_oneOf_i0) |
| [item 1](#blueprint_label_color_a_oneOf_i1)          |

##### <a name="blueprint_label_color_a_oneOf_i0"></a>2.3.4.1. Property `color-component`

|                        |                               |
| ---------------------- | ----------------------------- |
| **Type**               | `number`                      |
| **Required**           | No                            |
| **Same definition as** | [r](#blueprint_label_color_r) |

##### <a name="blueprint_label_color_a_oneOf_i1"></a>2.3.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="blueprint_description"></a>2.4. Property `description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** The player-given description of this blueprint. Can be specified with rich text colors and icons.

### <a name="blueprint_icons"></a>2.5. Property `icons`

**Title:** Icons

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The list of icons to display over the blueprint item, with a maximum of 4 icons total.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | 4                  |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be     | Description |
| ----------------------------------- | ----------- |
| [icon.json](#blueprint_icons_items) | -           |

#### <a name="blueprint_icons_items"></a>2.5.1. icon.json

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | common/icon.json |

| Property                                   | Pattern | Type   | Deprecated | Definition                 | Title/Description |
| ------------------------------------------ | ------- | ------ | ---------- | -------------------------- | ----------------- |
| - [index](#blueprint_icons_items_index )   | No      | number | No         | In ../../common/uint8.json | uint8             |
| - [signal](#blueprint_icons_items_signal ) | No      | object | No         | In signal-id.json          | SignalID          |

##### <a name="blueprint_icons_items_index"></a>2.5.1.1. Property `index`

**Title:** uint8

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Defined in** | ../../common/uint8.json |

**Description:** An unsigned 8-bit integer.

##### <a name="blueprint_icons_items_signal"></a>2.5.1.2. Property `signal`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                            | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| --------------------------------------------------- | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#blueprint_icons_items_signal_name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#blueprint_icons_items_signal_type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#blueprint_icons_items_signal_quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

###### <a name="blueprint_icons_items_signal_name"></a>2.5.1.2.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="blueprint_icons_items_signal_type"></a>2.5.1.2.2. Property `type`

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

###### <a name="blueprint_icons_items_signal_quality"></a>2.5.1.2.3. Property `quality`

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

### <a name="blueprint_version"></a>2.6. Property `version`

**Title:** Version

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** The version of the game associated with this blueprint string. Encoded as four bytes, where each byte corresponds to a semantic version number.

### <a name="blueprint_snap-to-grid"></a>2.7. Property `snap-to-grid`

**Title:** Snap to Grid

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | common/position.json |

**Description:** A snapping grid with a width ('x') and height ('y') to apply when placing this blueprint. If this field is omitted, this means the blueprint has no snapping grid.

### <a name="blueprint_absolute-snapping"></a>2.8. Property `absolute-snapping`

**Title:** Absolute Snapping

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this blueprint will use absolute coordinates when snapping to it's defined snapping grid. If no snapping grid is defined, this key does nothing.

### <a name="blueprint_position-relative-to-grid"></a>2.9. Property `position-relative-to-grid`

**Title:** Position Relative to Grid

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Default**               | `{"x": 0, "y": 0}`      |
| **Defined in**            | ../common/position.json |

**Description:** The coordinate offset to give the snapping grid (as indicated by the flag icon in the Blueprint's inspection GUI).

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#blueprint_position-relative-to-grid_x ) | No      | number | No         | -          | -                 |
| - [y](#blueprint_position-relative-to-grid_y ) | No      | number | No         | -          | -                 |

#### <a name="blueprint_position-relative-to-grid_x"></a>2.9.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="blueprint_position-relative-to-grid_y"></a>2.9.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

### <a name="blueprint_entities"></a>2.10. Property `entities`

**Title:** Entities

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |
| **Default**  | `[]`    |

**Description:** The list of all entities stored inside this blueprint.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [entities items](#blueprint_entities_items) | -           |

#### <a name="blueprint_entities_items"></a>2.10.1. entities items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                              |
| ----------------------------------------------------------- |
| [Accumulator](#blueprint_entities_items_anyOf_i0)           |
| [Agricultural Tower](#blueprint_entities_items_anyOf_i1)    |
| [Ammo Turret](#blueprint_entities_items_anyOf_i2)           |
| [Arithmetic Combinator](#blueprint_entities_items_anyOf_i3) |
| [Artillery Turret](#blueprint_entities_items_anyOf_i4)      |
| [Artillery Wagon](#blueprint_entities_items_anyOf_i5)       |
| [Assembling Machine](#blueprint_entities_items_anyOf_i6)    |
| [Asteroid Collector](#blueprint_entities_items_anyOf_i7)    |

##### <a name="blueprint_entities_items_anyOf_i0"></a>2.10.1.1. Property `Accumulator`

**Title:** Accumulator

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | entity/accumulator.json |

**Description:** An entity that stores electricity for periods of high demand.

| Property                                                                   | Pattern | Type              | Deprecated | Definition                  | Title/Description |
| -------------------------------------------------------------------------- | ------- | ----------------- | ---------- | --------------------------- | ----------------- |
| + [entity_number](#blueprint_entities_items_anyOf_i0_entity_number )       | No      | number            | No         | In ../common/uint64.json    | Entity Number     |
| + [name](#blueprint_entities_items_anyOf_i0_name )                         | No      | string            | No         | -                           | Name              |
| + [position](#blueprint_entities_items_anyOf_i0_position )                 | No      | object            | No         | In ../common/position.json  | Position          |
| - [direction](#blueprint_entities_items_anyOf_i0_direction )               | No      | enum (of integer) | No         | -                           | Direction         |
| - [mirror](#blueprint_entities_items_anyOf_i0_mirror )                     | No      | boolean           | No         | -                           | Mirror            |
| - [quality](#blueprint_entities_items_anyOf_i0_quality )                   | No      | enum (of string)  | No         | In common/quality-name.json | Quality           |
| - [tags](#blueprint_entities_items_anyOf_i0_tags )                         | No      | object            | No         | -                           | Tags              |
| - [control_behavior](#blueprint_entities_items_anyOf_i0_control_behavior ) | No      | object            | No         | -                           | -                 |

###### <a name="blueprint_entities_items_anyOf_i0_entity_number"></a>2.10.1.1.1. Property `entity_number`

**Title:** Entity Number

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** A unique ID given to every entity contained within a blueprint. In practice, this value is the 1-indexed position of the entity inside it's parent blueprint's 'entities' list. This is not enforced however, so an entity's number can be specified with any value as long as it's unique inside that particular blueprint. This value is used for resolving associations between different entities, such as wire connections or schedule definitions.

###### <a name="blueprint_entities_items_anyOf_i0_name"></a>2.10.1.1.2. Property `name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the entity. If this name is not recognized by Factorio when importing the entity is omitted with a notification to the console.

###### <a name="blueprint_entities_items_anyOf_i0_position"></a>2.10.1.1.3. Property `position`

**Title:** Position

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | ../common/position.json |

**Description:** The position where the entity is located inside of it's parent blueprint. This position is (almost) always located at the spatial center of the entity. For grid-aligned entities, this position always lies either in the center of a tile or on its transition.

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#blueprint_position-relative-to-grid_x ) | No      | number | No         | -          | -                 |
| - [y](#blueprint_position-relative-to-grid_y ) | No      | number | No         | -          | -                 |

###### <a name="blueprint_position-relative-to-grid_x"></a>2.10.1.1.3.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="blueprint_position-relative-to-grid_y"></a>2.10.1.1.3.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="blueprint_entities_items_anyOf_i0_direction"></a>2.10.1.1.4. Property `direction`

**Title:** Direction

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | No                  |
| **Default**  | `0`                 |

**Description:** The direction of the entity, where 0 corresponds to north and incrementing spins clockwise. Not all entities can manipulate their direction, so setting this attribute may have no effect.

Must be one of:
* 0
* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15

###### <a name="blueprint_entities_items_anyOf_i0_mirror"></a>2.10.1.1.5. Property `mirror`

**Title:** Mirror

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not the input/output fluid boxes are mirrored on this particular entity.

###### <a name="blueprint_entities_items_anyOf_i0_quality"></a>2.10.1.1.6. Property `quality`

**Title:** Quality

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `enum (of string)`       |
| **Required**   | No                       |
| **Default**    | `"normal"`               |
| **Defined in** | common/quality-name.json |

**Description:** The quality of the entity itself.

Must be one of:
* "normal"
* "uncommon"
* "rare"
* "epic"
* "legendary"
* "quality-unknown"

###### <a name="blueprint_entities_items_anyOf_i0_tags"></a>2.10.1.1.7. Property `tags`

**Title:** Tags

|                           |                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                            |
| **Required**              | No                                                                                                                  |
| **Additional properties** | [Each additional property must conform to the schema](#blueprint_entities_items_anyOf_i0_tags_additionalProperties) |

**Description:** Any additional metadata associated with this entity, mostly intended for including mod information inside exported blueprint strings. Each key must be a string, and each value can be either a string, a boolean, a number, or another JSON object.

| Property                                                            | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [](#blueprint_entities_items_anyOf_i0_tags_additionalProperties ) | No      | Combination | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i0_tags_additionalProperties"></a>2.10.1.1.7.1. Property `additionalProperties`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                  |
| ------------------------------------------------------------------------------- |
| [item 0](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1) |
| [item 2](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2) |
| [object](#blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0"></a>2.10.1.1.7.1.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1"></a>2.10.1.1.7.1.2. Property `item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

###### <a name="blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2"></a>2.10.1.1.7.1.3. Property `item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3"></a>2.10.1.1.7.1.4. Property `object`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | object           |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i0_control_behavior"></a>2.10.1.1.8. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                              | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [output_signal](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal ) | No      | Combination | No         | -          | Output Signal     |

###### <a name="blueprint_entities_items_anyOf_i0_control_behavior_output_signal"></a>2.10.1.1.8.1. Property `output_signal`

**Title:** Output Signal

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `combining`                               |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Default**               | `{"name": "signal-A", "type": "virtual"}` |

**Description:** What signal to send the current accumulator charge level value (in the range [0, 100]) if this accumulator is connected to a circuit network.

| One of(Option)                                                                         |
| -------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0"></a>2.10.1.1.8.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1"></a>2.10.1.1.8.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="blueprint_entities_items_anyOf_i1"></a>2.10.1.2. Property `Agricultural Tower`

**Title:** Agricultural Tower

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/agricultural-tower.json |

**Description:** An entity that seeds and harvests plants automatically.

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i1_control_behavior ) | No      | object | No         | -          | -                 |

| All of(Requirement)                                                    |
| ---------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i1_allOf_i0)          |
| [item-requests.json](#blueprint_entities_items_anyOf_i1_allOf_i1)      |
| [circuit-enabled.json](#blueprint_entities_items_anyOf_i1_allOf_i2)    |
| [circuit-condition.json](#blueprint_entities_items_anyOf_i1_allOf_i3)  |
| [logistic-condition.json](#blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i0"></a>2.10.1.2.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i1"></a>2.10.1.2.2. Property `item-requests.json`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | features/item-requests.json |

| Property                                                      | Pattern | Type  | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [items](#blueprint_entities_items_anyOf_i1_allOf_i1_items ) | No      | array | No         | -          | Item Requests     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i1_items"></a>2.10.1.2.2.1. Property `items`

**Title:** Item Requests

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of item requests objects, which contain the item name, it's quality, the amount to request, as well as exactly what inventories to request to and where inside those inventories.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:item-request](#blueprint_entities_items_anyOf_i1_allOf_i1_items_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i1_items_items"></a>2.10.1.2.2.1.1. urn:factorio:item-request

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:item-request |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i2"></a>2.10.1.2.3. Property `circuit-enabled.json`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | features/circuit-enabled.json |

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior"></a>2.10.1.2.3.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                           | Pattern | Type    | Deprecated | Definition | Title/Description                                                                 |
| -------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------------- |
| - [circuit_enabled](#blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled ) | No      | boolean | No         | -          | Whether or not this entity should be controlled by a specified circuit condition. |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled"></a>2.10.1.2.3.1.1. Property `circuit_enabled`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified circuit condition.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3"></a>2.10.1.2.4. Property `circuit-condition.json`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | features/circuit-condition.json |

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior"></a>2.10.1.2.4.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                               | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| ------------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [circuit_condition](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition ) | No      | object | No         | In ../../common/condition.json | Condition         |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition"></a>2.10.1.2.4.1.1. Property `circuit_condition`

**Title:** Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** A conditional statement between either 2 signals or 1 signal and 1 constant value.

| Property                                                                                                         | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ---------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal"></a>2.10.1.2.4.1.1.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>2.10.1.2.4.1.1.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>2.10.1.2.4.1.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator"></a>2.10.1.2.4.1.1.2. Property `comparator`

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

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant"></a>2.10.1.2.4.1.1.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal"></a>2.10.1.2.4.1.1.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>2.10.1.2.4.1.1.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>2.10.1.2.4.1.1.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i4"></a>2.10.1.2.5. Property `logistic-condition.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/logistic-condition.json |

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior"></a>2.10.1.2.5.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                                   | Pattern | Type    | Deprecated | Definition                     | Title/Description            |
| -------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ------------------------------ | ---------------------------- |
| - [connect_to_logistic_network](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network ) | No      | boolean | No         | -                              | Connect to logistic network? |
| - [logistic_condition](#blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition )                   | No      | object  | No         | In ../../common/condition.json | Logistic Condition           |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network"></a>2.10.1.2.5.1.1. Property `connect_to_logistic_network`

**Title:** Connect to logistic network?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified logistic condition.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition"></a>2.10.1.2.5.1.2. Property `logistic_condition`

**Title:** Logistic Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** The logistic condition that the entity should be enabled with, if 'connect_to_logistic_network' is 'true'.

| Property                                                                                                         | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ---------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal"></a>2.10.1.2.5.1.2.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>2.10.1.2.5.1.2.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>2.10.1.2.5.1.2.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator"></a>2.10.1.2.5.1.2.2. Property `comparator`

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

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant"></a>2.10.1.2.5.1.2.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal"></a>2.10.1.2.5.1.2.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>2.10.1.2.5.1.2.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>2.10.1.2.5.1.2.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i1_control_behavior"></a>2.10.1.2.6. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                              | Pattern | Type    | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [read_contents](#blueprint_entities_items_anyOf_i1_control_behavior_read_contents ) | No      | boolean | No         | -          | Read Contents     |

###### <a name="blueprint_entities_items_anyOf_i1_control_behavior_read_contents"></a>2.10.1.2.6.1. Property `read_contents`

**Title:** Read Contents

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should broadcast the contents of its inventory to a connected circuit network.

##### <a name="blueprint_entities_items_anyOf_i2"></a>2.10.1.3. Property `Ammo Turret`

**Title:** Ammo Turret

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | entity/ammo-turret.json |

**Description:** A turret that uses item-based ammunition.

| All of(Requirement)                                                    |
| ---------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i2_allOf_i0)          |
| [item-requests.json](#blueprint_entities_items_anyOf_i2_allOf_i1)      |
| [circuit-enabled.json](#blueprint_entities_items_anyOf_i2_allOf_i2)    |
| [circuit-condition.json](#blueprint_entities_items_anyOf_i2_allOf_i3)  |
| [logistic-condition.json](#blueprint_entities_items_anyOf_i2_allOf_i4) |
| [turret-priorities.json](#blueprint_entities_items_anyOf_i2_allOf_i5)  |
| [read-ammo.json](#blueprint_entities_items_anyOf_i2_allOf_i6)          |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i0"></a>2.10.1.3.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i1"></a>2.10.1.3.2. Property `item-requests.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i1](#blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i2"></a>2.10.1.3.3. Property `circuit-enabled.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i2](#blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i3"></a>2.10.1.3.4. Property `circuit-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i3](#blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i4"></a>2.10.1.3.5. Property `logistic-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i4](#blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5"></a>2.10.1.3.6. Property `turret-priorities.json`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | features/turret-priorities.json |

| Property                                                                                                              | Pattern | Type    | Deprecated | Definition                       | Title/Description                 |
| --------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | -------------------------------- | --------------------------------- |
| - [priority_list](#blueprint_entities_items_anyOf_i2_allOf_i5_priority_list )                                         | No      | array   | No         | -                                | Priority List                     |
| - [ignore_unprioritized](#blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized )                           | No      | boolean | No         | -                                | Ignore Unprioritized              |
| - [set_priority_list](#blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list )                                 | No      | boolean | No         | -                                | Set Priority List                 |
| - [set_ignore_unprioritized](#blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized )                   | No      | boolean | No         | -                                | Set Ignore Unprioritized          |
| - [ignore_unlisted_targets_condition](#blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition ) | No      | object  | No         | In urn:factorio:simple-condition | Ignore Unlisted Targets Condition |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_priority_list"></a>2.10.1.3.6.1. Property `priority_list`

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

| Each item of this array must be                                                           | Description                                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:target-id](#blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items"></a>2.10.1.3.6.1.1. urn:factorio:target-id

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:target-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized"></a>2.10.1.3.6.2. Property `ignore_unprioritized`

**Title:** Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not to completely ignore enemies that do not lie in this turret's target priority lists.

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list"></a>2.10.1.3.6.3. Property `set_priority_list`

**Title:** Set Priority List

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should set its target priorities via connected circuit network signals.

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized"></a>2.10.1.3.6.4. Property `set_ignore_unprioritized`

**Title:** Set Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should have it's ignore unprioritized behavior be set conditionally via 'ignore_unlisted_targets_condition'.

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition"></a>2.10.1.3.6.5. Property `ignore_unlisted_targets_condition`

**Title:** Ignore Unlisted Targets Condition

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | urn:factorio:simple-condition |

**Description:** A condition which must be true in order for non-prioritized targets to be entirely ignored when this turret is targeting. Does nothing unless 'set_ignore_unprioritized' is 'true'.

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i6"></a>2.10.1.3.7. Property `read-ammo.json`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | features/read-ammo.json |

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior"></a>2.10.1.3.7.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                               | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [read_ammo](#blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo ) | No      | boolean | No         | -          | Read Ammo         |

###### <a name="blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo"></a>2.10.1.3.7.1.1. Property `read_ammo`

**Title:** Read Ammo

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not to broadcast the current amount of ammo in the turrets inventory to a connected circuit network.

##### <a name="blueprint_entities_items_anyOf_i3"></a>2.10.1.4. Property `Arithmetic Combinator`

**Title:** Arithmetic Combinator

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `combining`                       |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | entity/arithmetic-combinator.json |

**Description:** A combinator that can perform mathematical operations on one or more values.

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#blueprint_entities_items_anyOf_i3_control_behavior ) | No      | object | No         | -          | -                 |

| All of(Requirement)                                                    |
| ---------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i3_allOf_i0)          |
| [player-description.json](#blueprint_entities_items_anyOf_i3_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i3_allOf_i0"></a>2.10.1.4.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i3_allOf_i1"></a>2.10.1.4.2. Property `player-description.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/player-description.json |

| Property                                                                                | Pattern | Type   | Deprecated | Definition | Title/Description  |
| --------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------ |
| - [player_description](#blueprint_entities_items_anyOf_i3_allOf_i1_player_description ) | No      | string | No         | -          | Player Description |

###### <a name="blueprint_entities_items_anyOf_i3_allOf_i1_player_description"></a>2.10.1.4.2.1. Property `player_description`

**Title:** Player Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** An attached string, intended for entity documentation.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior"></a>2.10.1.4.3. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                              | Pattern | Type   | Deprecated | Definition | Title/Description     |
| ----------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | --------------------- |
| - [arithmetic_conditions](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions ) | No      | object | No         | -          | Arithmetic Conditions |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions"></a>2.10.1.4.3.1. Property `arithmetic_conditions`

**Title:** Arithmetic Conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Container for arithmetic combinator specific parameters.

| Property                                                                                                                      | Pattern | Type             | Deprecated | Definition                              | Title/Description      |
| ----------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | --------------------------------------- | ---------------------- |
| - [first_constant](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant )                 | No      | Combination      | No         | -                                       | First Constant         |
| - [first_signal](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal )                     | No      | Combination      | No         | -                                       | First Signal           |
| - [first_signal_networks](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks )   | No      | object           | No         | In ../common/network-specification.json | First Signal Networks  |
| - [operation](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation )                           | No      | enum (of string) | No         | -                                       | Operation              |
| - [second_constant](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant )               | No      | Combination      | No         | -                                       | Second Constant        |
| - [second_signal](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal )                   | No      | Combination      | No         | -                                       | Second Signal          |
| - [second_signal_networks](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks ) | No      | object           | No         | In ../common/network-specification.json | Second Signal Networks |
| - [output_signal](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal )                   | No      | Combination      | No         | -                                       | Output Signal          |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant"></a>2.10.1.4.3.1.1. Property `first_constant`

**Title:** First Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Constant value that goes in the leftmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- |
| [int32.json](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1)     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0"></a>2.10.1.4.3.1.1.1. Property `int32.json`

|                        |                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| **Type**               | `number`                                                                                            |
| **Required**           | No                                                                                                  |
| **Same definition as** | [constant](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant) |

**Description:** Signed 32-bit integer.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1"></a>2.10.1.4.3.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal"></a>2.10.1.4.3.1.2. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the leftmost slot. Takes precedence over 'first_constant', if both happen to be specified.

| One of(Option)                                                                                              |
| ----------------------------------------------------------------------------------------------------------- |
| [SignalID](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0"></a>2.10.1.4.3.1.2.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1"></a>2.10.1.4.3.1.2.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks"></a>2.10.1.4.3.1.3. Property `first_signal_networks`

**Title:** First Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the leftmost slot should consider for values. Only has an effect if the first slot is occupied by a signal.

| Property                                                                                                          | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red"></a>2.10.1.4.3.1.3.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green"></a>2.10.1.4.3.1.3.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation"></a>2.10.1.4.3.1.4. Property `operation`

**Title:** Operation

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"*"`              |

**Description:** The mathematical operation to perform.

Must be one of:
* "*"
* "/"
* "+"
* "-"
* "%"
* "^"
* "<<"
* ">>"
* "AND"
* "OR"
* "XOR"

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant"></a>2.10.1.4.3.1.5. Property `second_constant`

**Title:** Second Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `0`              |

**Description:** Constant value that goes in the rightmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- |
| [int32.json](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1)     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0"></a>2.10.1.4.3.1.5.1. Property `int32.json`

|                        |                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| **Type**               | `number`                                                                                            |
| **Required**           | No                                                                                                  |
| **Same definition as** | [constant](#blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant) |

**Description:** Signed 32-bit integer.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1"></a>2.10.1.4.3.1.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal"></a>2.10.1.4.3.1.6. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the rightmost slot. Takes precedence over 'second_constant', if both happen to be specified.

| One of(Option)                                                                                               |
| ------------------------------------------------------------------------------------------------------------ |
| [SignalID](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0"></a>2.10.1.4.3.1.6.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1"></a>2.10.1.4.3.1.6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks"></a>2.10.1.4.3.1.7. Property `second_signal_networks`

**Title:** Second Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the rightmost slot should consider for values. Only has an effect if the second slot is occupied by a signal.

| Property                                                                                                          | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red"></a>2.10.1.4.3.1.7.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green"></a>2.10.1.4.3.1.7.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal"></a>2.10.1.4.3.1.8. Property `output_signal`

**Title:** Output Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** What signal (or signals) should this combinator output.

| One of(Option)                                                                                               |
| ------------------------------------------------------------------------------------------------------------ |
| [SignalID](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1)   |

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0"></a>2.10.1.4.3.1.8.1. Property `SignalID`

**Title:** SignalID

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [signal](#blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1"></a>2.10.1.4.3.1.8.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="blueprint_entities_items_anyOf_i4"></a>2.10.1.5. Property `Artillery Turret`

**Title:** Artillery Turret

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `combining`                  |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | entity/artillery-turret.json |

**Description:** A turret that targets enemy structures over long ranges.

| All of(Requirement)                                                          |
| ---------------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i4_allOf_i0)                |
| [item-requests.json](#blueprint_entities_items_anyOf_i4_allOf_i1)            |
| [circuit-enabled.json](#blueprint_entities_items_anyOf_i4_allOf_i2)          |
| [circuit-condition.json](#blueprint_entities_items_anyOf_i4_allOf_i3)        |
| [logistic-condition.json](#blueprint_entities_items_anyOf_i4_allOf_i4)       |
| [read-ammo.json](#blueprint_entities_items_anyOf_i4_allOf_i5)                |
| [artillery-auto-targeting.json](#blueprint_entities_items_anyOf_i4_allOf_i6) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i0"></a>2.10.1.5.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i1"></a>2.10.1.5.2. Property `item-requests.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i1](#blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i2"></a>2.10.1.5.3. Property `circuit-enabled.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i2](#blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i3"></a>2.10.1.5.4. Property `circuit-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i3](#blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i4"></a>2.10.1.5.5. Property `logistic-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i4](#blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i5"></a>2.10.1.5.6. Property `read-ammo.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i2_allOf_i6](#blueprint_entities_items_anyOf_i2_allOf_i6) |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i6"></a>2.10.1.5.7. Property `artillery-auto-targeting.json`

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | features/artillery-auto-targeting.json |

| Property                                                                                            | Pattern | Type    | Deprecated | Definition | Title/Description        |
| --------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------ |
| - [artillery_auto_targeting](#blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting ) | No      | boolean | No         | -          | Artillery Auto Targeting |

###### <a name="blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting"></a>2.10.1.5.7.1. Property `artillery_auto_targeting`

**Title:** Artillery Auto Targeting

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should automatically target enemies in range.

##### <a name="blueprint_entities_items_anyOf_i5"></a>2.10.1.6. Property `Artillery Wagon`

**Title:** Artillery Wagon

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `combining`                 |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | entity/artillery-wagon.json |

**Description:** Rolling stock with an attached artillery turret.

| All of(Requirement)                                                          |
| ---------------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i5_allOf_i0)                |
| [orientation.json](#blueprint_entities_items_anyOf_i5_allOf_i1)              |
| [item-requests.json](#blueprint_entities_items_anyOf_i5_allOf_i2)            |
| [equipment-grid.json](#blueprint_entities_items_anyOf_i5_allOf_i3)           |
| [artillery-auto-targeting.json](#blueprint_entities_items_anyOf_i5_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i0"></a>2.10.1.6.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i1"></a>2.10.1.6.2. Property `orientation.json`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | features/orientation.json |

| Property                                                                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [orientation](#blueprint_entities_items_anyOf_i5_allOf_i1_orientation ) | No      | number | No         | -          | Orientation       |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i1_orientation"></a>2.10.1.6.2.1. Property `orientation`

**Title:** Orientation

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0.0`    |

**Description:** A number in the range [0.0, 1.0] representing the direction this entity is facing. Any value specified out of this range is modulo'd back into this range.

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i2"></a>2.10.1.6.3. Property `item-requests.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i1](#blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3"></a>2.10.1.6.4. Property `equipment-grid.json`

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | features/equipment-grid.json |

| Property                                                                                                      | Pattern | Type    | Deprecated | Definition | Title/Description              |
| ------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------ |
| - [enable_logistics_while_moving](#blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving ) | No      | boolean | No         | -          | Enable Logistics While Moving? |
| - [grid](#blueprint_entities_items_anyOf_i5_allOf_i3_grid )                                                   | No      | array   | No         | -          | Equipment Grid Components      |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving"></a>2.10.1.6.4.1. Property `enable_logistics_while_moving`

**Title:** Enable Logistics While Moving?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should try to fulfill it's logistic requests when it is in motion. Only has an effect if this entity is configured to have an equipment grid and that equipment grid contains personal roboports.

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid"></a>2.10.1.6.4.2. Property `grid`

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

| Each item of this array must be                                               | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [equipment-component](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items) | -           |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid_items"></a>2.10.1.6.4.2.1. equipment-component

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/equipment-component |

| Property                                                                         | Pattern | Type   | Deprecated | Definition               | Title/Description                                                                                         |
| -------------------------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| + [equipment](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment ) | No      | object | No         | In #/$defs/equipment-id  | Equipment ID                                                                                              |
| + [position](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position )   | No      | object | No         | In urn:factorio:position | The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies. |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment"></a>2.10.1.6.4.2.1.1. Property `equipment`

**Title:** Equipment ID

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/equipment-id |

**Description:** A particular type of equipment and its quality.

| Property                                                                               | Pattern | Type   | Deprecated | Definition                   | Title/Description                                                                                             |
| -------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [name](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name )       | No      | string | No         | -                            | The name of a valid piece of equipment (that can fit inside this particular equipment grid).                  |
| - [quality](#blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality ) | No      | object | No         | In urn:factorio:quality-name | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name"></a>2.10.1.6.4.2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid piece of equipment (that can fit inside this particular equipment grid).

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality"></a>2.10.1.6.4.2.1.1.2. Property `quality`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:quality-name |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position"></a>2.10.1.6.4.2.1.2. Property `position`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:position |

**Description:** The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies.

###### <a name="blueprint_entities_items_anyOf_i5_allOf_i4"></a>2.10.1.6.5. Property `artillery-auto-targeting.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i4_allOf_i6](#blueprint_entities_items_anyOf_i4_allOf_i6) |

##### <a name="blueprint_entities_items_anyOf_i6"></a>2.10.1.7. Property `Assembling Machine`

**Title:** Assembling Machine

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/assembling-machine.json |

**Description:** An entity that can convert items and fluids into other items and fluids.

| Property                                                                   | Pattern | Type             | Deprecated | Definition                     | Title/Description |
| -------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ----------------- |
| - [recipe](#blueprint_entities_items_anyOf_i6_recipe )                     | No      | Combination      | No         | -                              | Recipe            |
| - [recipe_quality](#blueprint_entities_items_anyOf_i6_recipe_quality )     | No      | enum (of string) | No         | In ../common/quality-name.json | Recipe Quality    |
| - [control_behavior](#blueprint_entities_items_anyOf_i6_control_behavior ) | No      | object           | No         | -                              | -                 |

| All of(Requirement)                                                    |
| ---------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i6_allOf_i0)          |
| [item-requests.json](#blueprint_entities_items_anyOf_i6_allOf_i1)      |
| [circuit-enabled.json](#blueprint_entities_items_anyOf_i6_allOf_i2)    |
| [circuit-condition.json](#blueprint_entities_items_anyOf_i6_allOf_i3)  |
| [logistic-condition.json](#blueprint_entities_items_anyOf_i6_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i6_allOf_i0"></a>2.10.1.7.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i6_allOf_i1"></a>2.10.1.7.2. Property `item-requests.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i1](#blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i6_allOf_i2"></a>2.10.1.7.3. Property `circuit-enabled.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i2](#blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="blueprint_entities_items_anyOf_i6_allOf_i3"></a>2.10.1.7.4. Property `circuit-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i3](#blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i6_allOf_i4"></a>2.10.1.7.5. Property `logistic-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i4](#blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="blueprint_entities_items_anyOf_i6_recipe"></a>2.10.1.7.6. Property `recipe`

**Title:** Recipe

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The recipe that this entity is configured to perform.

| One of(Option)                                               |
| ------------------------------------------------------------ |
| [item 0](#blueprint_entities_items_anyOf_i6_recipe_oneOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i6_recipe_oneOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i6_recipe_oneOf_i0"></a>2.10.1.7.6.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="blueprint_entities_items_anyOf_i6_recipe_oneOf_i1"></a>2.10.1.7.6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i6_recipe_quality"></a>2.10.1.7.7. Property `recipe_quality`

**Title:** Recipe Quality

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `enum (of string)`          |
| **Required**   | No                          |
| **Default**    | `"normal"`                  |
| **Defined in** | ../common/quality-name.json |

**Description:** The quality of the ingredients/output items that this machine should use.

Must be one of:
* "normal"
* "uncommon"
* "rare"
* "epic"
* "legendary"
* "quality-unknown"

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior"></a>2.10.1.7.8. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [set_recipe](#blueprint_entities_items_anyOf_i6_control_behavior_set_recipe )                         | No      | boolean     | No         | -          | -                 |
| - [read_contents](#blueprint_entities_items_anyOf_i6_control_behavior_read_contents )                   | No      | boolean     | No         | -          | -                 |
| - [include_in_crafting](#blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting )       | No      | boolean     | No         | -          | -                 |
| - [read_recipe_finished](#blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished )     | No      | boolean     | No         | -          | -                 |
| - [recipe_finished_signal](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal ) | No      | Combination | No         | -          | -                 |
| - [read_working](#blueprint_entities_items_anyOf_i6_control_behavior_read_working )                     | No      | boolean     | No         | -          | -                 |
| - [working_signal](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal )                 | No      | Combination | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_set_recipe"></a>2.10.1.7.8.1. Property `set_recipe`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_read_contents"></a>2.10.1.7.8.2. Property `read_contents`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting"></a>2.10.1.7.8.3. Property `include_in_crafting`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"true"`  |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished"></a>2.10.1.7.8.4. Property `read_recipe_finished`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal"></a>2.10.1.7.8.5. Property `recipe_finished_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

| Any of(Option)                                                                                                |
| ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:signal-id](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1)                 |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0"></a>2.10.1.7.8.5.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1"></a>2.10.1.7.8.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_read_working"></a>2.10.1.7.8.6. Property `read_working`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_working_signal"></a>2.10.1.7.8.7. Property `working_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                                        |
| ----------------------------------------------------------------------------------------------------- |
| [urn:factorio:signal-id](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0) |
| [item 1](#blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1)                 |

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0"></a>2.10.1.7.8.7.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1"></a>2.10.1.7.8.7.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

##### <a name="blueprint_entities_items_anyOf_i7"></a>2.10.1.8. Property `Asteroid Collector`

**Title:** Asteroid Collector

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/asteroid-collector.json |

**Description:** An entity uses arms to grab asteroid chunks from space.

| Property                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description       |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------------- |
| - [result_inventory](#blueprint_entities_items_anyOf_i7_result_inventory ) | No      | object | No         | -          | Result Inventory Object |
| - [chunk-filter](#blueprint_entities_items_anyOf_i7_chunk-filter )         | No      | array  | No         | -          | -                       |
| - [control_behavior](#blueprint_entities_items_anyOf_i7_control_behavior ) | No      | object | No         | -          | -                       |

| All of(Requirement)                                                   |
| --------------------------------------------------------------------- |
| [Generic Entity](#blueprint_entities_items_anyOf_i7_allOf_i0)         |
| [item-requests.json](#blueprint_entities_items_anyOf_i7_allOf_i1)     |
| [circuit-enabled.json](#blueprint_entities_items_anyOf_i7_allOf_i2)   |
| [circuit-condition.json](#blueprint_entities_items_anyOf_i7_allOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i7_allOf_i0"></a>2.10.1.8.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                      |
| ------------------------- | ---------------------------------------------------- |
| **Type**                  | `object`                                             |
| **Required**              | No                                                   |
| **Additional properties** | Any type allowed                                     |
| **Same definition as**    | [Generic Entity](#blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="blueprint_entities_items_anyOf_i7_allOf_i1"></a>2.10.1.8.2. Property `item-requests.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i1](#blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="blueprint_entities_items_anyOf_i7_allOf_i2"></a>2.10.1.8.3. Property `circuit-enabled.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i2](#blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="blueprint_entities_items_anyOf_i7_allOf_i3"></a>2.10.1.8.4. Property `circuit-condition.json`

|                           |                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                  |
| **Required**              | No                                                                                        |
| **Additional properties** | Any type allowed                                                                          |
| **Same definition as**    | [blueprint_entities_items_anyOf_i1_allOf_i3](#blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="blueprint_entities_items_anyOf_i7_result_inventory"></a>2.10.1.8.5. Property `result_inventory`

**Title:** Result Inventory Object

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Inventory object which holds the limiting bar for this entity.

| Property                                                          | Pattern | Type   | Deprecated | Definition                         | Title/Description |
| ----------------------------------------------------------------- | ------- | ------ | ---------- | ---------------------------------- | ----------------- |
| - [bar](#blueprint_entities_items_anyOf_i7_result_inventory_bar ) | No      | number | No         | Same as [uint16](#index_oneOf_i0 ) | uint16            |

###### <a name="blueprint_entities_items_anyOf_i7_result_inventory_bar"></a>2.10.1.8.5.1. Property `bar`

**Title:** uint16

|                        |                           |
| ---------------------- | ------------------------- |
| **Type**               | `number`                  |
| **Required**           | No                        |
| **Same definition as** | [uint16](#index_oneOf_i0) |

**Description:** An unsigned 16-bit integer.

###### <a name="blueprint_entities_items_anyOf_i7_chunk-filter"></a>2.10.1.8.6. Property `chunk-filter`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                            | Description |
| -------------------------------------------------------------------------- | ----------- |
| [asteroid-chunk-id](#blueprint_entities_items_anyOf_i7_chunk-filter_items) | -           |

###### <a name="blueprint_entities_items_anyOf_i7_chunk-filter_items"></a>2.10.1.8.6.1. asteroid-chunk-id

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/asteroid-chunk-id |

| Property                                                                | Pattern | Type   | Deprecated | Definition           | Title/Description                                                                                             |
| ----------------------------------------------------------------------- | ------- | ------ | ---------- | -------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [index](#blueprint_entities_items_anyOf_i7_chunk-filter_items_index ) | No      | object | No         | In ../../uint32.json | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |
| - [name](#blueprint_entities_items_anyOf_i7_chunk-filter_items_name )   | No      | string | No         | -                    | The name of a valid Factorio asteroid chunk.                                                                  |

###### <a name="blueprint_entities_items_anyOf_i7_chunk-filter_items_index"></a>2.10.1.8.6.1.1. Property `index`

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Defined in**            | ../../uint32.json |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="blueprint_entities_items_anyOf_i7_chunk-filter_items_name"></a>2.10.1.8.6.1.2. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid Factorio asteroid chunk.

###### <a name="blueprint_entities_items_anyOf_i7_control_behavior"></a>2.10.1.8.7. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                              | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [circuit_set_filters](#blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters )     | No      | boolean | No         | -          | -                 |
| - [circuit_read_contents](#blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents ) | No      | boolean | No         | -          | -                 |
| - [include_hands](#blueprint_entities_items_anyOf_i7_control_behavior_include_hands )                 | No      | boolean | No         | -          | -                 |

###### <a name="blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters"></a>2.10.1.8.7.1. Property `circuit_set_filters`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents"></a>2.10.1.8.7.2. Property `circuit_read_contents`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

###### <a name="blueprint_entities_items_anyOf_i7_control_behavior_include_hands"></a>2.10.1.8.7.3. Property `include_hands`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

### <a name="blueprint_tiles"></a>2.11. Property `tiles`

**Title:** Tiles

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |
| **Default**  | `[]`    |

**Description:** The list of all tiles stored inside this blueprint.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description                                                                                                   |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:tile](#blueprint_tiles_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

#### <a name="blueprint_tiles_items"></a>2.11.1. urn:factorio:tile

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Defined in**            | urn:factorio:tile |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

### <a name="blueprint_wires"></a>2.12. Property `wires`

**Title:** Wires

|              |                  |
| ------------ | ---------------- |
| **Type**     | `array of array` |
| **Required** | No               |
| **Default**  | `[]`             |

**Description:** The list of all wire connections stored inside this blueprint, including both power and circuit wires.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be       | Description |
| ------------------------------------- | ----------- |
| [wires items](#blueprint_wires_items) | -           |

#### <a name="blueprint_wires_items"></a>2.12.1. wires items

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                       | Description                                                                                       |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [uint64](#blueprint_wires_items_items_i0)             | 'entity_number' of the first entity being connected.                                              |
| [wires items item 1](#blueprint_wires_items_items_i1) | What kind of connection the wire has to entity1. See 'wire_connection_types' in Factorio defines. |
| [uint64](#blueprint_wires_items_items_i2)             | 'entity_number' of the second entity being connected.                                             |
| [wires items item 3](#blueprint_wires_items_items_i3) | What kind of connection the wire has to entity2. See 'wire_connection_types' in Factorio defines. |

##### <a name="autogenerated_heading_2"></a>2.12.1.1. uint64

**Title:** uint64

|                        |                               |
| ---------------------- | ----------------------------- |
| **Type**               | `number`                      |
| **Required**           | No                            |
| **Same definition as** | [version](#blueprint_version) |

**Description:** 'entity_number' of the first entity being connected.

##### <a name="autogenerated_heading_3"></a>2.12.1.2. wires items item 1

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | No                  |

**Description:** What kind of connection the wire has to entity1. See 'wire_connection_types' in Factorio defines.

Must be one of:
* 1
* 2
* 3
* 4
* 5
* 6

##### <a name="autogenerated_heading_4"></a>2.12.1.3. uint64

**Title:** uint64

|                        |                               |
| ---------------------- | ----------------------------- |
| **Type**               | `number`                      |
| **Required**           | No                            |
| **Same definition as** | [version](#blueprint_version) |

**Description:** 'entity_number' of the second entity being connected.

##### <a name="autogenerated_heading_5"></a>2.12.1.4. wires items item 3

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | No                  |

**Description:** What kind of connection the wire has to entity2. See 'wire_connection_types' in Factorio defines.

Must be one of:
* 1
* 2
* 3
* 4
* 5
* 6

### <a name="blueprint_schedules"></a>2.13. Property `schedules`

**Title:** Wires

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |
| **Default**  | `[]`    |

**Description:** The list of all schedules in this blueprint, including both train and space platform schedules.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                     | Description                                                                                                   |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:schedule](#blueprint_schedules_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

#### <a name="blueprint_schedules_items"></a>2.13.1. urn:factorio:schedule

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:schedule |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

### <a name="blueprint_stock_connections"></a>2.14. Property `stock_connections`

**Title:** Stock Connections

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |
| **Default**  | `[]`    |

**Description:** A list of all connections between train cars. In Factorio 1.0, train car connections were automatically made if two rolling stock entities were in the correct positions - but in this structure their connections are now made explicit.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                     | Description                                                                                                   |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:stock-connection](#blueprint_stock_connections_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

#### <a name="blueprint_stock_connections_items"></a>2.14.1. urn:factorio:stock-connection

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | urn:factorio:stock-connection |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

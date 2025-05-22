# Blueprintable

- [1. Property `Blueprint`](#oneOf_i0)
  - [1.1. Property `index`](#oneOf_i0_index)
    - [1.1.1. Property `uint16`](#oneOf_i0_index_oneOf_i0)
    - [1.1.2. Property `Null`](#oneOf_i0_index_oneOf_i1)
  - [1.2. Property `blueprint`](#oneOf_i0_blueprint)
    - [1.2.1. Property `item`](#oneOf_i0_blueprint_item)
    - [1.2.2. Property `label`](#oneOf_i0_blueprint_label)
    - [1.2.3. Property `label_color`](#oneOf_i0_blueprint_label_color)
      - [1.2.3.1. Property `r`](#oneOf_i0_blueprint_label_color_r)
      - [1.2.3.2. Property `g`](#oneOf_i0_blueprint_label_color_g)
      - [1.2.3.3. Property `b`](#oneOf_i0_blueprint_label_color_b)
      - [1.2.3.4. Property `a`](#oneOf_i0_blueprint_label_color_a)
        - [1.2.3.4.1. Property `color-component`](#oneOf_i0_blueprint_label_color_a_oneOf_i0)
        - [1.2.3.4.2. Property `item 1`](#oneOf_i0_blueprint_label_color_a_oneOf_i1)
    - [1.2.4. Property `description`](#oneOf_i0_blueprint_description)
    - [1.2.5. Property `icons`](#oneOf_i0_blueprint_icons)
      - [1.2.5.1. icon.json](#oneOf_i0_blueprint_icons_items)
        - [1.2.5.1.1. Property `index`](#oneOf_i0_blueprint_icons_items_index)
        - [1.2.5.1.2. Property `signal`](#oneOf_i0_blueprint_icons_items_signal)
          - [1.2.5.1.2.1. Property `name`](#oneOf_i0_blueprint_icons_items_signal_name)
          - [1.2.5.1.2.2. Property `type`](#oneOf_i0_blueprint_icons_items_signal_type)
          - [1.2.5.1.2.3. Property `quality`](#oneOf_i0_blueprint_icons_items_signal_quality)
    - [1.2.6. Property `version`](#oneOf_i0_blueprint_version)
    - [1.2.7. Property `snap-to-grid`](#oneOf_i0_blueprint_snap-to-grid)
    - [1.2.8. Property `absolute-snapping`](#oneOf_i0_blueprint_absolute-snapping)
    - [1.2.9. Property `position-relative-to-grid`](#oneOf_i0_blueprint_position-relative-to-grid)
      - [1.2.9.1. Property `x`](#oneOf_i0_blueprint_position-relative-to-grid_x)
      - [1.2.9.2. Property `y`](#oneOf_i0_blueprint_position-relative-to-grid_y)
    - [1.2.10. Property `entities`](#oneOf_i0_blueprint_entities)
      - [1.2.10.1. entities items](#oneOf_i0_blueprint_entities_items)
        - [1.2.10.1.1. Property `Accumulator`](#oneOf_i0_blueprint_entities_items_anyOf_i0)
          - [1.2.10.1.1.1. Property `entity_number`](#oneOf_i0_blueprint_entities_items_anyOf_i0_entity_number)
          - [1.2.10.1.1.2. Property `name`](#oneOf_i0_blueprint_entities_items_anyOf_i0_name)
          - [1.2.10.1.1.3. Property `position`](#oneOf_i0_blueprint_entities_items_anyOf_i0_position)
            - [1.2.10.1.1.3.1. Property `x`](#oneOf_i0_blueprint_position-relative-to-grid_x)
            - [1.2.10.1.1.3.2. Property `y`](#oneOf_i0_blueprint_position-relative-to-grid_y)
          - [1.2.10.1.1.4. Property `direction`](#oneOf_i0_blueprint_entities_items_anyOf_i0_direction)
          - [1.2.10.1.1.5. Property `mirror`](#oneOf_i0_blueprint_entities_items_anyOf_i0_mirror)
          - [1.2.10.1.1.6. Property `quality`](#oneOf_i0_blueprint_entities_items_anyOf_i0_quality)
          - [1.2.10.1.1.7. Property `tags`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags)
            - [1.2.10.1.1.7.1. Property `additionalProperties`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties)
              - [1.2.10.1.1.7.1.1. Property `item 0`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0)
              - [1.2.10.1.1.7.1.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1)
              - [1.2.10.1.1.7.1.3. Property `item 2`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2)
              - [1.2.10.1.1.7.1.4. Property `object`](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3)
          - [1.2.10.1.1.8. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior)
            - [1.2.10.1.1.8.1. Property `output_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal)
              - [1.2.10.1.1.8.1.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0)
              - [1.2.10.1.1.8.1.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1)
        - [1.2.10.1.2. Property `Agricultural Tower`](#oneOf_i0_blueprint_entities_items_anyOf_i1)
          - [1.2.10.1.2.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i0)
          - [1.2.10.1.2.2. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1)
            - [1.2.10.1.2.2.1. Property `items`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items)
              - [1.2.10.1.2.2.1.1. urn:factorio:item-request](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items_items)
          - [1.2.10.1.2.3. Property `circuit-enabled.json`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2)
            - [1.2.10.1.2.3.1. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior)
              - [1.2.10.1.2.3.1.1. Property `circuit_enabled`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled)
          - [1.2.10.1.2.4. Property `circuit-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3)
            - [1.2.10.1.2.4.1. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior)
              - [1.2.10.1.2.4.1.1. Property `circuit_condition`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition)
                - [1.2.10.1.2.4.1.1.1. Property `first_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal)
                  - [1.2.10.1.2.4.1.1.1.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
                  - [1.2.10.1.2.4.1.1.1.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
                - [1.2.10.1.2.4.1.1.2. Property `comparator`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator)
                - [1.2.10.1.2.4.1.1.3. Property `constant`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant)
                - [1.2.10.1.2.4.1.1.4. Property `second_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal)
                  - [1.2.10.1.2.4.1.1.4.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
                  - [1.2.10.1.2.4.1.1.4.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
          - [1.2.10.1.2.5. Property `logistic-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4)
            - [1.2.10.1.2.5.1. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior)
              - [1.2.10.1.2.5.1.1. Property `connect_to_logistic_network`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network)
              - [1.2.10.1.2.5.1.2. Property `logistic_condition`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition)
                - [1.2.10.1.2.5.1.2.1. Property `first_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal)
                  - [1.2.10.1.2.5.1.2.1.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0)
                  - [1.2.10.1.2.5.1.2.1.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)
                - [1.2.10.1.2.5.1.2.2. Property `comparator`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator)
                - [1.2.10.1.2.5.1.2.3. Property `constant`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant)
                - [1.2.10.1.2.5.1.2.4. Property `second_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal)
                  - [1.2.10.1.2.5.1.2.4.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0)
                  - [1.2.10.1.2.5.1.2.4.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)
          - [1.2.10.1.2.6. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior)
            - [1.2.10.1.2.6.1. Property `read_contents`](#oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior_read_contents)
        - [1.2.10.1.3. Property `Ammo Turret`](#oneOf_i0_blueprint_entities_items_anyOf_i2)
          - [1.2.10.1.3.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i0)
          - [1.2.10.1.3.2. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i1)
          - [1.2.10.1.3.3. Property `circuit-enabled.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i2)
          - [1.2.10.1.3.4. Property `circuit-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i3)
          - [1.2.10.1.3.5. Property `logistic-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i4)
          - [1.2.10.1.3.6. Property `turret-priorities.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5)
            - [1.2.10.1.3.6.1. Property `priority_list`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list)
              - [1.2.10.1.3.6.1.1. urn:factorio:target-id](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items)
            - [1.2.10.1.3.6.2. Property `ignore_unprioritized`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized)
            - [1.2.10.1.3.6.3. Property `set_priority_list`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list)
            - [1.2.10.1.3.6.4. Property `set_ignore_unprioritized`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized)
            - [1.2.10.1.3.6.5. Property `ignore_unlisted_targets_condition`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition)
          - [1.2.10.1.3.7. Property `read-ammo.json`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6)
            - [1.2.10.1.3.7.1. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior)
              - [1.2.10.1.3.7.1.1. Property `read_ammo`](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo)
        - [1.2.10.1.4. Property `Arithmetic Combinator`](#oneOf_i0_blueprint_entities_items_anyOf_i3)
          - [1.2.10.1.4.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i0)
          - [1.2.10.1.4.2. Property `player-description.json`](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1)
            - [1.2.10.1.4.2.1. Property `player_description`](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1_player_description)
          - [1.2.10.1.4.3. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior)
            - [1.2.10.1.4.3.1. Property `arithmetic_conditions`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions)
              - [1.2.10.1.4.3.1.1. Property `first_constant`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant)
                - [1.2.10.1.4.3.1.1.1. Property `int32.json`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0)
                - [1.2.10.1.4.3.1.1.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1)
              - [1.2.10.1.4.3.1.2. Property `first_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal)
                - [1.2.10.1.4.3.1.2.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0)
                - [1.2.10.1.4.3.1.2.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1)
              - [1.2.10.1.4.3.1.3. Property `first_signal_networks`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks)
                - [1.2.10.1.4.3.1.3.1. Property `red`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red)
                - [1.2.10.1.4.3.1.3.2. Property `green`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green)
              - [1.2.10.1.4.3.1.4. Property `operation`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation)
              - [1.2.10.1.4.3.1.5. Property `second_constant`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant)
                - [1.2.10.1.4.3.1.5.1. Property `int32.json`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0)
                - [1.2.10.1.4.3.1.5.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1)
              - [1.2.10.1.4.3.1.6. Property `second_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal)
                - [1.2.10.1.4.3.1.6.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0)
                - [1.2.10.1.4.3.1.6.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1)
              - [1.2.10.1.4.3.1.7. Property `second_signal_networks`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks)
                - [1.2.10.1.4.3.1.7.1. Property `red`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red)
                - [1.2.10.1.4.3.1.7.2. Property `green`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green)
              - [1.2.10.1.4.3.1.8. Property `output_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal)
                - [1.2.10.1.4.3.1.8.1. Property `SignalID`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0)
                - [1.2.10.1.4.3.1.8.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1)
        - [1.2.10.1.5. Property `Artillery Turret`](#oneOf_i0_blueprint_entities_items_anyOf_i4)
          - [1.2.10.1.5.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i0)
          - [1.2.10.1.5.2. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i1)
          - [1.2.10.1.5.3. Property `circuit-enabled.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i2)
          - [1.2.10.1.5.4. Property `circuit-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i3)
          - [1.2.10.1.5.5. Property `logistic-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i4)
          - [1.2.10.1.5.6. Property `read-ammo.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i5)
          - [1.2.10.1.5.7. Property `artillery-auto-targeting.json`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6)
            - [1.2.10.1.5.7.1. Property `artillery_auto_targeting`](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting)
        - [1.2.10.1.6. Property `Artillery Wagon`](#oneOf_i0_blueprint_entities_items_anyOf_i5)
          - [1.2.10.1.6.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i0)
          - [1.2.10.1.6.2. Property `orientation.json`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1)
            - [1.2.10.1.6.2.1. Property `orientation`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1_orientation)
          - [1.2.10.1.6.3. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i2)
          - [1.2.10.1.6.4. Property `equipment-grid.json`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3)
            - [1.2.10.1.6.4.1. Property `enable_logistics_while_moving`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving)
            - [1.2.10.1.6.4.2. Property `grid`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid)
              - [1.2.10.1.6.4.2.1. equipment-component](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items)
                - [1.2.10.1.6.4.2.1.1. Property `equipment`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment)
                  - [1.2.10.1.6.4.2.1.1.1. Property `name`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name)
                  - [1.2.10.1.6.4.2.1.1.2. Property `quality`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality)
                - [1.2.10.1.6.4.2.1.2. Property `position`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position)
          - [1.2.10.1.6.5. Property `artillery-auto-targeting.json`](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i4)
        - [1.2.10.1.7. Property `Assembling Machine`](#oneOf_i0_blueprint_entities_items_anyOf_i6)
          - [1.2.10.1.7.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i0)
          - [1.2.10.1.7.2. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i1)
          - [1.2.10.1.7.3. Property `circuit-enabled.json`](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i2)
          - [1.2.10.1.7.4. Property `circuit-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i3)
          - [1.2.10.1.7.5. Property `logistic-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i4)
          - [1.2.10.1.7.6. Property `recipe`](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe)
            - [1.2.10.1.7.6.1. Property `item 0`](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i0)
            - [1.2.10.1.7.6.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i1)
          - [1.2.10.1.7.7. Property `recipe_quality`](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_quality)
          - [1.2.10.1.7.8. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior)
            - [1.2.10.1.7.8.1. Property `set_recipe`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_set_recipe)
            - [1.2.10.1.7.8.2. Property `read_contents`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_contents)
            - [1.2.10.1.7.8.3. Property `include_in_crafting`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting)
            - [1.2.10.1.7.8.4. Property `read_recipe_finished`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished)
            - [1.2.10.1.7.8.5. Property `recipe_finished_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal)
              - [1.2.10.1.7.8.5.1. Property `urn:factorio:signal-id`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0)
              - [1.2.10.1.7.8.5.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1)
            - [1.2.10.1.7.8.6. Property `read_working`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_working)
            - [1.2.10.1.7.8.7. Property `working_signal`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal)
              - [1.2.10.1.7.8.7.1. Property `urn:factorio:signal-id`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0)
              - [1.2.10.1.7.8.7.2. Property `item 1`](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1)
        - [1.2.10.1.8. Property `Asteroid Collector`](#oneOf_i0_blueprint_entities_items_anyOf_i7)
          - [1.2.10.1.8.1. Property `Generic Entity`](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i0)
          - [1.2.10.1.8.2. Property `item-requests.json`](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i1)
          - [1.2.10.1.8.3. Property `circuit-enabled.json`](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i2)
          - [1.2.10.1.8.4. Property `circuit-condition.json`](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i3)
          - [1.2.10.1.8.5. Property `result_inventory`](#oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory)
            - [1.2.10.1.8.5.1. Property `bar`](#oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory_bar)
          - [1.2.10.1.8.6. Property `chunk-filter`](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter)
            - [1.2.10.1.8.6.1. asteroid-chunk-id](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items)
              - [1.2.10.1.8.6.1.1. Property `index`](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_index)
              - [1.2.10.1.8.6.1.2. Property `name`](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_name)
          - [1.2.10.1.8.7. Property `control_behavior`](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior)
            - [1.2.10.1.8.7.1. Property `circuit_set_filters`](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters)
            - [1.2.10.1.8.7.2. Property `circuit_read_contents`](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents)
            - [1.2.10.1.8.7.3. Property `include_hands`](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_include_hands)
    - [1.2.11. Property `tiles`](#oneOf_i0_blueprint_tiles)
      - [1.2.11.1. urn:factorio:tile](#oneOf_i0_blueprint_tiles_items)
    - [1.2.12. Property `wires`](#oneOf_i0_blueprint_wires)
      - [1.2.12.1. wires items](#oneOf_i0_blueprint_wires_items)
        - [1.2.12.1.1. uint64](#autogenerated_heading_2)
        - [1.2.12.1.2. wires items item 1](#autogenerated_heading_3)
        - [1.2.12.1.3. uint64](#autogenerated_heading_4)
        - [1.2.12.1.4. wires items item 3](#autogenerated_heading_5)
    - [1.2.13. Property `schedules`](#oneOf_i0_blueprint_schedules)
      - [1.2.13.1. urn:factorio:schedule](#oneOf_i0_blueprint_schedules_items)
    - [1.2.14. Property `stock_connections`](#oneOf_i0_blueprint_stock_connections)
      - [1.2.14.1. urn:factorio:stock-connection](#oneOf_i0_blueprint_stock_connections_items)
- [2. Property `Deconstruction Planner`](#oneOf_i1)
- [3. Property `Upgrade Planner`](#oneOf_i2)
- [4. Property `Blueprint Book`](#oneOf_i3)

**Title:** Blueprintable

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A schema that validates any encodable/decodable blueprint object, including blueprints, deconstruction planners, upgrade planners, and blueprint books.

| One of(Option)                      |
| ----------------------------------- |
| [Blueprint](#oneOf_i0)              |
| [Deconstruction Planner](#oneOf_i1) |
| [Upgrade Planner](#oneOf_i2)        |
| [Blueprint Book](#oneOf_i3)         |

## <a name="oneOf_i0"></a>1. Property `Blueprint`

**Title:** Blueprint

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | blueprint.json   |

**Description:** A regular blueprint, which can contain entities, tiles, schedules, wire connections, stock connections, in addition to additional metadata.

| Property                            | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [index](#oneOf_i0_index )         | No      | Combination | No         | -          | Index             |
| - [blueprint](#oneOf_i0_blueprint ) | No      | object      | No         | -          | Blueprint Object  |

### <a name="oneOf_i0_index"></a>1.1. Property `index`

**Title:** Index

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The unique index of the blueprint, if it lies inside of a parent blueprint book. If not inside of a blueprint book, this key has no effect.

| One of(Option)                     |
| ---------------------------------- |
| [uint16](#oneOf_i0_index_oneOf_i0) |
| [Null](#oneOf_i0_index_oneOf_i1)   |

#### <a name="oneOf_i0_index_oneOf_i0"></a>1.1.1. Property `uint16`

**Title:** uint16

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | No                    |
| **Defined in** | ../common/uint16.json |

**Description:** An unsigned 16-bit integer.

#### <a name="oneOf_i0_index_oneOf_i1"></a>1.1.2. Property `Null`

**Title:** Null

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="oneOf_i0_blueprint"></a>1.2. Property `blueprint`

**Title:** Blueprint Object

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Main object of the blueprint, which actually contains the majority of its keys.

| Property                                                                      | Pattern | Type           | Deprecated | Definition                 | Title/Description         |
| ----------------------------------------------------------------------------- | ------- | -------------- | ---------- | -------------------------- | ------------------------- |
| + [item](#oneOf_i0_blueprint_item )                                           | No      | const          | No         | -                          | Item                      |
| - [label](#oneOf_i0_blueprint_label )                                         | No      | string         | No         | -                          | Label                     |
| - [label_color](#oneOf_i0_blueprint_label_color )                             | No      | object         | No         | In ../common/color.json    | Label Color               |
| - [description](#oneOf_i0_blueprint_description )                             | No      | string         | No         | -                          | Description               |
| - [icons](#oneOf_i0_blueprint_icons )                                         | No      | array          | No         | -                          | Icons                     |
| + [version](#oneOf_i0_blueprint_version )                                     | No      | number         | No         | In ../common/uint64.json   | Version                   |
| - [snap-to-grid](#oneOf_i0_blueprint_snap-to-grid )                           | No      | object         | No         | In common/position.json    | Snap to Grid              |
| - [absolute-snapping](#oneOf_i0_blueprint_absolute-snapping )                 | No      | boolean        | No         | -                          | Absolute Snapping         |
| - [position-relative-to-grid](#oneOf_i0_blueprint_position-relative-to-grid ) | No      | object         | No         | In ../common/position.json | Position Relative to Grid |
| - [entities](#oneOf_i0_blueprint_entities )                                   | No      | array          | No         | -                          | Entities                  |
| - [tiles](#oneOf_i0_blueprint_tiles )                                         | No      | array          | No         | -                          | Tiles                     |
| - [wires](#oneOf_i0_blueprint_wires )                                         | No      | array of array | No         | -                          | Wires                     |
| - [schedules](#oneOf_i0_blueprint_schedules )                                 | No      | array          | No         | -                          | Wires                     |
| - [stock_connections](#oneOf_i0_blueprint_stock_connections )                 | No      | array          | No         | -                          | Stock Connections         |

#### <a name="oneOf_i0_blueprint_item"></a>1.2.1. Property `item`

**Title:** Item

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** The name of the item associated with this blueprintable.

Specific value: `"blueprint"`

#### <a name="oneOf_i0_blueprint_label"></a>1.2.2. Property `label`

**Title:** Label

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** The player-given title of this blueprint. Can be specified with rich text colors and icons. If omitted or specified as an empty string, then the blueprint is given the default name 'Blueprint'.

#### <a name="oneOf_i0_blueprint_label_color"></a>1.2.3. Property `label_color`

**Title:** Label Color

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | ../common/color.json |

**Description:** The color of the label. If omitted, this color defaults to a special hybrid color, where it is white in your inventory and black when being placed.

| Property                                  | Pattern | Type        | Deprecated | Definition                 | Title/Description |
| ----------------------------------------- | ------- | ----------- | ---------- | -------------------------- | ----------------- |
| + [r](#oneOf_i0_blueprint_label_color_r ) | No      | number      | No         | In #/$defs/color-component | Red               |
| + [g](#oneOf_i0_blueprint_label_color_g ) | No      | number      | No         | In #/$defs/color-component | Green             |
| + [b](#oneOf_i0_blueprint_label_color_b ) | No      | number      | No         | In #/$defs/color-component | Blue              |
| - [a](#oneOf_i0_blueprint_label_color_a ) | No      | Combination | No         | -                          | Alpha             |

##### <a name="oneOf_i0_blueprint_label_color_r"></a>1.2.3.1. Property `r`

**Title:** Red

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

##### <a name="oneOf_i0_blueprint_label_color_g"></a>1.2.3.2. Property `g`

**Title:** Green

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

##### <a name="oneOf_i0_blueprint_label_color_b"></a>1.2.3.3. Property `b`

**Title:** Blue

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | Yes                     |
| **Defined in** | #/$defs/color-component |

##### <a name="oneOf_i0_blueprint_label_color_a"></a>1.2.3.4. Property `a`

**Title:** Alpha

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| One of(Option)                                                |
| ------------------------------------------------------------- |
| [color-component](#oneOf_i0_blueprint_label_color_a_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_label_color_a_oneOf_i1)          |

###### <a name="oneOf_i0_blueprint_label_color_a_oneOf_i0"></a>1.2.3.4.1. Property `color-component`

|                        |                                        |
| ---------------------- | -------------------------------------- |
| **Type**               | `number`                               |
| **Required**           | No                                     |
| **Same definition as** | [r](#oneOf_i0_blueprint_label_color_r) |

###### <a name="oneOf_i0_blueprint_label_color_a_oneOf_i1"></a>1.2.3.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

#### <a name="oneOf_i0_blueprint_description"></a>1.2.4. Property `description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** The player-given description of this blueprint. Can be specified with rich text colors and icons.

#### <a name="oneOf_i0_blueprint_icons"></a>1.2.5. Property `icons`

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

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [icon.json](#oneOf_i0_blueprint_icons_items) | -           |

##### <a name="oneOf_i0_blueprint_icons_items"></a>1.2.5.1. icon.json

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | common/icon.json |

| Property                                            | Pattern | Type   | Deprecated | Definition                 | Title/Description |
| --------------------------------------------------- | ------- | ------ | ---------- | -------------------------- | ----------------- |
| - [index](#oneOf_i0_blueprint_icons_items_index )   | No      | number | No         | In ../../common/uint8.json | uint8             |
| - [signal](#oneOf_i0_blueprint_icons_items_signal ) | No      | object | No         | In signal-id.json          | SignalID          |

###### <a name="oneOf_i0_blueprint_icons_items_index"></a>1.2.5.1.1. Property `index`

**Title:** uint8

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Defined in** | ../../common/uint8.json |

**Description:** An unsigned 8-bit integer.

###### <a name="oneOf_i0_blueprint_icons_items_signal"></a>1.2.5.1.2. Property `signal`

**Title:** SignalID

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | signal-id.json   |

**Description:** An object which represents a valid signal.

| Property                                                     | Pattern | Type             | Deprecated | Definition           | Title/Description                                                                                 |
| ------------------------------------------------------------ | ------- | ---------------- | ---------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| - [name](#oneOf_i0_blueprint_icons_items_signal_name )       | No      | string           | No         | -                    | -                                                                                                 |
| - [type](#oneOf_i0_blueprint_icons_items_signal_type )       | No      | enum (of string) | No         | -                    | The category of the signal. There can be multiple signals with the same name but differing types. |
| - [quality](#oneOf_i0_blueprint_icons_items_signal_quality ) | No      | enum (of string) | No         | In quality-name.json | Quality                                                                                           |

###### <a name="oneOf_i0_blueprint_icons_items_signal_name"></a>1.2.5.1.2.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_icons_items_signal_type"></a>1.2.5.1.2.2. Property `type`

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

###### <a name="oneOf_i0_blueprint_icons_items_signal_quality"></a>1.2.5.1.2.3. Property `quality`

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

#### <a name="oneOf_i0_blueprint_version"></a>1.2.6. Property `version`

**Title:** Version

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** The version of the game associated with this blueprint string. Encoded as four bytes, where each byte corresponds to a semantic version number.

#### <a name="oneOf_i0_blueprint_snap-to-grid"></a>1.2.7. Property `snap-to-grid`

**Title:** Snap to Grid

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | common/position.json |

**Description:** A snapping grid with a width ('x') and height ('y') to apply when placing this blueprint. If this field is omitted, this means the blueprint has no snapping grid.

#### <a name="oneOf_i0_blueprint_absolute-snapping"></a>1.2.8. Property `absolute-snapping`

**Title:** Absolute Snapping

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this blueprint will use absolute coordinates when snapping to it's defined snapping grid. If no snapping grid is defined, this key does nothing.

#### <a name="oneOf_i0_blueprint_position-relative-to-grid"></a>1.2.9. Property `position-relative-to-grid`

**Title:** Position Relative to Grid

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Default**               | `{"x": 0, "y": 0}`      |
| **Defined in**            | ../common/position.json |

**Description:** The coordinate offset to give the snapping grid (as indicated by the flag icon in the Blueprint's inspection GUI).

| Property                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#oneOf_i0_blueprint_position-relative-to-grid_x ) | No      | number | No         | -          | -                 |
| - [y](#oneOf_i0_blueprint_position-relative-to-grid_y ) | No      | number | No         | -          | -                 |

##### <a name="oneOf_i0_blueprint_position-relative-to-grid_x"></a>1.2.9.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

##### <a name="oneOf_i0_blueprint_position-relative-to-grid_y"></a>1.2.9.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

#### <a name="oneOf_i0_blueprint_entities"></a>1.2.10. Property `entities`

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

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [entities items](#oneOf_i0_blueprint_entities_items) | -           |

##### <a name="oneOf_i0_blueprint_entities_items"></a>1.2.10.1. entities items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                       |
| -------------------------------------------------------------------- |
| [Accumulator](#oneOf_i0_blueprint_entities_items_anyOf_i0)           |
| [Agricultural Tower](#oneOf_i0_blueprint_entities_items_anyOf_i1)    |
| [Ammo Turret](#oneOf_i0_blueprint_entities_items_anyOf_i2)           |
| [Arithmetic Combinator](#oneOf_i0_blueprint_entities_items_anyOf_i3) |
| [Artillery Turret](#oneOf_i0_blueprint_entities_items_anyOf_i4)      |
| [Artillery Wagon](#oneOf_i0_blueprint_entities_items_anyOf_i5)       |
| [Assembling Machine](#oneOf_i0_blueprint_entities_items_anyOf_i6)    |
| [Asteroid Collector](#oneOf_i0_blueprint_entities_items_anyOf_i7)    |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0"></a>1.2.10.1.1. Property `Accumulator`

**Title:** Accumulator

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | entity/accumulator.json |

**Description:** An entity that stores electricity for periods of high demand.

| Property                                                                            | Pattern | Type              | Deprecated | Definition                  | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ----------------- | ---------- | --------------------------- | ----------------- |
| + [entity_number](#oneOf_i0_blueprint_entities_items_anyOf_i0_entity_number )       | No      | number            | No         | In ../common/uint64.json    | Entity Number     |
| + [name](#oneOf_i0_blueprint_entities_items_anyOf_i0_name )                         | No      | string            | No         | -                           | Name              |
| + [position](#oneOf_i0_blueprint_entities_items_anyOf_i0_position )                 | No      | object            | No         | In ../common/position.json  | Position          |
| - [direction](#oneOf_i0_blueprint_entities_items_anyOf_i0_direction )               | No      | enum (of integer) | No         | -                           | Direction         |
| - [mirror](#oneOf_i0_blueprint_entities_items_anyOf_i0_mirror )                     | No      | boolean           | No         | -                           | Mirror            |
| - [quality](#oneOf_i0_blueprint_entities_items_anyOf_i0_quality )                   | No      | enum (of string)  | No         | In common/quality-name.json | Quality           |
| - [tags](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags )                         | No      | object            | No         | -                           | Tags              |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior ) | No      | object            | No         | -                           | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_entity_number"></a>1.2.10.1.1.1. Property `entity_number`

**Title:** Entity Number

|                |                       |
| -------------- | --------------------- |
| **Type**       | `number`              |
| **Required**   | Yes                   |
| **Defined in** | ../common/uint64.json |

**Description:** A unique ID given to every entity contained within a blueprint. In practice, this value is the 1-indexed position of the entity inside it's parent blueprint's 'entities' list. This is not enforced however, so an entity's number can be specified with any value as long as it's unique inside that particular blueprint. This value is used for resolving associations between different entities, such as wire connections or schedule definitions.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_name"></a>1.2.10.1.1.2. Property `name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the entity. If this name is not recognized by Factorio when importing the entity is omitted with a notification to the console.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_position"></a>1.2.10.1.1.3. Property `position`

**Title:** Position

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | Yes                     |
| **Additional properties** | Any type allowed        |
| **Defined in**            | ../common/position.json |

**Description:** The position where the entity is located inside of it's parent blueprint. This position is (almost) always located at the spatial center of the entity. For grid-aligned entities, this position always lies either in the center of a tile or on its transition.

| Property                                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [x](#oneOf_i0_blueprint_position-relative-to-grid_x ) | No      | number | No         | -          | -                 |
| - [y](#oneOf_i0_blueprint_position-relative-to-grid_y ) | No      | number | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_position-relative-to-grid_x"></a>1.2.10.1.1.3.1. Property `x`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_position-relative-to-grid_y"></a>1.2.10.1.1.3.2. Property `y`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_direction"></a>1.2.10.1.1.4. Property `direction`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_mirror"></a>1.2.10.1.1.5. Property `mirror`

**Title:** Mirror

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not the input/output fluid boxes are mirrored on this particular entity.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_quality"></a>1.2.10.1.1.6. Property `quality`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags"></a>1.2.10.1.1.7. Property `tags`

**Title:** Tags

|                           |                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                     |
| **Required**              | No                                                                                                                           |
| **Additional properties** | [Each additional property must conform to the schema](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties) |

**Description:** Any additional metadata associated with this entity, mostly intended for including mod information inside exported blueprint strings. Each key must be a string, and each value can be either a string, a boolean, a number, or another JSON object.

| Property                                                                     | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties ) | No      | Combination | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties"></a>1.2.10.1.1.7.1. Property `additionalProperties`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                           |
| ---------------------------------------------------------------------------------------- |
| [item 0](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1) |
| [item 2](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2) |
| [object](#oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i0"></a>1.2.10.1.1.7.1.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i1"></a>1.2.10.1.1.7.1.2. Property `item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i2"></a>1.2.10.1.1.7.1.3. Property `item 2`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_tags_additionalProperties_anyOf_i3"></a>1.2.10.1.1.7.1.4. Property `object`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | object           |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior"></a>1.2.10.1.1.8. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                       | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [output_signal](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal ) | No      | Combination | No         | -          | Output Signal     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal"></a>1.2.10.1.1.8.1. Property `output_signal`

**Title:** Output Signal

|                           |                                           |
| ------------------------- | ----------------------------------------- |
| **Type**                  | `combining`                               |
| **Required**              | No                                        |
| **Additional properties** | Any type allowed                          |
| **Default**               | `{"name": "signal-A", "type": "virtual"}` |

**Description:** What signal to send the current accumulator charge level value (in the range [0, 100]) if this accumulator is connected to a circuit network.

| One of(Option)                                                                                  |
| ----------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i0"></a>1.2.10.1.1.8.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i0_control_behavior_output_signal_oneOf_i1"></a>1.2.10.1.1.8.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1"></a>1.2.10.1.2. Property `Agricultural Tower`

**Title:** Agricultural Tower

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/agricultural-tower.json |

**Description:** An entity that seeds and harvests plants automatically.

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior ) | No      | object | No         | -          | -                 |

| All of(Requirement)                                                             |
| ------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i0)          |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1)      |
| [circuit-enabled.json](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2)    |
| [circuit-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3)  |
| [logistic-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i0"></a>1.2.10.1.2.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1"></a>1.2.10.1.2.2. Property `item-requests.json`

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | features/item-requests.json |

| Property                                                               | Pattern | Type  | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [items](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items ) | No      | array | No         | -          | Item Requests     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items"></a>1.2.10.1.2.2.1. Property `items`

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

| Each item of this array must be                                                               | Description                                                                                                   |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:item-request](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1_items_items"></a>1.2.10.1.2.2.1.1. urn:factorio:item-request

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:item-request |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2"></a>1.2.10.1.2.3. Property `circuit-enabled.json`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | features/circuit-enabled.json |

| Property                                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior"></a>1.2.10.1.2.3.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                    | Pattern | Type    | Deprecated | Definition | Title/Description                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------------- |
| - [circuit_enabled](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled ) | No      | boolean | No         | -          | Whether or not this entity should be controlled by a specified circuit condition. |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2_control_behavior_circuit_enabled"></a>1.2.10.1.2.3.1.1. Property `circuit_enabled`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified circuit condition.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3"></a>1.2.10.1.2.4. Property `circuit-condition.json`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | features/circuit-condition.json |

| Property                                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior"></a>1.2.10.1.2.4.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                        | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| --------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [circuit_condition](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition ) | No      | object | No         | In ../../common/condition.json | Condition         |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition"></a>1.2.10.1.2.4.1.1. Property `circuit_condition`

**Title:** Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** A conditional statement between either 2 signals or 1 signal and 1 constant value.

| Property                                                                                                                  | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal"></a>1.2.10.1.2.4.1.1.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>1.2.10.1.2.4.1.1.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>1.2.10.1.2.4.1.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator"></a>1.2.10.1.2.4.1.1.2. Property `comparator`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant"></a>1.2.10.1.2.4.1.1.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal"></a>1.2.10.1.2.4.1.1.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>1.2.10.1.2.4.1.1.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>1.2.10.1.2.4.1.1.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4"></a>1.2.10.1.2.5. Property `logistic-condition.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/logistic-condition.json |

| Property                                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior"></a>1.2.10.1.2.5.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                                            | Pattern | Type    | Deprecated | Definition                     | Title/Description            |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ------------------------------ | ---------------------------- |
| - [connect_to_logistic_network](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network ) | No      | boolean | No         | -                              | Connect to logistic network? |
| - [logistic_condition](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition )                   | No      | object  | No         | In ../../common/condition.json | Logistic Condition           |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_connect_to_logistic_network"></a>1.2.10.1.2.5.1.1. Property `connect_to_logistic_network`

**Title:** Connect to logistic network?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should be controlled by a specified logistic condition.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4_control_behavior_logistic_condition"></a>1.2.10.1.2.5.1.2. Property `logistic_condition`

**Title:** Logistic Condition

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | ../../common/condition.json |

**Description:** The logistic condition that the entity should be enabled with, if 'connect_to_logistic_network' is 'true'.

| Property                                                                                                                  | Pattern | Type             | Deprecated | Definition                      | Title/Description |
| ------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------- | ----------------- |
| - [first_signal](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal )   | No      | Combination      | No         | -                               | First Signal      |
| - [comparator](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator )       | No      | enum (of string) | No         | In ../../common/comparator.json | Comparator        |
| - [constant](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant )           | No      | number           | No         | In ../../common/int32.json      | Constant          |
| - [second_signal](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal ) | No      | Combination      | No         | -                               | Second Signal     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal"></a>1.2.10.1.2.5.1.2.1. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The leftmost signal in the condition.

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i0"></a>1.2.10.1.2.5.1.2.1.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_first_signal_oneOf_i1"></a>1.2.10.1.2.5.1.2.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_comparator"></a>1.2.10.1.2.5.1.2.2. Property `comparator`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant"></a>1.2.10.1.2.5.1.2.3. Property `constant`

**Title:** Constant

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `number`                |
| **Required**   | No                      |
| **Default**    | `0`                     |
| **Defined in** | ../../common/int32.json |

**Description:** A constant to compare against, always lying in the rightmost slot. This value is ignored if 'second_signal' is also present.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal"></a>1.2.10.1.2.5.1.2.4. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** The rightmost signal of the condition. Takes precedence over 'constant', if both happen to be specified.

| One of(Option)                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i0"></a>1.2.10.1.2.5.1.2.4.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_second_signal_oneOf_i1"></a>1.2.10.1.2.5.1.2.4.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior"></a>1.2.10.1.2.6. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                       | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [read_contents](#oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior_read_contents ) | No      | boolean | No         | -          | Read Contents     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i1_control_behavior_read_contents"></a>1.2.10.1.2.6.1. Property `read_contents`

**Title:** Read Contents

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should broadcast the contents of its inventory to a connected circuit network.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2"></a>1.2.10.1.3. Property `Ammo Turret`

**Title:** Ammo Turret

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `combining`             |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | entity/ammo-turret.json |

**Description:** A turret that uses item-based ammunition.

| All of(Requirement)                                                             |
| ------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i0)          |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i1)      |
| [circuit-enabled.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i2)    |
| [circuit-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i3)  |
| [logistic-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i4) |
| [turret-priorities.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5)  |
| [read-ammo.json](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6)          |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i0"></a>1.2.10.1.3.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i1"></a>1.2.10.1.3.2. Property `item-requests.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i2"></a>1.2.10.1.3.3. Property `circuit-enabled.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i3"></a>1.2.10.1.3.4. Property `circuit-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i4"></a>1.2.10.1.3.5. Property `logistic-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5"></a>1.2.10.1.3.6. Property `turret-priorities.json`

|                           |                                 |
| ------------------------- | ------------------------------- |
| **Type**                  | `object`                        |
| **Required**              | No                              |
| **Additional properties** | Any type allowed                |
| **Defined in**            | features/turret-priorities.json |

| Property                                                                                                                       | Pattern | Type    | Deprecated | Definition                       | Title/Description                 |
| ------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- | ---------- | -------------------------------- | --------------------------------- |
| - [priority_list](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list )                                         | No      | array   | No         | -                                | Priority List                     |
| - [ignore_unprioritized](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized )                           | No      | boolean | No         | -                                | Ignore Unprioritized              |
| - [set_priority_list](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list )                                 | No      | boolean | No         | -                                | Set Priority List                 |
| - [set_ignore_unprioritized](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized )                   | No      | boolean | No         | -                                | Set Ignore Unprioritized          |
| - [ignore_unlisted_targets_condition](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition ) | No      | object  | No         | In urn:factorio:simple-condition | Ignore Unlisted Targets Condition |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list"></a>1.2.10.1.3.6.1. Property `priority_list`

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

| Each item of this array must be                                                                    | Description                                                                                                   |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:target-id](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_priority_list_items"></a>1.2.10.1.3.6.1.1. urn:factorio:target-id

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:target-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unprioritized"></a>1.2.10.1.3.6.2. Property `ignore_unprioritized`

**Title:** Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not to completely ignore enemies that do not lie in this turret's target priority lists.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_priority_list"></a>1.2.10.1.3.6.3. Property `set_priority_list`

**Title:** Set Priority List

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should set its target priorities via connected circuit network signals.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_set_ignore_unprioritized"></a>1.2.10.1.3.6.4. Property `set_ignore_unprioritized`

**Title:** Set Ignore Unprioritized

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether or not this entity should have it's ignore unprioritized behavior be set conditionally via 'ignore_unlisted_targets_condition'.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i5_ignore_unlisted_targets_condition"></a>1.2.10.1.3.6.5. Property `ignore_unlisted_targets_condition`

**Title:** Ignore Unlisted Targets Condition

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | urn:factorio:simple-condition |

**Description:** A condition which must be true in order for non-prioritized targets to be entirely ignored when this turret is targeting. Does nothing unless 'set_ignore_unprioritized' is 'true'.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6"></a>1.2.10.1.3.7. Property `read-ammo.json`

|                           |                         |
| ------------------------- | ----------------------- |
| **Type**                  | `object`                |
| **Required**              | No                      |
| **Additional properties** | Any type allowed        |
| **Defined in**            | features/read-ammo.json |

| Property                                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior ) | No      | object | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior"></a>1.2.10.1.3.7.1. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                        | Pattern | Type    | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [read_ammo](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo ) | No      | boolean | No         | -          | Read Ammo         |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6_control_behavior_read_ammo"></a>1.2.10.1.3.7.1.1. Property `read_ammo`

**Title:** Read Ammo

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not to broadcast the current amount of ammo in the turrets inventory to a connected circuit network.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3"></a>1.2.10.1.4. Property `Arithmetic Combinator`

**Title:** Arithmetic Combinator

|                           |                                   |
| ------------------------- | --------------------------------- |
| **Type**                  | `combining`                       |
| **Required**              | No                                |
| **Additional properties** | Any type allowed                  |
| **Defined in**            | entity/arithmetic-combinator.json |

**Description:** A combinator that can perform mathematical operations on one or more values.

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior ) | No      | object | No         | -          | -                 |

| All of(Requirement)                                                             |
| ------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i0)          |
| [player-description.json](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i0"></a>1.2.10.1.4.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1"></a>1.2.10.1.4.2. Property `player-description.json`

|                           |                                  |
| ------------------------- | -------------------------------- |
| **Type**                  | `object`                         |
| **Required**              | No                               |
| **Additional properties** | Any type allowed                 |
| **Defined in**            | features/player-description.json |

| Property                                                                                         | Pattern | Type   | Deprecated | Definition | Title/Description  |
| ------------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ------------------ |
| - [player_description](#oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1_player_description ) | No      | string | No         | -          | Player Description |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_allOf_i1_player_description"></a>1.2.10.1.4.2.1. Property `player_description`

**Title:** Player Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** An attached string, intended for entity documentation.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior"></a>1.2.10.1.4.3. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                       | Pattern | Type   | Deprecated | Definition | Title/Description     |
| -------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | --------------------- |
| - [arithmetic_conditions](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions ) | No      | object | No         | -          | Arithmetic Conditions |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions"></a>1.2.10.1.4.3.1. Property `arithmetic_conditions`

**Title:** Arithmetic Conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Container for arithmetic combinator specific parameters.

| Property                                                                                                                               | Pattern | Type             | Deprecated | Definition                              | Title/Description      |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | --------------------------------------- | ---------------------- |
| - [first_constant](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant )                 | No      | Combination      | No         | -                                       | First Constant         |
| - [first_signal](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal )                     | No      | Combination      | No         | -                                       | First Signal           |
| - [first_signal_networks](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks )   | No      | object           | No         | In ../common/network-specification.json | First Signal Networks  |
| - [operation](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation )                           | No      | enum (of string) | No         | -                                       | Operation              |
| - [second_constant](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant )               | No      | Combination      | No         | -                                       | Second Constant        |
| - [second_signal](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal )                   | No      | Combination      | No         | -                                       | Second Signal          |
| - [second_signal_networks](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks ) | No      | object           | No         | In ../common/network-specification.json | Second Signal Networks |
| - [output_signal](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal )                   | No      | Combination      | No         | -                                       | Output Signal          |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant"></a>1.2.10.1.4.3.1.1. Property `first_constant`

**Title:** First Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Constant value that goes in the leftmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ |
| [int32.json](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1)     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i0"></a>1.2.10.1.4.3.1.1.1. Property `int32.json`

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**               | `number`                                                                                                     |
| **Required**           | No                                                                                                           |
| **Same definition as** | [constant](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant) |

**Description:** Signed 32-bit integer.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_constant_oneOf_i1"></a>1.2.10.1.4.3.1.1.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal"></a>1.2.10.1.4.3.1.2. Property `first_signal`

**Title:** First Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the leftmost slot. Takes precedence over 'first_constant', if both happen to be specified.

| One of(Option)                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i0"></a>1.2.10.1.4.3.1.2.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_oneOf_i1"></a>1.2.10.1.4.3.1.2.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks"></a>1.2.10.1.4.3.1.3. Property `first_signal_networks`

**Title:** First Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the leftmost slot should consider for values. Only has an effect if the first slot is occupied by a signal.

| Property                                                                                                                   | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red"></a>1.2.10.1.4.3.1.3.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green"></a>1.2.10.1.4.3.1.3.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_operation"></a>1.2.10.1.4.3.1.4. Property `operation`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant"></a>1.2.10.1.4.3.1.5. Property `second_constant`

**Title:** Second Constant

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `0`              |

**Description:** Constant value that goes in the rightmost slot. This value is ignored if 'second_signal' is also present.

| One of(Option)                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------- |
| [int32.json](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1)     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i0"></a>1.2.10.1.4.3.1.5.1. Property `int32.json`

|                        |                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**               | `number`                                                                                                     |
| **Required**           | No                                                                                                           |
| **Same definition as** | [constant](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3_control_behavior_circuit_condition_constant) |

**Description:** Signed 32-bit integer.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_constant_oneOf_i1"></a>1.2.10.1.4.3.1.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal"></a>1.2.10.1.4.3.1.6. Property `second_signal`

**Title:** Second Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** Signal ID that goes in the rightmost slot. Takes precedence over 'second_constant', if both happen to be specified.

| One of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i0"></a>1.2.10.1.4.3.1.6.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_oneOf_i1"></a>1.2.10.1.4.3.1.6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_second_signal_networks"></a>1.2.10.1.4.3.1.7. Property `second_signal_networks`

**Title:** Second Signal Networks

|                           |                                      |
| ------------------------- | ------------------------------------ |
| **Type**                  | `object`                             |
| **Required**              | No                                   |
| **Additional properties** | Any type allowed                     |
| **Default**               | `{"red": true, "green": true}`       |
| **Defined in**            | ../common/network-specification.json |

**Description:** Which wire colors the rightmost slot should consider for values. Only has an effect if the second slot is occupied by a signal.

| Property                                                                                                                   | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [red](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red )     | No      | boolean | No         | -          | -                 |
| - [green](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green ) | No      | boolean | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_red"></a>1.2.10.1.4.3.1.7.1. Property `red`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_first_signal_networks_green"></a>1.2.10.1.4.3.1.7.2. Property `green`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal"></a>1.2.10.1.4.3.1.8. Property `output_signal`

**Title:** Output Signal

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

**Description:** What signal (or signals) should this combinator output.

| One of(Option)                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- |
| [SignalID](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1)   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i0"></a>1.2.10.1.4.3.1.8.1. Property `SignalID`

**Title:** SignalID

|                           |                                                  |
| ------------------------- | ------------------------------------------------ |
| **Type**                  | `object`                                         |
| **Required**              | No                                               |
| **Additional properties** | Any type allowed                                 |
| **Same definition as**    | [signal](#oneOf_i0_blueprint_icons_items_signal) |

**Description:** An object which represents a valid signal.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i3_control_behavior_arithmetic_conditions_output_signal_oneOf_i1"></a>1.2.10.1.4.3.1.8.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4"></a>1.2.10.1.5. Property `Artillery Turret`

**Title:** Artillery Turret

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `combining`                  |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | entity/artillery-turret.json |

**Description:** A turret that targets enemy structures over long ranges.

| All of(Requirement)                                                                   |
| ------------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i0)                |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i1)            |
| [circuit-enabled.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i2)          |
| [circuit-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i3)        |
| [logistic-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i4)       |
| [read-ammo.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i5)                |
| [artillery-auto-targeting.json](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i0"></a>1.2.10.1.5.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i1"></a>1.2.10.1.5.2. Property `item-requests.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i2"></a>1.2.10.1.5.3. Property `circuit-enabled.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i3"></a>1.2.10.1.5.4. Property `circuit-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i4"></a>1.2.10.1.5.5. Property `logistic-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i5"></a>1.2.10.1.5.6. Property `read-ammo.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6](#oneOf_i0_blueprint_entities_items_anyOf_i2_allOf_i6) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6"></a>1.2.10.1.5.7. Property `artillery-auto-targeting.json`

|                           |                                        |
| ------------------------- | -------------------------------------- |
| **Type**                  | `object`                               |
| **Required**              | No                                     |
| **Additional properties** | Any type allowed                       |
| **Defined in**            | features/artillery-auto-targeting.json |

| Property                                                                                                     | Pattern | Type    | Deprecated | Definition | Title/Description        |
| ------------------------------------------------------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | ------------------------ |
| - [artillery_auto_targeting](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting ) | No      | boolean | No         | -          | Artillery Auto Targeting |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6_artillery_auto_targeting"></a>1.2.10.1.5.7.1. Property `artillery_auto_targeting`

**Title:** Artillery Auto Targeting

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should automatically target enemies in range.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5"></a>1.2.10.1.6. Property `Artillery Wagon`

**Title:** Artillery Wagon

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `combining`                 |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | entity/artillery-wagon.json |

**Description:** Rolling stock with an attached artillery turret.

| All of(Requirement)                                                                   |
| ------------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i0)                |
| [orientation.json](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1)              |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i2)            |
| [equipment-grid.json](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3)           |
| [artillery-auto-targeting.json](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i0"></a>1.2.10.1.6.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1"></a>1.2.10.1.6.2. Property `orientation.json`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | features/orientation.json |

| Property                                                                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [orientation](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1_orientation ) | No      | number | No         | -          | Orientation       |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i1_orientation"></a>1.2.10.1.6.2.1. Property `orientation`

**Title:** Orientation

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0.0`    |

**Description:** A number in the range [0.0, 1.0] representing the direction this entity is facing. Any value specified out of this range is modulo'd back into this range.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i2"></a>1.2.10.1.6.3. Property `item-requests.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3"></a>1.2.10.1.6.4. Property `equipment-grid.json`

|                           |                              |
| ------------------------- | ---------------------------- |
| **Type**                  | `object`                     |
| **Required**              | No                           |
| **Additional properties** | Any type allowed             |
| **Defined in**            | features/equipment-grid.json |

| Property                                                                                                               | Pattern | Type    | Deprecated | Definition | Title/Description              |
| ---------------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------ |
| - [enable_logistics_while_moving](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving ) | No      | boolean | No         | -          | Enable Logistics While Moving? |
| - [grid](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid )                                                   | No      | array   | No         | -          | Equipment Grid Components      |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_enable_logistics_while_moving"></a>1.2.10.1.6.4.1. Property `enable_logistics_while_moving`

**Title:** Enable Logistics While Moving?

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether or not this entity should try to fulfill it's logistic requests when it is in motion. Only has an effect if this entity is configured to have an equipment grid and that equipment grid contains personal roboports.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid"></a>1.2.10.1.6.4.2. Property `grid`

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

| Each item of this array must be                                                        | Description |
| -------------------------------------------------------------------------------------- | ----------- |
| [equipment-component](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items) | -           |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items"></a>1.2.10.1.6.4.2.1. equipment-component

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | #/$defs/equipment-component |

| Property                                                                                  | Pattern | Type   | Deprecated | Definition               | Title/Description                                                                                         |
| ----------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| + [equipment](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment ) | No      | object | No         | In #/$defs/equipment-id  | Equipment ID                                                                                              |
| + [position](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position )   | No      | object | No         | In urn:factorio:position | The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies. |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment"></a>1.2.10.1.6.4.2.1.1. Property `equipment`

**Title:** Equipment ID

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | Yes                  |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/equipment-id |

**Description:** A particular type of equipment and its quality.

| Property                                                                                        | Pattern | Type   | Deprecated | Definition                   | Title/Description                                                                                             |
| ----------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [name](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name )       | No      | string | No         | -                            | The name of a valid piece of equipment (that can fit inside this particular equipment grid).                  |
| - [quality](#oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality ) | No      | object | No         | In urn:factorio:quality-name | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_name"></a>1.2.10.1.6.4.2.1.1.1. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid piece of equipment (that can fit inside this particular equipment grid).

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_equipment_quality"></a>1.2.10.1.6.4.2.1.1.2. Property `quality`

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | urn:factorio:quality-name |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i3_grid_items_position"></a>1.2.10.1.6.4.2.1.2. Property `position`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | Yes                   |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:position |

**Description:** The position of the equipment in integer coordinates, corresponding to the top-leftmost tile it occupies.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i5_allOf_i4"></a>1.2.10.1.6.5. Property `artillery-auto-targeting.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6](#oneOf_i0_blueprint_entities_items_anyOf_i4_allOf_i6) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6"></a>1.2.10.1.7. Property `Assembling Machine`

**Title:** Assembling Machine

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/assembling-machine.json |

**Description:** An entity that can convert items and fluids into other items and fluids.

| Property                                                                            | Pattern | Type             | Deprecated | Definition                     | Title/Description |
| ----------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ----------------- |
| - [recipe](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe )                     | No      | Combination      | No         | -                              | Recipe            |
| - [recipe_quality](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_quality )     | No      | enum (of string) | No         | In ../common/quality-name.json | Recipe Quality    |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior ) | No      | object           | No         | -                              | -                 |

| All of(Requirement)                                                             |
| ------------------------------------------------------------------------------- |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i0)          |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i1)      |
| [circuit-enabled.json](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i2)    |
| [circuit-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i3)  |
| [logistic-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i0"></a>1.2.10.1.7.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i1"></a>1.2.10.1.7.2. Property `item-requests.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i2"></a>1.2.10.1.7.3. Property `circuit-enabled.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i3"></a>1.2.10.1.7.4. Property `circuit-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_allOf_i4"></a>1.2.10.1.7.5. Property `logistic-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i4) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_recipe"></a>1.2.10.1.7.6. Property `recipe`

**Title:** Recipe

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The recipe that this entity is configured to perform.

| One of(Option)                                                        |
| --------------------------------------------------------------------- |
| [item 0](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i0"></a>1.2.10.1.7.6.1. Property `item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_oneOf_i1"></a>1.2.10.1.7.6.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_recipe_quality"></a>1.2.10.1.7.7. Property `recipe_quality`

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

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior"></a>1.2.10.1.7.8. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                         | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [set_recipe](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_set_recipe )                         | No      | boolean     | No         | -          | -                 |
| - [read_contents](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_contents )                   | No      | boolean     | No         | -          | -                 |
| - [include_in_crafting](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting )       | No      | boolean     | No         | -          | -                 |
| - [read_recipe_finished](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished )     | No      | boolean     | No         | -          | -                 |
| - [recipe_finished_signal](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal ) | No      | Combination | No         | -          | -                 |
| - [read_working](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_working )                     | No      | boolean     | No         | -          | -                 |
| - [working_signal](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal )                 | No      | Combination | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_set_recipe"></a>1.2.10.1.7.8.1. Property `set_recipe`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_contents"></a>1.2.10.1.7.8.2. Property `read_contents`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_include_in_crafting"></a>1.2.10.1.7.8.3. Property `include_in_crafting`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"true"`  |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_recipe_finished"></a>1.2.10.1.7.8.4. Property `read_recipe_finished`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal"></a>1.2.10.1.7.8.5. Property `recipe_finished_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `null`           |

| Any of(Option)                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:signal-id](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1)                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i0"></a>1.2.10.1.7.8.5.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_recipe_finished_signal_anyOf_i1"></a>1.2.10.1.7.8.5.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_read_working"></a>1.2.10.1.7.8.6. Property `read_working`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal"></a>1.2.10.1.7.8.7. Property `working_signal`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                                                                 |
| -------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:signal-id](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0) |
| [item 1](#oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1)                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i0"></a>1.2.10.1.7.8.7.1. Property `urn:factorio:signal-id`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | urn:factorio:signal-id |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i6_control_behavior_working_signal_anyOf_i1"></a>1.2.10.1.7.8.7.2. Property `item 1`

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7"></a>1.2.10.1.8. Property `Asteroid Collector`

**Title:** Asteroid Collector

|                           |                                |
| ------------------------- | ------------------------------ |
| **Type**                  | `combining`                    |
| **Required**              | No                             |
| **Additional properties** | Any type allowed               |
| **Defined in**            | entity/asteroid-collector.json |

**Description:** An entity uses arms to grab asteroid chunks from space.

| Property                                                                            | Pattern | Type   | Deprecated | Definition | Title/Description       |
| ----------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------------- |
| - [result_inventory](#oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory ) | No      | object | No         | -          | Result Inventory Object |
| - [chunk-filter](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter )         | No      | array  | No         | -          | -                       |
| - [control_behavior](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior ) | No      | object | No         | -          | -                       |

| All of(Requirement)                                                            |
| ------------------------------------------------------------------------------ |
| [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i0)         |
| [item-requests.json](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i1)     |
| [circuit-enabled.json](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i2)   |
| [circuit-condition.json](#oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i0"></a>1.2.10.1.8.1. Property `Generic Entity`

**Title:** Generic Entity

|                           |                                                               |
| ------------------------- | ------------------------------------------------------------- |
| **Type**                  | `object`                                                      |
| **Required**              | No                                                            |
| **Additional properties** | Any type allowed                                              |
| **Same definition as**    | [Generic Entity](#oneOf_i0_blueprint_entities_items_anyOf_i0) |

**Description:** A schema which contains the keys that all entities share.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i1"></a>1.2.10.1.8.2. Property `item-requests.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i1) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i2"></a>1.2.10.1.8.3. Property `circuit-enabled.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i2) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_allOf_i3"></a>1.2.10.1.8.4. Property `circuit-condition.json`

|                           |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                    |
| **Required**              | No                                                                                                          |
| **Additional properties** | Any type allowed                                                                                            |
| **Same definition as**    | [oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3](#oneOf_i0_blueprint_entities_items_anyOf_i1_allOf_i3) |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory"></a>1.2.10.1.8.5. Property `result_inventory`

**Title:** Result Inventory Object

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Inventory object which holds the limiting bar for this entity.

| Property                                                                   | Pattern | Type   | Deprecated | Definition                                  | Title/Description |
| -------------------------------------------------------------------------- | ------- | ------ | ---------- | ------------------------------------------- | ----------------- |
| - [bar](#oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory_bar ) | No      | number | No         | Same as [uint16](#oneOf_i0_index_oneOf_i0 ) | uint16            |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_result_inventory_bar"></a>1.2.10.1.8.5.1. Property `bar`

**Title:** uint16

|                        |                                    |
| ---------------------- | ---------------------------------- |
| **Type**               | `number`                           |
| **Required**           | No                                 |
| **Same definition as** | [uint16](#oneOf_i0_index_oneOf_i0) |

**Description:** An unsigned 16-bit integer.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter"></a>1.2.10.1.8.6. Property `chunk-filter`

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

| Each item of this array must be                                                     | Description |
| ----------------------------------------------------------------------------------- | ----------- |
| [asteroid-chunk-id](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items) | -           |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items"></a>1.2.10.1.8.6.1. asteroid-chunk-id

|                           |                           |
| ------------------------- | ------------------------- |
| **Type**                  | `object`                  |
| **Required**              | No                        |
| **Additional properties** | Any type allowed          |
| **Defined in**            | #/$defs/asteroid-chunk-id |

| Property                                                                         | Pattern | Type   | Deprecated | Definition           | Title/Description                                                                                             |
| -------------------------------------------------------------------------------- | ------- | ------ | ---------- | -------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [index](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_index ) | No      | object | No         | In ../../uint32.json | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |
| - [name](#oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_name )   | No      | string | No         | -                    | The name of a valid Factorio asteroid chunk.                                                                  |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_index"></a>1.2.10.1.8.6.1.1. Property `index`

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Defined in**            | ../../uint32.json |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_chunk-filter_items_name"></a>1.2.10.1.8.6.1.2. Property `name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of a valid Factorio asteroid chunk.

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior"></a>1.2.10.1.8.7. Property `control_behavior`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                                       | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [circuit_set_filters](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters )     | No      | boolean | No         | -          | -                 |
| - [circuit_read_contents](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents ) | No      | boolean | No         | -          | -                 |
| - [include_hands](#oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_include_hands )                 | No      | boolean | No         | -          | -                 |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_set_filters"></a>1.2.10.1.8.7.1. Property `circuit_set_filters`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_circuit_read_contents"></a>1.2.10.1.8.7.2. Property `circuit_read_contents`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

###### <a name="oneOf_i0_blueprint_entities_items_anyOf_i7_control_behavior_include_hands"></a>1.2.10.1.8.7.3. Property `include_hands`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

#### <a name="oneOf_i0_blueprint_tiles"></a>1.2.11. Property `tiles`

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

| Each item of this array must be                      | Description                                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:tile](#oneOf_i0_blueprint_tiles_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

##### <a name="oneOf_i0_blueprint_tiles_items"></a>1.2.11.1. urn:factorio:tile

|                           |                   |
| ------------------------- | ----------------- |
| **Type**                  | `object`          |
| **Required**              | No                |
| **Additional properties** | Any type allowed  |
| **Defined in**            | urn:factorio:tile |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

#### <a name="oneOf_i0_blueprint_wires"></a>1.2.12. Property `wires`

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

| Each item of this array must be                | Description |
| ---------------------------------------------- | ----------- |
| [wires items](#oneOf_i0_blueprint_wires_items) | -           |

##### <a name="oneOf_i0_blueprint_wires_items"></a>1.2.12.1. wires items

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

| Each item of this array must be                                | Description                                                                                       |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [uint64](#oneOf_i0_blueprint_wires_items_items_i0)             | 'entity_number' of the first entity being connected.                                              |
| [wires items item 1](#oneOf_i0_blueprint_wires_items_items_i1) | What kind of connection the wire has to entity1. See 'wire_connection_types' in Factorio defines. |
| [uint64](#oneOf_i0_blueprint_wires_items_items_i2)             | 'entity_number' of the second entity being connected.                                             |
| [wires items item 3](#oneOf_i0_blueprint_wires_items_items_i3) | What kind of connection the wire has to entity2. See 'wire_connection_types' in Factorio defines. |

###### <a name="autogenerated_heading_2"></a>1.2.12.1.1. uint64

**Title:** uint64

|                        |                                        |
| ---------------------- | -------------------------------------- |
| **Type**               | `number`                               |
| **Required**           | No                                     |
| **Same definition as** | [version](#oneOf_i0_blueprint_version) |

**Description:** 'entity_number' of the first entity being connected.

###### <a name="autogenerated_heading_3"></a>1.2.12.1.2. wires items item 1

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

###### <a name="autogenerated_heading_4"></a>1.2.12.1.3. uint64

**Title:** uint64

|                        |                                        |
| ---------------------- | -------------------------------------- |
| **Type**               | `number`                               |
| **Required**           | No                                     |
| **Same definition as** | [version](#oneOf_i0_blueprint_version) |

**Description:** 'entity_number' of the second entity being connected.

###### <a name="autogenerated_heading_5"></a>1.2.12.1.4. wires items item 3

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

#### <a name="oneOf_i0_blueprint_schedules"></a>1.2.13. Property `schedules`

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

| Each item of this array must be                              | Description                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:schedule](#oneOf_i0_blueprint_schedules_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

##### <a name="oneOf_i0_blueprint_schedules_items"></a>1.2.13.1. urn:factorio:schedule

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Defined in**            | urn:factorio:schedule |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

#### <a name="oneOf_i0_blueprint_stock_connections"></a>1.2.14. Property `stock_connections`

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

| Each item of this array must be                                              | Description                                                                                                   |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [urn:factorio:stock-connection](#oneOf_i0_blueprint_stock_connections_items) | 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️ |

##### <a name="oneOf_i0_blueprint_stock_connections_items"></a>1.2.14.1. urn:factorio:stock-connection

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Defined in**            | urn:factorio:stock-connection |

**Description:** 😅 ERROR in schema generation, a referenced schema could not be loaded, no documentation here unfortunately 🏜️

## <a name="oneOf_i1"></a>2. Property `Deconstruction Planner`

**Title:** Deconstruction Planner

|                           |                             |
| ------------------------- | --------------------------- |
| **Type**                  | `object`                    |
| **Required**              | No                          |
| **Additional properties** | Any type allowed            |
| **Defined in**            | deconstruction-planner.json |

## <a name="oneOf_i2"></a>3. Property `Upgrade Planner`

**Title:** Upgrade Planner

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | upgrade-planner.json |

## <a name="oneOf_i3"></a>4. Property `Blueprint Book`

**Title:** Blueprint Book

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `object`            |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | blueprint-book.json |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)

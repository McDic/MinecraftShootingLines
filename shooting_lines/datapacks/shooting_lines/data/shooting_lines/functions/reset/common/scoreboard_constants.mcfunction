# Total tiles = pow(63 - (-64) + 1, 2) = 128 * 128 = 16384
scoreboard players set $total_tiles constants 16384

scoreboard players set $int_max constants 2147483647

scoreboard players set $global_tick variables 0
scoreboard players operation $last_reported_tick variables = $global_tick variables

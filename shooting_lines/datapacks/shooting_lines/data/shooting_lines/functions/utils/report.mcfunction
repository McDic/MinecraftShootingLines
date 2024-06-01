# Preventing report spam
scoreboard players operation $last_reported_gap variables = $global_tick variables
scoreboard players operation $last_reported_gap variables -= $last_reported_tick variables
execute if score $last_reported_gap variables matches ..19 run return fail
scoreboard players operation $last_reported_tick variables = $global_tick variables

# -------------------------------------------------

execute at @s run function shooting_lines:utils/gps
tellraw @a [{"text":"[ERROR] Report called at x="},{"score":{"name": "@s","objective": "gps_x"}},{"text":", y="},{"score":{"name": "@s","objective": "gps_y"}},{"text":", z="},{"score":{"name": "@s","objective": "gps_z"}}]

return fail

# Execute this function for each player.
# This function will automatically generates arguments for particle color, occupying, and more.

execute unless entity @s[x=-64,y=2,z=-64,dx=128,dy=300,dz=128,x_rotation=-30..90.1] run return fail
kill @e[type=minecraft:marker,tag=sl_raycasting]
summon minecraft:marker ~ ~ ~ {Tags:["sl", "sl_raycasting"], Invulnerable: true}
tp @e[type=minecraft:marker,tag=sl_raycasting] @s

scoreboard players set $current_team variables 0
execute if entity @s[team=redteam] run scoreboard players set $current_team variables 1
execute if entity @s[team=blueteam] run scoreboard players set $current_team variables 2
execute if entity @s[team=greenteam] run scoreboard players set $current_team variables 3

scoreboard players set $raycast_phase variables 0
scoreboard players set $raycast_recursion_depth variables 0
scoreboard players operation $raycast_depth_since_phase1a variables = $int_max constants
scoreboard players operation $raycast_depth_since_phase1b variables = $int_max constants

execute at @s as @e[type=minecraft:marker,tag=sl_raycasting] run function shooting_lines:game/select/raycast/body/main
kill @e[type=minecraft:marker,tag=sl_raycasting]

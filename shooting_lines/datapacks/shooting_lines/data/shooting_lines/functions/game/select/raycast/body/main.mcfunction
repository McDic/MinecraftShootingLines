# Run as/at temporary `sl_raycasting` entity
execute at @s run function shooting_lines:utils/gps
execute at @s if score $raycast_phase variables matches ..0 if block ~ 0 ~ minecraft:light_gray_concrete run scoreboard players set $raycast_phase variables 1
execute at @s if score $raycast_phase variables matches ..1 if score @s gps_y matches ..1 run scoreboard players set $raycast_phase variables 2
execute at @s if score $raycast_phase variables matches 2 if block ~ 0 ~ minecraft:light_gray_concrete run scoreboard players set $raycast_phase variables 3
# execute unless entity @s[x=-70,y=-64,z=-64,dx=140,dy=999,dz=140] run scoreboard players set $raycast_phase variables 3

# Set depth and checkpoints
scoreboard players add $raycast_recursion_depth variables 1
execute if score $raycast_phase variables matches 1.. run scoreboard players operation $raycast_depth_since_phase1a variables < $raycast_recursion_depth variables
execute if score $raycast_phase variables matches 2.. run scoreboard players operation $raycast_depth_since_phase1b variables < $raycast_recursion_depth variables
execute at @s if score $raycast_recursion_depth variables = $raycast_depth_since_phase1a variables align xyz run tp @s ~ ~ ~
execute at @s if score $raycast_recursion_depth variables = $raycast_depth_since_phase1b variables run tp @s ~ 1 ~ ~ 0

# Run phase 0~2
execute at @s if score $raycast_phase variables matches 0 run function shooting_lines:game/select/raycast/body/phase0
execute at @s if score $raycast_phase variables matches 1 run function shooting_lines:game/select/raycast/body/phase1a
execute at @s if score $raycast_phase variables matches 2 run function shooting_lines:game/select/raycast/body/phase1b

# Error check
execute if score $raycast_recursion_depth variables matches 3000.. run return fail

# Determine next
execute as @s if score $raycast_phase variables matches 0..2 at @s run function shooting_lines:game/select/raycast/body/main
execute as @s unless score $raycast_phase variables matches 0..2 at @s run function shooting_lines:game/select/raycast/body/finale

# After everything is finished, if placeable then display particles
execute as @s unless score $raycast_occupiable variables matches 0 if score $raycast_recursion_depth variables >= $raycast_depth_since_phase1a variables run function shooting_lines:game/select/raycast/body/display_particles/entry
scoreboard players remove $raycast_recursion_depth variables 1
team leave @s

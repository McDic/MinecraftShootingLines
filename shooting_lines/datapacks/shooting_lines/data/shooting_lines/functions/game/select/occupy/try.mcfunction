# This function is executed from ../../raycast/entry as each player

# Check
execute store success score $occupy_try_check variables run function shooting_lines:game/select/occupy/check

# Failure
execute if score $occupy_check_on_outline variables matches 0 run tellraw @s [{"text":"That location is not outline border.","italic":true,"color":"gray"}]
execute if score $occupy_check_on_outline variables matches 0 run tellraw @s [{"text":"That location is not outline border.","italic":true,"color":"gray"}]
execute unless score $occupy_check_on_outline variables matches 0 unless score $occupy_check_reserved variables matches 0 run tellraw @s [{"text":"That location is already selected by other players. It is not disclosed who chose the location.","italic":true,"color":"gray"}]
execute unless score $occupy_check_on_outline variables matches 0 unless score $occupy_check_occupied variables matches 0 run tellraw @s [{"text":"That location is already occupied.","italic":true,"color":"gray"}]
execute if score $occupy_try_check variables matches 0 run return fail

function shooting_lines:game/select/occupy/generated/reset_reservations
execute if entity @s[team=redteam] run setblock ~ -1 ~ minecraft:red_wool
execute if entity @s[team=redteam] run scoreboard players set $reserved_red variables 1
execute if entity @s[team=blueteam] run setblock ~ -1 ~ minecraft:blue_wool
execute if entity @s[team=blueteam] run scoreboard players set $reserved_blue variables 1
execute if entity @s[team=greenteam] run setblock ~ -1 ~ minecraft:green_wool
execute if entity @s[team=greenteam] run scoreboard players set $reserved_green variables 1

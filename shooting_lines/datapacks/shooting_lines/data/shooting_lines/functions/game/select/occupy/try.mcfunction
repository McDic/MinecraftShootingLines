# This function is executed from ../../raycast/entry as each player
execute unless function shooting_lines:game/select/occupy/check run return fail

function shooting_lines:game/select/occupy/generated/reset_reservations
execute if entity @s[team=redteam] run setblock ~ -1 ~ minecraft:red_wool
execute if entity @s[team=redteam] run scoreboard players set $reserved_red variables 1
execute if entity @s[team=blueteam] run setblock ~ -1 ~ minecraft:blue_wool
execute if entity @s[team=blueteam] run scoreboard players set $reserved_blue variables 1
execute if entity @s[team=greenteam] run setblock ~ -1 ~ minecraft:green_wool
execute if entity @s[team=greenteam] run scoreboard players set $reserved_green variables 1

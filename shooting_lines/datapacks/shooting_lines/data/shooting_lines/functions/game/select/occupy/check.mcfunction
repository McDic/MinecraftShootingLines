execute store success score $occupy_check_on_outline variables if block ~ 0 ~ minecraft:light_gray_concrete
execute store success score $occupy_check_reserved variables unless score $occupy_check_on_outline variables matches 0 if block ~ -1 ~ #shooting_lines:outline/reserved
execute store success score $occupy_check_occupied variables unless score $occupy_check_on_outline variables matches 0 if block ~ -1 ~ #shooting_lines:outline/occupied
execute unless score $occupy_check_on_outline variables matches 0 if score $occupy_check_reserved variables matches 0 if score $occupy_check_occupied variables matches 0 run return 1
return fail

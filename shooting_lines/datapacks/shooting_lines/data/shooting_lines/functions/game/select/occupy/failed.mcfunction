execute if score $occupy_check_on_outline variables matches 0 run tellraw @s [{"text":"That location is not outline border.","italic":true,"color":"gray"}]
execute if score $occupy_check_on_outline variables matches 0 run tellraw @s [{"text":"That location is not outline border.","italic":true,"color":"gray"}]
execute unless score $occupy_check_on_outline variables matches 0 unless score $occupy_check_reserved variables matches 0 run tellraw @s [{"text":"That location is already selected by other players. It is not disclosed who chose the location.","italic":true,"color":"gray"}]
execute unless score $occupy_check_on_outline variables matches 0 unless score $occupy_check_occupied variables matches 0 run tellraw @s [{"text":"That location is already occupied.","italic":true,"color":"gray"}]
return fail

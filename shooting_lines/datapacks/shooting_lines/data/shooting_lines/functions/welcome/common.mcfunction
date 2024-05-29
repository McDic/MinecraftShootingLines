# This function must ran as individual users.

effect clear @s

scoreboard players set @s welcome -1
title @s title [{"text":"Welcome, ","bold":true,"color":"gray"},{"selector":"@s","bold":true,"color":"gray"}]
title @s subtitle {"text":"Shooting Lines - Made by McDic","italic":true,"color":"gray"}
title @s times 1.5s 4s 1.5s

execute unless score $gamemode settings matches 1 run function shooting_lines:welcome/idle
execute if score $gamemode settings matches 1 run function shooting_lines:welcome/ingame

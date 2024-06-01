# Copied from: https://github.com/McDic/Highliner/blob/master/Highliner/datapacks/highliner/data/highliner/functions/utils/gps.mcfunction
execute store result score @s gps_x run data get entity @s Pos[0] 1
execute store result score @s gps_y run data get entity @s Pos[1] 1
execute store result score @s gps_z run data get entity @s Pos[2] 1

tag @a[team=redteam] add temp_target
tag @a[team=blueteam] add temp_target
tag @a[team=greenteam] add temp_target

execute as @a[tag=temp_target] at @s run function shooting_lines:game/select/raycast/entry {"func": "shooting_lines:game/select/occupy/try"}

tag @a[tag=temp_target] remove temp_target

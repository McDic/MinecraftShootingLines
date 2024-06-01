# This should be the only registered function on #minecraft:tick.

# Add global tick timestamp
scoreboard players add $global_tick variables 1

# Welcome
scoreboard players add @a welcome 0
execute as @a[scores={welcome=0}] at @s run function shooting_lines:welcome/common

# Common effects
effect give @a night_vision infinite 0 true
effect give @a saturation infinite 10 true
effect give @a regeneration infinite 10 true
effect give @a resistance infinite 10 true
scoreboard players add @a sneak_for_slow 0
effect give @a[scores={sneak_for_slow=..0}] speed infinite 15 true
effect clear @a[scores={sneak_for_slow=..0}] slowness
effect give @a[scores={sneak_for_slow=1..},gamemode=adventure] slowness infinite 15 true
effect clear @a[scores={sneak_for_slow=1..},gamemode=adventure] speed
scoreboard players set @a[scores={sneak_for_slow=1..}] sneak_for_slow 0
effect give @a jump_boost infinite 7 true

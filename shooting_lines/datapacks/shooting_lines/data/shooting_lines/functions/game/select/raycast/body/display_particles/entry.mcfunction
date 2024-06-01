data modify storage sl: temp_args prepend value {}

execute if score $raycast_recursion_depth variables >= $raycast_depth_since_phase1b variables run data modify storage sl: temp_args[0].coord set value "~ 2 ~"
execute if score $raycast_recursion_depth variables >= $raycast_depth_since_phase1a variables if score $raycast_depth_since_phase1b variables > $raycast_recursion_depth variables run data modify storage sl: temp_args[0].coord set value "~ ~ ~"

execute if score $current_team variables matches 1 run data modify storage sl: temp_args[0].color set value "[1,0,0]"
execute if score $current_team variables matches 2 run data modify storage sl: temp_args[0].color set value "[0,0,1]"
execute if score $current_team variables matches 3 run data modify storage sl: temp_args[0].color set value "[0,1,0]"
execute if score $current_team variables matches 1 run data modify storage sl: temp_args[0].target set value "@a[team=redteam]"
execute if score $current_team variables matches 2 run data modify storage sl: temp_args[0].target set value "@a[team=blueteam]"
execute if score $current_team variables matches 3 run data modify storage sl: temp_args[0].target set value "@a[team=greenteam]"

execute if data storage sl: temp_args[0].coord if data storage sl: temp_args[0].color if data storage sl: temp_args[0].target run function shooting_lines:game/select/raycast/body/display_particles/raw with storage sl: temp_args[0]
data remove storage sl: temp_args[0]

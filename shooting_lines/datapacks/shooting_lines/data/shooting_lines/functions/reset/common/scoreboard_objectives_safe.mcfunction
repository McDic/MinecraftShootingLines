# setdisplay
scoreboard objectives setdisplay sidebar
scoreboard objectives setdisplay list
scoreboard objectives setdisplay below_name

# Restore objectives
scoreboard objectives remove constants
scoreboard objectives add constants dummy
scoreboard objectives remove literal_numbers
scoreboard objectives add literal_numbers dummy
scoreboard objectives remove welcome
scoreboard objectives add welcome minecraft.custom:leave_game
scoreboard objectives remove settings
scoreboard objectives add settings dummy
scoreboard objectives remove sneak_for_slow
scoreboard objectives add sneak_for_slow minecraft.custom:sneak_time

# Team
team remove spectators
team add spectators {"text":"Spectators","color":"gray","bold":true}
team modify spectators color gray
team modify spectators collisionRule pushOwnTeam
team modify spectators seeFriendlyInvisibles true
team modify spectators friendlyFire false
team modify spectators nametagVisibility hideForOtherTeams

team remove redteam
team add redteam {"text":"Red Player","color":"dark_red","bold":true}
team modify redteam color dark_red
team modify redteam collisionRule never
team modify redteam nametagVisibility always

team remove blueteam
team add blueteam {"text":"Blue Player","color":"aqua","bold":true}
team modify blueteam color aqua
team modify blueteam collisionRule never
team modify blueteam nametagVisibility always

team remove greenteam
team add greenteam {"text":"Green Player","color":"green","bold":true}
team modify greenteam color green
team modify greenteam collisionRule never
team modify greenteam nametagVisibility always

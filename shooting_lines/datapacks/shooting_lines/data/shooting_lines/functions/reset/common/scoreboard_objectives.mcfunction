# setdisplay
scoreboard objectives setdisplay sidebar
scoreboard objectives setdisplay list
scoreboard objectives setdisplay below_name

# Restore objectives
scoreboard objectives remove constants
scoreboard objectives add constants dummy
scoreboard objectives remove literal_numbers
scoreboard objectives add literal_numbers dummy

# imports for random and regular expressions
import random
import re

# Character selection screen
# Opted to make this a function as I reuse it depending on how many players
def character_select():
      print("1. ( ಠ_ಠ) Drake Firefist\n"
            "Special Move: Comet Fireball\n"
            "Deals 15 damage, 2 turns cooldown\n")

      print("2. ( •`⎽´•) Ripper\n"
            "Special Move: Rip\n"
            "Deals 10 damage, then 10 damage next turn, 3 turn cooldown\n")

      print("3. ( -⎚_⎚) The Machine\n"
            "Special Move: Laser Blast\n"
            "Deals 5 damage, and stuns the target, 3 turn cooldown\n")

      print("4. ( :) ) Guy Dudeman\n"
            "Special Move: Weak Punch\n"
            "Deals NO damage (or does it?)\n")

# Function that forces user to select a valid option
# Infinitely reusible provided a selection and list of available options is given
# selection is what the user selected, options is a list including only the options that are valid as provided
def verify_select(selection, options):
      # loops forever
      while 1==1:
            if selection in options:
                  #returns selection if valid, exiting the function and ending the infinite loop
                  return selection
            else:
                  # will tell the player to select a valid option if their selection isnt in the list of valid options provided to the function
                  selection = input("Please select a valid option: ")

# Mode selection menu
print("Welcome to the arena!")
print(" ------------------------- \n"
      "| 1. Player 1 vs Player 2 |\n"
      "| 2. Player 1 vs CPU      |\n"
      " -------------------------")

# Asks for a mode, then verifies the selection based on available options
mode_selected = input("Type number to select a mode: ")
available_options = ["1", "2"]
verified_mode = verify_select(mode_selected, available_options)

# Tracks each character's stats for reference later
character_dictionary = {
      "Drake Firefist": {"SpecialDamage": 15, "Cooldown": 2, "Effect": None, "IconL": "( ಠ_ಠ)", "IconR": "(ಠ_ಠ )"},
      "Ripper": {"SpecialDamage": 10, "Cooldown": 3, "Effect": "Bleed", "IconL": "( •`⎽´•)", "IconR": "(•`⎽´• )"},
      "The Machine": {"SpecialDamage": 5, "Cooldown": 3, "Effect": "Stun", "IconL": "( -⎚_⎚)", "IconR": "(⎚_⎚- )"},
      "Guy Dudeman": {"SpecialDamage": 0, "Cooldown": 0, "Effect": "?", "IconL": "( :) )", "IconR": "( (: )"}
}

# Converts keys in character_dictionary to a list, so the number the player types for character select can be used to index from the list of playable characters
character_list = list(character_dictionary)

# only 4 playable characters, so available options list is 1 to 4
available_options = ["1", "2", "3", "4"]

# if player selected player 1 vs player 2
if mode_selected == "1":
      # running function to display characters
      character_select()

      #letting players choose character, and verifying they inputted a valid string
      playerone_choice = input("Player 1, please select your fighter: ")
      playerone_choice_verified = character_list[int(verify_select(playerone_choice, available_options))-1]

      playertwo_choice = input("Player 2, please select your fighter: ")
      playertwo_choice_verified = character_list[int(verify_select(playertwo_choice, available_options))-1]

# if the player selected player 1 vs CPU
else:
      character_select()
      print("Player, please select your fighter: ")
      playerone_choice = input("Player 1, please select your fighter: ")
      playerone_choice_verified = character_list[int(verify_select(playerone_choice, available_options))-1]

      # Player 2 character is randomly selected for the CPU
      playertwo_choice_verified = character_list[random.randint(0, 3)]

# Tracks player health, character choice, special ability cooldown and any status effects
player_stats = {
      "Player 1": {"HP": 100, "Character": playerone_choice_verified, "Cooldown": 0, "Status": None},
      "Player 2": {"HP": 100, "Character": playertwo_choice_verified, "Cooldown": 0, "Status": None}
}

# available options for players to make on their turn, only 3 so list goes from 1 to 3
# like earlier this is to ensure players don't select something like 4, 10 or even a non-integer as their move choice
available_options = ["1", "2", "3"]

# Pulls icons from the character dictionary, player 1 uses the left side icon and player 2 the right side one
# This ensures each character is facing in the correct direction
player1_icon = character_dictionary[playerone_choice_verified]["IconL"]
player2_icon = character_dictionary[playertwo_choice_verified]["IconR"]

# function for choosing move on your turn
def player_turn_choice(current_player):
      # reduces cooldown value per turn
      if player_stats[current_player]["Cooldown"] > 0:
            player_stats[current_player]["Cooldown"] -= 1

      # stats HUD for each player, displays current HP and other stats
      player1_HUD = re.sub("[{},']", "", str(player_stats["Player 1"]))
      player2_HUD = re.sub("[{},']", "", str(player_stats["Player 2"]))

      # print command for visuals
      print(f"\n\n\n\n\n\n")
      print(f"{player1_HUD} || {player2_HUD}")
      print(f"||_ {player1_icon} _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ {player2_icon} _||")

      # If CPU is player 2, will automatically select their moves randomly from 1 to 3 (or 1 to 2 if special attack is on cooldown)
      if verified_mode == "2" and current_player == "Player 2":

            if player_stats[current_player]["Cooldown"] > 0:
                  attack_choice_verified = str(random.randint(1, 2))
            else:
                  attack_choice_verified = str(random.randint(1, 3))
      else:
            # allows player to select attack, and verifies its a valid selection
            attack_choice = input(f"{current_player} select your move (1. Attack, 2. Recover, 3. Special Attack): ")
            attack_choice_verified = verify_select(attack_choice, available_options)

      # executes status effect
      if player_stats[current_player]["Status"] == "Bleed":
            player_stats[current_player]["HP"] -= 10
            player_stats[current_player]["Status"] = None

      # skips turn if stunned by returning out of the function
      if player_stats[current_player]["Status"] == "Stun":
            player_stats[current_player]["Status"] = None
            return

      # handles 'attack' command
      if attack_choice_verified == "1":
            if current_player == "Player 1":
                  player_stats["Player 2"]["HP"] -= 10
            else:
                  player_stats["Player 1"]["HP"] -= 10

      # handles 'recover' command (recovers random HP between 0 and 15)
      if attack_choice_verified == "2":
            if current_player == "Player 1":
                  player_stats["Player 1"]["HP"] += random.randint(0, 15)
            else:
                  player_stats["Player 2"]["HP"] += random.randint(0, 15)

      # handles 'Special Attack' command
      if attack_choice_verified == "3":
            if current_player == "Player 1":
                  # special attack does nothing if it is still cooling down (cooldown greater than 0)
                  if player_stats["Player 1"]["Cooldown"] == 0:
                        # sets cooldown based on character specific values listed in character dictionary
                        player_stats["Player 1"]["Cooldown"] = character_dictionary[playerone_choice_verified]["Cooldown"]

                        # deals appropriate damage based on character
                        player_stats["Player 2"]["HP"] -= character_dictionary[playerone_choice_verified]["SpecialDamage"]

                        # sets negative status (if any)
                        player_stats["Player 2"]["Status"] = character_dictionary[playerone_choice_verified]["Effect"]
            else:
                  if player_stats["Player 2"]["Cooldown"] == 0:
                        # sets cooldown
                        player_stats["Player 2"]["Cooldown"] = character_dictionary[playertwo_choice_verified]["Cooldown"]

                        # deals appropriate damage based on character
                        player_stats["Player 1"]["HP"] -= character_dictionary[playertwo_choice_verified]["SpecialDamage"]

                        # sets negative status
                        player_stats["Player 1"]["Status"] = character_dictionary[playertwo_choice_verified]["Effect"]

# converts dict keys of players to list of players, then randomises it to determine player order
player_order = list(player_stats)
random.shuffle(player_order)

# this is to track if the game has ended
gameover = False

# will only loop provided the game is not over
while gameover == False:
      for player in player_order:
            # once a players HP drops to 0 or below, they have lost and the game is over
            if player_stats["Player 1"]["HP"] > 0 and player_stats["Player 2"]["HP"] > 0:
                  player_turn_choice(player)
            else:
                  gameover = True

# prints the name of the player who won (the one with remaining HP)
if player_stats["Player 1"]["HP"] > 0:
      print("Player 1 wins!")
else:
      print("Player 2 wins!")

print("Thank you for playing!")
# imports for random and regular expressions
import random
import re
import requests
import json

# Character selection screen
# Opted to make this a function as I reuse it depending on how many players
def character_select(ID_number):
      # get data on all pokemon from API request
      poke_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{ID_number}")

      # returns response as a dictionary
      return poke_data.json()

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

available_options = list(range(1, 151))

# if player selected player 1 vs player 2
if mode_selected == "1":
      #letting players choose pokemon, and verifying they inputted a valid string
      poke_id = input("Player 1, select your Pokemon (gen 1 only): ")
      poke_id_verified = verify_select(int(poke_id), available_options)
      playerone_choice_verified = character_select(poke_id_verified)

      poke_id = input("Player 2, select your Pokemon (gen 1 only): ")
      poke_id_verified = verify_select(int(poke_id), available_options)
      playertwo_choice_verified = character_select(poke_id_verified)

# if the player selected player 1 vs CPU
else:
      poke_id = input("Player 1, select your Pokemon (gen 1 only): ")
      poke_id_verified = verify_select(int(poke_id), available_options)
      playerone_choice_verified = character_select(poke_id_verified)

      # Player 2 pokemon is randomly selected for the CPU
      playertwo_choice_verified = character_select(random.randint(1, 151))

# Tracks player health, character choice, special ability cooldown and any status effects
player_stats = {
      "Player 1": {
            "Name": playerone_choice_verified["forms"][0]["name"],
            "HP": playerone_choice_verified["stats"][0]["base_stat"] * 10,
            "Atk": playerone_choice_verified["stats"][1]["base_stat"],
            "Def": playerone_choice_verified["stats"][2]["base_stat"],
            "Sp.Atk": playerone_choice_verified["stats"][3]["base_stat"],
            "Sp.Def": playerone_choice_verified["stats"][4]["base_stat"],
            "Speed": playerone_choice_verified["stats"][5]["base_stat"]
                   },
      "Player 2": {
            "Name": playertwo_choice_verified["forms"][0]["name"],
            "HP": playertwo_choice_verified["stats"][0]["base_stat"] * 10,
            "Atk": playertwo_choice_verified["stats"][1]["base_stat"],
            "Def": playertwo_choice_verified["stats"][2]["base_stat"],
            "Sp.Atk": playertwo_choice_verified["stats"][3]["base_stat"],
            "Sp.Def": playertwo_choice_verified["stats"][4]["base_stat"],
            "Speed": playertwo_choice_verified["stats"][5]["base_stat"]
      }
}

# available options for players to make on their turn, only 3 so list goes from 1 to 3
# like earlier this is to ensure players don't select something like 4, 10 or even a non-integer as their move choice
available_options = ["1", "2", "3"]

# function for choosing move on your turn
def player_turn_choice(current_player):
      # stats HUD for each player, displays current HP and other stats
      player1_HUD = re.sub("[{},']", "", str(player_stats["Player 1"]))
      player2_HUD = re.sub("[{},']", "", str(player_stats["Player 2"]))

      # print command for visuals
      print(f"\n\n\n\n\n\n")
      print(f"{player1_HUD} || {player2_HUD}")
      print(f"||_ ( o_o) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ (o_o ) _||")

      # If CPU is player 2, will automatically select their moves randomly from 1 to 3 (or 1 to 2 if special attack is on cooldown)
      if verified_mode == "2" and current_player == "Player 2":
            attack_choice_verified = str(random.randint(1, 3))

      else:
            # allows player to select attack, and verifies its a valid selection
            attack_choice = input(f"{current_player} select your move (1. Attack, 2. Special Attack, 3. Recover): ")
            attack_choice_verified = verify_select(attack_choice, available_options)

      # handles 'attack' command
      if attack_choice_verified == "1":
            if current_player == "Player 1":
                  player_stats["Player 2"]["HP"] -= int(round(player_stats["Player 1"]["Atk"] * (1 - (player_stats["Player 2"]["Def"])/255), 0))
            else:
                  player_stats["Player 1"]["HP"] -= int(round(player_stats["Player 2"]["Atk"] * (1 - (player_stats["Player 1"]["Def"])/255), 0))

      # handles 'recover' command (recovers random HP between 0 and 15)
      if attack_choice_verified == "2":
            if current_player == "Player 1":
                  player_stats["Player 2"]["HP"] -= int(round(player_stats["Player 1"]["Sp.Atk"] * (1 - (player_stats["Player 2"]["Sp.Def"])/255), 0))
            else:
                  player_stats["Player 1"]["HP"] -= int(round(player_stats["Player 2"]["Sp.Atk"] * (1 - (player_stats["Player 1"]["Sp.Def"])/255), 0))

      # handles 'Special Attack' command
      if attack_choice_verified == "3":
            if current_player == "Player 1":
                  player_stats["Player 1"]["HP"] += random.randint(0, 15)
            else:
                  player_stats["Player 2"]["HP"] += random.randint(0, 15)

# converts dict keys of players to list of players, then randomises it to determine player order
player_order = list(player_stats)
if player_stats["Player 1"]["Speed"] > player_stats["Player 2"]["Speed"]:
      player_order = ["Player 1", "Player 2"]
else:
      player_order = ["Player 2", "Player 1"]

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
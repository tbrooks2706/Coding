#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

valid_plays = ["Rock", "Paper", "Scissors"]
results_dict = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}
replay = ""

while replay != "quit":
    print("Input 'Rock', 'Paper' or 'Scissors'.")
    player_1 = input("P1 plays: ")
    player_2 = input("P2 plays: ")
    if (player_1 not in valid_plays):
        result = "Incorrect input player 1!"
    elif (player_2 not in valid_plays):
        result = "Incorrect input player 2!"
    elif player_1 == player_2:
        result = "Game drawn."
    else:
        for key, value in results_dict.items():
            if player_1 == key:
                if player_2 == value:
                    result = "Player 1 wins!"
                else:
                    result = "Player 2 wins!"
    print(result)
    replay = input("Type 'quit' to stop: ")
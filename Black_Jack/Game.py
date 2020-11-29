import CardDeck
import Player

def boolean_input(input):
    if (input == 'y'): return True
    else: return False


def play_round(new_deck):

    one_more = True
    sum = 0

    while(one_more):
        current = new_deck.deal()
        sum += CardDeck.values[current.rank]
        print(f"you were dealt {str(current)} and your current score is {sum}")

        if (sum > 21):
            print("BUST!")
            return 0
        if (sum == 21):
            print("BLACK JACK!")
            return sum
        
        one_more = boolean_input(input("would you like one more card? (y for yes)"))

    return sum


def comp_round(new_deck, player_score):

    sum = 0

    while(sum <= player_score):
        current = new_deck.deal()
        sum += CardDeck.values[current.rank]
        print(f"the dealer got {str(current)} and his current score is {sum}")

        if (sum > 21):
            print("BUST!")
            return 'p'
        if (sum == 21):
            print("BLACK JACK!")
            return 'c'



#start of the game
print('Hello and welcome to BLACK JACK!!!')
new_deck = CardDeck.Deck()
new_deck.shuffle()
new_player = Player.Player()
print(str(new_player))
keep_playing = True

#each round
while keep_playing:
    bet = new_player.bet()
    who_won = ''
    player_score = play_round(new_deck)
    
    if (player_score == 0):
        who_won = 'c'
    elif (player_score == 21):
        who_won = 'p'
    else:
        who_won = comp_round(new_deck, player_score)
    
    if (who_won == 'p'):
        new_player.add_funds(bet * 2)
        print(f"You have won the round and earned {bet * 2}$")
    
    if (who_won == 'c'):
        print(f"You have lost this round")
        if (new_player.bank == 0):
            print ("You went broke, better luck next time")
            break

    keep_playing = boolean_input(input("would you like to play another round? (y for yes)"))

if (new_player.bank != 0):
    print(f"you finished the game with {new_player.bank}$, have a nice day!")
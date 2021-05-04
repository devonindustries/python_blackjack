import random
import math

nums = ['A', 'K', 'Q', 'J'] + [str(x) for x in range(2, 11)]
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

def generate_deck():
    deck = []

    for x in suits:
        for y in nums:
            deck.append((y, x))
            
    return deck
    
def get_value(hand):
    total = 0
    aces = 0
    
    for x in hand:
        if x[0] == 'A':
            aces += 1
        elif x[0] in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(x[0])
            
    for ace in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
            
    return total
    
def play_round(player_tokens):
    
    # Generate a deck
    deck = generate_deck()
    hand = []
    dealer_hand = []
    
    # Get the user bet
    bet = 0
    while bet < 2:
        bet = int(input('Place a bet (minimum 2 chips): '))
        
    # Decrement the bet from the players tokens
    player_tokens -= bet
    
    # Shuffle the order of the deck
    random.shuffle(deck)
    
    # Deal two cards
    hand.append(deck.pop())
    hand.append(deck.pop())
    
    # Deal two cards to the dealer
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # Show one of the dealer's cards to the player
    print(f'Dealer has {dealer_hand[0][0]} of {dealer_hand[0][1]}.')
    
    # Set the playing flag
    playing = True
    
    # Start playing
    while playing:
        
        # Give the user their stats
        print(hand, get_value(hand))
        
        # Get their input if the user value is not already too high
        user_input = input('Hit (H) / Stand (S): ') if get_value(hand) < 21 else 's'

        # Make the input lower case
        user_input = user_input.lower()

        # See if the user hit
        if user_input == 'h': hand.append(deck.pop())

        # Get the value of the users hand
        player_value = get_value(hand)

        # Check that the user has lost or decided to stand
        if user_input == 's' or player_value > 21:

            # If the user stands, or the user value is too high, evaluate the position
            while get_value(dealer_hand) <= 17:
                dealer_hand.append(deck.pop())
            
            # Store the dealer value
            dealer_value = get_value(dealer_hand)
            
            # Print the final score
            print('Player final hand:')
            print(hand, player_value)

            # Check the outcome
            if player_value > 21 and dealer_value > 21:
                
                # Nobody wins
                print(f'Nobody won that round. Dealer went bust with {dealer_value}.')
                player_tokens += bet
            
            elif player_value == 21:

                # The player got blackjack
                print(f'Blackjack!')
                player_tokens += math.floor(bet * 2)
                
            elif player_value > 21:
                
                # The player went bust
                print(f'You went bust! Dealer had {dealer_value}.')
                
            elif dealer_value > 21:

                # The dealer went bust
                print(f'You won this round! Dealer went bust with {dealer_value}')
                player_tokens += math.floor(bet * 1.5)
            
            elif dealer_value >= player_value:

                # The dealer won
                print(f'Dealer won this round with {dealer_value}. Better luck next time!')
                
            elif player_value > dealer_value:
                
                # You won
                print(f'You beat the dealer. Dealer had {dealer_value}.')
                player_tokens += math.floor(bet * 1.5)
                            
            playing = False

    return player_tokens
    
def play():
    
    # Give the player some tokens
    player_tokens = 50
    
    # Print the banner
    print('[}-----------------{]')
    print('| B L A C K J A C K |')
    print('[}-----------------{]')
    print('| Welcome to Python |')
    print('|     Blackjack!    |')
    print('[}-----------------{]')
    print('|   Please gamble   |')
    print('|  responsibly, and |')
    print('|     have fun!     |')
    print('[}-----------------{]')
    
    playing = True
    
    prompt = 'Begin? (Y | N)'
    
    while playing:
        
        # Print the number of tokens
        print(f'Tokens: {player_tokens}')
        
        # Get the player input
        player_input = input(prompt).lower()
        
        # Play again and store the tokens if the user wishes to play
        if player_input == 'y':
            
            # Play a round
            player_tokens = play_round(player_tokens)
            
            # Reset the prompt
            prompt = 'Play again? (Y | N)'
            
        elif player_input == 'n':
            playing = False
        else:
            print('Did not recognise input. Please try again!')
    
    # Thank the player for playing if they choose to quit
    print('Thank you for playing!')

if __name__ == '__main__':
    play()
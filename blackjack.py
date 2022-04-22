'''Driver for playing Blackjack.'''
from random import randint
from deck import card_name, card_value, end_turn_status, end_game_status

def draw_card():
    '''Picks a random card, prints out "Drew a x",
    and returns the value of the card.
    '''
    card_rank = randint(1, 13)
    print("Drew a " + card_name(card_rank))
    return card_value(card_rank)

def print_header(message):
    '''Prints the given message with dashes above and below it.'''
    print('-----------')
    print(message)
    print('-----------')

def main():
    '''Runs a full game of blackjack.'''
    # Play the user's turn.
    # The user can choose to hit or stand, as long
    # as they haven't busted (gone over 21).
    print_header('YOUR TURN')
    user_hand = draw_card() + draw_card()
    will_hit = 'y'
    while user_hand < 21 and will_hit == 'y':
        will_hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ')
        if will_hit == 'y':
            user_hand = user_hand + draw_card()

    print("Final hand: " + str(user_hand) + ".")
    status = end_turn_status(user_hand)
    if status != '':
        print(status)

    # Play the dealer's turn.
    # The dealer continues drawing cards until their
    # hand total reaches 17.
    print_header('DEALER TURN')
    dealer_hand = draw_card() + draw_card()  # dealer's turn
    while dealer_hand <= 17:
        print("Dealer has " + str(dealer_hand) + ".")
        dealer_hand = dealer_hand + draw_card()

    print("Final hand: " + str(dealer_hand) + ".")
    status = end_turn_status(dealer_hand)
    if status != '':
        print(status)

    # Determine which player won.
    print_header('GAME RESULT')
    print(end_game_status(user_hand, dealer_hand))

if __name__ == "__main__":
    main()

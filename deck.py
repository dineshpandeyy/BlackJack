'''Helper functions for playing Blackjack.'''

def card_name(card_rank):
    '''Returns the given card's official name.

    Args:
        card_rank: The numeric representation of a card.

    Returns:
        A string representing the official name of the given card.

    Examples:
        card_name(2) returns
        "2"

        card_name(11) returns
        "Jack"
    '''
    if card_rank == 1:
        return 'Ace'
    if card_rank == 11:
        return 'Jack'
    if card_rank == 12:
        return 'Queen'
    if card_rank == 13:
        return 'King'
    # All other cards are named by their rank.
    return str(card_rank)


def card_value(card_rank):
    '''Returns the given card's value.

    Args:
        card_rank: The numeric representation of a card.

    Returns:
        Face value of the given card as an int.
        The face value of a card is the same as numeric value,
        except for Ace, Jack, Queen, and King.

    Examples:
        card_value() returns 11 for Ace
        card_value() returns 4 for 4
        card_value() returns 10 for face cards
    '''
    if card_rank >= 11 and card_rank <= 13:
        # Jacks, Queens, and Kings are worth 10.
        return 10
    if card_rank == 1:
        # Aces are worth 11.
        return 11
    # All other cards are worth the same as
    # their rank.
    return card_rank

def end_turn_status(hand):
    '''Returns the status at the end of a player's turn.

    Args:
        hand: The sum of of all the cards in the hand.

    Returns:
        '', 'BLACKJACK!', or 'BUST.', depending on the value of the given hand.

    Examples:
        if hand is less than 21:
        ''

        if hand is equal to 21.
        'BLACKJACK!'

        if hand is greater than 21:
        'BUST.'
    '''
    if hand == 21:
        return 'BLACKJACK!'
    if hand > 21:
        return 'BUST.'
    return ''

def end_game_status(user_hand, dealer_hand):
    '''Prints the winner based on the final hands.

    Args:
        user_hand: The sum of all the cards in the user's hand.
        dealer_hand: The sum of all the cards in the dealer's hand.

    Returns:
        'You win!', 'Dealer wins!', or 'Tie.',
        depending on the values of the given hands.

    Examples:
        if user_hand beats dealer_hand:
        'You win!'

        if dealer_hand beats user_hand:
        'Dealer wins!'

        if user_hand and dealer_hand are tied:
        'Tie.'
    '''
    if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
        return 'You win!'
    if dealer_hand <= 21 and (dealer_hand > user_hand or user_hand > 21):
        return 'Dealer wins!'
    return 'Tie.'

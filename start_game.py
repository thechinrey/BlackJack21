import random

# Create a standard deck of cards
def create_deck():
    deck = []
    # Numbers 2-10 (4 of each)
    for card in range(2, 11):
        deck.extend([card] * 4)
    # Face cards and Aces (4 of each)
    deck.extend(["J", "Q", "K", "A"] * 4)
    return deck

# Determine the numeric value of a card
def card_value(card):
    if isinstance(card, int):
        return card
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        return 11  # Adjust later if needed
    return 0

# Calculate the total value of a hand, adjusting for Aces
def calculate_hand_value(hand):
    value = sum(card_value(card) for card in hand)
    aces = hand.count("A")
    # Adjust Aces from 11 to 1 if we're busting
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Play one round of blackjack with the bot using basic strategy
def play_blackjack_bot():
    deck = create_deck()
    random.shuffle(deck)
    
    # Initial deal: two cards each
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("Dealer shows:", dealer_hand[0])
    print("Player hand:", player_hand, "Value:", calculate_hand_value(player_hand))
    
    # Bot's strategy: hit until the hand's value is at least 17
    while calculate_hand_value(player_hand) < 17:
        card = deck.pop()
        player_hand.append(card)
        print("Bot hits and gets:", card)
        current_value = calculate_hand_value(player_hand)
        print("Player hand now:", player_hand, "Value:", current_value)
        if current_value > 21:
            print("Bot busted! Damn, better luck next time.")
            return False  # Bot loses
    
    print("Bot stands with value:", calculate_hand_value(player_hand))
    
    # Dealer's turn: dealer hits until reaching at least 17
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)
    
    print("Dealer hand:", dealer_hand, "Value:", dealer_value)
    
    # Determine the outcome
    if dealer_value > 21:
        print("Dealer busted! Bot wins.")
        return True
    elif player_value > dealer_value:
        print("Bot wins!")
        return True
    elif player_value == dealer_value:
        print("It's a push—a tie.")
        return None
    else:
        print("Bot loses.")
        return False

if __name__ == "__main__":
    play_blackjack_bot()

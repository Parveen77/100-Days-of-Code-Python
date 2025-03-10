import random
#from replit import clear


def deal_card():
    '''Gives a random card'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(hands):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(hands) == 21 and len(hands)==2:
        return 0
    elif 11 in hands and sum(hands) > 21:
        hands.remove(11)
        hands.append(1)
    return sum(hands)

def compare_score(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    
    dealer_card = []
    player_card = []
    for _ in range(2):
        dealer_card.append(deal_card())
        player_card.append(deal_card())
    print(f"Your cards are {player_card}")
    print(f"Dealer's first card is {dealer_card[0]}")

    game_over = False

    while not game_over:
        dealer_score = calculate_score(dealer_card)
        player_score = calculate_score(player_card)
        print(f"Your cards are {player_card} and your score is {player_score}")
        print(f"Dealer's first card is {dealer_card[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            next_card  = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if next_card == "y":
                player_card.append(deal_card())
            else:
                game_over = True
        
        while dealer_score != 0 and dealer_score < 17:
            dealer_card.append(deal_card())
            dealer_score = calculate_score(dealer_card)
        
        
        
    print(f"   Your final hand: {player_card}, final score: {player_score}")
    print(f"   Computer's final hand: {dealer_card}, final score: {dealer_score}")
    print(compare_score(dealer_score, player_score))
    
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()
        
play_game()
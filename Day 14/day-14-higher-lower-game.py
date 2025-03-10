import random
from game_data import data, logo, vs

print(logo)
score = 0
game_over = False

def printable_form(account):
    '''return the account in a printable format'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_follower_count, b_follower_count):
    """Checks followers against user's guess and returns True if they got it right.
        Or False if they got it wrong."""
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'
    
account_b = random.choice(data)

while not game_over:
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)
        
    print(f"Compare A: {printable_form(account_a)}")
    print(vs)
    print(f"Against B: {printable_form(account_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    if check_answer(guess,a_follower_count,b_follower_count):
        score += 1
        print(f"You won. Your score is {score}")
    else: 
        game_over = True
        print(f"you lost. Your final score is {score}")
        
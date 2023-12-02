import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

while(True):
    play =  input('''Do you want to play a Game of BlackJack? type 'y' or 'n''')
    if play=='n':
        break
    print(chr(27) + "[2J")
    print(logo)

    my_cards=[]
    score = 0
    first = random.choice(cards)
    second = random.choice(cards)
    if first==11 and second == 11:
        first=2
    my_cards = [first,second]
    score = first+second

    dealer_cards=[]
    dealer_score = 0
    dealer = random.choice(cards)
    dealer_score += dealer
    dealer_cards.append(dealer)

    print(f'Computer first card: {dealer_score}')
    print(f'your cards : {my_cards}, current score: {score}')
    while(True):
        hit = input('''Type 'y' to get another card ,type 'n' to pass ''') 
        if hit=='y':
            choice = random.choice(cards)
            score+=choice
            if score>21 and choice==11:
                choice=1
                score-=10
            my_cards.append(choice)
            print(f'your cards : {my_cards}, current score: {score}')
            print(f'Computer first card: {dealer_score}')
            if score>=21 :
                break
        else:
            break
    
    print(f'your final Hand : {my_cards}, Final score: {score}')
    while(True):
        dealer = random.choice(cards)
        dealer_score += dealer
        if dealer_score>21 and dealer==11:
            dealer = 1
            dealer_score-=10
        
        dealer_cards.append(dealer)

        if dealer_score>=17:
            break

    print(f'Computers final Hand : {dealer_cards}, Final score: {dealer_score}')
    
    if score>21:
        print('You went over.... You Lose')
    elif score<dealer_score:
        print('Computer has the better score.. You Lose')
        
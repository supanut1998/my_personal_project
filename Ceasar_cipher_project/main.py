from art import logo
from material import alphabet, caesar

start_over = True
print(logo)

while start_over : 
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    
    
    
    caesar(start_text=text, shift_amount=shift,  cipher_direction=direction)
    check = input("do you to start over again? : Type 'yes' or 'no'\n")
    if check.lower() == "yes" :
        start_over = True 
    elif check.lower() == "no" : 
        start_over = False
    else : 
        print("stop programming error!")
        break
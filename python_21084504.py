import random
#Instructions to play the game
def instruction():
    print("                               HOW TO PLAY ?                                         ")
    print("-------------------------------------------------------------------------------------")
    print("|                                                                                   |")
    print("|Try to guess the random sequence of fruits to win the game and become a mastermind.|")
    print("|The sequence consists of 4 of the following 8 fruits:                              |")
    print("|APPLE  BANANA   ORANGE   MANGO   KIWI   GRAPES   PEAR  GUAVA                       |")
    print("|Enter the fruit names in one line with space in between.                           |")
    print("|Enter 3 to quit game halfway.                                                      |")
    print("|Name of the fruit can be repeated.                                                 |")
    print("|Hints will be given to help you guess the correct sequence.                        |")
    print("|   BULL: Number of correct fruits in the correct position                          |")
    print("|   COW: Number of correct fruits in the wrong position                             |")
    print("|                                                                                   |")
    print("-------------------------------------------------------------------------------------")

 #creating button that will always take back to menu
    x = input("Press any button to go back to menu: ")
#creating menu    
def menu():
    print("          Press 1 to START the game                                                ")
    print("          Press 2 to get INSTRUCTIONS on how to play the game                      ")
    print("          Press 3 to QUIT game halfway                                             ")
#Creating list of fruits
def game():
    fruits=["apple","banana","orange","mango","kiwi","grapes","pear","guava"]
    
#generating random code   
    computer_fruits=random.choices(fruits, weights=None,cum_weights=None, k=4)
    def checker(computer,user):
        bull=0
        cow=0
        checked=["n","n","n","n"]
        for i in range (4):
            for j in range(4):
                if  user[i]==computer[j]:
                    if checked[j]=="n":
 
                        if i==j:
                            bull+=1
                            checked[j]="b"                       
                        else:
                            cow+=1
                            checked[j]="c"
                    elif checked[j]=="c" : 
                
                        if i==j:
                            bull+=1 
                            cow-=1
                            checked[j]="b" 
                    else:
                        pass

        return cow,bull          
                            
    no_attempts=10
    while no_attempts>0:
        print("You have " + str(no_attempts)+ " attempts left!!")
        while True:
            guess=input("Enter your guess here:").split()
            if guess[0]=="3":
                quit()

            guess_len = len(guess)
            if guess_len!=4:
                print("Error please enter 4 fruits")
            else:
                break
        cow,bull=checker(computer_fruits,guess)
        print("number of cows: ",str(cow),", number of bulls: ",str(bull))
#creating winning condition        
        if bull == 4:
            print("Congrats,You Win!!!!!!!!!!!!")
            print("It took you ",str(11-no_attempts)," guesses.")
            break            

        no_attempts -= 1
#creating losing condition
    if no_attempts==0:
        print("You lose :( ")
        print("the correct answer was:  ")
        print(computer_fruits)
        yesno=input("Do you want to try playing again?  y/n:  ")
        if yesno=="y":
            game()
            

#taking user input for menu 
def user_ip():
    user_input= (input("Enter a number: "))
    if user_input == "1" :
        game()
    elif user_input == "2" : 
        instruction()

    elif user_input == "3" : 
        quit()

    else: 
        print("Invalid entry !!!!! Enter 1,2 or 3 \n")
        
        user_ip() 


while True :
    menu()
    user_ip()
       




     

   
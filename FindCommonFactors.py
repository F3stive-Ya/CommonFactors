##Purpose: collect two positive integers, find common factors, ask to play again
# Description: Collects two positive integers from the user, finds common factors they share, and asks to play again.
# Created and commented by Shane Borges (F3stive-Ya)

while True:
    finalstr = ""
    num_factors = 0
    
    # Logic deciding if inputted numbers are positive and not equal to zero
    int_1 = int(input("Please enter positive integer one: "))
    while not int_1 > 0:
        print("Provided integer is not positive.")
        int_1 = int(input("Please enter positive integer one: "))
    int_2 = int(input("Please enter positive integer two: "))
    while not int_2 > 0:
        print("Provided integer is not positive.")
        int_2 = int(input("Please enter positive integer two: "))
    
    # Handles logic deciding which number is greater than the other or equals
    if int_1 and int_2 > 0:
        if (int_1 > int_2):
            print(f"{int_1} is greater than {int_2}")
        elif (int_2 > int_1):
            print(f"{int_1} is less than {int_2}")
        else:
            print(f"{int_1} and {int_2} are equal")

    #Loops through integers and checks for factors before adding them to a string.
    for x in range(1,65):
        if (int_1 % x == 0 and int_2 % x == 0):
            finalstr += str(x); finalstr += " "
        

    print(f'The common factors between {int_1} and {int_2} are: {finalstr} ')
   
    
    # Logic for the player ending the game or restarting
    end_loop = True

    while end_loop == True:

        is_playing = input("Do you want to play again? (Y/N or y/n) ")
        
        if is_playing != "y" and is_playing != "Y" and \
             is_playing != "N" and is_playing != 'n':
            print("Error: Options are (Y/N and y/n)")
        
        elif is_playing != "n" and is_playing != "N":
            end_loop = False

        elif is_playing != "y" and is_playing != "Y":
            exit()
    
    


        

   
    



    
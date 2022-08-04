
def name():
    play_again = True
    while play_again:
        name = input("Hello what is your name?")
        x = input("hello " + name + " do you have the faint of heart?:Y or N")
        game_running = True
        while game_running == True:
            if (x == "Y"):
                print("then get out of here")
                game_running = False
            else:
                print("okay then lets proceed.....")
                
    #intro^
                print("You were driving to work because your coworker called out \nyou pull into the  gas station that's taken the last year of life away from you, but there is a troubling \n decision ")
                y = input("do you park in front of the store, or do you park in the back? \n:front or back")
                if y == "back":
                    print("\nyou chose to park in the back of the store, away from all the customers and away from all the cars")
                if y == "front":
                    print("\nyou being lazy, decided to park in thr front of the store, you nearly swipe another car while parking")
                print("You walk into the station and clock in, not in a hurry to start the night shift \nThe manager says: make sure to lock the store when your shifts over, take it easy "+name+"\n")
                #if y != "back" or "front":
                print("\n\ntime: 10:30\n no one came into the store till an hour later\n")
                print(name + "\n suddenly woke up as they heard their name being called \n STRANGER: can I get 20 on pump 3?\n")
                print("\n as " +name +" looks up, they see a tall man towering over them \n StRANGER:also can u ring this up for me?\n you look down to see a beer in their hand\n ")        
                
                print("\nas you ring them out, they ask a single question \n OPTIONS:Y or N")
                z = input("\n STRANGER: are you alone?")
                if z == "Y":
                    print("\n thats nice to know, hmm")
                if z == "N":
                    print("oh, dam")

                print("\n the dude leaves, as you watch him fill up his tank and leave, you decide to start sweeping the floor\n")
                print("\nyou sweep the whole store in an hour","\n time:11:30\n")
                print("\n" + name + ":only 30 minutes till i get to clock out, night shift my ass I'm closing early\n")
                print("\n")
                print("\n **CRASHHH**")
                a = input("sounds like that came from the storage room, Should I go check? yes or no")
                
            
                if a == "yes":
                    print("you go to the storage room to see the back door of the store wide open,\n you take two steps before a masked man lunges at you")
                    print("YOUR DEAD:")
                elif a =="no":
                    print("\nyou shut the store down at 11:40 not wanting to be there any longer \n ")
                    print("\n")
                    print("\nyou walk to the " + y +" of the store,\n noticing that the back door was open, and a shadowy figure crouching by the door\n")
                    print("\nthank god i didn't check the back you murmur as you drive away")
                    print("END")
                
                break
        ask = input("do you want to play again Y or N")
        if ask == "Y":
            play_again = True
        elif ask =="N":
            play_again = False











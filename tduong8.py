#Timothy Duong
#CTC 389 Lab 8

def main_menu():
    name = input("Please enter your name: ")
    print("Hello", name, "it's morning and you have just woken up. What do you do?")
    print("1. Press the snooze button on your alarm")
    print("2. Get ready to go to work")
    print("3. Call in sick")
    return name

def first_decision():
    choice = int(input("What do you choose? "))
    if choice == 1:
        print("You woke up late again! This was the last straw. You got fired from work. Restart the game.")
        return "restart"
    elif choice == 2:
        print("You brush your teeth, shower, and get dressed. Time to go to work!")
        return "continue"
    elif choice == 3:
        print("Oops, it turns out that you don't have sick days left. Restart the game.")
        return "restart"

def second_decision(name):
    print("How will you go to work today,", name)
    print("1. Ride your bike to work")
    print("2. Take the bus to work")
    print("3. Drive to work")
    choice = int(input("What do you choose? "))
    if choice == 1:
        print("It took too long to ride to work and you were late again! You got fired. Restart the game.")
        return "restart"
    elif choice == 2:
        print("There is an ongoing strike and the bus got delayed. You got fired from work for being late. Restart the game.")
        return "restart"
    elif choice == 3:
        print("You got to work just on time!")
        return "continue"

def third_decision(name):
    print("You are now at work. What do you do next,", name)
    print("1. Go to your classroom")
    print("2. Go make copies")
    print("3. Chat with a coworker")
    choice = int(input("What do you choose? "))
    if choice == 1:
        print("You got to your classroom right before the bell rang!")
        return "continue"
    elif choice == 2:
        print("The copy machine jammed, and caused you go be late. You got fired. Restart the game.")
        return "restart"
    elif choice == 3:
        print("Your coworker spent too much time talking and now you're late and got fired. Restart the game.")
        return "restart"

def fourth_decision():
    print("You are now in your classroom, and you realize you forgot to plan for today's lessons. What do you do?")
    print("1. Play a movie and give the students a free day")
    print("2. Make up a lesson on the spot")
    print("3. Use last year's lesson")
    choice = int(input("What do you choose? "))
    if choice == 1:
        print("Later, one of your students' parents filed a complaint. You got fired. Restart the game.")
        return "restart"
    elif choice == 2:
        print("Unfortunately, an administrator decided to evaluate your lesson today. You got fired. Restart.")
        return "restart"
    elif choice == 3:
        print("The lesson went fine though could have been better.")
        return "continue"

def fifth_decision(name):
    print("It is now lunchtime, and you realized you forgot to bring your lunch. What do you do next,", name)
    print("1. Buy lunch from the cafeteria")
    print("2. Drive to Chipotle to buy some food")
    print("3. Decide to not eat anything and try to make it to the end of the day")
    choice = int(input("What do you choose? "))
    if choice == 1:
        print("It's a little awkward buying lunch with the students but you're not hungry anymore.")
        return "continue"
    elif choice == 2:
        print("You didn't make it back on time. You got fired. Restart the game.")
        return "restart"
    elif choice == 3:
        print("You got too hungry to teach effectively during an important evaluation. You got fired. Restart.")
        return "restart"

def ending(name):
    print("Congratulations", name, "you made it through the day without getting fired! You won the game!")


play_again = "yes"
while play_again == "yes":
    name = main_menu()
    first_result = first_decision()
    if first_result != "restart":
        second_result = second_decision(name)
        if second_result != "restart":
            third_result = third_decision(name)
            if third_result != "restart":
                fourth_result = fourth_decision()
                if fourth_result != "restart":
                    fifth_result = fifth_decision(name)
                    if fifth_result != "restart":
                        ending(name)

    play_again = input("Would you like to play again? ")

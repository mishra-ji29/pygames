from random import randint


print("this is a guess game \nin which you have to guess the number in 5 chances.")
print("You have 5 chances\n")
a = randint(0, 100)
gusses = 1
while gusses <= 5:
    b = int(input("Guess the number:\n"))
    if a < b:
        print("You should try smaller number\n")

    elif a > b:
        print("you should try grater number\n")

    elif a == b:
        print("You  did it\n")
        print("you took", gusses, "gusses to complete")
        break

    print("You are left with", 5 - gusses, "gusses\n")
    gusses = gusses + 1

    if gusses > 5:
        print("Game over")
        print(f"The number was {a}")
        break

    # again = input(print("DO you want to play again?\n"))
    #
    # if again == "yes":
    #     continue
    #
    # else:
    #     print("Thank you")
    #     break

import random


def main():
    # creates a variable random_numb from 0-9
    random_numb = random.randint(0, 9)

    # asks the user to guess a number between 1 and 10
    user_guess = int((input("guess a number between 0 and 9 :")))

    # confirm if users guess is correct
    if user_guess == random_numb:
        print("you got it right")
    # If users guess is wrong display
    else:
        print("sorry wrong guess the real number was {}".format(random_numb))


if __name__ == "__main__":
    main()

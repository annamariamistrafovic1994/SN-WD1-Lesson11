import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                best_score = int(score_file.write())

        print("Congrats! it's number " +str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct, try again with a smaller number.")
    elif guess < secret:
        print("Your guess is not correct, try again with a bigger number.")


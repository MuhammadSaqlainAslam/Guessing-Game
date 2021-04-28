# Building a Guessing Game
secret_word = "Hello"
guess = ""
guess_count = 0
guess_limit = len(secret_word) - 1
out_of_guesses = False
hint = secret_word

while guess != secret_word and not (out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        print("Hint: {}".format(hint[0:guess_count]))
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE")
else:
    print("Hey: You win!")
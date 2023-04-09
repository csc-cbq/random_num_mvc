import random

class GuessingGameModel:
    def __init__(self):
        self.number = None
        self.guesses = 0

    def start_game(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def guess_number(self, guess):
        self.guesses += 1
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "low"
        else:
            return "high"

    def get_guess_count(self):
        return self.guesses

class GuessingGameView:
    def display_welcome(self):
        print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100.")

    def get_guess(self):
        return int(input("Enter your guess: "))

    def display_guess_result(self, result):
        if result == "correct":
            print("You guessed it! Congratulations!")
        elif result == "low":
            print("Your guess is too low. Try again.")
        elif result == "high":
            print("Your guess is too high. Try again.")

    def display_guess_count(self, count):
        print(f"You made {count} guesses.")

class GuessingGameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_game(self):
        self.view.display_welcome()
        self.model.start_game()

        while True:
            guess = self.view.get_guess()
            result = self.model.guess_number(guess)
            self.view.display_guess_result(result)

            if result == "correct":
                count = self.model.get_guess_count()
                self.view.display_guess_count(count)
                break

# Tạo một đối tượng GuessingGameModel
model = GuessingGameModel()

# Tạo một đối tượng GuessingGameView
view = GuessingGameView()

# Tạo một đối tượng GuessingGameController và kết nối Model và View
controller = GuessingGameController(model, view)

# Chơi trò chơi đoán số
controller.play_game()

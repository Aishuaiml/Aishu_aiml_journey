import random

print("🎯 Number Guessing Game - Day 04 by Aishu")
print("I'm thinking of a number between 1 and 50!")

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Un guess enna da? : "))
    attempts += 1

    if guess < secret_number:
        print("Too low da! Konjam perusa try pannu 👆")
    elif guess > secret_number:
        print("Too high da! Konjam chinna number try pannu 👇")
    else:
        print(f"DEI AISHU CORRECT DA! 🎉 {attempts} attempts la kandupuditta!")
        print("Nee vera level da!")
        break
from random import choice

questions = [
    "What is the color of the sky?: ",
    "What is you favorite song?: ",
    "How are you?: ",
    "Who is your dady?: ",
    "Do you want to eat?: "
]
question = choice(questions)
answer = input(question).lower().strip()
while answer != "because":
    answer = input("Why?").strip().lower()

print("Oh.... OK")
import random 

dice_bot = random.randint(1,6)
dice_you = random.randint(1,6)

print(f"You rolled a {dice_you} \nwhile the bot rolled a {dice_bot}!")
if dice_you > dice_bot:
    print("You win!")
elif dice_you < dice_bot:
    print("You lose")
else:
  print("You tied")
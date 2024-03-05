import random
import time

done = False
version = 1.0
# These will change throughout game
distance_from_oregon = 1500
days = 0
rest = 10
r_days = 0
disease_risk = 0
disease_effect = 0
disease_infect = random.randrange(15, 25)
dysentery_heal = random.randrange(5, 10)

# These are supply variables
money = 1500
oxen = 0
food = 0
clothes = 0
ammo = 0
spare_wheel = 0
spare_axles = 0

def shop_open():
    # Global Variables
    global oxen
    global food
    global clothes
    global ammo
    global money
    global spare_wheel
    global spare_axles
    global ox_final_money
    global food_final_money
    global clothes_final_money
    global bullet_final_money
    global spare_final_money

    while 1 == 1:
        # This is the prices and how much money you have
        print(f"Hello {p_name}! I have many things you may need in your journey to Oregon. Come take a look")
        print(f"you have ${money}")
        print("1.Oxen           $30")
        print("2.food           $1")
        print("3.clothes         $10")
        print("4.Ammo           $1")
        print("5.spare parts    $10")
        print("6.Leave shop")
        shop_action = input("")

        if shop_action == "1":
            # Oxen
            ox_buy = int(input("How many oxen would you like? "))
            ox_final_money = ox_buy * 30
            money = money - ox_final_money
            oxen = oxen + ox_buy
            time.sleep(1)

        elif shop_action == "2":
            # Food
            food_buy = int(input("How many pounds would you like? "))
            food_final_money = food_buy
            money = money - food_final_money
            food = food + food_buy
            time.sleep(1)

        elif shop_action == "3":
            # Clothes
            clothes_buy = int(input("How many sets would you like? "))
            clothes_final_money = clothes_buy * 10
            money = money - clothes_final_money
            clothes = clothes + clothes_buy
            time.sleep(1)

        elif shop_action == "4":
            # Bullets
            bullet_buy = int(input("How many boxes would you like? (1 box is 10 bullets)"))
            bullet_final_money = bullet_buy * 1
            bullet_amt = bullet_buy * 10
            money = money - bullet_final_money
            ammo = ammo + bullet_amt
            time.sleep(1)

        elif shop_action == "5":
            # Spare parts
            spare_buy = int(input("How many spare parts would you like? "))
            spare_final_money = spare_buy * 10
            money = money - spare_final_money
            spare_axles = spare_axles + spare_buy
            spare_wheel = spare_wheel + spare_buy
            time.sleep(1)

        elif shop_action == "6":
            print(f"you now have {money} dollars left")
            print(f"Thanks for stopping in, {p_name}")
            time.sleep(1)
            break
        if money < 0 or money == 0:
            print("You ran out of money")
            done = True
            break

def check_status():

    print(f"you have {distance_from_oregon} miles to go")
    time.sleep(1)

    print(f"you have {food} pounds of food left")
    time.sleep(1)

    print(f"you have {oxen} oxen")
    time.sleep(1)

    print(f"you have {ammo} rounds of ammo left")
    time.sleep(1)

    print(f"you have {spare_axles} axles left")
    time.sleep(1)

    print(f"you have {spare_wheel} wheels left\n")
    time.sleep(1)

def credits():
  # These are the credits
  print(f"\nMade by Matthew Brittain\nlast update on 03/05/2024, Version {version}\nIspired by The Oregon Trail game\nMade with 231 lines of code!")
  time.sleep(1)
  print("\n\nBeta testers:\nSimon McCann\nOdin Kelly\nVincent Knowlmayer\nDymion Cherry\nPreston Bloodhart")
  print("\nSpecial thanks to Ryan Brill")
  time.sleep(1)
  print("Thank you for Playing the Oregon Trail Game")

# Intro
p_name = input("What is your name? ")
print(f"Welcome to the Oregon Trail Game Version {version} made in python, {p_name}! Use number keys")
print("to take action. You will need to buy supplies. You are going")
print("from Missouri to Oregon which is 1,500 miles Good luck.")
time.sleep(1)
input("\nWhere are you from?\n1.Boston\n2.Ohio\n3.Illinois\n")
time.sleep(1)
shop_open()

# This is the main code for going along the trail
if money < 0 or money == 0:
    print("You ran out of money")
    done = True

while done == False and distance_from_oregon >= 0:
    print("What would you like to do?")
    print("1.Continue traveling")
    print("2.Stop and Rest")
    print("3.Hunt for food")
    print("4.Check Status")
    print("5.Quit")
    action = input("")

    if action == "1":
      if rest > 0:
        if oxen > 0:
            distance_from_oregon = distance_from_oregon - random.randrange(10, 15)
            print(f"You have {distance_from_oregon} miles left")
            time.sleep(1)
        else:
            print("You don't have any oxen")
            time.sleep(1)
            shop_open()
      else:
        print("You need to rest in order to continue")
        time.sleep(1)

    elif action == "2":
        print("How many days would you like to rest for?")
        r_days = int(input(""))
        rest = rest + r_days
        days = days + r_days
        time.sleep(1)
        if r_days > 5:
          print("plase do not rest for more than 5 days at a time")
        print(f"you rested for {r_days} days.")
        rest = rest + r_days
        time.sleep(1)

    elif action == "3":
      if ammo > 0:
          hunt_food = random.randrange(51, 101)
          print(f"you were able to get {hunt_food} pounds of food!")
          ammo = ammo - 1
          time.sleep(1)
      else:
        print("You don't have any bullets to hunt")
        time.sleep(1)

    elif action == "4":
        time.sleep(1)
        check_status()

    elif action == "5":
        done = True

    if distance_from_oregon <= 0:
        time.sleep(1)
        done = True

    # This triggers at the end of each day
    days = days + 1
    rest = rest - 1
    time.sleep(1)
    if rest == 0:
        print("You are tired, you may want to rest")
    disease_risk = disease_risk + 1
    if disease_risk == disease_infect:
        print("You have dysentery")
        if rest > 10:
            print("You were well rested and fought it off")
        if rest < 9:
            print(f"You spent {dysentery_heal} days recovering.")
            days = days + dysentery_heal
    food = food - random.randrange(15, 20)
    if food < 0:
        print("You ran out of food")
        done = True

# This is detecting if the player quit or finished the game
if done == True:
    print(f"Thank you for playing, {p_name}.")

if done == True and distance_from_oregon <= 0:
    print(f"You made it to oregon in {days} days, {p_name}! Congraulations!")

credits()

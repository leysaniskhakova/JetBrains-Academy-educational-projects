water, milk, coffee_beans, disposable_cups, money = 400, 540, 120, 9, 550

def print_coffee_machine (water, milk, coffee_beans, disposable_cups, money):
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cups} of disposable cups""")
    if money != 0:
        print(f"${money} of money")
    else:
        print(f"{money} of money")

def espresso(water, coffee_beans, disposable_cups, money):
    if water < 250:
        print('Sorry, not enough water!')
    elif coffee_beans < 16:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        water -= 250
        coffee_beans -= 16
        disposable_cups -= 1
        money += 4
    return water, coffee_beans, disposable_cups, money

def latte(water, milk, coffee_beans, disposable_cups, money):
    if water < 350:
        print('Sorry, not enough water!')
    elif milk < 75:
        print('Sorry, not milk!')
    elif coffee_beans < 20:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        water -= 350
        milk -= 75
        coffee_beans -= 20
        disposable_cups -= 1
        money += 7
    return water, milk, coffee_beans, disposable_cups, money

def cappuccino(water, milk, coffee_beans, disposable_cups, money):
    if water < 200:
        print('Sorry, not enough water!')
    elif milk < 100:
        print('Sorry, not milk!')
    elif coffee_beans < 12:
        print('Sorry, not enough coffee beans!')
    else:
        print('I have enough resources, making you a coffee!')
        water -= 200
        milk -= 100
        coffee_beans -= 12
        disposable_cups -= 1
        money += 6
    return water, milk, coffee_beans, disposable_cups, money

def coffee(water, milk, coffee_beans, disposable_cups, money):
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    buy = input()
    if buy != 'back':
        if buy == '1':
            water, coffee_beans, disposable_cups, money = espresso(water, coffee_beans, disposable_cups, money)
        elif buy == '2':
            water, milk, coffee_beans, disposable_cups, money = latte(water, milk, coffee_beans, disposable_cups, money)
        elif buy == '3':
            water, milk, coffee_beans, disposable_cups, money = cappuccino(water, milk, coffee_beans, disposable_cups, money)
    return water, milk, coffee_beans, disposable_cups, money

def add(water, milk, coffee_beans, disposable_cups):
    print('Write how many ml of water do you want to add:')
    add_water = int(input())
    water += add_water
    print('Write how many ml of milk do you want to add:')
    add_milk = int(input())
    milk += add_milk
    print('Write how many grams of coffee beans do you want to add:')
    add_beans = int(input())
    coffee_beans += add_beans
    print('Write how many disposable cups of coffee do you want to add:')
    add_cups = int(input())
    disposable_cups += add_cups
    return water, milk, coffee_beans, disposable_cups

def left(money):
    print(f'I gave you ${money}')
    money -= money
    return money

while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    print()
    if action == 'buy':
        water, milk, coffee_beans, disposable_cups, money = coffee(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'fill':
        water, milk, coffee_beans, disposable_cups = add(water, milk, coffee_beans, disposable_cups)
    elif action == 'take':
        money = left(money)
    elif action == 'remaining':
        print_coffee_machine(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'exit':
        break
    print()
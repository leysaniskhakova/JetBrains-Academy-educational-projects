water, milk, coffee_beans, disposable_cups, money = 400, 540, 120, 9, 550

def print_coffee_machine(water, milk, coffee_beans, disposable_cups, money):
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cups} of disposable cups
{money} of money""")

def coffee(water, milk, coffee_beans, disposable_cups, money):
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    buy = input()
    if buy == '1':
        water -= 250
        coffee_beans -= 16
        money += 4
    elif buy == '2':
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
    elif buy == '3':
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
    disposable_cups -= 1
    print()
    print_coffee_machine(water, milk, coffee_beans, disposable_cups, money)

def add(water, milk, coffee_beans, disposable_cups, money):
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
    print()
    print_coffee_machine(water, milk, coffee_beans, disposable_cups, money)

def left(money):
    print(f'I gave you ${money}')
    money -= money
    print()
    print_coffee_machine(water, milk, coffee_beans, disposable_cups, money)

def action():
    print()
    print('Write action (buy, fill, take):')
    action = input()
    if action == 'buy':
        coffee(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'fill':
        add(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'take':
        left(money)

print_coffee_machine(water, milk, coffee_beans, disposable_cups, money)
action()
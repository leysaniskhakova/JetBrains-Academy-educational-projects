from textwrap import dedent as dedent

class CoffeMachine:
	ESPRESSO = '1'
	LATTE = '2'
	CAPPUCCINO = '3'
	BACK = 'back'
	STATE_IDLE = 'idle'
	STATE_BUY = 'buy'
	STATE_WATER = 'water'
	STATE_MILK = 'milk'
	STATE_COFFEE_BEANS = 'coffee_beans'
	STATE_DISPOSABLE_CUPS = 'disposable_cups'
	ERROR_WATER = 'error_water'
	ERROR_MILK = 'error_milk'
	ERROR_COFFEE_BEANS = 'error_coffee_beans'
	ERROR_DISPOSABLE_CUPS = 'error_disposable_cups'
	RESULT_BACK = 'back'
	RESULT_COFFEE_OK = 'result_coffee_ok'
	RESULT_MONEY_TAKEN = 'result_money_taken'
	RESULT_GET_STATE = 'result_get_state'
	STATE_OFF = 'off'

	def __init__(self, water, milk, coffee_beans, disposable_cups, money):
		self.water = water
		self.milk = milk
		self.coffee_beans = coffee_beans
		self.disposable_cups = disposable_cups
		self.money = money
		self.state = CoffeMachine.STATE_IDLE

	def process(self, action):
		if self.state == CoffeMachine.STATE_IDLE:
			if action == 'buy':
				self.state = CoffeMachine.STATE_BUY
			elif action == 'fill':
				self.state = CoffeMachine.STATE_WATER
			elif action == 'take':
				return self.left()
			elif action == 'remaining':
				return self.display_info()
			elif action == 'exit':
				self.state = CoffeMachine.STATE_OFF
		elif self.state == CoffeMachine.STATE_BUY:
			result_coffee = self.coffee(action)
			self.state = CoffeMachine.STATE_IDLE
			return result_coffee
		else:
			self.fill(action)
		return 

	def coffee(self, action):
		if action == CoffeMachine.ESPRESSO:
			return self.espresso()
		elif action == CoffeMachine.LATTE:
			return self.latte()
		elif action == CoffeMachine.CAPPUCCINO:
			return self.cappuccino()
		return CoffeMachine.RESULT_BACK

	def espresso(self):
		return self.make_coffee(250, 0, 16, 6)

	def latte(self):
		return self.make_coffee(350, 75, 20, 7)

	def cappuccino(self):
		return self.make_coffee(200, 100, 12, 6)

	def make_coffee(self, water_now, milk_now, coffe_beans_now, money_now):
		if self.water < water_now:
			return CoffeMachine.ERROR_WATER
		elif self.milk < milk_now:
			return CoffeMachine.ERROR_MILK
		elif self.coffee_beans < coffe_beans_now:
			return CoffeMachine.ERROR_COFFEE_BEANS
		elif self.disposable_cups == 0:
			return CoffeMachine.ERROR_DISPOSABLE_CUPS
		else:
			self.water -= water_now
			self.milk -= milk_now
			self.coffee_beans -= coffe_beans_now
			self.disposable_cups -= 1
			self.money += money_now
			return CoffeMachine.RESULT_COFFEE_OK

	def fill(self, action):
		if self.state == CoffeMachine.STATE_WATER:
			self.add_water(int(action))
			self.state = CoffeMachine.STATE_MILK
		elif self.state == CoffeMachine.STATE_MILK:
			self.add_milk(int(action))
			self.state = CoffeMachine.STATE_COFFEE_BEANS
		elif self.state == CoffeMachine.STATE_COFFEE_BEANS:
			self.add_coffee_beans(int(action))
			self.state = CoffeMachine.STATE_DISPOSABLE_CUPS
		elif self.state == CoffeMachine.STATE_DISPOSABLE_CUPS:
			self.add_disposable_cups(int(action))
			self.state = CoffeMachine.STATE_IDLE
		return self.state

	def display_info(self):
		self_water = self.water
		self_milk = self.milk
		self_coffee_beans = self.coffee_beans
		self_disposable_cups = self.disposable_cups
		self_money = self.money
		return CoffeMachine.RESULT_GET_STATE,self_water, self_milk, self_coffee_beans, self_disposable_cups, self_money

	def left(self):
		money = self.money
		self.money -= self.money
		return CoffeMachine.RESULT_MONEY_TAKEN, money

	def add_water(self, water):
		self.water += water
		return self.water

	def add_milk(self, milk):
		self.milk += milk
		return self.milk

	def add_coffee_beans(self, coffee_beans):
		self.coffee_beans += coffee_beans
		return self.coffee_beans

	def add_disposable_cups(self, disposable_cups):
		self.disposable_cups += disposable_cups
		return self.disposable_cups


def print_coffee_machine_result(action_result):
	if isinstance(action_result, str):
		if action_result == CoffeMachine.ERROR_WATER:
			print('Sorry, not enough water!')
		elif action_result == CoffeMachine.ERROR_MILK:
			print('Sorry, not milk!')
		elif action_result == CoffeMachine.ERROR_COFFEE_BEANS:
			print('Sorry, not enough coffee beans!')
		elif action_result == CoffeMachine.ERROR_DISPOSABLE_CUPS:
			print('Sorry, not enough disposable cups!')
		elif action_result == CoffeMachine.RESULT_COFFEE_OK:
			print('I have enough resources, making you a coffee!')
	elif isinstance(action_result, tuple):
		if action_result[0] == CoffeMachine.RESULT_MONEY_TAKEN:
			print(f'I gave you ${action_result[1]}')
		elif action_result[0] == CoffeMachine.RESULT_GET_STATE:
			water, milk, coffee_beans, disposable_cups, money = action_result[1:]
			print(dedent(f"""\
				The coffee machine has:
				{water} of water
				{milk} of milk
				{coffee_beans} of coffee beans
				{disposable_cups} of disposable cups"""))
			print(f"{'$' if money != 0 else ''}{money} of money", end='\n')


def promt_action(state_coffee_machine):
	if state_coffee_machine == CoffeMachine.STATE_IDLE:
		print('Write action (buy, fill, take, remaining, exit):')
	elif state_coffee_machine == CoffeMachine.STATE_BUY:
		print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
	elif state_coffee_machine == CoffeMachine.STATE_WATER:
		print('Write how many ml of water do you want to add:')
	elif state_coffee_machine == CoffeMachine.STATE_MILK:
		print('Write how many ml of milk do you want to add:')
	elif state_coffee_machine == CoffeMachine.STATE_COFFEE_BEANS:
		print('Write how many grams of coffee beans do you want to add:')
	elif state_coffee_machine == CoffeMachine.STATE_DISPOSABLE_CUPS:
		print('Write how many disposable cups of coffee do you want to add:')




water, milk, coffee_beans, disposable_cups, money = 400, 540, 120, 9, 550
coffee_machine = CoffeMachine(water, milk, coffee_beans, disposable_cups, money)

print('Write action (buy, fill, take, remaining, exit):')
while True:
	user_input = input()
	print()
	action_result = coffee_machine.process(user_input)
	print_coffee_machine_result(action_result)
	state_coffee_machine = coffee_machine.state
	if state_coffee_machine == CoffeMachine.STATE_OFF:
		break
	else:
		promt_action(state_coffee_machine)
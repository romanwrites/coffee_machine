class CoffeeMachine:

    def __init__(self, water_has, milk_has, coffee_beans_has, cups_has, money_has):
        self.water_has = water_has
        self.milk_has = milk_has
        self.coffee_beans_has = coffee_beans_has
        self.cups_has = cups_has
        self.money_has = money_has

    def make_coffee(self, water, milk, coffee_beans, cost):
        if self.water_has - water < 0:
            print("Sorry, not enough water!")
            return 0
        elif self.milk_has - milk < 0:
            print("Sorry, not enough milk!")
            return 0
        elif self.coffee_beans_has - coffee_beans < 0:
            print("Sorry, not enough coffee beans!")
            return 0
        if self.cups_has <= 0:
            print("Sorry, not enough cups!")
            return 0
        self.water_has -= water
        self.milk_has -= milk
        self.coffee_beans_has -= coffee_beans
        self.money_has += cost
        self.cups_has -= 1
        print("I have enough resources, making you a coffee!")
        return 1

    def buy_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == '1':
            self.make_coffee(250, 0, 16, 4)
        elif choice == '2':
            self.make_coffee(350, 75, 20, 7)
        elif choice == '3':
            self.make_coffee(200, 100, 12, 6)
        elif choice == 'back':
            return

    def give_money(self):
        money_has_str = str(self.money_has)
        print('I gave you $' + money_has_str)
        self.money_has = 0

    def load_of_machine_output(self):
        water_has_str = str(self.water_has)
        milk_has_str = str(self.milk_has)
        coffee_beans_has_str = str(self.coffee_beans_has)
        cups_has_str = str(self.cups_has)
        money_has_str = str(self.money_has)
        print()
        print("The coffee machine has:")
        print(water_has_str + ' of water')
        print(milk_has_str + ' of milk')
        print(coffee_beans_has_str + ' of coffee beans')
        print(cups_has_str + ' of disposable cups')
        print(money_has_str + ' of money')
        print()

    def fill_machine(self):
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        coffee_beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.water_has += water_add
        self.milk_has += milk_add
        self.coffee_beans_has += coffee_beans_add
        self.cups_has += cups_add


lucky_coffee = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    task = input("Write action (buy, fill, take, remaining, exit):")
    if task == 'buy':
        lucky_coffee.buy_coffee()
    elif task == 'fill':
        lucky_coffee.fill_machine()
    elif task == 'take':
        lucky_coffee.give_money()
    elif task == 'remaining':
        lucky_coffee.load_of_machine_output()
    elif task == 'exit':
        break
    else:
        print("I don't understand the task. Insert the task again:")

### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.machine_on = True

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        total = 0
        total += int(input("how many large dollars: ")) * 1.00
        total += int(input("how many half dollars: ")) * 0.50
        total += int(input("how many quarters: ")) * 0.25
        total += int(input("how many nickels: ")) * 0.05
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that’s not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)

while sandwich_machine.machine_on:
    choice = input("What would you like? (small/medium/large/off/report): ").lower()
    if choice == "off":
        sandwich_machine.machine_on = False
        print("Turning off the machine. Goodbye!")
    elif choice == "report":
        for item, amount in sandwich_machine.machine_resources.items():
            unit = "slice(s)" if item in ["bread", "ham"] else "pound(s)"
            print(f"{item.capitalize()}: {amount} {unit}")
    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid selection. Please choose small, medium, large, report, or off.")

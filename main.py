### Data ###
import cashier
import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_machine = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    ### Main Program Loop ###
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
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_machine.make_sandwich(choice, sandwich["ingredients"])

        else:
            print("Invalid selection. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()

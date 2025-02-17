class Cashier:
    def __init__(self):
        pass

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
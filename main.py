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
    """initialize machine with available ingredients,
    dictionary of ingredient: quantity"""

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    """verify resources needed for the order,
    return true if all ingredients are available,
    false otherwise"""

    def check_resources(self, ingredients):
        """Returns True when user's order can be made, False if ingredients are insufficient."""
        for item, needed in ingredients.items():
            available = self.machine_resources.get(item, 0)
            if needed > available:
                print(f"Sorry, not enough {item}. ")
                return False
        return True

    """prompt the user to insert coins and calculate total value,
    return the total amount of money inserted"""
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("\nPlease insert coins.")
        quarters = int(input("How many quarters ($0.25)?: "))
        dimes = int(input("How many dimes ($0.10)?: "))
        nickels = int(input("How many nickels? ($0.05): "))
        pennies = int(input("How many pennies? ($0.01): "))
        """sum the total amount of money inserted"""
        total = (0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = payment - cost
            if change > 0:
                print(f"Here is ${change:.2f}.")
            print("Transaction complete. Making sandwich now. \n")
            return True
        else:
            print("Sorry, that is not enough coins. Money refunded. \n")
            return False
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount


### Make an instance of SandwichMachine class and write the rest of the codes ###

"""Main loop for user interaction"""

machine = SandwichMachine(resources)

while True:
    """ask the user what they'd like"""
    choice = input("What would you like? (small/medium/large/off): ").lower()
    """ if user chooses 'off', shut down the machine"""
    if choice == "off": #exit machine
        print("Turning off the machine. Goodbye.")
        break

    if choice in recipes:
        recipe = recipes[choice]
        if machine.check_resources(recipe["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, recipe["cost"]):
                machine.make_sandwich(choice, recipe["ingredients"])
    else:
        print("Invalid selection. Please choose small, medium, large, or off. \n")
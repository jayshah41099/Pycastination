class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []  # Store all transactions (balance added and spending)
        self.subscriptions = {}

    def add_money_to_wallet(self, amount):
        self.balance += amount
        self.transactions.append((f"Added ${amount} to wallet", self.balance))
        print(f"Added ${amount} to your wallet. Your current balance is ${self.balance}")

        if self.balance < 300:
            print("Reminder: Your balance is lower than $300.")

    def add_spending(self, amount, description):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append((f"Spent ${amount} on {description}", self.balance))
            print(f"Spent ${amount} on {description}. Your current balance is ${self.balance}")

            if self.balance < 300:
                print("Reminder: Your balance is lower than $300.")
        else:
            print("Insufficient funds. Transaction cannot be completed.")

    def add_subscription(self, name, amount):
        self.subscriptions[name] = amount
        self.transactions.append((f"Added {name} subscription of ${amount} monthly", self.balance))
        print(f"Added {name} subscription of ${amount} monthly.")

        if self.balance < amount:
            print("Reminder: Subscription added, but your balance is lower than the subscription amount.")

    def show_chart(self):
        print("\nTransaction History:")
        print("----------------------------")
        print("Transaction          | Balance")
        print("----------------------------")
        for transaction in self.transactions:
            print(f"{transaction[0]:<20} | {transaction[1]}")

    def track_budget(self):
        print("Welcome to Budget Tracker!")
        while True:
            print("\n1. Add money to wallet")
            print("2. Add spending")
            print("3. Add monthly subscription")
            print("4. Show Chart")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                amount = float(input("Enter amount to add to wallet: $"))
                self.add_money_to_wallet(amount)
            elif choice == '2':
                amount = float(input("Enter amount spent: $"))
                description = input("Enter description of spending: ")
                self.add_spending(amount, description)
            elif choice == '3':
                name = input("Enter name of subscription: ")
                amount = float(input("Enter monthly subscription amount: $"))
                self.add_subscription(name, amount)
            elif choice == '4':
                self.show_chart()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option.")

def main():
    # Initialize and run the budget tracker
    tracker = BudgetTracker()
    tracker.track_budget()

if __name__ == '__main__':
    main()

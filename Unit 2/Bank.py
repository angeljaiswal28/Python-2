class Bank:
    def __init__(self, balance):
        self.balance = balance 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def check(self, account_number):
        print(f"Balance in account {account_number} is: {self.balance}")

# --- Main Logic ---
an = input("Enter account number: ")
# Initialize the bank object with a starting balance of 10,000
b = Bank(10000)

t = 0
while t != -1:
    print("\n--- Bank Menu ---")
    print("1: Check Balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("-1: Quit")
    
    t = int(input("Enter choice: "))
    
    if t == 1:
        b.check(an)
    elif t == 2:
        k = int(input("Enter amount to Deposit: "))
        b.deposit(k)
    elif t == 3:
        l = int(input("Enter amount to Withdraw: "))
        b.withdraw(l)
    elif t == -1:
        print("Goodbye!")
    else:
        print("Invalid choice, try again.")

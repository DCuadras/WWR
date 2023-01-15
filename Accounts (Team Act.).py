accounts = []
balances = []


new_account = None

print("Enter the names and balances of bank accounts")
print("Type quit when done")

while new_account != "quit":
    print("")
    new_account = input("What is the name of this account? ")
    if new_account != "quit":
        account_balance = float(input("What is the balance? "))

        accounts.append(new_account)
        balances.append(account_balance)

total = 0

print("")
print("Account Information: ")
for i in range(len(accounts)):
    print(f"{accounts[i]} ${balances[i]}")
    total += balance[i]

average = total / len(balances)

print()
print(f"Total: ${total:.2f}" )
print(f"Average: ${average:.2f}")
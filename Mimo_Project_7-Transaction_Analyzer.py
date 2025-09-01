data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

#####################################################################################

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")
  return


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Total deposited: {total_deposited}")

  withdraw = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdraw)
  print(f"Total withdrawn: {total_withdrawn}")

  balance = round(total_deposited + total_withdrawn, 2)
  print(f"Total balance: {balance}")
  return


def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"The largest withdrawal was: {largest_withdrawal}")
  print(f"The largest deposit was: {largest_deposit}")

  positive_transactions = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]

  total_withdrawals = sum(withdrawals)
  if total_withdrawals == 0:
    print("No withdrawals")
  else:
    average_withdrawals = round(total_withdrawals / len(withdrawals), 2)
    print(f"Average withdrawal ammount: {average_withdrawals}")

  if sum(positive_transactions) == 0:
    return 0
  else:
    total_deposit = sum(positive_transactions)
    deposit_average = round(total_deposit / len(positive_transactions), 2)
    print (f"Average deposit amount: {deposit_average}")
    return

#####################################################################################

#print_transactions(data)
#print_summary(data)
#analyze_transactions(data)

while True:
  print()
  print(f"Please enter an option: \n'print'\n'analyze'\n'stop'")
  choice = input()
  if choice.lower() == "print":
    print_summary(data)
  elif choice.lower() == "analyze":
    analyze_transactions(data)
  elif choice.lower() == "stop":
    break
  else:
    print("Invalid choice")

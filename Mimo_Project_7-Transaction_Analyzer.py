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


print_transactions(data)

print_summary(data)

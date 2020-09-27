# Initial balance of the bank account
initial_balance = 200

# Bank statement with all transactions for the past 6 months
statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]

# # We want to:
# # - Know the current balance
# # - Know the total income and expenses each month (Week 3)
# # - Pay 0.5% monthly interest into the account (every 6 months)
# # - Overdraft fees: deduce £10 for each time the balance became negative (every 6 months) (week 3)
#
# # Get current balance (at the end of the 6 months)
# # balance = initial_balance
# # for month in statement:
# #     balance = balance + sum(month)
# #     print(round(balance, 2))
#
# # # (Week 3) Total income and expenses each month
# # in_out = []
# # for month in statement:
# #     income = 0
# #     expenses = 0
# #     for transaction in month:
# #         if transaction >= 0:
# #             income += transaction
# #         else:
# #             expenses += transaction
# #     in_out.append([round(income, 2), round(expenses, 2)])
# #
# # print(in_out)
#
#
# # # Did they ever go into overdraft (in the red)?
# # balance = initial_balance
# # overdraft = []
# #
# # for month in statement:
# #     for transaction in month:
# #         balance = balance + transaction
# #         overdraft.append(balance < 0)
# #
# # print(True in overdraft)
#
# # Pay 0.5% monthly interest into the account
# # and deduct overdraft fees
# balance = initial_balance
# interest = 0
# fees = 0
#
# # For each month...
# for month in statement:
#     # For each transaction that month...
#     for transaction in month:
#
#         # Update the balance
#         balance = balance + transaction
#
#         # Add overdraft fees if the balance is negative
#         fees = fees + (balance < 0)*10
#
#     # After the balance is updated for that month,
#     # calculate 2% interest, add it to the total so far
#     interest = interest + 0.02 * balance
#
# # Display the balance before interest and fees
# print(f'Balance before interest and fees: £{balance:.2f}')
#
# # Pay the total interest for the last 6 months into the account
# statement[-1].append(interest)
#
# # Charge the overdraft fee to the account
# statement[-1].append(-fees)
#
# # Display the balance after interest and fees
# print(f'Total interest for the last 6 months: £{interest:.2f}')
# print(f'Overdraft fees for the last 6 months: £{fees:.2f}')
# balance = balance + interest - fees
# print(f'Balance after interest and fees: £{balance:.2f}')

# Use this with any other bank statement: write some functions.
def update_balance(month, initial_balance):
    '''
    Return the account balance given a list of transactions
    for a given month, and an initial_balance (float).
    '''
    balance = initial_balance + sum(month)
    return balance


def total_interest(balance, interest_rate):
    '''
    Return the interest earned in a given month at a given rate (in %),
    for a given balance at the end of the month.
    '''
    interest = 0.01 * interest_rate * balance
    return interest


# def overdraft_fees(month, initial_balance, amount):
#     '''
#     Return the total overdraft fees to deduce in a given month,
#     where "amount" is the amount deducted each time the
#     balance becomes negative.
#     '''
#     # Initialise the balance and fees
#     balance = initial_balance
#     fees = 0
#
#     # Add each transaction one by one
#     for transaction in month:
#
#         # Update the balance
#         balance = balance + transaction
#
#         # Add amount to the fees, only if balance is negative
#         fees = fees + (balance < 0)*amount
#
#     return fees


def update_statement(statement, initial_balance, interest_rate):
    '''
    Update a given 6-month bank statement by paying interest
    with monthly rate interest_rate, and deducting overdraft
    fees by amount for every occurrence.
    Display the balance, and return the updated bank statement.
    '''
    # Initialise the balance and total interest
    balance = initial_balance
    interest = 0

    # Compute the total interest and fees to pay into the account
    for month in statement:

        # Update the monthly balance
        balance = update_balance(month, balance)

        # Calculate interest
        interest = interest + total_interest(balance, interest_rate)
        # fees = overdraft_fees(month, balance, amount) # week 3


    # Display a summary before interest
    print(f'Balance 6 months ago: £{initial_balance:.2f}')
    print(f'Current balance before interest: £{balance:.2f}')

    # Pay the interest and update the statement for the last month with payment
    balance = balance + interest
    statement[-1].append(interest)
    print(f'Total interest earned: £{interest:.2f}')
    print(f'Current balance after interest paid: £{balance:.2f}')

    # Return the updated statement
    return statement


def display_statement(statement):
    '''
    Display bank statement in a nicely readable form.
    '''
    for i, month in enumerate(statement):
        print(f'Month {i+1}:')
        for transaction in month:
            print(f'{transaction:8.2f}')
        print()

# Test our function: print statement, pay interest, print the new statement
print('Previous statement:')
display_statement(statement)

statement = update_statement(statement, 200, 0.5)
print('Updated statement:')
display_statement(statement)

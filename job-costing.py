# Job Costing Script for Construction Companies
# by @rpriven

# This is a simple job costing script that asks you financial questions on a job
# and calculates your overhead, expenses and reports back your profit and commission

expenses = list()

print('\nJob Costing Report\n')
# Asks user for Customer Name / Job
customer = input('Enter the customer name:  ')
while not customer:
    print('Error:  You must enter a customer name.')
    customer = input('Enter the customer name:  ')

# Asks user for total amount of job $
price = input('Enter the total amount of the job / the amount paid by the customer:  $ ')
while not price or price == '' or price == '0':
    print('You cannot have a total job price of $0')
    price = input('Enter the total amount of the job / the amount paid by the customer:  $ ')
price = int(price)

# Asks user for Overhead %
overhead = input('Enter the percentage of overhead for this job:  ')
while not overhead:  # or while not isnumeric(overhead)
    print('Error:  Surely you had some overhead on this job.  If there truly was no overhead, enter 0')
    overhead = input('Enter the percentage of overhead for this job:  ')


# Asks user for permit cost
permit = input('Enter the cost of permit expenses for this job:  ')
while not permit:
    print("You didn't pull a permit on this job?  If not, then enter 0")
    permit = input('Enter the cost of permit expenses for this job:  ')
expenses.append(int(permit))

# Asks user for materials cost
materials = input('Enter the cost of materials for this job:  ')
while not materials:
    print('Error:  No materials were entered.')
    materials = input('Enter the cost of materials for this job:  ')
expenses.append(int(materials))

# Yes = ['Yes', 'yes', 'y']
# No = ['No', 'no', 'n']
# if m_add in Yes:

# Asks user if there additional material costs
m_add = input('Are there more material expenses to enter?  [ Y / N ]  ')
if m_add == 'Y' or m_add == 'y' or m_add == 'Yes' or m_add == 'yes':
    m_add = True
elif m_add == 'N' or m_add == 'n' or m_add == 'No' or m_add == 'no':
    m_add = False
else: 
    print('Please enter Y or N for Yes or No')
    m_add = input('Are there more material expenses to enter?  [ Y / N ]  ')
# if yes, asks for amount
while m_add is True:
    more_materials = input('Enter the additional material cost (or enter "0" or "done" to stop):  ')
    expenses.append(int(more_materials))
    if more_materials == '0':
        break
    elif more_materials == 'done':
        expenses.pop()
        break

# Asks user for labor costs
labor = input('Enter the cost of labor for this job:  ')
while not labor:
    print('Error:  No labor expenses were entered.')
    labor = input('Enter the cost of labor for this job:  ')
expenses.append(int(labor))

# Asks for misc costs
misc_add = input('Are there any additional / miscellaneous expenses to add?  [ Y / N ]  ')
# while Yes in misc_add:
if misc_add == 'Y' or misc_add == 'y' or misc_add == 'Yes' or misc_add == 'yes':
    misc_add = True
elif misc_add == 'N' or misc_add == 'n' or misc_add == 'No' or misc_add == 'no':
    misc_add = False
else: 
    print('Please enter Y or N for Yes or No')
    misc_add = input('Are there any additional / miscellaneous expenses to add?  [ Y / N ]  ')
while misc_add is True:
    misc = input('Enter the additional material cost (or enter "0" or "done" to stop):  ')
    expenses.append(int(misc))
    if misc == '0':
        break
    elif misc == 'done':
        expenses.pop()
        break

# Commission
commission = input('What percentage of the profit does the Salesperson get on this job for commission?  ')
while not commission:  # or while not isnumeric(overhead)
    print("Hey, I can understand why you wouldn't want to pay your salesperson on this job.  If there is actually no commission to be paid, enter 0")
    commission = input('What percentage of the profit does the Salesperson get on this job for commission?  ')

cost = sum(expenses)

overhead = int(overhead) / 100
overhead = price * overhead

profit = price - overhead - cost

commission = int(commission) / 100
commission = profit * commission

# Output
print('\nJob Costing Report for', customer,'\n')
print(f'Total Job Price:  ${price:,.2f}')
print(f'Overhead:  ${overhead:,.2f}')
print(f'Expenses:  ${cost:,.2f}')
print(f'Profit:  ${profit:,.2f}')

profit = profit - commission

print('\nCongratulations!  On the job for: ', customer + ':')
print(f'Your company made ${profit:,.2f} and your Salesperson made ${commission:,.2f}')
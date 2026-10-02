from expense import Expense
from datetime import date
from calendar import monthrange

def main():
    print('🎯 RUNNING EXPENSE TRACKER....')
    expense_file_path='expenses.csv'
    budget=600000
    # expense=get_user_expense()
    # save_to_file(expense,expense_file_path)
    summarize_expenses(expense_file_path,budget)
    pass

def get_user_expense():
    print('💰Getting the user expense')
    expense_name=input('📝Enter the expense name: ')
    expense_amount=float(input('💵Enter the expense amount: ₹'))
    expense_category=['🍔Food','💳Bills','🏠Home','🎬Entertainment','🎵Music']
    while True:
        print('📂Select a category:')
        for i,category_name in enumerate(expense_category):
            print(f'🔢{i+1}.{category_name}')
        value_range=f'[1-{len(expense_category)}]'
        selected_index=int(input(f'👉Enter a category number {value_range}: '))-1
        if selected_index in range(len(expense_category)):
            selected_category=expense_category[selected_index]
            new_expense=Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount
            )
            return new_expense
        else:
            print('❌Invalid category.Please try again!')

def save_to_file(expense:Expense,expense_file_path):
    print(f'💾Saving expense:{expense.name}to{expense_file_path}')
    with open(expense_file_path,'a') as f:
        f.write(f'{expense.name},{expense.category},{expense.amount}\n')

def summarize_expenses(expense_file_path,budget):
    print('📊Summarising expenses')
    expenses:list[Expense]=[]
    with open(expense_file_path,'r') as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_category,expense_amount=line.strip().split(',')
            line_expense=Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.amount
        else:
            amount_by_category[key]=expense.amount

    print('💹Expenses by category:')
    for key,amount in amount_by_category.items():
        print(f'📌{key}:₹{amount:.2f}')

    total_spent=sum([expense.amount for expense in expenses])
    print(f'💸Total spent:₹{total_spent:.2f}this month')

    remaining_budget=budget-total_spent``
    print(f'💰Remaining budget:₹{remaining_budget:.2f}')

    today=date.today()
    last_day=monthrange(today.year,today.month)[1]
    remaining_days=last_day-today.day+1
    print(f'📅Days remaining:{remaining_days}')

    if remaining_budget>0:
        daily_budget=remaining_budget/remaining_days
        print(f'💵You can spend per day:₹{daily_budget:.2f}')
    else:
        print('⚠️You have exceeded your budget!')

if __name__=='__main__':
    main()
#Kyle_Segrist
#Chapter_3_Lab_2
#June_23_2025

LIMIT = int(input("How many items would you like to buy? : "))

total=0
for num in range(1, LIMIT + 1):
    
    price = float(input(f'Enter the price of item {num}: '))
    #calculate the total cost of all items
    total += price
    
#Calculate the average cost per item then display the total and average costs
average = total / num
print()
print(f'The total is ${total:,.2f}')
print()
print(f'The average cost is ${average:,.2f} per item')
print()
print('Thank You')
    

total_rows = 5  # initializing the variable with total number of rows required

# Here the outer loop tells the number of rows, and the inner loop tells the number of coloumns required to print the pattern
for i in range(0, total_rows): #outer loop to iterate the number of rows using for loop and range() function
    
    for j in range(0, total_rows-i):   # inner loop to handle the number of coloumns. This internal loop iteration is depending on the values on the outer loop
      print(total_rows - j, end='')   
    print('') # After each iteration of the outer loop, it displays pattern appropriately

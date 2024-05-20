header = "  |"

# Printing the headers
for i in range(1,11):
    header = header + "  " + str(i)
print(header)
print("--+--------------------------------")

for rows in range(1,11):
    # Building the firts part of the row
    row = str(rows).rjust(2) + "|"

    # Cicling for the products
    for j in range(1,11):
        # Necessary to format well 10*10
        if rows*j == 100:
            row = row + " " + str(rows*j)
        else:
            row = row + str(rows*j).rjust(3)
    print(row)
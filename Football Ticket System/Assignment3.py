# Süleyman Yolcu
# b2210765016

import sys


# This function used for creating dictionaries for categorys and the seat status related to the category.
def CREATECATEGORY(category_name, rowsxcolumns):
    global category_dict
    if category_name not in category_names:
        category_names.append(category_name)  # Creating categoryname list to use for if category already exist or not.
        rows = int(rowsxcolumns.split("x")[0])
        columns = int(rowsxcolumns.split("x")[1])
        category_row_column_dict[category_name] = rows, columns
        category_rows = [chr(i) for i in range(65, 65 + rows)]
        category_columns = [i for i in range(columns + 1)]
        category_seats = [i + str(j) for i in category_rows for j in category_columns]
        seat_status = {seats: "X" for seats in category_seats}
        category_dict[category_name] = seat_status
        save_otuput(f"The category '{category_name}' having {rows * columns} seats has been created")
    elif category_name in category_names:
        save_otuput(f"Warning: Cannot create the category for the second time. The stadium has already {category_name}")


# This function used for selling tickets and changing the seat status related to the category seats.
def SELLTICKET(customer_name, ticket_type, category_name, *seats):
    if category_name in category_names:
        wanted_seats = list(*seats)
        for seat in wanted_seats:
            if len(seat) <= 3:  # The if statement for single seats.
                if seat in category_dict[category_name]:
                    if category_dict[category_name][seat] == 'X':
                        if ticket_type == 'student':
                            category_dict[category_name][seat] = 'S'
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                        if ticket_type == 'full':
                            category_dict[category_name][seat] = 'F'
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                        if ticket_type == 'season':
                            category_dict[category_name][seat] = 'T'
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                    elif category_dict[category_name][seat] != 'X':
                        save_otuput(
                            f"Warning: The seat {seat} cannot be sold to {customer_name} due to it have already been sold")
                elif category_row_column_dict[category_name][1] < seat[1:]:
                    save_otuput(
                        f"Error: The category '{category_name}' has less column than the specified index {seat}!")
                elif category_row_column_dict[category_name[0]] < ord(seat[0]) - 65:
                    save_otuput(f"Error: The category '{category_name}' has less row than the specified index {seat}!")
                elif category_row_column_dict[category_name][1] < seat[1:] and category_row_column_dict[
                    category_name[0]] < ord(seat[0]) - 65:
                    save_otuput(
                        f"Error: The category '{category_name}' has less row and column than the specified index {seat}!")

            elif len(seat) > 3:  # The elif statement for ranged seats.
                k = seat.split("-")
                row_letter = k[0][0]
                starting_number = int(k[0][1:])
                ending_number = int(k[1])
                seat_range_values = [category_dict[category_name].get(row_letter + str(j)) for j in
                                     range(starting_number, ending_number + 1)]
                if category_row_column_dict[category_name][0] >= ord(row_letter) - 65 and \
                        category_row_column_dict[category_name][1] >= ending_number:
                    if all(a == 'X' for a in seat_range_values):  # Checking if all the seats are available.
                        if ticket_type == 'student':
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                            for j in range(starting_number, ending_number + 1):
                                category_dict[category_name][row_letter + str(j)] = 'S'
                        if ticket_type == 'full':
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                            for j in range(starting_number, ending_number + 1):
                                category_dict[category_name][row_letter + str(j)] = 'F'
                        if ticket_type == 'season':
                            save_otuput(f"Success: {customer_name} has bought {seat} at {category_name}")
                            for j in range(starting_number, ending_number + 1):
                                category_dict[category_name][row_letter + str(j)] = 'T'
                    elif not all(a == 'X' for a in seat_range_values):
                        save_otuput(
                            f"Warning: The seats {seat} cannot be sold to {customer_name} due some of them have already been sold")
                elif category_row_column_dict[category_name][1] < ending_number and \
                        category_row_column_dict[category_name][
                            0] < ord(row_letter) - 65:
                    save_otuput(
                        f"Error: The category '{category_name}' has less row and column than the specified index {seat}!")
                elif category_row_column_dict[category_name][1] < ending_number:
                    save_otuput(
                        f"Error: The category '{category_name}' has less column than the specified index {seat}!")
                elif category_row_column_dict[category_name][0] < ord(row_letter) - 65:
                    save_otuput(f"Error: The category '{category_name}' has less row than the specified index {seat}!")

    else:
        save_otuput(f"Error: The category '{category_name}' does not exist!")


# This function is used for cancelling the seats of related category.
def CANCELTICKET(category_name, *seats):
    if category_name in category_names:
        wanted_seats = list(*seats)
        for seat in wanted_seats:
            if len(seat) <= 3:
                if seat in category_dict[category_name]:
                    if category_dict[category_name][seat] != "X":
                        category_dict[category_name][seat] = "X"
                        save_otuput(
                            f"Success: The seat {seat} at '{category_name}' has been canceled and now ready to sell again")
                    elif category_dict[category_name][seat] == "X":
                        save_otuput(
                            f"Error: The seat {seat} at '{category_name}' has already been free! Nothing to cancel ")
                elif category_row_column_dict[category_name][1] < int(seat[1:]):
                    save_otuput(
                        f"Error: The category '{category_name}' has less column than the specified index {seat}!")
                elif category_row_column_dict[category_name[0]] < ord(seat[0]) - 65:
                    save_otuput(f"Error: The category '{category_name}' has less row than the specified index {seat}!")
                elif category_row_column_dict[category_name][1] < int(seat[1:]) and category_row_column_dict[
                    category_name[0]] < ord(seat[0]) - 65:
                    save_otuput(
                        f"Error: The category '{category_name}' has less row and column than the specified index {seat}!")
    else:
        save_otuput(f"Error: The category '{category_name}' does not exist!")


# This function is used for calculating the revenue of related category.
def BALANCE(category_name):
    if category_name in category_names:
        lenght = len("category report of ''") + len(category_name)
        print(f"category report of '{category_name}'")
        output_file.write(f"category report of '{category_name}'\n")
        print('-' * lenght)
        my_string = '-' * lenght
        output_file.write(f"{my_string}\n")
        values = category_dict[category_name].values()
        student = 0
        full = 0
        season = 0
        for value in values:
            if value == 'S':
                student += 1
            if value == 'F':
                full += 1
            if value == 'T':
                season += 1
        revenues = (student * 10) + (full * 20) + (season * 250)
        save_otuput(
            f"Sum of students = {student}, Sum of full pay = {full}, Sum of season ticket = {season}, and Revenues = {revenues} Dollars")
    else:
        save_otuput(f"Error: The category '{category_name}' does not exist!")


# This function is used for printing the layout of the related category.
def SHOWCATEGORY(category_name):
    if category_name in category_names:
        category_row = category_row_column_dict[category_name][0]
        category_column = category_row_column_dict[category_name][1]
        category_rows = [chr(i) for i in range(64 + category_row, 64, -1)]
        category_columns = [i for i in range(category_column)]
        save_otuput(f"Printing category layout of {category_name}")
        for i in category_rows:  # The loop for row index.
            print()
            output_file.write("\n")
            print(i, end=" ")
            output_file.write(f"{i} ")
            for j in category_columns:  # The loop for seat status.
                print(f"{category_dict[category_name][i + str(j)]}  ", end="")
                output_file.write(f"{category_dict[category_name][i + str(j)]}  ")
        print()
        output_file.write("\n")
        for k in category_columns:  # The loop for column index.
            print("%3d" % k, end="")
            output_file.write("%3d" % k)
        print()
        output_file.write("\n")
    else:
        save_otuput(f"Error: The category '{category_name}' does not exist!")


def save_otuput(output):
    print(output)
    output_file.write(f"{output}\n")


input_file_name = sys.argv[1]  # Taking input file name as an argument.
input_file = open(input_file_name, "r", encoding="utf-8")
output_file = open("output.txt", "w", encoding="utf-8")
input_lines = input_file.readlines()
inputs_list = [line.strip("\n").split() for line in input_lines]
category_names = []
category_dict = {}
category_row_column_dict = {}
for inputs in inputs_list:
    if inputs[0] == "CREATECATEGORY":
        CREATECATEGORY(inputs[1], inputs[2])
    if inputs[0] == "SELLTICKET":
        SELLTICKET(inputs[1], inputs[2], inputs[3], inputs[4:])
    if inputs[0] == "CANCELTICKET":
        CANCELTICKET(inputs[1], inputs[2:])
    if inputs[0] == "BALANCE":
        BALANCE(inputs[1])
    if inputs[0] == "SHOWCATEGORY":
        SHOWCATEGORY(inputs[1])

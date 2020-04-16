'''
This program allow a user to create a matrix using numpy in representation of a
building with 'x' floors and 'y' spaces for rent per floor.  It then allows the
user to add clients, print a sorted client list with the clients location in
the building. You can print a layout of the building, the numerical information
of used and available spaces for rent. Clients can also be removed.

This is a work in progress.  There are no safeguards yet checking if the spaces
are taken or not, this is provided with a visual representation.
'''



import numpy as np

# This is the Main Menu where all choices are made
while True:
    print("\n\t\tMain Menu")
    print("\t1. Initialise Building")
    print("\t2. View Building Spaces")
    print("\t3. View Spaces Per Floor")
    print("\t4. Add a Client")
    print("\t5. View client list")
    print("\t6. Remove a client")
    print("\t7. Exit")
    choice = input("\n\tPlease make your selection: ")

# Depending on the choice user makes, a different action takes place

    if choice == '1':
        # This module initialises the building using numpy and initialises the client list
        building_size = int(input("\n\tHow many floors does the building have? "))
        spaces_per_floor = int(input("\tHow many spaces per floor can be rented out? "))

        building = np.zeros([building_size, spaces_per_floor], dtype=int)
        client_list = {}

    elif choice == '2':
        # This module prints the floor plan of the building just created
        # It uses [0] for empty spaces and [1] for used spaces
        print()
        count = len(building)
        rvs_building = building[::-1]
        for x in rvs_building:
            print("\tFloor {} {}".format(count, x))
            count -= 1

    elif choice == '3':
        # This module gives numerical information as to how many spaces are
        # available in the building
        print()
        available_spaces = 0
        for i in building:
            for j in i:
                if j == 0:
                    available_spaces += 1

        print("\tThere are {} available spaces in the building\n".format(available_spaces))


        # This will provide the spaces available per floor
        for i in range(len(building)):
            spaces_per_floor = 0
            for j in range(len(building[i])):
                if building[i][j] == 0:
                    spaces_per_floor += 1
            print("\tThe {} floor has {} spaces available.".format(i+1, spaces_per_floor))

    elif choice == '4':
        # This module allows you to create a new customer, and allocate a floor and
        # space for the client
        print()
        customer_name = str(input("\tEnter customer name: "))
        floor_chosen_by_customer = int(input("\tWhat floor do you wish to rent on? (1 to {}) ".format(len(building))))


        # depending on the floor selected, it shows how many spaces are available on that floor
        # It prints out a visual representation and shows whish spaces are [0] available
        # and which spaces are [1] occupied
        count = 0
        for i in building[floor_chosen_by_customer-1]:
            if i == 0:
                count += 1

        print("\tThere are {} spaces available on floor {}.".format(count, floor_chosen_by_customer))

        print("\t", building[floor_chosen_by_customer-1])

        space_chosen_by_customer = int(input("\tWhat space do you wish to rent? "))

        # Prints the information provided for the new customer and asks for confirmation:
        # If the answer is 'Y', it adds the customer to the list and reserves the space on the
        # given floor.  If 'N' then the information is discarded and nothing happens
        print("\n\tThe client {} has chosen to rent space {} on floor {}.".format(customer_name, space_chosen_by_customer, floor_chosen_by_customer))
        correct = str(input("\tIs this correct? (Y/N)"))

        coordinates = [floor_chosen_by_customer, space_chosen_by_customer]

        if correct.upper() == 'Y':
            client_list[customer_name.upper()] = coordinates
            building[floor_chosen_by_customer-1, space_chosen_by_customer-1] = 1
            print("\tThe customer has been added")
            print("\t", building[int(floor_chosen_by_customer)-1])
        else:
            print("\tThe customer has not been added")

    elif choice == '5':
        # This module prints a sorted list of the clients with their floor and space location
        print()
        sorted_client_list = list(client_list)
        sorted_client_list.sort()
        for client in sorted_client_list:
            loc = client_list.get(client)
            print("\t{} is on floor {}, locale {}.".format(client, loc[0], loc[1]))

    elif choice == '6':
        # This module allows you to remove a client using the client name.
        print()
        client_to_remove = str(input("\tEnter clients name to remove: "))

        # Checks to see if client is in the client list  If not, it gives a warning
        # otherwise confirms if you want to delete the client. If 'Y', it removes the
        # client from the list and restores the space used to available [0]
        if client_to_remove.upper() not in client_list:
            print("\t{} is not a client. Check spelling".format(client_to_remove))
        else:
            answer = input("\tAre you sure you want to remove {}? (Y/N)".format(client_to_remove))
            if answer.upper() == 'Y':
                are_you_sure = client_list.pop(client_to_remove.upper())
                rmv_floor = are_you_sure[0]-1
                rmv_space = are_you_sure[1]-1
                building[rmv_floor, rmv_space] = 0
                print("\t{} has been removed and space restored".format(client_to_remove))
            else:
                print("\t{} was not removed".format(client_to_remove))

    elif choice == '7':
        # This module exits the program
        print("\n\tExiting program")
        break

    else:
        # This else statement will catch any wrong choices the user might make from
        # the Main Menu
        print("\tIncorrect selection, Please choose between 1 and 6 from the menu")


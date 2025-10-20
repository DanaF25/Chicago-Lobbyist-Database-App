#
#  Project 02: Chicago Lobbyist Database App
#  Course: CS 341, Fall 2024
#  System: VS Code and Windows 11 
#  Student Author: Dana Fakhreddine 
#
 
import sqlite3
import objecttier

##################################################################  
#
# main
#

# executes command one, where we find the lobbyists that have similar name to lobbyist name input
# parameter: dbConn
# return: none

def command_one(dbConn):
    # gets input
    name = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): \n")
    lobbyist = objecttier.get_lobbyists(dbConn, name)
    
    print("\nNumber of lobbyists found:", len(lobbyist))
    
    # checking if they want more than 100 lobbyists to output
    if len(lobbyist) > 100:
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")
    else:
        # printing out lobbyists with same name from input
        if len(lobbyist) != 0:
            print()
        for i in lobbyist:
            print(i.Lobbyist_ID, ":",i.First_Name, i.Last_Name, "Phone:",i.Phone)

# executes command two, where given a lobbyist id, we output the detials of that certain lobbyist
# parameter: dbConn
# return: none
def command_two(dbConn):
    # retreiving information about lobbyist
    lobbyist_id = input("\nEnter Lobbyist ID: ")
    lobbyist = objecttier.get_lobbyist_details(dbConn, lobbyist_id)
    
    # outputting information if lobbyist found
    if lobbyist == None:
        print("\nNo lobbyist with that ID was found.\n")
    else:
        years= ""
        for i in lobbyist.Years_Registered:
            years += str(i)
            years += ", "
        employers = ""
        for i in lobbyist.Employers:
            employers += i
            employers += ", "
       
        compensation = '{:,.2f}'.format(lobbyist.Total_Compensation)
        print()
        lobbyist_info = """
{} :
  Full Name: {} {} {} {} {}
  Address: {} {} , {} , {} {} {}
  Email: {}
  Phone: {}
  Fax: {}
  Years Registered: {}
  Employers: {}
  Total Compensation: ${}
        """.format(lobbyist.Lobbyist_ID, lobbyist.Salutation, lobbyist.First_Name, lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix,
                   lobbyist.Address_1, lobbyist.Address_2, lobbyist.City, lobbyist.State_Initial, lobbyist.Zip_Code, lobbyist.Country,
                    lobbyist.Email, lobbyist.Phone,lobbyist.Fax, years, employers, compensation).strip()     
        print(lobbyist_info)

# executing command three, where we output the top N lobbyists based on their total compensation for that year
# parameter: dbConn
# return: none
def command_three(dbConn):
    n = int(input("\nEnter the value of N: "))
    
    # ensuring n is a positive value
    if(n < 1):
        print("Please enter a positive value for N...")
        return
    
    # retreiving results
    year = input("Enter the year: ")
    lobbyists = objecttier.get_top_N_lobbyists(dbConn, n, year)

    count = 1

    # printing results if lobbyist exist
    if lobbyists == None:
        return
    
    print()
    for lobbyist in lobbyists: 
        print(count, ".", lobbyist.First_Name, lobbyist.Last_Name)
        print(" Phone:", lobbyist.Phone)
        print(" Total Compensation: $" + '{:,.2f}'.format(lobbyist.Total_Compensation))
        print(" Clients:", end = " ")
        for i in lobbyist.Clients:
            print(i, end = ", ")
        count+=1
        print()

# executing command four, where we register an existing lobbyist for a new year
# parameter: dbConn
# return: none
def command_four(dbConn):
    # getting input and retreiving results
    year = input("\nEnter year: ")
    id = input("Enter the lobbyist ID: ")

    result =  objecttier.add_lobbyist_year(dbConn, id, year)

    # printing if action was successful or not
    print()
    if result == 1:
        print("Lobbyist successfully registered.")
    else:
        print("No lobbyist with that ID was found.")

# executing command five, where we set the salutation for a given lobbyist
def command_five(dbConn):
    # getting input and retreiving data
    id = input("\nEnter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")

    result = objecttier.set_salutation(dbConn, id, salutation)

    # printing if action was successful or not
    print()
    if result == 0:
        print("No lobbyist with that ID was found.")
    elif result == 1:
        print("Salutation successfully set.")

# start of program
if __name__ == '__main__':
    # connecting to database
    dbConn = sqlite3.connect("Chicago_Lobbyists.db") # connecting to database
    print('** Welcome to the Chicago Lobbyist Database Application **')

    # outputting statistics
    num_lobbyists = f'{objecttier.num_lobbyists(dbConn):,}'
    num_employers = f'{objecttier.num_employers(dbConn):,}'
    num_clients = f'{objecttier.num_clients(dbConn):,}'

    gen_stats_string = """
General Statistics:
  Number of Lobbyists: {}
  Number of Employers: {}
  Number of Clients: {}
    """.format(num_lobbyists, num_employers,num_clients).strip()
    print(gen_stats_string)
        
    # getting user input and executing different commands
    user_command = input("\nPlease enter a command (1-5, x to exit): ")

    while user_command != "x":
            if user_command == "1":
                command_one(dbConn)
            elif user_command == "2":
                command_two(dbConn)
            elif user_command == "3":
                command_three(dbConn)
            elif user_command == "4":
                command_four(dbConn)
            elif user_command == "5":
                command_five(dbConn)
            else:
                print("**Error, unknown command, try again...")
            user_command = input("\nPlease enter a command (1-5, x to exit): ")
    #
    # done
    #
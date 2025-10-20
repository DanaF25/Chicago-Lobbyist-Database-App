# 
#  Project 02: Chicago Lobbyist Database App
#  Course: CS 341, Fall 2024
#  System: VS Code and Windows 11 
#  Student Author: Dana Fakhreddine 
# 

#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#

import datatier

##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   # creating constructor, initializing variables, and making the read-only properties
   def __init__(self, id, first_name, last_name, phone):
      self._Lobbyist_ID = id
      self._First_Name = first_name
      self._Last_Name = last_name
      self._Phone = phone
   
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   @property
   def First_Name(self):
      return self._First_Name
   @property
   def Last_Name(self):
      return self._Last_Name
   @property
   def Phone(self):
      return self._Phone
   

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
   # creating constructor, initializing variables, and making the read-only properties
   def __init__(self, id, salutation, first_name, middle, last_name, suffix, address1, address2, city, state, zip, country, email, phone, fax, years, employers, compensation):
      self._Lobbyist_ID = id
      self._Salutation = salutation
      self._First_Name = first_name
      self._Middle_Initial = middle
      self._Last_Name = last_name
      self._Suffix = suffix
      self._Address_1 =  address1
      self._Address_2 =  address2
      self._City = city
      self._State_Initial = state
      self._Zip_Code = zip
      self._Country = country
      self._Email = email
      self._Phone = phone
      self._Fax = fax
      self._Years_Registered = years
      self._Employers = employers
      self._Total_Compensation = compensation
   
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   @property
   def Salutation(self):
      return self._Salutation
   @property
   def First_Name(self):
      return self._First_Name
   @property
   def Middle_Initial(self):
      return self._Middle_Initial
   @property
   def Last_Name(self):
      return self._Last_Name
   @property
   def Suffix(self):
      return self._Suffix
   @property
   def Address_1(self):
      return self._Address_1
   @property
   def Address_2(self):
      return self._Address_2
   @property
   def City(self):
      return self._City
   @property
   def State_Initial(self):
      return self._State_Initial
   @property
   def Zip_Code(self):
      return self._Zip_Code
   @property
   def Country(self):
      return self._Country
   @property
   def Email(self):
      return self._Email
   @property
   def Phone(self):
      return self._Phone
   @property
   def Fax(self):
      return self._Fax
   @property
   def Years_Registered(self):
      return self._Years_Registered
   @property
   def Employers(self):
      return self._Employers
   @property
   def Total_Compensation(self):
      return self._Total_Compensation
   
##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   # creating constructor, initializing variables, and making the read-only properties
   def __init__(self, id, first_name, last_name, phone, compensation, clients):
      self._Lobbyist_ID = id
      self._First_Name = first_name
      self._Last_Name = last_name
      self._Phone = phone
      self._Total_Compensation = compensation
      self._Clients = clients
   
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   @property
   def First_Name(self):
      return self._First_Name
   @property
   def Last_Name(self):
      return self._Last_Name
   @property
   def Phone(self):
      return self._Phone
   @property
   def Total_Compensation(self):
      return self._Total_Compensation
   @property
   def Clients(self):
      return self._Clients
##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   # retreiving amount of lobbysits
   sql_query = """
      SELECT COUNT(Lobbyist_ID)
      FROM LobbyistInfo
   """
   result = datatier.select_one_row(dbConn, sql_query)

   return result[0]

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   # retreiving amount of employers
   sql_query = """
      SELECT COUNT(Employer_ID) FROM EmployerInfo
      """
   result = datatier.select_one_row(dbConn, sql_query)

   return result[0]
   
##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   # retreiving amount of clients
   sql_query = """
      SELECT COUNT(Client_ID) FROM ClientInfo
   """
   result = datatier.select_one_row(dbConn, sql_query)
   return result[0]

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   # getting lobbyist with similar name to pattern
   sql_first = """
      SELECT Lobbyist_ID, First_Name, Last_Name, Phone FROM LobbyistInfo
      WHERE First_Name LIKE ? OR Last_Name LIKE ?
      ORDER BY Lobbyist_ID asc
   """
   result = datatier.select_n_rows(dbConn, sql_first, [pattern, pattern])
   
   # creating object of Lobbyist class with information from the result of the sql query
   Lobbyists = []
   for row in result:
      object = Lobbyist(row[0], row[1], row[2], row[3])
      Lobbyists.append(object)
   return Lobbyists


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   # getting all the information about a lobbyist based off of their id
   sql_query = """
      SELECT LobbyistInfo.Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2,
      City, State_Initial, ZipCode, Country, Email, Phone, Fax FROM LobbyistInfo
      WHERE LobbyistInfo.Lobbyist_ID = ?
      """
   sql_year = """
      SELECT Year FROM LobbyistYears 
      WHERE Lobbyist_ID = ? """
   sql_compensation = """
      SELECT SUM(Compensation_Amount) FROM Compensation
      WHERE Lobbyist_ID = ?
   """
   sql_employers = """
      SELECT DISTINCT Employer_Name FROM EmployerInfo
      JOIN LobbyistAndEmployer ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID
      WHERE Lobbyist_ID = ?
      ORDER BY Employer_Name
      """
   
   # fetching results from all of the sql queries
   result = datatier.select_one_row(dbConn, sql_query, [lobbyist_id])
   result_compensation = datatier.select_one_row(dbConn, sql_compensation, [lobbyist_id])
   result_employers = datatier.select_n_rows(dbConn, sql_employers, [lobbyist_id])
   result_year = datatier.select_n_rows(dbConn, sql_year, [lobbyist_id])
   
   # checking if lobbyist was found
   if result == ():
      return None
   
   # creating arrays of the information to add to object
   years = []
   for i in result_year:
      years.append(i[0])
   employers = []
  
   for i in result_employers:
      employers.append(i[0])
   
   if result_compensation[0] == None:
      total_Compensation = 0
   else:
      total_Compensation = result_compensation[0]
   
   # creating object of LobbyistDetails class with information from the result of the sql query
   lobbyist = LobbyistDetails(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], 
                   result[10], result[11], result[12], result[13], result[14],years, employers, total_Compensation)
   return lobbyist 
##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   # getting the top lobbyists based off of their total compensation 
   sql_query = """
      SELECT LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, SUM(Compensation_Amount) as total FROM LobbyistInfo
      JOIN Compensation ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      WHERE strftime('%Y', Period_Start) = ? OR strftime('%Y', Period_End) = ?
      GROUP BY LobbyistInfo.Lobbyist_ID
      ORDER BY total desc
      LIMIT ?
   """

   result = datatier.select_n_rows(dbConn, sql_query, [year, year, N])
   
   # checking if any lobbyists were found
   if len(result) == 0:
      return None
   
   # creating array of objects of LobbyistClients class with information from the result of the sql query
   objects = []
   
   for row in result:
      clients = []

      # getting a list of the corresponding clients for each lobbyist
      sql = """ 
         SELECT Client_Name FROM ClientInfo
         JOIN Compensation ON ClientInfo.Client_ID = Compensation.Client_ID
         JOIN LobbyistInfo ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
         WHERE LobbyistInfo.Lobbyist_ID = ? AND (strftime('%Y', Period_Start) = ? OR strftime('%Y', Period_End) = ?)
         GROUP BY ClientInfo.Client_ID
         ORDER BY Client_Name asc
      """
      clients_result = datatier.select_n_rows(dbConn, sql, [row[0], year, year])

      for i in clients_result:
         clients.append(i[0])
      
      # adding the object made of the LobbyistClients class to add to array
      objects.append(LobbyistClients(row[0], row[1], row[2], row[3], row[4], clients))
   return objects

##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   # checking to see if lobbyist id exists
   sql_year = """
      SELECT Lobbyist_ID FROM LobbyistInfo
      WHERE Lobbyist_ID = ?
   """
   found_year = datatier.select_one_row(dbConn, sql_year, [lobbyist_id])

   if found_year == ():
      return 0
   
   # adding another year for lobbiyst id
   sql = """
      INSERT INTO LobbyistYears(Lobbyist_ID, Year) 
      VALUES(?,?)
      """
   datatier.perform_action(dbConn, sql, [lobbyist_id, year])
   
   return 1

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   # checking if lobbyist id exists
   sql_year = """
      SELECT Lobbyist_ID FROM LobbyistInfo
      WHERE Lobbyist_ID = ?
   """
   found_year = datatier.select_one_row(dbConn, sql_year, [lobbyist_id])

   if found_year == ():
      return 0
   
   # updating that lobbyist's salutation
   sql = """
      UPDATE LobbyistInfo
      SET Salutation = ?
      WHERE Lobbyist_ID = ?
"""

   datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
   return 1
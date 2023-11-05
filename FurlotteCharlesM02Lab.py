"""
Name: Charles Furlotte
File Name: FurlotteCharlesM02Lav.py
Description: This app will take the students last name, first name, and GPA and take and tell you if they should be on the deans list.
"""

#Initializes Vars
lastName = ''
firstName = ''
gpa = 0.00
sentinel = 'ZZZ'

#Main Loop
#get users lastName or quit
lastName = input(f'Enter the students last name or enter {sentinel} to quit:\n')
#Runs the loop till user enter {sentinel} to quit
while lastName != sentinel:
    #Takes and get the first name
    firstName = input(f'Enter the students first name:\n')
    #gets the students gpa
    gpa = float(input(f'What is the students GPA: \n'))
    if gpa >= 3.5:
        print(f'{firstName} {lastName} has made the Dean\'s List.')
    if gpa >= 3.25:
        print(f'{firstName} {lastName} has made the Honor Roll.')
    lastName = input(f'Enter a new students last name or enter {sentinel} to quit:\n')
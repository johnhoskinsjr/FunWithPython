#This script is used to find phone numbers and
#email address in a clipboard paste

import re, pyperclip

#Regex for phone number
phoneNumRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?                   #Area Code(optional)
    (\s|-|\.)?                          #Seperator(optional)
    (\d{3})                             #First 3 Digits
    (\s|-|\.)                           #Seperator
    (\d{4})                             #Last 4 Digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #Extension(optional)
    )''', re.VERBOSE)

#Regex for email address
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #Username
    @                  
    [a-zA-Z0-9.-]+     #Domain Name
    (\.[a-zA-Z]{2,4})  #Extension
    )''', re.VERBOSE)

#Assign text in clipboard to a variable for Regex search
text = str(pyperclip.paste())
#Declare list for holding search results
matches = []

#For loop that adds all phone numbers to the matches list
for  groups in phoneNumRegex.findall(text):
    #join the 3 groups of numbers together and seperate with a hyphen
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    
    #If there is a phone extention line
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        
    #append the results to our matches list
    matches.append(phoneNum)

#For loop that appends all found email addresses to the matches list
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Print results of Regex search and copys result back to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

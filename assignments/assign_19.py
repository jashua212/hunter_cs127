
# assignment 19

promptForChoice = """
(a) convert centimeters to feet
(b) convert centimeters to feet and inches
(c) convert feet and inches to centimeters
Enter a or b or c: """

'''
docstring
'''

choice = input(promptForChoice)

resultMessage = 'height is '

if choice == 'a':
    cm = int(input('Enter height in centimeters: '))
    floatFeetRounded = round(cm / 30.48, 2)

    resultMessage = resultMessage + str(floatFeetRounded) + ' feet'
    print(resultMessage)

elif choice == 'b':
    cm = int(input('Enter height in centimeters: '))
    floatFeet = cm / 30.48
    wholeFeet = int(floatFeet)
    #print('feet: ', wholeFeet)

    decimals = floatFeet - wholeFeet
    inches = int(decimals * 12)
    #print('inches: ' inches)

    inchMessage = ''
    if (inches > 0):
        inchMessage = ' and ' + str(inches) + ' inches'

    resultMessage = resultMessage + str(wholeFeet) + ' feet' + inchMessage
    print(resultMessage)

elif choice == 'c':
    ft = input('Enter height in feet and inches, separated by a space: ')
    feetAndInches = ft.split()
    totalInches = (int(feetAndInches[0]) * 12) + int(feetAndInches[1])
    totalCentimeters = totalInches * 2.54

    # assignment says rounded to 1 decimal place, but example is rounded to integer
    totalCentimetersRounded = round(totalCentimeters, 1)

    resultMessage = resultMessage + str(totalCentimetersRounded) + ' cm'
    print(resultMessage)

else:
    print('Wrong choice, please enter only a or b or c.')

import sys

def tolower(tempdata):
    converted_string = tempdata.lower()
    print("In lower case: " + converted_string)
    return converted_string


def toupper(tempdata):
    converted_string = tempdata.upper()
    print("In upper case: " + converted_string)
    return converted_string


def tosnake(tempdata):
    tempdata1 = tempdata[:].lower()
    tempdata2 = tempdata1.replace(" ", "_")
    print(f"In snake_case: " + tempdata2)
    return tempdata2


def tocamel(tempdata):
    tempdata = tempdata.split()
    converted = tempdata[0].lower()
    # One two three
    result = ""
    for word in tempdata[1:]:
        word = word.title()
        # print(word)
        result = result + word
    output = converted + result
    print("In camelCase: " + output)

n = 0
if len(sys.argv) == 3:
    try:
        n = int(sys.argv[2])
        print(type(n))
        if int(n) > 4:  # corner case condition if n > 4 or n = str
            print("Invalid value")
            sys.exit(0)
        elif int(n) < 0:
            print("Invalid value")
            sys.exit(0)
    except ValueError:
        print("Integer only accepted as key")
        sys.exit(0)#Terminate the flow for further line

elif len(sys.argv)==2:
    pass #instead of print() or do nothing code

else:
    print("Invalid input arguemnts")
    sys.exit(0)
    #if not type(n) == int():
    #if int(n) >4:  #corner case condition if n > 4 or n = str
     #   print("Invalid value")

data = str(sys.argv[1])
tempdata = data
print("Statrting Conversion ")
if n == 1 or len(sys.argv)==2:
    tolower(tempdata)

if n == 2 or len(sys.argv)==2:
    toupper(tempdata)

if n == 3 or len(sys.argv)==2:
    tosnake(tempdata)

if n == 4 or len(sys.argv)==2:
    tocamel(tempdata)

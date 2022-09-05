print(" Try except success")
try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
#Content written successfully

print("\n Try except fail")
try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
#Error: Could not find file or read data
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
#Error: Could not find file or read data

print("\n Try except with finally")
def askint():
    try:
        val = int(input("1. Please enter a integer ( enter a number ): "))
    except:
        print("Looks like you did not enter an integer!")
    else:
        print(val)
    finally:
        print("Finally, I executed!")
askint() #1 (according to the number input you enter)
def askint():
    while True:
        try:
            val = int(input("2. Please enter an integer (enter a string or number): "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")
askint() #1 (according to the number input you enter)

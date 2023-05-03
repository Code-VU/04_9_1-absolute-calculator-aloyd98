def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    
    try:
        if in_num > 21:
            diff = (in_num - 21) * 2

        else:
            diff = (in_num - 21) * -1
    except:
        print('Please enter a whole number.')

    print('Result:', diff) 
    
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()

a = int(input(" enter number of digits you want to perform operations on "))
answer = int (input("enter the first number :"))
for i in range (a-1):
    b = input (" enter a operator ( +, -, /, * ): ")
    numb = float(input("enter a number: "))

    if b == '+':
        answer += numb
    if b == '-':
        answer -= numb
    if b == '*':
        answer *= numb
    if b == '/':
        if numb != 0:
            answer /= numb
        else:
            print ("dividon by 0 is not possible ")

        print("current result = ", answer)

    print ("final result = ", answer )
                    


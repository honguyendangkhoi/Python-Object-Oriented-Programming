print("CALCULATOR")

result=[]
def calculation():
    over=True
    num1=float(input("type a number: "))
    sym=input("choose + - * /: ")
    num2=float(input("type a next number: "))
    if sym == '+':
        total=num1+num2
        result.append(total)
    
    elif sym == '-':
        total=num1-num2
        result.append(total)

    elif sym=='*':
        total=num1*num2
        result.append(total)

    else:
        total=num1/num2
        result.append(total)
    
    choice=input(f"your result: {total}. Press 'y' to countinue calculate, 'n' for return calculator, 'h' for calculate history, 'x' for exit: ")
    
    while over!=False:
        if choice=='y':
            num1=total
            num2=float(input("type a next number: "))
            sym=input("choose + - * /: ")
            if sym == '+':
                total=num1+num2
                result.append(total)
            
            elif sym == '-':
                total=num1-num2
                result.append(total)

            elif sym=='*':
                total=num1*num2
                result.append(total)

            else:
                total=num1/num2
                result.append(total)
            
            choice=input(f"your result: {total}. Press 'y' to countinue calculate, 'n' for return calculator, 'h' for calculate history, 'x' for exit: ")

        elif choice=='n':
            return calculation()
        
        elif choice=='h':
            for h in result:
                print(f"your history: {h}")
                choice=input(f"your result: {total}. Press 'y' to countinue calculate, 'n' for return calculator, 'h' for calculate history, 'x' for exit: ")

        else:
            over=False
        break

calculation()
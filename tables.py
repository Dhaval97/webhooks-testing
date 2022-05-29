def table(num):
    i = 1
    while i <= 10:
        ans = num * i
        print(num,'*',i,'=',ans)
        i += 1

a = int(input("Enter which table to print\n"))

while True:
    table(int(a))
    con = str(input("Do you want to continue: Yes or No\n"))

    if (con.upper() == "YES" or con.upper() == "Y"):
        a = int(input("Enter which table to print\n"))
    else:
        print("GoodBye!!!")
        break
    

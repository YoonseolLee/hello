n = int(input("정수를 입력하세요"))
for i in range(n):
    for j in range(n-1-i):
        print(" ", end = "")
    for j in range(i+1):
        print("*", end = " ")
    print()
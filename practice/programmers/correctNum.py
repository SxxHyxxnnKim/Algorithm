min =0
max = 100
answer = 33
while True :
    what = int(input("숫자 입력 ==>"))

    if what <0 or what >100 :
        print("insert right number in range(0~100)")

    elif what < min or what > max :
        print(f"insert right number in range({min}~{max})")

    elif what > answer :
        max = what
        print(f"less than {max}")
        print(f"the range of the number is {min}~{max}")
    
    elif what < answer :
        min = what
        print(f"greater than {min}")
        print(f"the range of the number is {min}~{max}")

    elif what == answer:
        print("correct!")
        print("answer is ", what)
        break;

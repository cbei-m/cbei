#시험 점수를 입력받아 90 ~ 100점은 A
#80 ~ 89점은 B
#70 ~ 79점은 C
#60 ~ 69점은 D
#나머지 점수는 F

a = int(input()) #점수

if a>=90:
    print("A")
elif a>=80:
    print("B")
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")
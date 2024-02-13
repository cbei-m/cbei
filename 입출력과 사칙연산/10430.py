A,B,C= input().split()
A,B,C = int(A), int(B), int(C)

#첫째 줄에 (A+B)%C, 
print((A+B)%C)
#둘째 줄에 ((A%C) + (B%C))%C, 
print(((A%C) + (B%C))%C)
#셋째 줄에 (A×B)%C, 
print((A*B)%C)
#넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
print(((A%C) * (B%C))%C)
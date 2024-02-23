input()
l = list(map(int, input().split()))
t = int(input())

ans = 0 #정답

# for i in l:
#     if i==t:
#         ans+=1
# print(ans)

ans = l.count(t)
print(ans)
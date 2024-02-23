input()
l = list(map(int, input().split()))
# 최대 = -1_000_000
# 최소 = 1_000_000

# for i in l:
#     if i>최대:
#         최대 = i
#     if i<최소:
#         최소 = i
# print(최소, 최대)

print(min(l), max(l))
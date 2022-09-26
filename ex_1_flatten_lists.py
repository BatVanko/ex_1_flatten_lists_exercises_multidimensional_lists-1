import strip as strip

sublist = input().split('|')
result = []

for i in range (len(sublist)-1,-1,-1):
    result.extend(sublist[i].strip().split())

print(*result, sep=' ')
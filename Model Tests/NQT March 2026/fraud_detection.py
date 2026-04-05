from collections import defaultdict

n = int(input())

groups = defaultdict(list)
transactions = []

for i in range(n):
    s, r, t, a = input().split()
    t = float(t)
    a = int(a)

    transactions.append((s,r,t,a))
    groups[(s,r,a)].append((i,t))

fraud = set()

for key in groups:
    lst = groups[key]

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):

            idx1,t1 = lst[i]
            idx2,t2 = lst[j]

            if abs(t1-t2) <= 1:
                fraud.add(idx1)
                fraud.add(idx2)

for i in sorted(fraud):
    s,r,t,a = transactions[i]
    t_str = ('%.2f' % t).rstrip('0').rstrip('.')
    print(s,r,t_str,a)
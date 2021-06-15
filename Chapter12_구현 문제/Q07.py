a = input()
n = len(a)>>1
left = a[:n]
right = a[n:]

l, r = 0, 0
for i in left:
    l += int(i)
for j in right:
    r += int(j)

if (l==r):
    print("LUCKY")
else:
    print("READY")
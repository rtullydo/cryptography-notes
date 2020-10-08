n = 37
m = n -1
i, q, r = 0,0,0
while True:
  q, r = divmod(m, 2)
  if r == 1:
    break
  m = q
  i = i + 1
print("%d has the form (2^%d)%d"%(n-1, i, m))

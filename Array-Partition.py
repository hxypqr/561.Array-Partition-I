sums=[3,25,2,35,3421,18000]
i=0
j=0
k=0
r=0
l=0
for i in range(0,5):
    k=sums[5-i]
    for j in range(0,6-i):

        if sums[j]>k:
            k=sums[j]
    for l in range(0,6-i):
        if sums[l]==k:
            break
    r=sums[5-i]
    sums[5-i]=k
    sums[l]=r
    print r
    print l
print sums
s=0
for i in range(0,6):
    if (i-1)%2!=0:
     s=s+sums[i]
     print s
print s

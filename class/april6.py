def pt(n):
    retL = []
    for a in range(1,n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                if a*a + b*b == c*c:
                    retL.append([a,b,c])
    return retL

def pt2(n):
    return [(a,b,c) 
            for a in range(1,n) 
            for b in range(a+1,n) 
            for c in range(b+1,n) 
            if a*a + b*b == c*c]
            
print pt(20)
print pt2(20)

# Quick Sort
# 1) Pick a Pivot
# 2) Partition into 2 Lists, st.
#   * All v's < p are LH
#   * All v's > p are UH
#   * Pivot in Final Resting Place
# 3) qsort(LH) + p + qsort(UH)
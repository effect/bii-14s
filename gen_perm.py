k = 3
def gen_perm (a,p,k):
	if p<k:
		for i in range (1, k+1):
			if i not in a:
				a[p] = i
				gen_perm (a, p+1, k)
				a[p] = 0
	else:
		print (a)
gen_perm ([0 for i in range (k)],0,k)

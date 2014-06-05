k = 3
def gen_bin(a,p):
	if p < k:
		a[p] = 0
		gen_bin(a, p+1)
		a[p] = 1
		gen_bin(a, p+1)
	else:
		print(a)

gen_bin([0 for i in range (k)], 0)

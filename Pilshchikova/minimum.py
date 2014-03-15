a = [3, 2, 7, 5]
if len(a) > 0:
	m = a[0]
	for i in a:
		if i < m:
			m = i
	print m
else:
	print 'No'
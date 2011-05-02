import operator
import time

def qsort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less, greater, equal = [], [], []
        for x in list:
            if x < pivot:
                less.append( x )
            elif x == pivot:
                equal.append( x )
            else:
                greater.append( x )

    return qsort(less) + equal + qsort(greater)

def merge(left,right):
	res=[]
	il=0,ir=0
	while (il < len(left)) or (ir < len(right)):
		if (il < len(left)) and (ir < len(right)):
			if left[il] <= right[ir]:
				res.append(left[il])
				il++
			else:
				res.append(right[ir])
				ir++
		elif il < len(left):
			res.append(left[range(il,len(left)-1] # gotta check on this
			il = len(left)
		elif ir < len(right):
			res.append(right[range(ir,len(right)-1]
			ir = len(right)
	return res

def merge_sort(list):
	if len(list) <= 1:
		return list
	else:
		l = len(list)
		imid = len(list)/2
		mid = list[imid]
		left, right = [], []
		for i in range(0,l):
			if i <= imid:
				left.append(list[i])
			elif i > imid:
				right.append(list[i])
	return merge(merge_sort(left) + merge_sort(right))

if __name__ == "__main__":
	d = [0,11.6,2,4.3,5.5,9,112,8,77.4,4]
	ftimes = 1000000
	t0 = time.clock()
	for i in range(0,ftimes):
		sorted = d
#		e = qsort(sorted)
		e = merge_sort(sorted)
		if not(i%100000):
			print e,time.clock()-t0
		
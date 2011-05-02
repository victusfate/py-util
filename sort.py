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

# mergesort not working at the moment. will fix later. clean versions from 
# http://en.literateprograms.org/Merge_sort_%28Python%29

def my_merge(left,right):
	res=[]
	il,ir = 0,0
	while il < len(left) or ir < len(right):
		print il,ir
		if il < len(left) and ir < len(right):
			if left[il] <= right[ir]:
				res.append(left[il])
				il=il+1
			else:
				res.append(right[ir])
				ir=ir+1
		elif il < len(left):
			res.extend(left[il:len(left)]) # gotta check on this
			il = len(left)
		elif ir < len(right):
			res.extend(right[ir:len(right)])
			ir = len(right)
		print il,ir
		
	return res
	
def nobodys_merge(left, right):
	result = []
	while len(left) or len(right):
		if len(left) and len(right):
			if left[0] <= right[0]:
				result.append(left[0])
				left = left[1:]
			else:
				result.append(right[0])
				right = right[1:]
		elif len(left):
			result.append(left[0])
			left = left[1:]
		elif len(right):
			result.append(right[0])
			right = right[1:]
	return result

def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	else:
		l = len(lst)
		imid = len(lst)/2
		mid = lst[imid]
		left, right = [], []
		for i in range(0,l):
			if i <= imid:
				left.append(lst[i])
			elif i > imid:
				right.append(lst[i])
	return my_merge(merge_sort(left),merge_sort(right))


def clean_merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def clean_mergesort(list):
    if len(list) < 2:
        return list
    else:
        middle = len(list) / 2
        left = clean_mergesort(list[:middle])
        right = clean_mergesort(list[middle:])
        return clean_merge(left, right)

if __name__ == "__main__":
	d = [0,11.6,2,4.3,5.5,9,112,8,77.4,4]
#	ftimes = 1000000
	ftimes = 1
	t0 = time.clock()
	for i in range(0,ftimes):
		sorted = d
		e = qsort(sorted)
#		e = merge_sort(sorted)
		if not(i%100000):
			print e,time.clock()-t0

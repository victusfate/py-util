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

# mergesort not working at the moment. will fix later.
def merge(left, right):
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

def cleaner_mergesort(list):
    if len(list) < 2:
        return list
    else:
        middle = len(list) / 2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
        return merge(left, right)

	
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
	return merge(merge_sort(left),merge_sort(right))

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

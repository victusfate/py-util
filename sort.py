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

# mergesort clean versions from 
# http://en.literateprograms.org/Merge_sort_%28Python%29

def merge(left,right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] # nifty syntax instead of result.extend(left[i,len(left)])
    result += right[j:]
    return result

def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	else:
		imid = len(lst)/2
		left = merge_sort(lst[:imid])
		right = merge_sort(lst[imid:])
		return merge(left,right)
		

if __name__ == "__main__":
	d = [0,11.6,2,4.3,5.5,9,112,8,77.4,4]
	ftimes = 1000000
#	ftimes = 1
	t0 = time.clock()
	for i in range(0,ftimes):
		sorted = d
#		e = qsort(sorted)
		e = merge_sort(sorted)
		if not(i%100000):
			print e,time.clock()-t0

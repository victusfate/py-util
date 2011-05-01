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


if __name__ == "__main__":
	d = [0,11.6,2,4.3,5.5,9,112,8,77.4,4]
	ftimes = 1000000
	t0 = time.clock()
	for i in range(0,ftimes):
		sorted = d
		e = qsort(sorted)
		if not(i%100000):
			print e,time.clock()-t0
		
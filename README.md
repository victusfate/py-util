<h1>qsort ala python</h1>
original source modified from this [stackoverflow question](http://stackoverflow.com/questions/4322823/how-to-make-this-naive-python-implement-of-quicksort-more-pythonic)
thanks Frankie, I'm learning from your learning

in case your curious here's it's execution time of a million sorts
with 0.7.1
<pre>
Mark-Essels-iMac:py-util messel$ python qsort.py
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 0.028202
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 2.341727
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 4.670012
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 7.012248
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 9.346553
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 11.666572
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 13.997745
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 16.314619
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 18.643811
[0, 2, 4, 4.2999999999999998, 5.5, 8, 9, 11.6, 77.400000000000006, 112] 20.968307
</pre>

with pypy 1.5 alpha
<pre>
Mark-Essels-iMac:py-qsort messel$ pypy qsort.py
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 0.000207
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 0.436853
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 0.775002
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 1.108878
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 1.449188
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 1.783163
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 2.12146
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 2.453842
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 2.786009
[0, 2, 4, 4.3, 5.5, 8, 9, 11.6, 77.4, 112] 3.117207
</pre>

whoa. 
that pypy version is not too shabby compared to my home brewed [c++ qsort](https://github.com/victusfate/proj)

<pre>
in place sorting 1000000 arrays 
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.000
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.097
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.194
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.292
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.388
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.485
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.583
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.680
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.777
sorted 0    2   4   4.3 5.5 8   9   11.6    77.4    112
in place method: 0.874
</pre>


# CMPS 2200 Assignment 1

**Name:** Ali Sulehria


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  No, the exponent is of  a higher degree and grows faster than 2^n, also having a higher initial value from n = 0 (2 vs. 1).
 
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  No, as with 1a, it is of a higher degree. 2^n > n for all n >= 0, so 2^(2^n) cannot exist on O(2^n)
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No, log^2(n) takes a lower value than n^1.01 to infinity.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, for the same reason as  1c: it is lower than n^1.01 for n approaching inifinity.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, as sqrt(n) grows faster than log(n)^3 forn values of n approaching infinity, though both diverge to infinity.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, for the same reason that 1d is false. log(n)^3 exists as a lower bound tp sqrt(n)


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  It takes in a value x, then finds the xth value in the fibonacci sequence.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

  The work of this implementation is of O(n) and the span is of O(1).
  The work is of O(n) because the loop will iterate through each element once and log the longest run as it iterates. 
  After one run of depth and work _n_, the longest run has been computed.
  The span is O(1) because there is no recursion or parallelism, so the depth remains 1 through all cases. 
  Parallelizing this algorithm would result in no speedup, as this implementation is linear.
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  

At each level, O(n) work is done. 
Given that the number of levels is of the order O(log(n)), the total work done is in O(nlogn). 
.  
Given that at each level, the work itself remains of the same order O(n), 
and the depth of the tree remains in the order O(logn), 
the span for a depth of O(logn) with O(n) work done at each level is O(nlogn), just as with the work.

This means that the span and work are greater than the iterative algorithm, and thus it is slower than the simple, sequential version.
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  Given that the work is the same (there's no change in the number of computations), it would remain the same at O(nlogN).

Span would be reduced to O(n), 
as the spawning of new threads in parallel brings down the depth of the tree while halving the work 
(since only 1 side of the array is considered with each split)
. 
.  


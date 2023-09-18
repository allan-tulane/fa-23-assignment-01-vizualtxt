"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      (ra, rb) = (foo(x-1), foo(x-2))
      return ra + rb
    
    pass

def longest_run(mylist, key):
    ### TODO
    longestRun = 0
    currentRun = 0

  # iterate through list, check key at each index, and add to the 
  # current run if key == mylist[i]. 
  # Otherwise, reset val of current run.
  # If current run > longest, then it's the new longest.
    for i in range(len(mylist)):
      if mylist[i] == key:
        currentRun += 1
        if currentRun > longestRun:
          longestRun = currentRun
      else:
        currentRun = 0
    return longestRun
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
#   I wasn't sure how to use the Result class, 
# so I included all relevant code in this fn definition.
def longest_run_recursive(mylist, key):
    ### TODO
    # empty and base cases
    if not mylist:
      return 0
    if len(mylist) == 1:
      return 1 if mylist[0] == key else 0
    
    # divide list and recursively find longest run
    cent = len(mylist) // 2
    leftHalf = mylist[:cent]
    rightHalf = mylist[cent:]
  
    longLeft = longest_run_recursive(leftHalf, key)
    longRight = longest_run_recursive(rightHalf, key)

    # check center for cutoff
    countLeft = 0
    i = cent - 1
    while i >= 0 and leftHalf[i] == key:
      countLeft += 1
      i -= 1
    countRight = 0
    i = 0
    while i < len(rightHalf) and rightHalf[i] == key:
      countRight += 1
      i += 1
    midLength = countRight + countLeft
    return max(midLength, longLeft, longRight)

    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([4,4,5,3,3,3,4,8,4,4,4,4,2,3,8,2,8], 4) == 4

def test_longest_run_recursive():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([4,4,5,3,3,3,4,8,4,4,4,4,2,3,8,2,8], 4) == 4


#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The Big O of this algo is O(n) because the while loop which is the limiting step in this code will run the n amount of times. Big O of other lines is 1 as they are independent of the n value

b)
The Big O of this algo is O(n log n) because we have two loops, a for loop whose BigO is O(n) because it's in range(n) and we have a while loop whose BigO is O(log n) because the j doubles after every itteration and reaches n logarithmically.

c)
The Big O of this algo is O(n) because it has recursion in it that calls with bunnies-1, so it will run the bunnies number of times :) 

## Exercise II

Use Binary Sort algo to test wether the egg will break or not. So cut the number of floors and 'drop' the egg from the middle. If it breaks, our solution is lower, if not, it is higher. This would be most time efficient solution and it's time complexity is O(log n) because I cut the sample size in half after each iteration

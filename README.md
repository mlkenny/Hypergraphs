# Repo Author
Michael Kenny
# Project Details
This project delves into the creation of a Hypergraph: an n-set that satifies the Sidon set condition and the square power condition.
At this given moment there have only been 2 examples of a hypergraph of girth 6.
The ultimate goal is to reach a general formula for a hypergraph of size n; Current goal is to find a hypergraph of girth 7.


# Project Goals
    1. Recreate functional hypergraph example sets of girth 3 and 4.
    2. Attempt to find more example sets of girth 5.
    3. If applicable, attempt to find more example sets of girth 6.

# Functional 6-set Solution
Consider the set {1, 35, 161, 170, 251, 545}

A set is considered a Sidon set if the differences of all the elements in the set are unique.
545 - 251           545 - 170           545 - 161           545 - 35          545 - 1
251 - 170           251 - 161           251 - 35            251 - 1
170 - 161           170 - 35            170 - 1
161 - 35            161 - 1
35 - 1

Then, if the given set is a Sidon set, the set exhibits the square products property if
you select any 4 of the elements within the Sidon set and find their differences, then multiply the product and find the
prime factorization of the product. Looking at the prime bases, if the exponent is odd then add the base to an auxiliary set.
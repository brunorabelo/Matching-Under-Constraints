# Matching under constraints

**Task 1:** 

​	We will prove the equivalence in both ways. First we assume that it's stable as defined in the introduction. As it's stable, it's fair, so no student has a justified envy towards any other, which is the definition of stability for Gale and Shapely.
​	We now assume that it's stable by the notions from Gale and Shapely. As we saw before, it's also fair. By the construction of the Gale Shapely problem, we can't match a student with a school that doesn't support him - as we will see in the next task, it's doable by multiplying each school by its capacity and then doing single matches with the students. So it's feasible. Using the same argument, it's also non-wasteful, because the Gale Shapely stability optimizes the matching choices, so if a student is whiling to go to a school and he can't, it must be that the school is already fully matched, hence adding the student wouldn't respect the constraint and it wouldn't be feasible. Finally, it's also individually rational. If it's possible, it's also going to be individual rational by optimality of Gale Shapely algorithm.

**Task 2:**

​	The idea to solve the problem is to use the Gale Shapely algorithm with an adapted set of lists of preferences. For this, we duplicate the preference of each school $s$ by $q_s$ in each students preference lists. Similarly we also duplicate the lists of preferences of each school  $s$ by $q_s$. The algorithm has the same complexity of Gale Shapely, as these operations are doable in time $n$. So in the end we still have a $n²$ 

**Task 3:**

The idea now is to make an additional if for checking is the group quota is still letting the match to happen. If it's not, we simply pass to the following school in the list. 

**Task 4**



**Task 5**



**Task 6**

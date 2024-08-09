# Formulation of the problem
The state space, the notes also use a succinct code to describe the configurations. This is the same as the image above:<br />
```
[[B, A], [C]] -> [[B, A, C]]
```
![blockworld](https://github.com/user-attachments/assets/9eb8c1cb-191c-49d9-ac29-7ab8d18d91ca)

Obviously, we can move only the pieces which are on top of any stack. We can also use all the ground space around. We will write the actions as follows:<br />
```
[[B, A], [C]] -> [[B, A, C]]
--------------------------
(B, 0) -> [[B], [A], [C]]
(A, C) -> [[B], [A, C]]
(B, A) -> [[B, A, C]]
```
Note that the order of stacks does not matter: <br />
```
[[B, A], [C]] == [[C], [B, A]]
```

# Solution of the problem

A heuristic function calculates the total number of elements in all stacks that are not in their correct positions when compared to the goal state. The lower the heuristic value, the closer the current state 
is to the goal state. It's a measure of how "far" the current configuration is from the goal. This heuristic is then used in a search algorithm like A* to find the optimal path to the goal.

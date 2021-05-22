# Water_Jug_Problem
Solution for water jug problem using state space technique using BFS ( Breadth First Search )

Here in the problem given a 4 litre jug and a 3 litre jug . Two jugs are empty at the start state. Jugs have no markings to measure the quantity.
Have to measure 2 litres using the above jugs. Here the 2 litres < 3 litres and 4 litres.

1. Initial State--> (0,0)
2. Desired/ Goal State--> (0,2) or (2,0)
3. Operators(Rules)
*Water in Jug1--> x
*Water in Jug2--> y
          (x, y) -> (0, y) if x > 0
          (x, y) -> (x, 0) if y > 0
          (x, y) -> (a, y) if x < a
          (x, y) -> (x, b) if y < b
          (x, y) -> (min(x+y, a), max(0, x+y - a)) if y > 0
          (x, y) -> (max(0, x+y - b), min(x+y, b)) if x > 0



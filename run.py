# Search methods
import search

problem = search.GPSProblem('A', 'B', search.romania)
breadth_result = search.breadth_first_graph_search(problem)
depth_result = search.depth_first_graph_search(problem)
branch_result = search.branch_and_bound_graph_search(problem)
heuristic_result = search.branch_and_bound_heuristic_graph_search(problem)

print("----------------------------------------------------------------------------------------------------------")
print("Recorrido en Amplitud:")
print("Ruta:", breadth_result[0].path(), "Generados:", breadth_result[1], "Visitados:", breadth_result[2],
      "Coste total:", breadth_result[0].path()[0].path_cost, "Tiempo de ejecución:", breadth_result[3], "ms")

print("----------------------------------------------------------------------------------------------------------")
print("Recorrido en Profundidad:")
print("Ruta:", depth_result[0].path(), "Generados:", depth_result[1], "Visitados:", depth_result[2],
      "Coste total:", depth_result[0].path()[0].path_cost, "Tiempo de ejecución:", depth_result[3], "ms")

print("----------------------------------------------------------------------------------------------------------")
print("Ramificación y Acotación:")
print("Ruta:", branch_result[0].path(), "Generados:", branch_result[1], "Visitados:", branch_result[2],
      "Coste total:", branch_result[0].path()[0].path_cost, "Tiempo de ejecución:", branch_result[3], "ms")

print("----------------------------------------------------------------------------------------------------------")
print("Ramificación y Acotación con Subestimación:")
print("Ruta:", heuristic_result[0].path(), "Generdos:", heuristic_result[1], "Visitados:", heuristic_result[2],
      "Coste total:", heuristic_result[0].path()[0].path_cost, "Tiempo de ejecución:", heuristic_result[3], "ms")

print("----------------------------------------------------------------------------------------------------------")
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

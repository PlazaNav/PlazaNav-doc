def test_compute_dijkstra_shortest_paths():
    graph_edges = [LineString([(0, 0), (0, 1)]), LineString([(0, 1), (1, 1)]),
                   LineString([(1, 1), (1, 0)]), LineString([(0, 0), (1, 0)]),
                   LineString([(0, 0), (1, 1)]), LineString([(1, 1), (2, 1)])]

    entry_points = [Point((0, 0)), Point((2, 1)), Point((1, 0))]
    expected_lines = [[(0, 0), (1, 1), (2, 1)], [(0, 0), (1, 0)], 
                      [(1, 0), (1, 1), (2, 1)]]

    graph = shortest_paths.create_graph(graph_edges)
    lines = shortest_paths.compute_dijkstra_shortest_paths(graph, entry_points)
    assert expected_lines == [list(line.coords) for line in lines]

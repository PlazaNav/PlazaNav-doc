def optimized_visibility_graph():
    visibility_graph = []
    for edge in all_edges:
        if edge_does_not_collide(edge):
            visibility_graph += edge
    for point in entry_points:
        paths = shortest_path_to_all(visibility_graph, entry_points)
        add_to_routing_graph(paths)

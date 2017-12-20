def create_spiderweb_graph(plaza_list):
    for plaza in plaza_list:
        spiderweb = draw_spiderweb(plaza)
        entry_points = get_entry_points(plaza, road_layer)
        connect_entry_points_with_spiderweb(entry_points, spiderweb)
        calculate_shortest_path(spiderweb)

def create_spiderweb_graph(plaza_list, building_layer, road_layer):
    for plaza in plaza_list:
        intersecting_buildings = find_buildings_inside_plaza(plaza, building_layer)
        spiderweb = draw_spiderweb(plaza, intersecting_buildings)
        entry_points = get_entry_points(plaza, road_layer)
        connect_entry_points_with_spiderweb(entry_points, spiderweb)
        shortest_path(spiderweb)

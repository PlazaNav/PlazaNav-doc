def create_spiderweb_graph(plaza_list, line_layer):
    for plaza in plaza_list:
        spiderweb = draw_spiderweb(plaza)
        intersecting_features = get_intersecting_features(plaza, line_layer)
        entry_points = get_entry_points(plaza, line_layer)
        connect_entry_points_with_spiderweb(entry_points, spiderweb)
        # TODO hier Schritte wie bei Visibility Graph um Hindernisse zu entfernen
        shortest_path(spiderweb)
        remove_unnecessary_lines(spiderweb)

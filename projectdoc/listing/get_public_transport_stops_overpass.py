def get_public_transport_stops(south, west, north, east):
    api = overpy.Overpass(url=API_URL)

    bbox = parse_bounding_box(south, west, north, east)

    query_str = """f
        [bbox:{bbox}];
        (
          node["public_transport"="stop_position"];
        );
        out body;
        """

    return api.query(query_str)

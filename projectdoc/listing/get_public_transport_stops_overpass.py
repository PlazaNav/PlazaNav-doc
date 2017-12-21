def get_public_transport_stops(start_position: tuple) -> dict:
    
    bbox = _parse_bounding_box(*start_position, BUFFER)
    
    query_str = f"""
        [bbox:{bbox}];
        node["public_transport"="stop_position"];node["highway"="bus_stop"];
        out body;
        rel["type"="public_transport"];
        out center;
        """

    public_transport_stops = _query(query_str)
    # ...

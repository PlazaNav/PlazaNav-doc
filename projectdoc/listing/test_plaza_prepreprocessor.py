@pytest.fixture(params=['visibility', 'spiderweb'])
def process_strategy(request):
    if request.param == 'visibility':
        return VisibilityGraphProcessor(visibility_delta_m=0.1)
    elif request.param == 'spiderweb':
        return SpiderWebGraphProcessor(spacing_m=5, visibility_delta_m=0.1)


@pytest.fixture(params=['astar', 'dijkstra'])
def shortest_path_strategy(request):
    if request.param == 'astar':
        return shortest_paths.compute_dijkstra_shortest_paths
    elif request.param == 'dijkstra':
        return shortest_paths.compute_astar_shortest_paths

def test_optimized_lines_inside_plaza(process_strategy, 
                                      shortest_path_strategy, config):
    # test PlazaPreprocessor
    # ...

def mock_get_connection(monkeypatch):
    monkeypatch.setattr(search_ch_service, "_query",
                        lambda payload:
                        utils.get_file(_get_get_connection_filename(payload), 
                                       'search_ch'))

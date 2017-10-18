class PlazaHandler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)

    def area(self, a):
        if isPlaza(a):
            # import as plaza

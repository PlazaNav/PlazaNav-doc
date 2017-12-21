from qgis.gui import QgsRubberBand

canvas = self.iface.mapCanvas()

rubber_band = QgsRubberBand(canvas, geometry_type)
rubber_band.setColor(color)
rubber_band.setWidth(width)

rubber_band.addPoint(start)
rubber_band.addPoint(destination)

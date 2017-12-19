# PlazaRoute Documentation

[![Build Status](https://travis-ci.org/PlazaRoute/doc.svg?branch=master)](https://travis-ci.org/PlazaRoute/doc)

This repository contains the PlazaRoute project documentation written in LaTeX. The PDF is built using Travis.

## Abstract

Today's most notable open source routing engines are optimized for motorized traffic but show deficiencies in pedestrian routing. With open spaces, routers usually navigate along the edges of the available area, whereas pedestrians would naturally take shortcuts through the open space while avoiding obstacles.
Past research has shown multiple approaches to this problem. This thesis compares a few of the approaches used to address this problem.

Utilizing publicly available geographic data from OpenStreetMap and the help of existing algorithms, an implementation is proposed to optimize geographic data for existing routing engines that enhances the capacity to produce pedestrian routing approximating natural behavior. The optimization is refined using shortest-path algorithms to minimize additional data volume.

Furthermore, the optimized pedestrian routing is used in combination with existing services for public transport routing in Switzerland, providing a practical application addressing multimodal transportation. With a newly-developed plugin for QGIS, users are able to visualize the optimized routes.

The implementation of two of the different approaches toward data processing, visibility graph and SpiderWeb graph, demonstrates a clear improvement of routes for pedestrian navigation compared to existing methodology utilized in current routing engines. In the future, this implementation could serve as a reference to integrate these approaches directly into routing engines to enhance the usability of these programs for pedestrians and provide an optimized user experience regardless of the method of transit.

The project is available under https://github.com/PlazaRoute
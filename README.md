# slippypkg

`slippypkg` is a simple Python application that uses FastAPI to expose a 
GeoPackage file's raster tiles over HTTP.

It is compatible with web tile-map (aka slippy-map hence the name) clients such
as Leaflet, OpenLayers etc.

The geopackage raster tiles must be 256x256 pixels and in PNG format.

For more information on GeoPackage files please see: https://www.geopackage.org/

## Tile URL format

The tiles can be accessed using URLs of the following form:

    http:///{table}/{z}/{x}/{y}

where:
 - `table` is the GeoPackage file's table holding the raster tiles
 - `z` is the zoom level
 - `x` and `y` are the tilemap grid coordinates of the tile at the given zoom 
   level


## Requirements

Python 3.6+

## Installation

Install the required dependencies using `pip` with the following command 
(using a Python virtual environment is highly recommended):

    pip install -r requirements.txt

Then install using `pip` from Github (requires `git` installed on your system):

    pip install git+https://github.com/cyberpython/slippypkg.git

## Execution

You can run the application using Uvicorn using the following command:

    GPKG_PATH=<path_to_gpkg_file> uvicorn slippypkg:app --host="0.0.0.0" --port=8000

where `<path_to_gpkg_file>` is the path to the GeoPackage file you want to use.
If the `GPKG_PATH` environment variable is not set, the application defaults to 
trying to load `map.gpkg` from the current working directory.

Please note that the `--host="0.0.0.0"` argument above will make the server 
accessible via all the network interfaces of the host system.
If you would like to allow access via only a specific network interface you can
replace `0.0.0.0` with the IP address of the specific network interface.

The server's listening port can be specified using the `--port` argument as 
shown above.

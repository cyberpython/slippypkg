#!/bin/env python3

# MIT License
#
# Copyright (c) 2022 Georgios Migdos
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.



# Python app that serves map tiles from a geopackage file.
# The geopackage tiles must be 256x256 pixels in PNG format.

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    gpkg_path: str = 'map.gpkg'

settings = Settings()

db_uri = f"sqlite:///{os.path.abspath(settings.gpkg_path)}"

database = Database(db_uri)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/{table}/{z}/{x}/{y}")
async def fetch_data(table, z, x, y):
    try:
        query = f"SELECT tile_data FROM '{table}' WHERE zoom_level = {int(z)} AND tile_column = {int(x)} and tile_row = {int(y)}"
        row = await database.fetch_one(query=query)
        if row is None:
            return Response(status_code=404)
        else:
            return Response(content=row["tile_data"], media_type="image/png")
    except:
        return Response(status_code=500)



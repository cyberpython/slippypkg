import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slippypkg",
    version="0.1.0",
    author="George Migdos",
    author_email="cyberpython@gmail.com",
    description="Python application that exposes a GeoPackage file's raster tiles as web map tiles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyberpython/slippypkg",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['databases','fastapi','uvicorn[standard]']
)
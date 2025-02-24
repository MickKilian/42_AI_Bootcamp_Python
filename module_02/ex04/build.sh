#!/bin/bash

# Remove old distribution files
rm -rf dist/

# Create the distribution files
python3 setup.py sdist bdist_wheel

echo "Build complete. You can install the package with:"
echo "pip install ./dist/my_minipack-1.0.0.tar.gz"
echo "or"
echo "pip install ./dist/my_minipack-1.0.0-py3-none-any.whl"

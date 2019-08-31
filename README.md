# conan-libtensorflow

This repository contains a basic recipe for packaging prebuilt tensorflow libraries into a Conan package.

### Setup for development

First, make sure you have conan installed
```bash
# From your Python environment
pip install conan
```

Copy in the repository folder the lib and include folders containing the tensorflow libraries.
```
cp -r $TENSORFLOW_LIB_DIR/lib .
cp -r $TENSORFLOW_LIB_DIR/include .
```

Create a build directory and initialize conan
```bash
mkdir -p build
cd build
conan install ..
```

Now you can export the package and upload it with conan
```bash
# From the build folder
conan export-pkg .. <account>/<channel>
conan upload libtensorflow -r totemic-private --all
```

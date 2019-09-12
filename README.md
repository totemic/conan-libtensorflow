# conan-libtensorflow

This repository contains a basic recipe for packaging prebuilt tensorflow libraries into a Conan package.

### Setup for development

First, make sure you have conan installed
```bash
# From your Python environment
pip install conan
```

Download tensorflow libraries for Linux and OSX
```
https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.13.1.tar.gz
https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.13.1.tar.gz
https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.13.1.tar.gz
```

Unpack them into a common base directory and make sure the directories are named the exact same way as the archives (without the `.tar.gz` suffix). The directories should contain a `lib` and and `include` folder.

In addition, create directories
```
libtensorflow-cpu-linux-armv8-1.13.1
libtensorflow-gpu-linux-armv8-1.13.1
````

and copy the self compiled versions into the `lib` and `include` directories.

Next, set the path to the root tensorflow directory in [conanfile.py](conanfile.py) in variable `tensorflow_location`


Next make sure to set the libraries to readable, otherwise conan cannot copy them during the `[import]` step in a `conanfile.txt` (it works the first time but then a read-only file cannot be overwritten by conan):

```
chmod -R 755 <tensorflow directory>
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

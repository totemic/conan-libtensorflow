#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools
from os.path import join, dirname, realpath

class LibTensorflowConan(ConanFile):
    name = "libtensorflow"
    version = "1.13.1"
    settings = "os", "arch"
    options = {"gpu": [True, False]}
    default_options = {"gpu": False}
    topics = ("conan", "tensorflow", "libtensorflow")
    homepage = "https://github.com/tensorflow/tensorflow"
    url = "http://github.com/hardsetting/conan-libtensorflow"
    license = "Apache License 2.0"
    description = "Tensorflow C API library."
    exports = ["LICENSE.md"]

    def configure(self):
        if self.settings.os != "Linux" and self.settings.os != "Macos":
            raise ConanInvalidConfiguration("This library is only supported on Linux and Macos")

    def triplet_name(self):
        if self.settings.os == "Linux":
            osname = "linux"
        elif self.settings.os == "Macos":
            osname = "darwin"

        gpuname = "gpu" if self.options.gpu else "cpu"

        return "libtensorflow-%s-%s-%s-%s" % (gpuname, osname, str(self.settings.arch), str(self.version))

    def package(self):
        if 'TF_ROOT' in os.environ:
            tensorflow_location = os.environ['TF_ROOT']
        else:
            tensorflow_location = os.environ['HOME'] + "/Develop/jetson/tensorflow/"
            # tensorflow_location = dirname(realpath(__file__))
            # raise RuntimeError('Please specifiy TF_ROOT in your environment.')

        prefix = join(tensorflow_location, self.triplet_name())
        print('Prefix: ', prefix)
        # copy the non-symlink versions first to avoid conan error when copying symlinks first
        self.copy(pattern="*.so."+str(self.version), dst="lib", src=prefix+"/lib", symlinks=True)
        self.copy(pattern="*.so.1", dst="lib", src=prefix+"/lib", symlinks=True)
        self.copy(pattern="*.so", dst="lib", src=prefix+"/lib", symlinks=True)
        self.copy(pattern="*", dst="include", src=prefix+"/include", symlinks=True)
        # self.copy("lib/*.so")
        # self.copy("include/*")

    def package_info(self):
        self.cpp_info.libs = ['tensorflow', 'tensorflow_framework']
        self.cpp_info.includedirs.append(os.path.join("include"))


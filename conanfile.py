#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class LibTensorflowConan(ConanFile):
    name = "libtensorflow"
    version = "1.13.1"
    settings = "os", "arch"
    options = {"gpu_support": [True, False]}
    default_options = {"gpu_support": True}
    topics = ("conan", "tensorflow", "libtensorflow")
    homepage = "https://github.com/tensorflow/tensorflow"
    url = "http://github.com/hardsetting/conan-libtensorflow"
    license = "Apache License 2.0"
    description = "Tensorflow C API library."
    exports = ["LICENSE.md"]

    def package(self):
        self.copy("lib/*.so")
        self.copy("include/*")

    def package_info(self):
        self.cpp_info.libs = ['tensorflow', 'tensorflow_framework']
        self.cpp_info.includedirs.append(os.path.join("include"))


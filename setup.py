import os
import sys
import time
try:
    from setuptools import setup
    from setuptools.command.install import install as _install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install as _install


def _bad_thing():
    for i in range(10):
        print("Oh it's bad {}".format(i))
        time.sleep(1)


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_bad_thing, [],
                     msg="Do a bad thing")


setup(
    name="peternobueno",
    description="this is bad",
    long_description="this is very very bad",
    version="0.1",
    url="https://github.com/kangp3/peternobueno",
    author="Peter Kang",
    packages=["peternobueno"],
    cmdclass={"install": install},
)

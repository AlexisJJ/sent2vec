# Automated install inspired by https://github.com/PyO3/pyo3/blob/master/examples/word-count/setup.py#L6
import subprocess
import sys

try:
    from Cython.Build import cythonize
except ImportError:

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "cython"])
    if errno:
        print("Automated install of cython failed. Please install it manually.")
        raise SystemExit(errno)
    else:
        from Cython.Build import cythonize


try:
    import numpy
except ImportError:

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "numpy"])
    if errno:
        print("Automated install of numpy failed. Please install it manually.")
        raise SystemExit(errno)
    else:
        import numpy


from distutils.core import setup
from distutils.extension import Extension

sourcefiles  = ['src/sent2vec.pyx', 
                'src/fasttext.cc', 
                "src/args.cc", 
                "src/dictionary.cc", 
                "src/matrix.cc", 
                "src/qmatrix.cc", 
                "src/model.cc", 
                'src/real.cc', 
                'src/utils.cc', 
                'src/vector.cc', 
                'src/real.cc', 
                'src/productquantizer.cc']
compile_opts = ['-std=c++0x', '-Wno-cpp', '-pthread', '-Wno-sign-compare']
ext=[Extension('*',
            sourcefiles,
            extra_compile_args=compile_opts,
            language='c++',
            include_dirs=[numpy.get_include()])]

setup(
  name='sent2vec',
  ext_modules=cythonize(ext)
)

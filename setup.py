import os
import sys
import shutil
from setuptools import setup

if sys.version_info.major != 3:
    raise RuntimeError("Wishbone requires Python 3")

with open("src/wishbone/version.py") as f:
    exec(f.read())

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="wishbone_dev",
    version=__version__,
    description=(
        "Wishbone algorithm for identifying bifurcating trajectories from "
        "single-cell data"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email="manu.talanki@gmail.com",
    package_dir={"": "src"},
    packages=["wishbone"],
    install_requires=[
        "numpy>=1.12.0",
        "pandas>=0.19.2",
        "scipy>=0.18.1",
        "Cython",
        "bhtsne",
        "matplotlib>=2.0.0",
        "seaborn>=0.7.1",
        "sklearn",
        "networkx>=1.11",
        "fcsparser>=0.1.2",
        "statsmodels>=0.8.0",
    ],
    scripts=["src/wishbone/wishbone_gui.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.6",
)

# get location of setup.py
setup_dir = os.path.dirname(os.path.realpath(__file__))

# install GSEA, diffusion components
tools_dir = os.path.expanduser("~/.wishbone/tools")
if os.path.isdir(tools_dir):
    shutil.rmtree(tools_dir)
shutil.copytree(setup_dir + "/tools/", tools_dir)
shutil.unpack_archive(tools_dir + "/mouse_gene_sets.tar.gz", tools_dir)
shutil.unpack_archive(tools_dir + "/human_gene_sets.tar.gz", tools_dir)

# Copy test data
data_dir = os.path.expanduser("~/.wishbone/data")
if os.path.isdir(data_dir):
    shutil.rmtree(data_dir)
shutil.copytree(setup_dir + "/data/", data_dir)

# Create directory for GSEA reports
os.makedirs(os.path.expanduser("~/.wishbone/gsea/"), exist_ok=True)

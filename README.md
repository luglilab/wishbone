Wishbone 
--------

Wishbone is an algorithm to align single cells from differentiation systems with bifurcating branches. Wishbone has been designed to work 
with multidimensional single cell data from diverse technologies such as Mass cytometry and single cell RNA-seq. 

#### Installation and dependencies
1. Wishbone has been implemented in Python3 and can be installed using

        $> pip install wishbone_dev

2. Wishbone depends on a number of `python3` packages available on pypi and these dependencies are listed in `setup.py`
All the dependencies will be automatically installed using the above commands

#### Usage

##### Command line
A tutorial on Wishbone usage and results visualization for single cell RNA-seq data can be found in this notebook: http://nbviewer.jupyter.org/github/ManuSetty/wishbone/blob/master/notebooks/Wishbone_for_single_cell_RNAseq.ipynb


A tutorial on Wishbone usage and results visualization for mass cytometry data can be found in this notebook: http://nbviewer.jupyter.org/github/ManuSetty/wishbone/blob/master/notebooks/Wishbone_for_mass_cytometry.ipynb


##### GUI
A python GUI is now available for Wishbone. After following the installation steps listed below, the GUI can be invoked using

        $> wishbone_gui.py

A tutorial on using the interface is available in the [Wishbone tutorial](docs/wishbone_tutorial.pptx).


#### Citation

Wishbone manuscript is available from [Nature Biotechnology](https://www.nature.com/articles/nbt.3569). If you use Wishbone for your work, please cite our paper.

        @article{Wishbone_2016,
                title = {Wishbone identifies bifurcating developmental trajectories from single-cell data},
                author = {Manu Setty and Michelle D Tadmor and Shlomit Reich-Zeliger and Omer Angel and Tomer Meir Salame and Pooja Kathail and Kristy Choi and Sean Bendall and Nir Friedman and Dana Pe'er},
                journal = {Nature Biotechnology},
                year = {2016},
                month = {may},
                url = {http://dx.doi.org/10.1038/nbt.3569},
                doi = {doi:10.1038/nbt.3569}
        }
                
#### Data availability
FCS files for the mouse thymus data can be downloaded from the following links 
[Thymus, Panel 1- Replicate 1](https://dp-lab-data-public.s3.amazonaws.com/wishbone/wishbone_thymus_panel1_rep1.fcs)
[Thymus, Panel 1- Replicate 2](https://dp-lab-data-public.s3.amazonaws.com/wishbone/wishbone_thymus_panel1_rep2.fcs)
[Thymus, Panel 1- Replicate 3](https://dp-lab-data-public.s3.amazonaws.com/wishbone/wishbone_thymus_panel1_rep3.fcs)
[Thymus, Panel 2- Replicate 1](https://dp-lab-data-public.s3.amazonaws.com/wishbone/wishbone_thymus_panel2_rep1.fcs)
[Thymus, Panel 2- Replicate 1](https://dp-lab-data-public.s3.amazonaws.com/wishbone/wishbone_thymus_panel2_rep2.fcs)

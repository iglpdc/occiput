
# occiput - Computational engine for volumetric imaging 
# Stefano Pedemonte
# Harvard University, Martinos Center for Biomedical Imaging 
# Dec 2013, Boston 


# Use old Python build system, otherwise the extension libraries cannot be found. FIXME 
import sys
for arg in sys.argv: 
    if arg=="install":
        sys.argv.append('--old-and-unmanageable') 

from setuptools import setup, Extension
from glob import glob 


setup(
    name='occiput',
    version='0.4.4',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['occiput', 
              'occiput.test', 
              'occiput.notebooks',
              'occiput.Core',
              'occiput.Reconstruction', 
              'occiput.Reconstruction.PET', 
              'occiput.Reconstruction.SPECT', 
              'occiput.Reconstruction.CT', 
              'occiput.Reconstruction.MR',
              'occiput.Transformation', 
              'occiput.Registration',
              'occiput.Registration.Affine',
              'occiput.Registration.TranslationRotation',
              'occiput.Classification', 
              'occiput.DataSources', 
              'occiput.DataSources.Synthetic', 
              'occiput.DataSources.FileSources', 
              'occiput.Visualization',
              ],
    package_data={'occiput': ['Data/*.pdf','Data/*.png','Data/*.jpg','Data/*.svg','Data/*.nii','Data/*.dcm','Data/*.h5','Data/*.txt','Data/*.dat']},
    scripts=[],
    url='http://www.occiput.io/',
    license='LICENSE.txt',
    description='Tomographic Vision - PET, SPECT, CT, MRI reconstruction and processing.',
    long_description=open('README.rst').read(),
    keywords = ["PET", "SPECT", "emission tomography", "transmission tomography", "tomographic reconstruction","nuclear magnetic resonance"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
                     ],
    install_requires=[
        "numpy >= 1.6.0", 
        #"scipy >= 0.14.0",
        #"pil >= 1.0.0",
        "matplotlib >= 1.4.0",
        "simplewrap >= 0.3.0",
        "petlink >= 0.3.0",  
        "interfile >= 0.3.0", 
        "DisplayNode >= 0.3.0", 
        "ilang >= 0.3.0", 
        "ipy_table >= 1.11.0",
        "nibabel >= 2.0.0",  
        "pydicom >= 0.9.0",
        "nipy >= 0.3.0",
        "ipython >= 2.0.0",
        "h5py >= 2.3.0",
    ], 
) 



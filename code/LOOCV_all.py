#!/usr/bin/env python

import pandas as pd 
import numpy as np
import os
from pathlib import Path 
from nimare.correct import FWECorrector
from nimare.dataset import Dataset
from nimare.utils import get_resource_path
import matplotlib.pyplot as plt
from nilearn.plotting import plot_stat_map
from nimare.correct import FDRCorrector
from nimare.generate import create_coordinate_dataset
from nimare.meta import ALE
from nimare.meta.cbma.mkda import MKDADensity
from nimare.meta.cbma import ALESubtraction
from nimare.io import convert_sleuth_to_dataset,convert_sleuth_to_dict
import datetime

print("")
now = datetime.datetime.now()
print ("Script Starting - Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("")
print("#################################################################")
print("")

# change dir
os.chdir('C:\\Users\\jmerch\\Documents\\Meta\\GitHub')
os.getcwd()


dset_file = "./data/coordinate_datasets/All_dset.pkl"
dset = Dataset.load(dset_file)
IDs=dset.ids

# Loop through the IDs
for x in range(len(IDs)):
    
    # reload everytime
    dset_file = "./data/coordinate_datasets/All_dset.pkl"
    dset = Dataset.load(dset_file)
    Ones=np.ones(len(IDs))
    dset.annotations['all']=Ones
    ones=Ones
    ones[x]=0
    dset.annotations['all']=ones
    
    # get studies
    dset_cur_idx = dset.get_studies_by_label("all")
    dset_cur = dset.slice(dset_cur_idx)
    #print(len(dset_cur.ids))
    
    meta = ALE()
    corr = FWECorrector(method="montecarlo", n_iters=1000, n_cores=10)
    
    print("")
    print("##############################")
    now = datetime.datetime.now()
    print ("ALE Starting - Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    results = meta.fit(dset_cur)

    cres = corr.transform(results)

    # create file name prefix for current iteration
    cur_file='./results/loocv/iter_' + str(f'{x:03d}') + '.nii.gz'

    # use nilearn to binarize image and save 
    binimage=binarize_img(cres.get_map("z_desc-size_level-cluster_corr-FWE_method-montecarlo"))
    binimage.to_filename(cur_file) # save binarized thresholded image


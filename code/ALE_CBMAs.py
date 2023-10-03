# REQUIRED USE OF NILEARN v0.10.1
import pandas as pd 
import numpy as np
import os
from pathlib import Path 
from nimare.correct import FWECorrector
from nimare.dataset import Dataset
from nimare.utils import get_resource_path
import matplotlib.pyplot as plt
from nilearn.plotting import plot_stat_map
from nimare.dataset import Dataset
from nimare.correct import FDRCorrector
from nimare.generate import create_coordinate_dataset
from nimare.meta import ALE
from nimare.meta.cbma.mkda import MKDADensity
from nimare.meta.cbma import ALESubtraction

from nimare.io import convert_sleuth_to_dataset,convert_sleuth_to_dict
from nimare.diagnostics import FocusCounter
from nimare.diagnostics import Jackknife
from nilearn.plotting import plot_stat_map
from nilearn.reporting import get_clusters_table
from datetime import datetime

# Change and define directories
os.chdir('C:\\Users\\jmerch\\Documents\\Meta\\GitHub')
os.getcwd()
InDir=os.path.abspath("./results/cbma/")
TxtDir=os.path.abspath("./data/coordinate_datasets/GingerALEtextFiles/")


Files=os.listdir(InDir)


# Start loop through files
for f in range(len(Files)):
    
    # set up ALE estimator and correction
    meta = ALE(n_cores=10)
    corr = FWECorrector(method="montecarlo", n_iters=10000, n_cores=10)

    # define current file and print time
    Short=Files[f]
    print('============================================')
    print(Short)
    print("")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Start Time =", current_time)
    print("")
    
    # define in dir
    indir=InDir + Short + '\\'
    
    # read in data
    Dset=convert_sleuth_to_dataset(TxtDir + Short + "_byStudy.txt")
    Dset.save(indir + Short + "_dset.pkl")

    # set up ALE estimator and correction
    meta = ALE(n_cores=10)
    corr = FWECorrector(method="montecarlo", n_iters=10000, n_cores=10)

    # start meta fit and correction
    print('meta-fit')
    print("")
    results = meta.fit(Dset)
    results.save_maps(output_dir=indir, prefix=Short + "_UnThr", prefix_sep='_')
    results.save(indir + Short + "_ALE_UnThrResults.pkl")


    print('correction')
    print("")
    cres = corr.transform(results)
    
    print("")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Fit and correction ended at =", current_time)
    print("")

    # Focus counter
    print('focus counter')
    print("")
    counter = FocusCounter(
    target_image="z_desc-size_level-cluster_corr-FWE_method-montecarlo",
    voxel_thresh=None,n_cores=10)

    cres = counter.transform(cres)

    # Jacknife
    print('jackknife')
    print("")
    jackknife = Jackknife(
    target_image="z_desc-size_level-cluster_corr-FWE_method-montecarlo",
    voxel_thresh=None,n_cores=10)

    cres = jackknife.transform(cres)

    print("")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("diagnostics ended at =", current_time)
    print("")

    # save data
    print('saving results')
    print("")
    cres.save_maps(output_dir=indir, prefix=Short + "_FWE", prefix_sep='_')
    cres.save(indir + Short + "_ALE_FWEResults.pkl")
    cres.save_tables(output_dir=indir, prefix=Short + "_Coordinates", prefix_sep='_')

    print("")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("saving ended at =", current_time)
    print("")
    print('============================================')
    del(cres)
    del(results)
    del(Dset)


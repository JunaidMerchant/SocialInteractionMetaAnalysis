#!/usr/bin/env python

# REQUIRED USE OF NILEARN v0.100

import os
import pandas as pd
import nibabel as nib
import numpy as np
from nilearn.plotting import plot_roi
from nilearn import datasets, image, plotting
from nimare.dataset import Dataset
from nimare.decode import discrete
from nimare.utils import get_resource_path
from nimare.decode import continuous
from nimare.utils import get_template
from nilearn.image import resample_to_img
import datetime
import pathlib
import glob

# change directories
os.chdir('C:\\Users\\jmerch\\Documents\\Meta\\GitHub')
os.getcwd()

# define directories and datasets
ds_dir = os.path.abspath("./data/coordinate_datasets/")
out_dir1 = os.path.abspath("./results/decode/ns_ALLclusters/")
roi_dir = os.path.abspath("./data/rois/clusters/")

# read in ROI images
roi_files=os.listdir('./data/rois/clusters')


rois=[s.replace('Clust_', '') for s in roi_files]
rois=[s.replace('.nii.gz', '') for s in rois]
rois=[s.split('_')[1] for s in rois]


data_sets = 'LDA50 LDA100 LDA200 LDA400'.split()


for d in range(len(data_sets)):

    # load dataset
    NS = Dataset.load(ds_dir + "\\" + "Neurosynth_" + data_sets[d] + "_dataset.pkl.gz")

    print("current ds: ")
    print(data_sets)
    print("")

    template = get_template()


    # loop through ROIs
    for r in range(len(roi_files)):
        
        # get current file
        cur_file = pathlib.Path(roi_files[r])
        
        # set output folder
        out_dir = out_dir1 + "\\" + rois[r] + "\\"
        if not os.path.exists(out_dir1 + "\\" + rois[r]):
            os.makedirs(out_dir1 + "\\" + rois[r])
        
        # roiname = cur_file.name[0:-4]
        roiname = rois[r]

        print(roiname)
        roi_img1= image.load_img(roi_dir + "/" + roi_files[r])
        roi_img = resample_to_img(roi_img1,template,interpolation='nearest')
        # print("")

        # AllRoiImg1 = image.load_img(cur_file)
        # AllRoiImg = resample_to_img(AllRoiImg1, template)
        AllRoiStudies=NS.get_studies_by_mask(roi_img)
        
        print(f"{len(AllRoiStudies)}/{len(NS.ids)} studies report at least one coordinate in the ROI")
        
        # Run BrainMapDecoder discrete
        if not os.path.isfile(out_dir + "/" + roiname + "_BrainMapDecoder_" + data_sets[d] + ".csv"):
            print('working on BrainMapDecoder')
            decoder = discrete.BrainMapDecoder()
            decoder.fit(NS)
            decoded_df = decoder.transform(ids=AllRoiStudies)
            decoded_df.sort_values(by="zReverse", ascending=False,inplace=True)
            decoded_df.to_csv(out_dir + "/" + roiname + "_BrainMapDecoder_" + data_sets[d] + ".csv")


        # Run NeurosynthDecoder discrete
        if not os.path.isfile(out_dir + "/" + roiname + "_NeurosynthDecoder_" + data_sets[d] + ".csv"):
            print('working on NeurosynthDecoder')
            decoder = discrete.NeurosynthDecoder()
            decoder.fit(NS)
            decoded_df = decoder.transform(ids=AllRoiStudies)
            decoded_df.sort_values(by="zReverse", ascending=False,inplace=True)
            decoded_df.to_csv(out_dir + "/" + roiname + "_NeurosynthDecoder_" + data_sets[d] + ".csv")

        # Run ROIAssociationDecoder discrete
        if not os.path.isfile(out_dir + "/" + roiname + "_ROIAssociationDecoder_" + data_sets[d] + ".csv"):
            print('working on ROIAssociationDecoder')
            decoder = discrete.ROIAssociationDecoder(roi_img)
            decoder.fit(NS)
            # The `transform` method doesn't take any parameters.
            decoded_df = decoder.transform()
            decoded_df.sort_values(by="r", ascending=False,inplace=True)
            decoded_df.to_csv(out_dir + "/" + roiname + "_ROIAssociationDecoder_" + data_sets[d] + ".csv")

        
        print('----')
        print('')

        # print time 
        print("")
        now = datetime.datetime.now()
        print ("Script Starting - Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print("")
        print("#################################################################")
        print("")
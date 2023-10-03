#!/usr/bin/env python

# REQUIRED USE OF NILEARN v0.100
import pandas as pd 
import numpy as np
import os
from pathlib import Path 
from nilearn.image import resample_to_img
from nimare.correct import FWECorrector
from nimare.dataset import Dataset
from nimare.utils import get_resource_path
import datetime
from nimare.correct import FDRCorrector
from nimare.generate import create_coordinate_dataset
from nimare.meta import ALE
from nimare.meta.cbma.mkda import MKDADensity
from nimare.meta.cbma import ALESubtraction
from nimare.dataset import Dataset
from nimare.meta.cbma.ale import SCALE
from nimare.meta.cbma.mkda import MKDAChi2
from nimare.extract import download_abstracts, fetch_neuroquery, fetch_neurosynth
import nibabel as nib
import numpy as np
from nilearn import datasets, image, plotting
from nimare.correct import FWECorrector
from nimare.utils import get_template
from nimare.meta.kernel import ALEKernel
from nimare.results import MetaResult

# print time 
print("")
now = datetime.datetime.now()
print ("Script Starting - Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("")
print("#################################################################")
print("")

# change directories
os.chdir('C:\\Users\\jmerch\\Documents\\Meta\\GitHub')
os.getcwd()

# define directories and datasets
ds_dir = os.path.abspath("./data/coordinate_datasets")
out_dir = os.path.abspath("./results/macm/clusters/")
roi_dir = os.path.abspath("./data/rois/clusters/")
data_sets = 'Neurosynth_dataset'
d = 'Neurosynth_dataset'


########################################################################################################################
# resample to template
# template = load_mni152_template(resolution=2)
# template = get_template(space='ale_2mm')
template = get_template()

# read in ROI images
roi_files=os.listdir('./data/rois/clusters')


rois=[s.replace('Clust_', '') for s in roi_files]
rois=[s.replace('.nii.gz', '') for s in rois]
rois=[s.split('_')[1] for s in rois]

print("working on: ")
print(d)
print("")

# load dataset
dset = Dataset.load(ds_dir + "/" + d + ".pkl.gz")

r=0

# while loop through ROIs
while r < len(roi_files):

	# define out put directory
	out = out_dir + "\\" + rois[r]

	if os.path.exists(out + "\\" + rois[r] + "_MACM_FWEResults.pkl"):
		r += 1 
		continue
	else: 
		if not os.path.exists(out):
			os.makedirs(out)

		############## MKDAchi2 ##############

		# print time
		print("")
		print("##############################")
		now = datetime.datetime.now()
		print("For " + rois[r])
		print ("MKDAchi2 Starting - Current date and time : ")
		print (now.strftime("%Y-%m-%d %H:%M:%S"))
		print("")


		# MKDA Chi2 with FWE correction
		if os.path.exists(out + "\\" + rois[r] + "_MACM_UnThrResults.pkl"):
			print("loading unthresholded results:")
			# now = datetime.datetime.now()
			# print (now.strftime("%Y-%m-%d %H:%M:%S"))
			results=MetaResult.load(out + "\\" + rois[r] + "_MACM_UnThrResults.pkl")
			print('')
		else:
			print("estimating unthresholded results:")
			now = datetime.datetime.now()
			print (now.strftime("%Y-%m-%d %H:%M:%S"))
			roi_img1= image.load_img(roi_dir + "/" + roi_files[r])
			roi_img = resample_to_img(roi_img1,template,interpolation='nearest')

			# Select studies with a reported coordinate in the ROI
			roi_ids = dset.get_studies_by_mask(roi_img)
			dset_sel = dset.slice(roi_ids)
			print(f"{len(roi_ids)}/{len(dset.ids)} studies report at least one coordinate in the ROI")

			# Select studies with no reported coordinates in the ROI
			no_roi_ids = list(set(dset.ids).difference(roi_ids))
			dset_unsel = dset.slice(no_roi_ids)
			print(f"{len(no_roi_ids)}/{len(dset.ids)} studies report zero coordinates in the ROI")
			mkda = MKDAChi2(kernel__r=10)
			results = mkda.fit(dset_sel, dset_unsel)
			results.save_maps(output_dir=out, prefix=rois[r] + "_UnThr", prefix_sep='_')
			results.save(out + "\\" + rois[r] + "_MACM_UnThrResults.pkl")
			print('')


		print("estimating FWE thresholded results:")
		now = datetime.datetime.now()
		print (now.strftime("%Y-%m-%d %H:%M:%S"))
		print('')
		corr = FWECorrector(method="montecarlo", n_iters=1000,n_cores=10)
		cres = corr.transform(results)
		cres.save_maps(output_dir=out, prefix=rois[r] + "_FWE", prefix_sep='_')
		cres.save(out + "\\" + rois[r] + "_MACM_FWEResults.pkl")

		# print time
		print("")

		now = datetime.datetime.now()
		print("Finished: " + rois[r] + " at:")
		print (now.strftime("%Y-%m-%d %H:%M:%S"))
		print("")
		print("##############################")
		del(cres)

		r += 1 

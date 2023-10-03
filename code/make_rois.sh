#!/bin/bash

## THIS IS FOR THE THRESHOLDED CLUSTERS FROM ALL META-ANALYSIS

# change into the right directory
cd "C:\\Users\\jmerch\\Documents\\Meta\\GitHub"

# define the outdirs, ROI names, and in files
OutDir="./data/rois/clusters/"
RoiNames="./data/rois/RoiNames.txt"
InFile="./results/cbma/ALL/ALL_FWE_label_tail-positive.nii.gz"

# loop through 17 lines of text
for n in `seq 1 9`; do

# get name
Name=${OutDir}Clust_$(printf "%02d" ${n})_$(more ${RoiNames} | head -n ${n} | tail -n 1).nii.gz

# use fslmaths to threshold and binarize
fslmaths ${InFile} -thr $n -uthr $n -bin $Name
done


## THIS IS FOR CREATING SPHERE ROIS PEAKS OF CLUSTERS FROM ALL META-ANALYSIS
## USING 6 MM TO MATCH THE WHAT NEUROSYNTH DOES

# define the outdirs, ROI names, and in files
OutDir="./data/rois/spheres/"
RoiNames="./data/rois/RoiNames.txt"
InFile="./results/cbma/ALL/ALL_FWE_label_tail-positive.nii.gz"
Coordinates="./data/rois/Coordinates.txt"
ALL_6mmSphereRoiFile="./data/rois/ALL_9_6mmSphere_Rois.nii.gz"


# # create one file with all ROIs
3dUndump -master ${InFile} -prefix ${ALL_6mmSphereRoiFile} -orient LPI -xyz ${Coordinates}

# loop through 17 lines of text
for n in `seq 1 9`; do

# get name
Name=${OutDir}Sphere_$(printf "%02d" ${n})_$(more ${RoiNames} | head -n ${n} | tail -n 1)_6mm.nii.gz

# use fslmaths to threshold and binarize
fslmaths ${ALL_6mmSphereRoiFile} -thr $n -uthr $n -bin $Name
done

############## REDO WITH 14 ROIs of SUBPEAKS IN ALL
# define the outdirs, ROI names, and in files
OutDir="./data/rois/spheres14/"
RoiNames="./data/rois/RoiNames14.txt"
InFile="./results/cbma/ALL/ALL_FWE_label_tail-positive.nii.gz"
Coordinates="./data/rois/Coordinates14.txt"
ALL_6mmSphereRoiFile="./data/rois/ALL_14_6mmSphere_Rois.nii.gz"


# # create one file with all ROIs
3dUndump -master ${InFile} -prefix ${ALL_6mmSphereRoiFile} -orient LPI -xyz ${Coordinates}

# loop through 17 lines of text
for n in `seq 1 14`; do

# get name
Name=${OutDir}Sphere_$(printf "%02d" ${n})_$(more ${RoiNames} | head -n ${n} | tail -n 1)_6mm.nii.gz

# use fslmaths to threshold and binarize
fslmaths ${ALL_6mmSphereRoiFile} -thr $n -uthr $n -bin $Name
done
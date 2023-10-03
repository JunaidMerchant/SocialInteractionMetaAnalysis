# Coordinate Datasets

This folder contains NiMare coordinate datasets saved in pythons pickle format, including the datasets used to run our ALE CBMAs, as well as Neurosynth and Brainmap datasets we used to run conduct meta-analytic coactivation modeling (MACM) and functional decoding analyses.


## Datasets used to run the Social Interaction ALE CBMAs are as follows: 

"All" overarching CBMA of 108 studies - ```./ALL_dset.pkl```

"Social Engagement" CBMA of contrasts using non-social, but interactive control condition - ```./SocialEngagement_dset.pkl```

"Interaction" CBMA of contrasts using social, but non-interactive control condition - ```./Interaction_dset.pkl```

"Human vs Computer" CBMA of contrasts using interaction with computer/robot as control condition - ```./HvC_dset.pkl```

"Initiating" CBMA of contrasts wherein participants initiates interactive behavior - ```./Initiating_dset.pkl```

"Responding" CBMA of contrasts wherein participants respond to interactive behavior - ```./Responding_dset.pkl```


## Larger neuroimaging datasets used to conduct MACM and functional decoding analysis: 

Brainmap database of 4,226 papers used for functional decoding of behavioral domains and paradigm classes - ```./BrainMap_dataset.pkl.gz```

Neurosynth database of 14,371 studies used for MACM - ```./Neurosynth_dataset.pkl.gz```

Neurosynth database of 50 LDA-derived topics for functional decoding - ```./Neurosynth_LDA50_dataset.pkl.gz```

Neurosynth database of 100 LDA-derived topics for functional decoding - ```./Neurosynth_LDA100_dataset.pkl.gz```

Neurosynth database of 200 LDA-derived topics for functional decoding - ```./Neurosynth_LDA200_dataset.pkl.gz```

Neurosynth database of 400 LDA-derived topics for functional decoding - ```./Neurosynth_LDA400_dataset.pkl.gz```


### GingerALE compatible text files can be found in ```./GingerALEtextFiles/```
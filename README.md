# Brain bases of real-time social interaction: A meta-analytic investigation of human neuroimaging studies

This repository contains data, code, and hands-on example notebooks to accompany the submitted manuscript entitled "Brain bases of real-time social interaction: A meta-analytic investigation of human neuroimaging studies". 


![alt text](https://github.com/JunaidMerchant/SocialInteractionMetaAnalysis/blob/main/image.png)

## Repository

```/WalkThroughExamples.ipynb``` is interactive Python Jupyter Notebook that provides a hands-on walk through the different analyses conducted for this project. It includes code for running coordinate-based meta-analyses (CBMA) using the activation Likelihood Estimation (ALE) approach, leave one study out cross-validation (LOOCV) of CBMA, diagnostics of significant clusters, visualizing results and coordinates tables, and tips on how to build off this repository to conduct novel analyses.

```/code ``` contains the run code used to conduct the analyses presented in the main and supplemental text

```/data ``` contains spreadsheets for study meta-data, coordinates, and contrast annotations for each of the studies used in our social interaction coordinate-based meta-analyses (CBMA)
```/data/coordinate_datasets ``` contains NiMare coordinate datasets for the overarching and sub-CBMAs, and Neurosynth and Brainmap datasets for meta-analytic coactivation modeling (MACM) and functional decoding analyses.
```/data/fc ``` contains resting-state functional connectivity maps for each of the 14 sub-peaks of the overarching CBMA as seeds. These data were obtained from neurosynth.org
```/data/rois ``` contains regions of interest (ROI) masks for each of the 9 significant clusters from the overarching CBMA, and spherical ROIs with a 6 mm radius centered around each of the 14 sub-peaks. 

```/results ``` contains all the results files for the analyses implemented for the manuscript.
```/results/cbma ``` contains results for each of the CBMAs we conducted, including thresholded and unthresholded whole-brain maps ALE and stats maps, coordinates tables, and NiMare results objects
```/results/decode``` contains results for functional decoding of each cluster and spherical ROI using the Brainmap and Neurosynth LDA datasets
```/results/loocv``` contains results for the leave one (study) out cross-validation (LOOCV) analysis
```/results/macm``` contains meta-analytic coactivation modeling (MACM) results for each cluster and spherical ROI using the Neurosynth database


## Abstract 
**Background:** Social interactions play a central role in shaping brain function, but neuroscientific research on interactive social behavior has been limited by the restrictions of brain imaging environments. A growing body of neuroimaging research is situating participants in real-time social interactive contexts. However, there are still open questions about the brain systems that are critical for social interaction. This study aims to address three primary questions: 1) Is there a common network of brain regions that underlies diverse forms of social interaction? 2) Are there dissociable brain systems that contribute different aspects of social interactive behavior? 3) What are the brain networks and cognitive functions associated with the socially interactive brain?
**Methods:** We implemented a systematic search of the human neuroimaging literature to find studies involving social interaction – participants were socially engaged and interacted with perceived social partners in real-time – that contrasted against non-socially interactive control conditions. We used coordinate-based meta-analysis (CBMA) of 108 studies to elucidate common social interaction brain regions. We further analyzed different subsets of studies to probe social engagement with a human (versus non-human) partner, interaction (versus non-interactive) social contexts, and reciprocal initiating (participant elicits a response from a partner) and responding (to partners actions). Finally, we used the Brainmap and Neurosynth databases to conduct meta-analytic coactivation modeling (MACM) and functional decoding to better characterize the neurocognitive systems associated with social interaction.
**Results:** The overarching CBMA uncovered significant convergence in nine brain areas that cut across different large-scale brain networks. Follow-up analyses suggest that regions of the reward system contribute to perceived social engagement, regions of the ventral attention network are associated with reciprocal interaction, and partially dissociable brain systems relate to initiating and responding behaviors. MACM and functional decoding results suggest that 3-4 overlapping neurocognitive systems underlie social interaction: a social cognition system that includes temporoparietal junction, medial prefrontal cortex, and precuneus; lateral frontoparietal regions associated with cognitive control processes; and intermediary midcingulo-insular areas that is associated with social alignment and empathy. 
**Conclusion:**  The current study used a data-driven investigation of the neuroimaging literature to advance our understanding of the neural and cognitive systems important for human social interaction. Our findings suggest that the myriad forms of social interaction may be subserved by a common network of brain areas that are otherwise associated with multiple different neurocognitive systems, and adds support to emerging theories proposing the centrality social interaction in human brain function. 

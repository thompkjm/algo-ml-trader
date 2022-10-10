# algo-ml-trader
## Overview
The idea stemmed from our belief that the irony of technical analysis is the more people that believe in it, the more effective it is.
Thus, the simpler the strategy the more likely it is efficient.
SMA is the most commonly used signal, and is very proven to be profitable. Thus, finding a way where you can manage to generate alpha over this strategy should be effective.

## Usage
The order to run the files is bestwindows.py (takes around 2 hours to run, don't have to run it to run the next notebook) -> bestwindows.ipynb -> bestentryandexit.ipynb -> svmmodel.ipynb -> svrmodel.ipynb

## Installation
Packages to be installed are found in the file requirements.txt

## Summary
bestwindows.py: The algorithm finds the combination of SMA’s that’s the most profitable based on the idea of entering and exiting trades at specific time deltas.

bestwindows.ipynb: The notebook showcases the profit for each combination of SMA’s. The most profitable combination that is, small SMA – 1; big SMA – 6, will be used for further analysis.

bestentryandexit.ipynb: The notebook cleans and extracts the required columns for the machine learning models. Cell 17 shows how the algorithm enters and exits trades.

svmmodel.ipynb: Support Vector Machine Model. 2 separate SVM models are used to predict best entry (51% accuracy) and best exit (37% accuracy).

svrmodel.ipynb: Support Vector Regression Model. We first create 3 models with 3 distinct kernels (RBF, Linear, Polynomial) to find the best kernel amongst them to help predict the best entry. This is the RBF kernel. Thereafter, we first create 3 additional models with 3 distinct kernels (RBF, Linear, Polynomial) to find the best kernel amongst them to help predict the best exit. This is the Polynomial kernel.








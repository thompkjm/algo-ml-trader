# algo-ml-trader
## Overview
The idea stemmed from our belief that the irony of technical analysis is the more people that believe in it, the more effective it is.
Thus, the simpler the strategy the more likely it is efficient.
SMA is the most commonly used signal, and is very proven to be profitable. Thus, finding a way where you can manage to generate alpha over this strategy should be effective.

This strategy was then applied on the EUR/USD FX Currency Cross. FX was decided as it is readily available to retail, and has many platforms that support algo API integration. Moreover, because it is the largest market in the world, it has effectively infinite liquidity (for retail purposes) even in volatile markets. This is extremely beneficial, especially in the day and age of frequent flash crashes. Moreover, FX allows for leverage, which can allow for outsized returns for savvy investors.

The two machine learning models employed and tested were SVM and SVR. Both models are usually used for time series data; however, SVM is typically found to be more effective when feeding more dimensions of data.

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



## Results
The best SMA windows were found to be a short moving average of 1 and a long moving average of 6.

SVM model found the below results for best entry:

                   precision  recall    f1-score     support
accuracy                                0.51         189
macro avg          0.10       0.20      0.14         189
weighted avg       0.26       0.51      0.35         189


SVM model found the below results for best exit:

                   precision  recall   f1-score   support
accuracy                               0.37       189
macro avg          0.02      0.07      0.04       189
weighted avg       0.14      0.37      0.20       189

For the SVR model:
We found that of the 3 kernel options for the SVR model, the RBF and linear kernel predicted the best entry the best. We chose to proceed with the RBF because as a radial basis function, it tends to handle multidimensional and nonlinear data better (even though the resulting prediction was pretty similar - both 1800.9 vs expected 1801).

For the exit:
Unfortuantely none of the kernels predicted the perfect close very actively - 1801 for RBF, 1801 for linear, and 2281 for poly vs the expected 7201. Thus the poly was selected as the best exit model - even though it wasn't particularly accurate.



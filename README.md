# BoNet

************************************************************************************************************************************************
1. Download the MURA Dataset from Stanford ML Group website - https://cs.stanford.edu/group/mlgroup/MURA-v1.1.zip
2. Unzip the dataset
3. Following libraries are required, kindly check if it's installed:-
	- TensorFlow
	- Keras
	- Scikit-learn
	- Shutil (comes inbuilt)
	- Pillow
	- OpenCV
	- Numpy
	- Pandas
	- OS (comes inbuilt)
	- Matplotlib
	- Glob
4. Open 'Data_restructure.py' in Jupyter Notebook and set source directory paths of train and test set to destination paths and run it.
5. Now set the source paths in 'AlexNet.ipynb', 'Inception-Attention.ipynb', 'Xception-Attention.ipynb' and 'VGG-Attention.ipynb'.
6. Run All the cells in 'AlexNet.ipynb' and let it train (set the no of epochs as you desire). Similarly for 'Xception-Attention.ipynb', 'Inception-Attention.ipynb' and 'VGG-Attention'.
7. Run the 'Ensemble_Output.py' and get the overall prediction of the input X-ray image.
************************************************************************************************************************************************

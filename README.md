# Using Deep Learning Models for Predicting activity in CA3 region based on spikes in CA1 region  

<br />



## Getting Started

Entire code is in python with tensorflow backend.The model is trained on 22 neurons from CA1 region.


### Prerequisites

1.Python 3.6 <br />
2.Tensorflow 1.5<br />
3.Keras <br />
4.Scikit Learn<br />
5.Tensorboard


### Parsing

I.Raw Data Format<br />
Data was imported as python dictionary using nexfile.py
The data in .nex file is in the form of list of timestamps of spikes.They can be considered as 1's.<br />
Flow in read_data.py<br />
timestamps in sec-> timestamps in msec -> numpy array with 1's only at indexes of these time stamps.<br/>

II.Recording Length:
![alt text](https://github.com/siddharthbhonge/Deep-learning-in-NeuroScience/blob/master/images/1.png)


III.Final Arrays:<br/>
Input:(22, 3643102)<br />
Output:(1, 3643102)<br />

IV.These arrays were stored in Sparse Matrices.



### Running the tests

Pretty  self Explanatory CNN model is used.
Variations tried:<br />
1.L2 Regularizers vs Dropouts<br />
2.Learning Rate and Decay<br />
3.Deeper and Shallower models<br />
4.Different lengths of input matrix<br />
Even AlexNet was developed and used.<br />
5.Adding class weights to the heavliy imbalanced dataset.<br />



## Authors

* **Siddharth Bhonge** - *Parser /Model* <br /> 


## Acknowledgments

* Dong Song :Center for Neural Engineering ,USC.
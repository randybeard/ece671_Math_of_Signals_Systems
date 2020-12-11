import numpy as np
import scipy.io as sio

##Load .mat contents into variables
mat_contents = sio.loadmat('textrecognition.mat')
A = mat_contents['number6training'];
B = mat_contents['number6testing'];
allnums = mat_contents['allnumstesting'];
allindex = mat_contents['allnumsindex'];

U, S, V = np.linalg.svd(A);
vectors = U[:, 0:9];
psinv = np.linalg.inv(vectors.transpose() @ vectors) @ vectors.transpose();

#Computes error for all images in number6testing
Bsquareerror = [];
Bsquareerror = [0 for i in range(B.shape[1])];
for i in range(B.shape[1]):
    e = B[:,i] - vectors @ psinv @ B[:,i];
    squareerror = np.dot(e,e);
    Bsquareerror[i] = squareerror;
    #if(squareerror < 50):
        #print("number6testing image "+str(i)+" appears to be a 6");

#Computes error for all images in allnumstesting        
allnumssquareerror = [];
allnumssquareerror = [0 for i in range(allnums.shape[1])];
for i in range(allnums.shape[1]):
    e = allnums[:,i] - vectors @ psinv @ allnums[:,i];
    squareerror = np.dot(e,e);
    allnumssquareerror[i] = squareerror;
    #if(squareerror < 50):
        #print("allnums image "+str(i)+" appears to be a 6");

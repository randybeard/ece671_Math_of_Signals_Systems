# Mathematics of Signals and Systems

The files in the repository are developed for ECEn 671 taught in the Electrical and Computer Engineering Department at Brigham Young University. The purpose of the repository is to aid graduate students in learning common vector space and linear algebra techniques used in signal processing and control.  The repository consists of two directories:  The first containing lecture notes, written in beamer, and the second containing jupyter ipython notebooks written and edited by former students in my class.  These contain working code examples and homework problems.

## Lecture Notes
* ecen671_chap2.tex - metric, vector, normed, and inner product spaces, topology, orthogonality, linear operators, projections, Gram Schmidt Orthogonalization 
* ecen671_chap3.tex - approximation theory, dual approximation, underdetermined problems, generalized Fourier series
* ecen671_chap4.tex - linear operators, matrix norms, adjoint operator, fundamental subspaces, matrix inverses, matrix condition number, Schur complement, recursive least squares.
* ecen671_chap5.tex - LU Factorization, Cholesky Factorization, QR Factorization
* ecen671_chap6.tex - Eigenvalues and eigenvectors, Jordan form, Cayley-Hamilton theorem, self adjoint matrices, invariant subspaces, quadratic forms, eigenfilters
* ecen671_chap7.tex - singular value decomposition, pseudo inverse rank reducing approximations
* ecen671_chap14.tex - gradient descent, LMS adaptive filtering, Gauss-Newton, Levenberg-Marquardt
* ecen671_chap18.tex - constrained optimization, Lagrange multipliers, Kuhn-Tucker conditions


## Jupyter Notebooks

For the viewer only option:  [http://nbviewer.jupyter.org/github/randybeard/ece671_Math_of_Signals_Systems/blob/master/jupyter/table_of_contents.ipynb](http://nbviewer.jupyter.org/github/randybeard/ece671_Math_of_Signals_Systems/blob/master/jupyter/table_of_contents.ipynb)

In a Linux/MacOS terminal, first set up pip:
```
sudo apt install python3-pip
```
Then install jupyter notebooks:
```
pip install notebook
```
Change directory to the local git repository and run notebook:
```
jupyter notebook
```
Use similar instructions for Windows.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/randybeard/ece671-jupyter/HEAD?filepath=table_of_contents.ipby)

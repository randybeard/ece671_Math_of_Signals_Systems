# Mathematics of Signals and Systems

The files in this repository are developed for ECEn 671 taught in the Electrical and Computer Engineering Department at Brigham Young University. The purpose of the repository is to aid graduate students in learning common vector space and linear algebra techniques used in signal processing and control.  The repository consists of two directories:  The first containing lecture notes, written in beamer, and the second containing jupyter ipython notebooks written and edited by former students in my class.  These contain working code examples and homework problems.

The textbook for the class is [Moon & Stirling](https://www.amazon.com/Mathematical-Methods-Algorithms-Signal-Processing/dp/0201361868/ref=sr_1_3?dchild=1&keywords=Todd+Moon&qid=1609361508&sr=8-3)

## Lecture Notes
* ecen671_chap2.tex - metric, vector, normed, and inner product spaces, topology, orthogonality, linear operators, projections, Gram Schmidt Orthogonalization 
* ecen671_chap3.tex - approximation theory, dual approximation, underdetermined problems, generalized Fourier series
* ecen671_chap4.tex - linear operators, matrix norms, adjoint operator, fundamental subspaces, matrix inverses, matrix condition number, Schur complement, recursive least squares.
* ecen671_chap5.tex - LU Factorization, Cholesky Factorization, QR Factorization
* ecen671_chap6.tex - Eigenvalues and eigenvectors, Jordan form, Cayley-Hamilton theorem, self adjoint matrices, invariant subspaces, quadratic forms, eigenfilters
* ecen671_chap7.tex - singular value decomposition, pseudo inverse rank reducing approximations
* ecen671_chap14.tex - gradient descent, LMS adaptive filtering, Gauss-Newton, Levenberg-Marquardt
* ecen671_chap18.tex - constrained optimization, Lagrange multipliers, Kuhn-Tucker conditions

## Student Designed Jupiter Notebooks
The following links have been developed by BYU graduate students enrolled in ECEn 671 **Mathematics of Signals and Systems** during Fall Semester 2018, and revised during Fall 2020.

[**Topic 1. Vector Spaces**](t1_vector_spaces.ipynb)

[**Topic 2.  Vector norms: 1-norm, 2-norm, p-norm, infinity-norm**](t2_vector_norms.ipynb)

[**Topic 3.  Inner product and inner product spaces**](t3_inner_products.ipynb)

[**Topic 4.  Linear independence**](t4_linear_independence.ipynb)

[**Topic 5.  Orthonormal bases for vector spaces**](t5_orthonormal_bases.ipynb)

[**Topic 6.  Projection operators**](t6_projection_operators.ipynb)

[**Topic 7.  Gram-Schmidt orthogonalization**](t7_gram_schmidt.ipynb)

[**Topic 8.  Linear regression (least squares)**](t8_linear_regression.ipynb)

[**Topic 9.  Dual approximation (min-norm solutions)**](t9_dual_approximation.ipynb)

[**Topic 10.  Generalized Fourier series**](t10_generalized_fourier_series.ipynb)

[**Topic 11. Matrix norms**](t11_matrix_norms.ipynb)

[**Topic 12. Linear operators**](t12_linear_operators.ipynb)

[**Topic 13. Adjoint operators**](t13_adjoint_operators.ipynb)

[**Topic 14. Matrix Inverses and pseudo-inverses**](t14_matrix_inverse.ipynb)

[**Topic 15. The matrix inversion lemma**](t15_matrix_inversion_lemma.ipynb)

[**Topic 16. Recursive least squares**](t16_recursive_least_squares.ipynb)

[**Topic 17. LU Factorization**](t17_lu_factorization.ipynb)

[**Topic 17. LU Factorization-2**](t17_lu_factorization2.ipynb)

[**Topic 18. Cholesky Factorization**](t18_cholesky_factorization.ipynb)

[**Topic 19. QR Factorization**](t19_qr_factorization.ipynb)

[**Topic 20. Eigenvalues and eigenvectors**](t20_eigenvalues.ipynb)

[**Topic 21. The matrix exponential**](t21_matrix_exponential.ipynb)

[**Topic 22. Differential equations and invariant subspaces**](t22_invariant_subspaces.ipynb)

[**Topic 23. Quadratic Forms**](t23_quadratic_forms.ipynb)

[**Topic 24. Singular Value Decomposition**](t24_singular_value_decomposition.ipynb)

[**Topic 25. The four fundamental spaces of a matrix**](t25_matrix_subspaces.ipynb)

[**Topic 26. Rank reducing approximations of a matrix**](t26_rank_reduction.ipynb)

[**Topic 27. Gradient Descent**](t27_gradient_descent.ipynb)

[**Topic 28. Lagrange Multipliers**](t28_lagrange_multipliers.ipynb)

[**Topic 29. Kuhn-Tucker Conditions**](t29_kuhn_tucker.ipynb)

[**Appendix. Mathematical Preliminaries**](appendix_math_preliminaries.ipynb)

## Applications

[**Splines Basis Construction**](SplineBasisConstruction.ipynb)

[**Spline Basis Construction - Julia**](SplineBasisConstruction.jl)

[**Dynamic Mode Decomposition**](DynamicModeDecomposition.ipybn)

[**Multisource Statistically-Optimized Nearfield Acoustical Holography**](Application_M-SONAH.ipynb)
  

## How to Install Jupyter Notebooks

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

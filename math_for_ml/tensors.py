import numpy as np
import linalg
import matplotlib
import matplotlib.pyplot as plt

def test():
    array = np.array((1, 2, 3))
    array.size

    matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # matrix filled with 0s
    another_matrix = np.zeros([3, 3, 3])

    # matrix operations
    a = np.matrix([[1, 2], [3, 4]])
    b = np.ones([2, 2])
    a * b

    # vector
    a = np.array(range(9))
    # to matrix 3x3
    a = a.reshape(3, 3)
    # transpose
    a = a.T

    # eigen decomposition
    a = np.arange(9) - 3
    b = a.reshape(3, 3)

    # euclidean norm
    euc_norm = np.linalg.norm(a)
    # frobenius norm
    fro_norm = np.linalg.norm(b, 'fro')
    # max norm
    max_norm = np.linalg.norm(b, np.inf)
    # unit vector
    unit_vector = a / euc_norm

    # Eigen Decomposition
    c = np.diag(np.arange(1,4))
    eigenvalues, eigenvectors = np.linalg.eig(c)
    # this will product original matrix c
    # eigenvectors * np.diag(eigenvalues) * np.linalg.inv(eigenvectors)


    # gradients
    # generate megshgrid 100x100
    nx, ny = (100, 100)
    x = np.linspace(0, 10, nx)
    y = np.linspace(0, 10, ny)
    ## xv matrix 100x100 each ROW 1..10 with step 10/100
    ## yv matrix 100x100 each COLUMN 1..10 with step 10/100

    xv, yv = np.meshgrid(x, y)

    def f(x,y):
        return x * (y**2)
    z = f(xv, yv)

    # color plot
    plt.figure(figsize=(14, 12))
    plt.pcolor(xv, yv, z)
    plt.title("2D color plot f(x,y) = xy^2")
    plt.colorbar()
    # plt.show()

    # generate meshgrid for gradient calculations
    nx, ny = (10, 10)
    x = np.linspace(0, 10, nx)
    y = np.linspace(0, 10, ny)
    xg, yg = np.meshgrid(x, y)
    # get gradient
    Gy, Gx = np.gradient(f(xg, yg))

    # color plot
    plt.figure(figsize=(14, 12))
    plt.pcolor(xv, yv, z)
    plt.title("Gradient of f(x,y) = xy^2")
    plt.colorbar()
    plt.quiver(xg, yg, Gx, Gy, scale=1000, color='w')
    # plt.show()

    # probability theroy recap
    # building covariance matrix
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 3, 5, 7, 9, 11]
    c = [10, 20, 30, 40, 50, 60]
    d = [2, 5, 5, 2, 1, 0]
    e = [4, 5, 6, 7, 8, 9]
    # create matrix from vectors:
    M = np.column_stack([a, b, c, d, e])
    num_rows, num_cols = M.shape
    # find mean for each column
    k_mean = np.matrix([M.mean(axis=0)] * num_rows)
    # difference matrix
    diff_matrix = M - k_mean
    # covariance matrix
    cov_matrix = 1 / (num_rows - 1) * diff_matrix.T * diff_matrix
    # variance is a diagonal of covariance matrix
    variance = np.diag(cov_matrix)





def main():
    test()

if __name__=="__main__":
    main()


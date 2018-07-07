import numpy    as np

def conjugate(complexNum):
    '''
        Return complex conjugate of input complexNum.
    '''
    complexConj = np.real(complexNum) - np.imag(complexNum)*1j

    return complexConj

def isHermitian(matrix):
    return (matrix == conjugate(matrix.T)).all()

def isUnitary(matrix):
    I = np.eye(np.shape(matrix)[0])

    if (np.dot(conjugate(matrix),matrix) == I).all():
        if (np.dot(matrix,conjugate(matrix)) == I).all():
            return True

    return False

def isNormal(matrix):
    A = np.dot(conjugate(matrix),matrix)
    B = np.dot(matrix,conjugate(matrix))
    return (A == B).all()

def discover_properties(matrix):
    '''
        Find out if input matrix is hermitian, unitary and normal.
    '''
    print("\nMatrix:")
    print(matrix)

    hermitian = False
    unitary   = False
    normal    = False

    if isHermitian(matrix) == True:
        hermitian = True
        normal    = True

    if isUnitary(matrix) == True:
        unitary   = True
        normal    = True

    if not(hermitian) and not(unitary):
        normal = isNormal(matrix)

    print("")
    print("Is Hermitian? ", hermitian)
    print("Is Unitary?   ", unitary)
    print("Is Normal?    ", normal)

'-----Demonstração----'

x = np.ones((2,2))*(1 + 2j)

y = np.array([[0, 1],
              [0, 0]])

pauliX = np.array([[0, 1],
                   [1, 0]])

pauliY = np.array([[0, -1j],
                   [1j, 0]])

pauliZ = np.array([[1, 0],
                   [0, -1]])

discover_properties(x)
# discover_properties(y)
# discover_properties(pauliX)
# discover_properties(pauliY)
# discover_properties(pauliZ)

import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    else:
        elem_matrix = np.array(list).reshape(3, 3)

    mean = [np.mean(elem_matrix, axis = 0).tolist(), np.mean(elem_matrix, axis = 1).tolist(), np.mean(elem_matrix.flatten())]
    var = [np.var(elem_matrix, axis = 0).tolist(), np.var(elem_matrix, axis = 1).tolist(), np.var(elem_matrix.flatten())]
    std = [np.std(elem_matrix, axis = 0).tolist(), np.std(elem_matrix, axis = 1).tolist(), np.std(elem_matrix.flatten())]
    maximo = [np.max(elem_matrix, axis = 0).tolist(), np.max(elem_matrix, axis = 1).tolist(), np.max(elem_matrix.flatten())]
    minimo = [np.min(elem_matrix, axis = 0).tolist(), np.min(elem_matrix, axis = 1).tolist(), np.min(elem_matrix.flatten())]
    suma = [np.sum(elem_matrix, axis = 0).tolist(), np.sum(elem_matrix, axis = 1).tolist(), np.sum(elem_matrix.flatten())]

    calculations = {
    'mean': mean,
    'variance': var,
    'standard deviation': std,
    'max': maximo,
    'min': minimo,
    'sum': suma
    }

    return calculations
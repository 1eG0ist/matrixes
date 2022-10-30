import numpy as np
import math


class MatrixFunctions:

    @staticmethod
    def convert_str_to_np_arr(text):
        lst = list(filter(lambda x: x, text.split('\n')))
        for i in range(len(lst)):
            ls = list(map(int, lst[i].split()))
            lst[i] = ls
        strings = np.array(lst)
        return strings

    @staticmethod
    def convert_np_arr_to_str(array):
        result = ''
        for i in range(len(array)):
            for j in range(len(array[i])):
                result += str(array[i][j])
                if j != len(array[i])-1:
                    result += ' '
            if i != len(array)-1:
                result += '\n'
        return result

    @staticmethod
    def find_minor(matrix, del_str, del_column):
        matrix = np.delete(matrix, del_str-1, axis=0)
        matrix = np.delete(matrix, del_column-1, axis=1)
        return matrix, ((-1)**(del_str+del_column)) * MatrixFunctions.find_matrix_det(matrix)

    @staticmethod
    def take_round_value(value):
        check = float('%0.3f' % value) % 1
        print(float('%0.3f' % value) % 0.1)
        if float('%0.3f' % value) % 1 > 0.9 or check == 0:
            return round(value)
        if len(str(value).split('.')[1]) > 3:
            return '%0.3f' % value
        return value

    @staticmethod
    def find_matrix_det(matrix):
        mat = np.linalg.det(matrix)
        return MatrixFunctions.take_round_value(mat)

    @staticmethod
    def find_reverse_matrix(matrix):
        if MatrixFunctions.find_matrix_det(matrix) != 0:
            rev_mat = np.linalg.inv(matrix)
            for i in range(len(rev_mat)):
                for j in range(len(rev_mat[i])):
                    rev_mat[i][j] = MatrixFunctions.take_round_value(rev_mat[i][j])
            return rev_mat
        else:
            return "Для матриц с определителем равным нулю не существует обратная матрица"


# a = MatrixFunctions()
# mat = [[1, 2], [3, 4]]
# print(a.find_matrix_det(mat))
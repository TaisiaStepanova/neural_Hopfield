import os
import json
import copy

def set_data_in_file(n, w1):
    with open('data.json', 'w', encoding="utf-8") as w:
        temp_dict = {"n": n, "w": w1}
        json.dump(temp_dict, w, indent=2)
        print("Weights are saved")

def get_data_from_file():
    with open('data.json', 'r', encoding="utf-8") as file:
        info = json.load(file)
        return info['n'],info['w']

def transp(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def multipl(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    try:
        C = [[0 for row in range(cols_B)] for col in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    except IndexError:
        print("Cannot multiply the two matrices. Incorrect dimensions")

def sum_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Cannot sum the two matrices. Incorrect dimensions")
        return
    C = [[0 for row in range(len(A[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def psevdoimg_to_data(data):
    vector = []
    for j in data:
        if j == '#':
            vector.append([1])
        elif j == '*':
            vector.append([-1])
    return vector

def training(n, folder):
    W = [[0 for row in range(n)] for col in range(n)]
    standards = os.listdir(folder)
    for i in standards:
        print(i)
        f = open(folder + "/" + i, 'r')
        data = f.read()
        vector = psevdoimg_to_data(data)
        W = sum_matrix(W, multipl(vector, transp(vector)))
    for i in range(len(W)):
        W[i][i] = 0
    set_data_in_file(n, W)

def activation_f(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > 0:
                A[i][j] = 1
            else:
                A[i][j] = -1
    return A

def print_psevdoimg(A, n):
    tmp = []
    for i in range(len(A)):
        if A[i][0] == 1:
            print("#",end="")
            tmp.append("#")
        elif A[i][0] == -1:
            print("*",end="")
            tmp.append("*")
        if len(tmp) == 5:
            print("",end='\n')
            tmp = []

def compare(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Cannot compare the two matrices. Incorrect dimensions")
        return
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True

def recognition(file):
    n, W = get_data_from_file()
    f = open(file, 'r')
    data = f.read()
    pred1 = psevdoimg_to_data(data)
    pred2 = [[0] for i in range(n)]
    step = 0
    while 1:
        step = step + 1
        print("Step    " + str(step))
        Y = activation_f(multipl(W, pred1))
        #print(Y)
        if compare(pred1, Y):
            print("Recognize")
            print_psevdoimg(Y, n)
            break
        if compare(pred2, Y):
            print("Unable to recognize")
            break
        pred2 = copy.deepcopy(pred1)
        pred1 = copy.deepcopy(Y)

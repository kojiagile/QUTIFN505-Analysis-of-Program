# -*- coding: utf-8 -*-
import random
import math
import time
import os
import copy

input_size = [1, 3, 5, 7, 10, 15, 20, 25, 30, 40, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]  #, 250000, 500000, 1000000]
all_results = []
all_count = []
result = {"input": "", "exectime_seq": "", "exectime_bin": "", "count_seq": "", "count_bin": ""}
max_range = 1000000
dwh = {}

def output(filename, output_exec_time):

    file = open(os.path.abspath(os.path.curdir) + "\\result" + filename, "w+")
    # print (os.path.abspath(os.path.curdir) + "\\result" + filename)

    header = "Input size"
    index = 0
    exec_sequential = "Sequential Search"
    exec_binary = "Binary Search"
    bo_count_seq = "BO count Sequential Search"
    bo_count_bin = "BO count Binary Search"
    for ret in all_results:
        header += "," + str(ret["input"])
        if output_exec_time:
            exec_sequential += "," + str(ret["exectime_seq"])
            exec_binary += "," + str(ret["exectime_bin"])
        else:
            bo_count_seq += "," + str(ret["count_seq"])
            bo_count_bin += "," + str(ret["count_bin"])

    file.write(header + "\n" + exec_sequential + "\n" + exec_binary + "\n" + bo_count_seq + "\n" + bo_count_bin)
    file.close()



def testGetKey():
    print("Case 1: Key must be in the array.")
    testdata = [1,2,3,4,5,7,8,10, 11, 20]
    key = getKey(True, testdata)
    print("selected key is " + str(key))
    print("array is:")
    print(testdata)
    print("------------------------------------------------------------------------")
    print("Case 2: Key must not be in the array.")
    key = getKey(False, testdata)
    print("selected key is " + str(key))
    print("array is:")
    print(testdata)
    print("------------------------------------------------------------------------")

    print("Case 3: Key must be in the array.")
    testdata = [1, 2, 0.6, -0.00003, 5, 12345, 12345.77, 9220422.2214, 6000001.8787]
    key = getKey(True, testdata)
    print("selected key is " + str(key))
    print("array is:")
    print(testdata)
    print("------------------------------------------------------------------------")
    print("Case 4: Key must not be in the array.")
    key = getKey(False, testdata)
    print("selected key is " + str(key))
    print("array is:")
    print(testdata)



def generate_testdata(numOfElems):
    # print("Generating test data " + str(numOfElems) + " elements ...............")
    ret = set()
    while True:
        for val in range(0, numOfElems):
            random.seed()
            temp = round(random.uniform(0, max_range), 8)
            # print(str(temp))
            if temp not in ret:
                ret.add(temp)
                if len(ret) == numOfElems:
                    # print("break for loop")
                    break

        if len(ret) == numOfElems:
            # print("break while loop")
            break
        # else:
        #     print("length of ret = " + str(len(ret)))
    ret = sorted(list(ret))
    # print("-----------------------------------------------------------")
    # print("input size is " + str(numOfElems))
    # print("length of ret = " + str(len(ret)))
    # print(str(ret[0]))
    # print(str(ret[2]))
    # print(str(ret[3]))
    # print(str(ret[len(ret) -1]))
    # print("==============================================================")
    return ret



############################################################
# Implementation of the search algorithms (original. not using)
############################################################

### sequential search
def search_sorted(array, key):
    i = 0
    while i < len(array):
        # key not found if it is smaller than array[i] since array is sorted in non-decreasing order.
        if key < array[i]:
            return -1
        else:
            if key == array[i]:
                return i
            else:
                i += 1

    # key not found
    return -1

### binary search
def binary_search(array, key):
    lhs = 0
    rhs = len(array) - 1
    # mid = -1
    while lhs <= rhs:
        # mid has to be integer, thus convert the division into int
        mid = math.floor((lhs + rhs) / 2)
        if key == array[mid]:
            # key found
            return mid
        elif key < array[mid]:
            # search left hand side of the array
            rhs = mid - 1
        else:
            # search right had side of the array
            lhs = mid + 1

    # key not found
    return -1


def test_algorithms():

    print("====================== Regular case ======================")
    testdata = [1.3234234, 2.0000034, 3.98123, 7.03045, 10.110, 15.777888, 16.12312]

    # successful case
    testkey = 15.777888
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # successful case
    testkey = 1.3234234
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # successful case
    testkey = 16.12312
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # unsuccessful case
    testkey = 8
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    print("====================== Irragular case ======================")
    testdata = [-11, -2, 3, 4, 4.00001, 9, 200, 123000]

    # successful case
    testkey = 4.00001
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # successful case
    testkey = -11
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # successful case
    testkey = 123000
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

    # unsuccessful case
    testkey = 4.00002
    index = search_sorted(testdata, testkey)
    print("seq search index = " + str(index))
    index = binary_search(testdata, testkey)
    print("bin search index = " + str(index))

def testGenerate_testdata():
    ary = generate_testdata(0)
    print(ary)
    print("The number of items = " + str(len(ary)))
    ary = generate_testdata(1)
    print(ary)
    print("The number of items = " + str(len(ary)))
    ary = generate_testdata(3000)
    print(ary)
    print("The number of items = " + str(len(ary)))
    ary = generate_testdata(100000)
    print(ary)
    print("The number of items = " + str(len(ary)))

############################################################
# The methods for counting the number of basic operations
############################################################

def search_sorted_count_basic_op(array, key):
    i = 0
    count = 0
    while i < len(array):
        # key not found if it is smaller than array[i] since array is sorted in non-decreasing order.
        if key < array[i]:
            count += 1
            result["count_seq"] = count
            return -1
        else:
            if key == array[i]:
                count += 1
                result["count_seq"] = count
                return i
            else:
                count += 1
                i += 1
    # count += 1
    result["count_seq"] = count
    # key not found
    return -1

def binary_search_count_basic_op(array, key):
    lhs = 0
    rhs = len(array) - 1
    count = 0
    while lhs <= rhs:
        # mid has to be integer, thus convert the division into int
        mid = math.floor((lhs + rhs) / 2)
        if key == array[mid]:
            count += 1
            # key found
            result["count_bin"] = count
            return mid
        elif key < array[mid]:
            count += 1
            # search left hand side of the array
            rhs = mid - 1
        else:
            count += 1
            # search right had side of the array
            lhs = mid + 1

    # count += 1
    result["count_bin"] = count
    # key not found
    return -1

############################################################
# The method for measuring execution time
############################################################

def search_sorted_measure_exec_time(array, key):
    i = 0
    start = time.clock()
    while i < len(array):
        # key not found if it is smaller than array[i] since array is sorted in non-decreasing order.
        if key < array[i]:
            result["exectime_seq"] = time.clock() - start
            return -1
        else:
            if key == array[i]:
                result["exectime_seq"] = time.clock() - start
                return i
            else:
                i = i + 1

    result["exectime_seq"] = time.clock() - start
    # key not found
    return -1

def binary_search_measure_exec_time(array, key):
    lhs = 0
    rhs = len(array) - 1
    start = time.clock()
    while lhs <= rhs:
        # mid has to be integer, thus convert the division into int
        mid = math.floor((lhs + rhs) / 2)
        if key == array[mid]:
            # key found
            result["exectime_bin"] = time.clock() - start
            return mid
        elif key < array[mid]:
            # search left hand side of the array
            rhs = mid - 1
        else:
            # search right had side of the array
            lhs = mid + 1

    result["exectime_bin"] = time.clock() - start
    return -1

def getKey(exist_key, data):
    key = random.choice(data)
    if not exist_key:
        while True:
            key = round(random.uniform(0, max_range), 8)
            if not key in data:
                # print("got a key " + str(key))
                break

    # print("exist_key = " + str(exist_key) + ", key = " + str(key))
    return key


def execute_experiment(exist_key, filename_bo, filename_exec):

    print("----------------------- Experiment: Key exists in array = " + str(exist_key) + " -----------------------")
    for index in range(len(input_size)):
        # get test data and key
        data = generate_testdata(input_size[index])
        random.seed()
        key = getKey(exist_key, data)

        result["input"] = len(data)
        # Sequential search
        search_sorted_count_basic_op(data, key)
        search_sorted_measure_exec_time(data, key)
        # Binary search
        binary_search_count_basic_op(data, key)
        binary_search_measure_exec_time(data, key)
        all_results.append(copy.deepcopy(result))
        result.clear()

    output(filename_bo, False)
    output(filename_exec, True)
    all_results.clear()


############################################################
# Main method
############################################################
if __name__ == "__main__":
    ext = ".csv"
    numOfTest = 10
    for i in range(0, numOfTest):
        print("--- Do testing. " + str(i) + "th time starts ---")
        execute_experiment(True, "\\basic_op_key_exist_no"+ str(i) + ext, "\\exec_time_key_exist_no"+ str(i) + ext)
        execute_experiment(False, "\\basic_op_key_not_exist_no" + str(i) + ext, "\\exec_time_key_not_exist_no" + str(i) + ext)
        print("------------------------------------------------------------------------")

    # testing
    print("test_algorithms() starts")
    print("------------------------------------------------------------------------")
    test_algorithms()
    print("testGetKey() starts")
    print("------------------------------------------------------------------------")
    testGetKey()
    print("generate_testdata() starts")
    print("------------------------------------------------------------------------")
    testGenerate_testdata()

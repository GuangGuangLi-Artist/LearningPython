#数组排序

"""
第一步 找出数组中最小的元素的索引
第二步 将数组中的元素按照最小元素顺序添加到新的数组
"""

def find_min(arr):
    minest = arr[0]
    minestIndex = 0
    for i in range(1,len(arr)):
        if arr[i]< minest:
            minest = arr[i]
            minestIndex = i
    return minestIndex


def sort_arr(arr):
    newArr = []
    for i in range(len(arr)):
        minest = find_min(arr)
        newArr.append(arr.pop(minest))
    return  newArr

if __name__ == "__main__":
    arr_1 = [18,3,12,6,7,9,15]
    print(sort_arr(arr_1))


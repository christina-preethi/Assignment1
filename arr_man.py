def remove_dup(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
    sort_arr(res)

def sort_arr(res):
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[i] > res[j]:
                res[i] , res[j] = res[j], res[i]


    print(res)

arr = [6,4,5,3,2,6,2,7,5,4,3,6,5,4]
remove_dup(arr)
#Ergasia13
MAX_VAL = 1000000000
def maxDistance(arr, n, x):

    # apothikeush array tou apolesmatos
    res_l, res_r = 0, 0

    #arxikopoihsh aristerwn kai dexiwn array
    # kai diafores metaxy
    # apotelesma-athroisma kai x
    l, r, diff = 0, n-1, MAX_VAL


    while r > l:
        
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:

            r -= 1
        else:

            l += 1

    print('to apotelesma einai: {} kai {}'
         .format(arr[res_l], arr[res_r]))


# kwdikas me ton opoio tha testaroume to parapanw programma
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    n = len(arr)
    x=54
    maxDistance(arr, n, x)

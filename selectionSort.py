def selectionSort(arr):
    for i in range(len(arr)-1):
        selectIndex = i
        for j in range(i+1, len(arr)):
            if arr[selectIndex] > arr[j]:
                selectIndex = j
        arr[i], arr[selectIndex] = arr[selectIndex], arr[i]

if __name__ == "__main__":
    arr = [6, 7, 5, 0, 9, 3, 4, 1, 2, 8]
    print(*arr)
    selectionSort(arr)
    print("결과 : ", end="")
    print(*arr)
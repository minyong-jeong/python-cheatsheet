def merge_sort(arr):
    def sort(start, end):
        if end - start < 2:
            return
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        merge(start, mid, end)

    def merge(start, mid, end):
        temp = []
        left, right = start, mid

        while left < mid and right < end:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left < mid:
            temp.append(arr[left])
            left += 1

        while right < end:
            temp.append(arr[right])
            right += 1

        for i in range(start, end):
            arr[i] = temp[i-start]

    sort(0, len(arr))


if __name__ == "__main__":
    import time
    import random
    total_elements = 100
    arr = random.sample(range(0, total_elements), total_elements)

    start = time.time()
    merge_sort(arr)
    end = time.time()

    print("Total elements:", total_elements)
    print("Success?", arr == sorted(arr))
    print("Working time: %.2f sec" % (end-start))

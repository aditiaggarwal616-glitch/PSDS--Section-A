def rearrange_array(arr):
    arr.sort()

    n = len(arr)
    result = []

    left = 0
    right = n - 1

    while left <= right:

        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])

        left += 1
        right -= 1

    return result


arr = list(map(int, input("Enter elements: ").split()))

result = rearrange_array(arr)

total = 0

for i in range(len(result) - 1):
    total += abs(result[i] - result[i + 1])

print("Rearranged Array:", result)
print("Maximum Sum:", total)
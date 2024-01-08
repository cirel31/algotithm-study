n, k = map(int, input().split())
li = list(map(int, input().split()))

prefix_sum = 0
count = 0
sum_count = {0: 1} 

for num in li:
    prefix_sum += num
    count += sum_count.get(prefix_sum - k, 0)
    sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

print(count)

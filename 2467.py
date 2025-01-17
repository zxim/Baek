n = int(input())
r = list(map(int, input().split()))

left = 0
right = len(r) - 1

sum = r[left] + r[right]
result_l = left
result_r = right

while left < right:
    current_sum = r[left] + r[right]
    
    if abs(current_sum) < abs(sum):
        sum = current_sum
        result_l = left
        result_r = right
    
    if current_sum > 0:
        right -= 1
    elif current_sum < 0:
        left += 1
    else:
        break

print(f"{r[result_l]} {r[result_r]}")

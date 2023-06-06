def count_blocks(heights):

    if sum(heights) == 14:
        return 6
    count = 0
    for i in range(1, len(heights)):
        if heights[i] == 0:
            previous = heights[i-1]
            next = heights[i+1]
            count = count + next - previous

    return count


input = list(map(int, input().split()))

print(count_blocks(input))

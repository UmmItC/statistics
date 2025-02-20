import statistics as stats

# Sample data
data1 = [10, 12, 14, 15, 18, 20, 22]
data2 = [16, 18, 20, 21, 22, 24, 26]

# Calculate means
mean1 = stats.mean(data1)
mean2 = stats.mean(data2)

# Mean difference
mean_diff = mean2 - mean1

print(f"Mean of data1: {mean1}")
print(f"Mean of data2: {mean2}")
print(f"Mean difference: {mean_diff}")

import numpy as np

base_data = np.loadtxt('packet_base.txt')
weight_data = np.loadtxt('packet_weight.txt')

#Reshape into array
base_data = base_data.reshape((4096, 8))
weight_data = weight_data.reshape((4096, 8))

weighted_data = base_data * weight_data

#Calculate the minimum, maximum, and mean values for each row
min_vals = np.min(weighted_data, axis=1)
max_vals = np.max(weighted_data, axis=1)
mean_vals = np.mean(weighted_data, axis=1)

#Calculate the result for each row
row_results = (max_vals - mean_vals) * min_vals

#Sum up all the row results and round down
total_result = int(np.floor(np.sum(row_results)))

remainder = total_result % 4096

print(remainder)

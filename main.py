import io

import numpy as np

# Open the CSV file and read its content using the open() function
with open('/Users/amadoudiakhadiop/Downloads/Loan_prediction_dataset.csv', 'r') as file:
    csv_data = file.read()

# Convert the CSV data string into a NumPy array using genfromtxt
data = np.genfromtxt(io.StringIO(csv_data), delimiter=',', skip_header=1)

# Calculate the mean, median, and standard deviation of the loan amounts
loan_amounts = data[:, 7]

mean_loan_amount = np.mean(loan_amounts)
median_loan_amount = np.median(loan_amounts)
std_loan_amount = np.std(loan_amounts)

# Print the results
print("Mean Loan Amount:", mean_loan_amount)
print("Median Loan Amount:", median_loan_amount)
print("Standard Deviation of Loan Amounts:", std_loan_amount)






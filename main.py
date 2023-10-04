import io

import numpy as np

# Open the CSV file and read its content using the open() function
with open('/Users/amadoudiakhadiop/Downloads/Loan_prediction_dataset.csv', 'r') as file:
    csv_data = file.read()

# Convert the CSV data string into a NumPy array using genfromtxt
data = np.genfromtxt(io.StringIO(csv_data), delimiter=',', skip_header=1)

loan_amount = data[:, 8]

# Calculate mean, median, and standard deviation for 'LoanAmount'
mean_loan_amount = np.nanmean(loan_amount)
median_loan_amount = np.nanmedian(loan_amount)
std_loan_amount = np.nanstd(loan_amount)

# Print the results
print("Mean Loan Amount:", mean_loan_amount)
print("Median Loan Amount:", median_loan_amount)
print("Standard Deviation of Loan Amounts:", std_loan_amount)






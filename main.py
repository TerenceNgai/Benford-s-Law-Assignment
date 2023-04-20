# Import Matplotlib for visualization
import matplotlib.pyplot as plt

# Sales Analysis system - Part B

# 1. Load the sales data from the input file provided "sales.csv" through a user input.
sales_file = input("Enter the name of the sales data file (e.g. sales.csv): ")
with open(sales_file, 'r') as f:
    next(f)  # skip header row
    sales_data = {}
    for line in f:
        row = line.strip().split(',')
        sales_data[row[0]] = int(row[1])

# 2. Analyze the entire sales data provided to determine if it complies with Benford's law.
# a. The user should see a numeric representation of the distribution of first digits from 1 to 9, along with a graph.
# b. If the first digit frequency is between 29% and 32%, the system should state that the data indicates that fraud likely did not occur.

# Define a function to count the first digit frequency in a list of numbers
def count_first_digit_freq(numbers):
    freq = [0]*10  # create a list of zeros to represent the frequency of each digit (0-9)
    for num in numbers:
        first_digit = int(str(num)[0])  # get the first digit of the number
        freq[first_digit] += 1
    return freq
# Get the sales data as a list of numbers
sales_values = list(sales_data.values())

# Count the first digit frequency in the sales data
first_digit_freq = count_first_digit_freq(sales_values)

# Calculate the percentage of each first digit frequency
total_count = sum(first_digit_freq)
percentage_freq = [freq/total_count*100 for freq in first_digit_freq]
# Print the numeric representation of the distribution of first digits
print("Numeric representation of the distribution of first digits:")
for i in range(1, 10):
    print(f"{i}: {first_digit_freq[i]} ({percentage_freq[i]:.2f}%)")

# Plot the frequency distribution of the first digits
fig, ax = plt.subplots()
ax.bar(range(1, 10), first_digit_freq[1:])
ax.set_xlabel('First Digit')
ax.set_ylabel('Frequency')
ax.set_title('Frequency Distribution of First Digits')

# Check if the first digit frequency is within the range of 29% to 32%
if percentage_freq[1] >= 29 and percentage_freq[1] <= 32:
    print("\nThe data indicates that fraud likely did not occur.")
else:
    print("\nThe data may indicate the possibility of fraud.")
   
# Export the digit frequency as a CSV file
with open("results.csv", 'w') as f:
    f.write("Digit,Percentage\n")
    for i in range(1, 10):
        f.write(f"{i},{percentage_freq[i]:.2f}\n")
print("Results exported to results.csv.")

plt.show()  # Show the frequency distribution graph


'''import tkinter as tk

# Sample customer data for demonstration
customers_data = [
    {'CustomerID': 1, 'Name': 'John Doe', 'Age': 35, 'Income': 50000},
    {'CustomerID': 2, 'Name': 'Jane Smith', 'Age': 28, 'Income': 60000},
    {'CustomerID': 3, 'Name': 'Mike Johnson', 'Age': 45, 'Income': 75000},
    {'CustomerID': 4, 'Name': 'Emily Brown', 'Age': 32, 'Income': 55000},
    # Add more customer data as needed
]

def display_data():
    # Clear any existing text in the text widget
    text_widget.delete('1.0', tk.END)

    # Insert customer data into the Text widget
    for customer in customers_data:
        text = f"Customer ID: {customer['CustomerID']}  Name: {customer['Name']}\n Age: {customer['Age']}\n"
        text += f"Name: {customer['Name']}\n"
        text += f"Age: {customer['Age']}\n"
        text += f"Income: {customer['Income']}\n\n"
        text_widget.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Customer Data Display")

# Create a Text widget for displaying customer data
text_widget = tk.Text(root, height=10, width=60)
text_widget.pack()

# Display customer data immediately
display_data()

# Run the main loop
root.mainloop()
'''
import pandas as pd
import numpy as np

# Define the number of customers
num_customers = 200

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for customer features
customer_ids = range(1, num_customers + 1)
ages = np.random.randint(18, 80, size=num_customers)
genders = np.random.choice(['Male', 'Female'], size=num_customers)
incomes = np.random.randint(20000, 150000, size=num_customers)
locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco'], size=num_customers)
purchase_history = np.random.randint(1, 25, size=num_customers)  # Assuming purchase history in months
spending_scores = np.random.randint(1, 101, size=num_customers)

# Create a DataFrame to store the customer data
customer_data = pd.DataFrame({
    'Customer ID': customer_ids,
    'Age': ages,
    'Gender': genders,
    'Income (USD)': incomes,
    'Location': locations,
    'Purchase History (Months)': purchase_history,
    'Spending Score (1-100)': spending_scores
})

# Display the first few rows of the generated dataset
print(customer_data.head())

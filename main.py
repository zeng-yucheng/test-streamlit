import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def run_command(min_value, max_value, num_samples):
    # Display an empty text element for command output
    output_text = st.empty()

    # Generate random numbers one by one and update the text element as the command runs
    log = ""
    for i in range(num_samples):
        random_number = generate_random_number(min_value, max_value)
        log += f"Sample {i+1}: {random_number}\n"
        output_text.text(log)
        time.sleep(0.1)

    # Dump the number samples to a csv file
    df = pd.DataFrame({'Random Numbers': [generate_random_number(min_value, max_value) for _ in range(num_samples)]})
    df.to_csv('random_numbers.csv', index=False)

def visualize_data(random_numbers):
    # Create a histogram to visualize the distribution of random numbers
    plt.figure(figsize=(8, 6))
    sns.histplot(random_numbers, bins=10, kde=True)
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.title('Distribution of Random Numbers')
    st.pyplot()

def main():
    st.title("Random Number Generator & Visualization")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Create tabs for generation and download/visualization
    tabs = st.sidebar.radio("Select Action:", ("Generate Numbers", "Download & Visualize"))

    if tabs == "Generate Numbers":
        # Input parameters using text inputs and a slider
        min_value = st.number_input("Enter the minimum boundary of random numbers", value=1)
        max_value = st.number_input("Enter the maximum boundary of random numbers", value=100)
        num_samples = st.slider("Enter the quantity of number samples", min_value=1, max_value=100, value=10)

        # Run the command to generate random numbers one by one
        if st.button("Generate Random Numbers"):
            st.text("Generating random numbers...")
            run_command(min_value, max_value, num_samples)
            st.text("Random number generation completed!")

    elif tabs == "Download & Visualize":
        # Download the CSV file
        with open('random_numbers.csv', 'r') as file:
            file_content = file.read()
        st.download_button("Download Random Numbers CSV", data=file_content, file_name="random_numbers.csv", mime="text/csv")

        # Visualize the distribution of random numbers
        if st.button("Visualize"):
            st.text("Visualizing the distribution of random numbers...")
            df = pd.read_csv('random_numbers.csv')
            visualize_data(df['Random Numbers'])

if __name__ == "__main__":
    main()

import streamlit as st
import subprocess
import time

def run_command(param1, param2):
    # Replace this command with the actual command you want to run
    command = f"echo 'Parameter 1: {param1}, Parameter 2: {param2}' && sleep 2 && echo 'Command running...' && sleep 2 && echo 'Command running...' && sleep 2 && echo 'Command completed!' > output.txt"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Display an empty text element for command output
    output_text = st.empty()

    # Update the text element and save to the file as the command runs
    log = ""
    with open("output.txt", "w") as file:
        while True:
            line = process.stdout.readline()
            if not line:
                break
            log += line
            output_text.text(log)
            file.write(line)

def main():
    st.title("Streamlit App with Command Output Log")

    # Input parameters using selection
    param1 = st.selectbox("Select Parameter 1", [1, 2, 3])
    param2 = st.selectbox("Select Parameter 2", ["A", "B", "C"])

    # Run the command
    if st.button("Run Command"):
        st.text("Running the command...")
        run_command(param1, param2)
        st.text("Command completed!")

        # Add a button to download the output file
        with open("output.txt", "r") as file:
            file_content = file.read()
        st.download_button("Download Output", data=file_content, file_name="output.txt", mime="text/plain")

if __name__ == "__main__":
    main()

import streamlit as st
import subprocess
import re
import io

# Specify the path to your Conda environment YAML file
conda_environment_yaml = 'https://github.com/harikrishnad1997/flask-app-r/blob/master/r_environment.yml?raw=true'

# Specify the name of your Conda R environment
conda_environment_name = 'my_r_environment'

# Create a Streamlit app
st.title("Run R Script")

# Create a file uploader for uploading R script files
r_code_file = st.file_uploader("Upload a .txt file containing R code", type=["txt"])

if r_code_file:
    r_code = r_code_file.read().decode('utf-8')

    if st.button("Check submission file"):
        try:
            # Create the Conda environment from the YAML file
            create_env_command = f'conda env create -f {conda_environment_yaml}'
            subprocess.run(create_env_command, shell=True, executable='/bin/bash')

            # Activate the Conda R environment
            activate_env_command = f'conda activate {conda_environment_name}'
            subprocess.run(activate_env_command, shell=True, executable='/bin/bash')

            # Print the Conda environment name
            st.write(f"Activated R Conda environment and running the code")

            # Execute the R code in the environment
            result = subprocess.check_output(['conda', 'run', '-n', conda_environment_name, 'Rscript', '-e', r_code], stderr=subprocess.STDOUT, universal_newlines=True)
            st.header("Output:")
            st.code(result)
            st.download_button('Download the correct code', r_code, file_name="r_code.txt", key="download_code")
        except subprocess.CalledProcessError as e:
            st.error(f"Error: {e.output}")

st.write("Example R code: `library(data.table)`")

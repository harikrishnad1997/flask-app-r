import streamlit as st
import subprocess
import re

# Specify the path to your Conda environment YAML file
conda_environment_yaml = '/Users/harikrishnadev/Desktop/Github/flask-app-r/r_environment.yml'

# Specify the name of your Conda R environment
conda_environment_name = 'my_r_environment'

# Create a Streamlit app
st.title("Run R Script")

r_code = ""

# Create a text area for entering R code
r_code = st.text_area("Enter R code here", height=200)

if st.button("Run R Script"):
    try:
        # Create the Conda environment from the YAML file
        create_env_command = f'conda env create -f {conda_environment_yaml}'
        subprocess.run(create_env_command, shell=True, executable='/bin/bash')

        # Activate the Conda R environment
        activate_env_command = f'conda activate {conda_environment_name}'
        subprocess.run(activate_env_command, shell=True, executable='/bin/bash')

        # Print the Conda environment name
        st.write(f"Activated Conda environment: {conda_environment_name}")

        # Install missing R packages (if not already installed)
        # install_packages_command = 'conda install -c conda-forge r-tidyverse r-broom'
        # subprocess.run(install_packages_command, shell=True, executable='/bin/bash')

        # Execute the R code in the environment
        result = subprocess.check_output(['conda', 'run', '-n', conda_environment_name, 'Rscript', '-e', r_code], stderr=subprocess.STDOUT, universal_newlines=True)
        st.header("Output:")
        st.code(result)
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e.output}")
        
st.download_button('Download the correct code', r_code)

st.write("Example R code: `library(data.table)`")

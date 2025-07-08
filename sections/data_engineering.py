import streamlit as st
import pandas as pd
import boto3
from io import StringIO

# --- Function to Read from S3 ---
def read_csv_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    return csv_string

# --- Streamlit App Entry Point ---
def run():
    st.title("🛠️ Data Engineering Project by Aashay")

    st.markdown("""
    ### Project Summary
    Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3, process it on an EC2 instance, and save the data in a GitHub repository using Streamlit.

    **Project Highlights:**
    - Uploading data to Amazon S3.
    - Setting up and configuring an EC2 instance.
    - Connecting to EC2 instance via VSCode.
    - Creating a Python virtual environment and installing packages.
    - Configuring AWS credentials.
    - Running and hosting a Streamlit app.
    """)

    with st.expander("🔹 Step 1: Upload CSV Files to Amazon S3"):
        st.markdown("""
        Amazon S3 offers scalable, durable, and secure object storage. Key benefits include:
        - **Scalability** and **Durability**
        - **Security** and **Accessibility**
        - **Cost-Effectiveness** with different storage classes
        """)

    with st.expander("🔹 Step 2: Create and Configure EC2 Instance"):
        st.markdown("""
        - EC2 provides resizable virtual servers in the cloud.
        - Used for running applications, data analysis, and more.
        - **Elastic IPs** and **Port 8501** (for Streamlit) were configured.
        """)

    with st.expander("🔹 Step 3: Python Environment Setup"):
        st.code("""
        sudo apt update && sudo apt upgrade -y
        sudo apt install python3-pip
        python3 -m venv myenv
        source myenv/bin/activate
        """, language='bash')

    with st.expander("🔹 Step 4: VSCode SSH Configuration"):
        st.code("""
        ssh-keygen -t rsa -b 2048
        ssh-copy-id -i ~/.ssh/your_key.pem ubuntu@your_ec2_ip
        """, language='bash')
        st.markdown("""
        Configure `~/.ssh/config`:
        ```
        Host my-ec2
            HostName your_ec2_ip
            User ubuntu
            IdentityFile ~/.ssh/your_key.pem
        ```
        """)

    with st.expander("🔹 Step 5: Install Dependencies"):
        st.code("""
        sudo apt install git curl unzip tar make sudo vim wget -y
        git clone "Your-repo-url"
        pip install -r requirements.txt
        """, language='bash')

    with st.expander("🔹 Step 6: Configure AWS Credentials"):
        st.code("""
        sudo apt-get install awscli -y
        aws configure
        aws s3 ls
        """, language='bash')

    st.markdown("---")
    st.header("📥 Load CSV from Amazon S3")

    file_selection = st.radio("Choose file to load:", ["1.csv", "2.csv"])

    bucket_name = "ecomsql"
    file_key = file_selection
    csv_string = read_csv_from_s3(bucket_name, file_key)

    # Save and read CSV into DataFrame
    local_csv_path = file_key
    with open(local_csv_path, 'w') as f:
        f.write(csv_string)
    df = pd.read_csv(local_csv_path)

    st.write(f"### Displaying: {file_key}")
    st.dataframe(df)

# --- Required for streamlit sections ---
if __name__ == "__main__":
    run()

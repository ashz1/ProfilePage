import streamlit as st
import boto3
import pandas as pd

def run():
    st.title("Data Engineering Project by Aashay")

    st.header("Project Summary")
    st.markdown("""
    Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3,
    process it on an EC2 instance, and save the data in a GitHub repository using Streamlit.
    
    **Project Highlights:**
    - Uploading data to Amazon S3.
    - Setting up and configuring an EC2 instance.
    - Connecting to the EC2 instance via VSCode for seamless development.
    - Creating a Python virtual environment and installing necessary packages.
    - Configuring AWS credentials for secure access.
    - Running and hosting a Streamlit app to visualize the data.
    """)

    st.header("Project Steps")
    st.markdown("""
    This project demonstrates an app, which imports data from Amazon S3, processes it on an EC2 instance, and saves
    the data in the Github repository, using Streamlit. Below is an overview of the steps involved in this project.
    """)

    st.subheader("Step 1: Upload CSV Files to S3")
    st.markdown("""
    The first step was to upload two CSV files to an Amazon S3 bucket.

    Amazon S3 (Simple Storage Service) is a scalable object storage service that offers high availability, security, and performance. It is designed to store and retrieve any amount of data from anywhere on the web.

    **Key Features of Amazon S3:**
    - Scalability: S3 automatically scales to handle large volumes of data and high request rates.
    - Durability: S3 is designed for 99.999999999% (11 9's) of durability.
    - Security: S3 provides comprehensive security and compliance capabilities that meet even the most stringent regulatory requirements.
    - Accessibility: Data stored in S3 can be accessed from anywhere via the internet.
    - Cost-Effectiveness: S3 offers a range of storage classes to help you optimize costs.
    """)

    st.subheader("Step 2: Create EC2 Instance")
    st.markdown("""
    Next, I created an EC2 instance on an Ubuntu machine. Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It allows users to run applications on a virtual server in the cloud, providing flexibility and scalability for various workloads.

    Elastic IP Addresses and exposing Streamlit port 8501 were part of the setup.
    """)

    st.subheader("Step 3: Downloading Packages and Creating Virtual Environment")
    st.code("""
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install python3-pip
python3 -m venv myenv
source myenv/bin/activate
""", language='bash')

    st.subheader("Step 4: Connecting Visual Code Studio to EC2")
    st.markdown("""
    After setting up the virtual environment, I cloned the GitHub repository containing the Streamlit app within the Ubuntu environment.
    
    **Connecting VSCode to EC2 via SSH:**
    - Generate SSH Key Pair: `ssh-keygen -t rsa -b 2048`
    - Copy SSH Key: `ssh-copy-id -i ~/.ssh/your_key.pem ubuntu@your_ec2_public_ip`
    - Configure VSCode SSH config:
    ```
    Host my-ec2-instance
        HostName your_ec2_public_ip
        User ubuntu
        IdentityFile ~/.ssh/your_key.pem
    ```
    - Connect using VSCode Remote - SSH extension.
    """)

    st.subheader("Step 5: Installing Required Packages and Libraries")
    st.code("""
sudo apt install git curl unzip tar make sudo vim wget -y
git clone "Your-repository"
pip install -r requirements.txt
""", language='bash')

    st.subheader("Step 6: Configure AWS Credentials")
    st.markdown("""
    Install and configure AWS CLI:
    ```bash
    sudo apt-get install awscli -y
    aws configure
    ```
    Enter your AWS Access Key ID, Secret Access Key, region, and output format.
    Verify configuration:
    ```bash
    aws s3 ls
    ```
    """)

    st.subheader("Step 7: Run Streamlit App")

    st.code('''
import streamlit as st
import boto3
import pandas as pd

def read_csv_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    return csv_string

def main():
    st.title('S3 CSV Import Example')
    bucket_name = 'ecomsql'
    file_key = '1.csv'  # Change to '2.csv' to read the second file
    csv_string = read_csv_from_s3(bucket_name, file_key)

    local_csv_path = file_key
    with open(local_csv_path, 'w') as f:
        f.write(csv_string)

    df = pd.read_csv(local_csv_path)
    st.write(df)

if __name__ == "__main__":
    main()
''', language='python')

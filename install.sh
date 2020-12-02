#!/usr/bin/env bash
source setup.sh
create_transfer_conda_env
activate_transfer_conda_env

# Setup transfer
pip install -e .

# Run quick tests
bash test.sh

# Download pre-collected trace files
wget "${S3_BUCKET}/program_data.zip"
yes | unzip program_data.zip
rm -rf program_data.zip

# Download dataset used by programs in demo trace files
mkdir -p demo-data/
pushd demo-data
wget "${S3_BUCKET}/loan_data.zip"
yes | unzip loan_data.zip
rm -rf loan_data.zip
popd
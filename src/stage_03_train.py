from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib

def train(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifacts_dir=config["artifacts"]["artifacts_dir"]
    split_data_dir=config["artifacts"]["split_data_dir"]
    train_data_filename=config["artifacts"]["train"]
    print(os.path.join(artifacts_dir,split_data_dir,train_data_filename))

if __name__ =="main":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()
    print(parsed_args.config)
    print(parsed_args.params)
    train(parsed_args.config,parsed_args.params)    

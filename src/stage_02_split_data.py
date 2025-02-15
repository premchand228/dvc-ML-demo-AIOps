from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_and_save(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifacts_dir=config["artifacts"]["artifacts_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]
    raw_local_file_path=os.path.join(artifacts_dir,raw_local_dir,raw_local_file)
    print(raw_local_file_path)
    df=pd.read_csv(raw_local_file_path )
    print(df.head(3))
    split_ratio=params["base"]["test_size"]
    random_state=params["base"]["random_state"]
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)
    print(train.head(1))
    split_data_dir=config["artifacts"]["split_data_dir"]
    print(os.path.join(artifacts_dir,split_data_dir))
    create_directory([os.path.join(artifacts_dir,split_data_dir)])
    train_data_file_name=config["artifacts"]["train"]
    test_data_file_name=config["artifacts"]["test"]
    train_data_file_path=os.path.join(artifacts_dir,split_data_dir,train_data_file_name)
    test_data_file_path=os.path.join(artifacts_dir,split_data_dir,test_data_file_name)
    for data,data_path in (train,train_data_file_path),(test,test_data_file_path):
        save_local_df(data,data_path)
        print("Stage 02 sucessfully run")



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()
    print(parsed_args.config)
    print(parsed_args.params)
    split_and_save(parsed_args.config,parsed_args.params)
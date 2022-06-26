import os
import logging
import subprocess
import pandas as pd
from subprocess import CompletedProcess
from typing import List
from zipfile36 import ZipFile
from pathlib import PosixPath

from utils import *
from constants import *

def extract(datasets: List[str]) -> None:

    set_kaggle_config_dir_venv()
    logging.info('Starting extract process')
    create_dir_to_save_dataset(datasets)
    download_data_from_kaggle(datasets)
    move_downloaded_zip_file(datasets)
    extract_data_from_zip_file(datasets)
    remove_zip_files(datasets)
    convert_csv_to_parquet_format(datasets)
    delete_csv_files()
    logging.info('Finished extract process')

def set_kaggle_config_dir_venv() -> None:
    """
    > Set the KAGGLE_CONFIG_DIR environment variable to .kaggle directory
    """

    pwd: str = os.getcwd()
    logging.info('Setting KAGGLE_CONFIG_DIR')
    os.environ['KAGGLE_CONFIG_DIR'] = f'{pwd}/.kaggle'

def download_data_from_kaggle(datasets: List[str]) -> None:
    """
    It takes a list of datasets as an argument and downloads them from Kaggle.

    Args:
        datasets (List[str]): List of datasets will be downloaded
    """

    for dataset in datasets:
        logging.info(f'Started to download {dataset} dataset')
        completed_process: CompletedProcess = subprocess.run(['kaggle', 'datasets', 'download', '-d', f'{dataset}'], capture_output=True)
        capture_output(completed_process)
        logging.info(f'Finished to download {dataset} dataset')

def create_dir_to_save_dataset(datasets: List[str]) -> None:
    """
    It creates a directory to save the dataset

    Args:
        datasets List[str]: The name of the dataset you want to download.
    """

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        completed_process: CompletedProcess = subprocess.run(['mkdir', f'data/raw/{dataset}'], capture_output=True)
        capture_output(completed_process)

def move_downloaded_zip_file(datasets: List[str]) -> None:
    """
    It takes a list of datasets, splits the dataset name from the url, prints the dataset name and then moves the zip file to the raw data folder

    Args:
        datasets (List[str]): List[str] = The name of the dataset you want to move.
    """

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        logging.info(f'moving {dataset}.zip to data/raw/{dataset}')
        completed_process: CompletedProcess = subprocess.run(['mv', f'{dataset}.zip', f'data/raw/{dataset}/'], capture_output=True)
        capture_output(completed_process)


def extract_data_from_zip_file(datasets: List[str]) -> None:
    """
    It takes a list of datasets, loops through each dataset, splits the dataset name from the path,
    creates a path to the dataset, finds the zip file in the dataset directory, logs the start of the
    extraction process, extracts the zip file, and logs the end of the extraction process

    Args:
        datasets (List[str]): List[str]
    """

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        dataset_path = DATA_RAW_DIR.resolve() / f'{dataset}'
        file_path = list(dataset_path.glob('*.zip'))[0]
        logging.info(f'Starting to extract {dataset}.zip')
        extract_zip_file(file_path)
        logging.info(f'Finished extraction process of the {dataset}.zip file')


def extract_zip_file(file_path: PosixPath) -> None:
    """
    It takes a zip file and extracts it to the same directory as the zip file

    Args:
        file_path (PosixPath): PosixPath = Path to the zip file
    """

    path = str(file_path.parent)
    file_path = str(file_path)
    with ZipFile(file_path, 'r') as zip:
        namelist: List[str] = zip.namelist()
        for member in namelist:
            logging.info(f'Start to extract {member} file')
            zip.extract(member=member, path=path)
            logging.info(f'{member} file extracted successfully')

def remove_zip_files(datasets: List[str]) -> None:
    """
    It takes a list of datasets, splits the dataset name, and then deletes the zip file

    Args:
        datasets (List[str]): List[str]
    """

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        logging.info(f'{dataset}.zip will be deleted')
        completed_process: CompletedProcess = subprocess.run(['find', '.', '-name', f'{dataset}.zip', '-delete'], capture_output=True)
        capture_output(completed_process)
        logging.info(f'{dataset} was deleted')

def convert_csv_to_parquet_format(datasets: List[str]) -> None:
    """
    It takes a list of datasets, loops through each dataset, loops through each csv file in the dataset,
    and then saves the csv file as a parquet file

    Args:
        datasets (List[str]): List[str]
    """

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        logging.info(f'Start to convert csv files in {dataset} to parquet')
        dataset_path = DATA_RAW_DIR.resolve() / f'{dataset}'
        csv_files: List[PosixPath] = list(dataset_path.glob('*.csv'))
        for csv_file in csv_files:
            save_parquet_file(csv_file)
        logging.info(f'conversion process finished in the {dataset} folder')

def save_parquet_file(csv_file: PosixPath) -> None:
    """
    > Read a CSV file, convert it to a Pandas DataFrame, and save it as a Parquet file.

    Args:
        csv_file (PosixPath): The path to the CSV file you want to convert to Parquet.
    """
    df = pd.read_csv(csv_file)
    new_file: str = str(csv_file).replace('csv', 'parquet')
    logging.info(f'save {new_file.split("/")[-1]}')
    df.to_parquet(new_file, engine='fastparquet', index=False)

def delete_csv_files() -> None:
    """
    It deletes all the CSV files in the project directory
    """

    logging.info('Deleting csv files')
    completed_process: CompletedProcess = subprocess.run(['find', '.', '-name', '*.csv', '-delete'], capture_output=True)
    capture_output(completed_process)
import os
import logging
import subprocess
from subprocess import CompletedProcess
from typing import List
from zipfile36 import ZipFile
from pathlib import PosixPath

from utils import *
from constants import *

def extract(datasets: List[str]) -> None:

    set_kaggle_config_dir_venv()
    logging.info('Starting extract process')
    #create_dir_to_save_dataset(datasets)
    #download_data_from_kaggle(datasets)
    #move_downloaded_zip_file(datasets)
    extract_data_from_zip_file(datasets)
    logging.info('Finished extract process')

def set_kaggle_config_dir_venv() -> None:
    """
    > Set the KAGGLE_CONFIG_DIR environment variable to .kaggle directory
    """

    pwd = os.getcwd()
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

    for dataset in datasets:
        dataset = dataset.split('/')[1]
        dataset_path = DATA_RAW_DIR.resolve() / f'{dataset}'
        file_path = list(dataset_path.glob('*.zip'))[0]
        print(file_path)
        #extract_zip_file(file_path)
        #    zip.printdir()
        #    zip.extractall()

def extract_zip_file(file_path: str) -> None:

    with ZipFile(file_path, 'r') as zip:
        zip.namelist()

import logging
import pandas as pd
from pathlib import Path
import subprocess
from subprocess import CompletedProcess
from utils import *
from constants import *
from transform.brazilian_ecommerce import *
                                            

def transform() -> None:

    logging.info('Starting transform process')
    #transform_products(PRODUCTS)
    create_processed_data_dir()
    transform_orders(ORDERS, PROCESSED_DATA_DIR)
    transform_products(PRODUCTS, PROCESSED_DATA_DIR)

def create_processed_data_dir() -> None:

    logging.info('Starting to create a processed data folder')
    completed_process: CompletedProcess = subprocess.run(['mkdir', 'data/processed/'], capture_output=True)
    capture_output(completed_process)
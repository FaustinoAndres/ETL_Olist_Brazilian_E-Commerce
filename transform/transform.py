import logging
import pandas as pd

from utils import *
from constants import *


def transform():

    logging.info("STARTING TRANSFORM")
    transform_products(PRODUCTS)

def transform_products(PRODUCTS) -> None:

    df = pd.read_parquet(PRODUCTS)
    print(df.head())
    print(df.info())
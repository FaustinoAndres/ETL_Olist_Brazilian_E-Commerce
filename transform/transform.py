import logging
import pandas as pd
from pathlib import Path

from utils import *
from constants import *
from transform.brazilian_ecommerce import transform_products

def transform() -> None:

    logging.info('Starting transform process')
    transform_products(PRODUCTS)


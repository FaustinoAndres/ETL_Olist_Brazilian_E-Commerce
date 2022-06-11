import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log.log', filemode='w', level=logging.INFO)

from extract import *
from constants import *


def pipeline() -> None:

    #Extract
    datasets = [OLIST_BRAZILIAN_ECOMMERCE, OLIST_MARKETING_FUNNEL]
    extract(datasets)

    #Transform

    #Load

if __name__ == '__main__':
    pipeline()
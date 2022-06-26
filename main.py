import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log.log', filemode='w', level=logging.INFO)

import extract.extract as extract
import transform.transform as transform
from constants import ( OLIST_BRAZILIAN_ECOMMERCE,
                        OLIST_MARKETING_FUNNEL,
                        )
from utils import connect_to_db

def pipeline() -> None:

    #Extract
    datasets = [OLIST_BRAZILIAN_ECOMMERCE, OLIST_MARKETING_FUNNEL]
    #extract(datasets)

    #Transform
    transform()

    #Load

if __name__ == '__main__':
    pipeline()
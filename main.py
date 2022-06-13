import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log.log', filemode='w', level=logging.INFO)

from extract import *
from transform import *
from constants import *
from utils import connect_to_db

def pipeline() -> None:

    #Extract
    datasets = [OLIST_BRAZILIAN_ECOMMERCE, OLIST_MARKETING_FUNNEL]
    #extract(datasets)

    try:
        conn = connect_to_db()

        print("Successful connection")

    except Exception as ex:
        print(ex)

    #Transform
    #transform()

    #Load

if __name__ == '__main__':
    pipeline()
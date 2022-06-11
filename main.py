from extract import *

import os
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='log.log', filemode='w', level=logging.INFO)

OLIST = 'olistbr/'
BRAZILIAN_ECOMMERCE = 'brazilian-ecommerce'
MARKETING_FUNNEL = 'marketing-funnel-olist'

def pipeline() -> None:

    #Extract
    datasets = [OLIST+BRAZILIAN_ECOMMERCE, OLIST+MARKETING_FUNNEL]
    extract(datasets)

    #Transform

    #Load

if __name__ == '__main__':
    pipeline()
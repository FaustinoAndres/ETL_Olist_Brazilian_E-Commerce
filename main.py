from extract import download_data_from_kaggle, extract_data_from_zip_file

import os
import logging
logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)

OLIST = 'olistbr/'
BRAZILIAN_ECOMMERCE = 'brazilian-ecommerce'
MARKETING_FUNNEL = 'marketing-funnel-olist'

def pipeline():

    #Extract
    braz_ecom_dir = download_data_from_kaggle(OLIST+BRAZILIAN_ECOMMERCE)
    mark_funnel_dir = download_data_from_kaggle(OLIST+MARKETING_FUNNEL)
    extract_data_from_zip_file(braz_ecom_dir, BRAZILIAN_ECOMMERCE)
    extract_data_from_zip_file(mark_funnel_dir, MARKETING_FUNNEL)

    #Transform

    #Load

if __name__ == '__main__':
    pipeline()
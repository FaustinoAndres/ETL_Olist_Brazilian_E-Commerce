from typing import List
import pandas as pd
from pathlib import Path
import logging
from constants import *


def transform_products(PRODUCTS: Path, PROCESSED_DATA_DIR: Path) -> None:

    df: pd.DataFrame = pd.read_parquet(PRODUCTS)
    columns_to_int: List[str] = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']

    df[columns_to_int] = df[columns_to_int].astype('Int64', errors='ignore')


def transform_orders(ORDERS: Path, PROCESSED_DATA_DIR: Path) -> None:


    df: pd.DataFrame = pd.read_parquet(ORDERS)

    df['order_purchase_timestamp'] = pd.to_datetime(df.order_purchase_timestamp, dayfirst=True, errors = 'coerce')
    
    df['order_approved_at'] = pd.to_datetime(df.order_approved_at, dayfirst=True, errors='coerce')
    
    df['order_delivered_carrier_date'] = pd.to_datetime(df.order_delivered_carrier_date, dayfirst=True, errors='coerce')

    df['order_delivered_customer_date'] = pd.to_datetime(df.order_delivered_customer_date, dayfirst=True, errors='coerce')

    df['order_estimated_delivery_date'] = pd.to_datetime(df.order_estimated_delivery_date, dayfirst=True, errors='coerce')

    processed_file: str = str(PROCESSED_DATA_DIR) + '/processed_' + str(ORDERS.name)

    df.to_parquet(processed_file, engine='fastparquet', index=False)
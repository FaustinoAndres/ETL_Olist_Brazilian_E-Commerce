from pathlib import Path

OLIST = 'olistbr/'
BRAZILIAN_ECOMMERCE = 'brazilian-ecommerce'
MARKETING_FUNNEL = 'marketing-funnel-olist'
OLIST_BRAZILIAN_ECOMMERCE = OLIST + BRAZILIAN_ECOMMERCE
OLIST_MARKETING_FUNNEL = OLIST + MARKETING_FUNNEL

ROOT = Path('.').resolve()
DATA_RAW_DIR = ROOT.joinpath('data', 'raw')

PROCESSED_DATA_DIR = ROOT.joinpath('data', 'processed')

PRODUCTS = DATA_RAW_DIR / BRAZILIAN_ECOMMERCE / 'olist_products_dataset.parquet'
ORDERS = DATA_RAW_DIR / BRAZILIAN_ECOMMERCE / 'olist_orders_dataset.parquet'
PRODUCTS_CATEGORY_NAME_TRANSLATION = DATA_RAW_DIR / BRAZILIAN_ECOMMERCE / 'olist_products_category_name_translation.parquet'


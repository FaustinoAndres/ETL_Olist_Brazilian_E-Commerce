from pathlib import Path

OLIST = 'olistbr/'
BRAZILIAN_ECOMMERCE = 'brazilian-ecommerce'
MARKETING_FUNNEL = 'marketing-funnel-olist'
OLIST_BRAZILIAN_ECOMMERCE = OLIST + BRAZILIAN_ECOMMERCE
OLIST_MARKETING_FUNNEL = OLIST + MARKETING_FUNNEL

ROOT = Path('.').resolve()
DATA_RAW_DIR = ROOT.joinpath('data', 'raw')

PRODUCTS = DATA_RAW_DIR / BRAZILIAN_ECOMMERCE / 'olist_products_dataset.parquet'
ORDERS = DATA_RAW_DIR / BRAZILIAN_ECOMMERCE / 'olist_order_dataset.parquet'
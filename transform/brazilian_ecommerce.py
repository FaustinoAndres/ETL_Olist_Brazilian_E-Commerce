

def transform_products(PRODUCTS: Path) -> None:

    df = pd.read_parquet(PRODUCTS)
    print(df.head())
    print(df.info())

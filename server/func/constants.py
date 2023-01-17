import ast
import os

LCD_DICT = ast.literal_eval(os.getenv("LCD_DICT", None))
HIVE_DICT = ast.literal_eval(os.getenv("HIVE_DICT", None))
GRAPHQL_DICT = ast.literal_eval(os.getenv("GRAPHQL_DICT", None))
SCANWORKS_URL = os.getenv("SCANWORKS_URL", None)
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", None)

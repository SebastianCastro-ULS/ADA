from loader import load_location_data, load_user_data
from eda import run_location_eda, run_user_eda
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Cargar archivos
    loc_df = load_location_data("10_million_location.txt")
    user_df = load_user_data("10_million_user.txt")

    # Análisis EDA
    if loc_df is not None:
        run_location_eda(loc_df)
    if user_df is not None:
        run_user_eda(user_df)

if __name__ == "__main__":
    main()

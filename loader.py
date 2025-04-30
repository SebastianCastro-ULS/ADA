import polars as pl
import os
import logging

def load_location_data(filepath: str):
    try:
        logging.info(f"Cargando archivo de ubicación: {filepath}")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"El archivo {filepath} no existe.")

        df = pl.read_csv(filepath, has_header=False, new_columns=["lat", "long"])
        df = df.with_columns([
            pl.col("lat").cast(pl.Float64),
            pl.col("long").cast(pl.Float64),
        ])
        logging.info(f"Archivo cargado: {df.height} registros")
        return df
    except Exception as e:
        logging.error(f"Error al cargar datos de ubicación: {e}")
        return None

def load_user_data(filepath: str):
    try:
        logging.info(f"Cargando archivo de usuarios: {filepath}")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"El archivo {filepath} no existe.")

        with open(filepath, "r") as f:
            lines = (line.strip() for line in f)
            df = pl.DataFrame({"adj_list": list(lines)})

        logging.info(f"Archivo cargado: {df.height} registros")
        return df
    except Exception as e:
        logging.error(f"Error al cargar datos de usuarios: {e}")
        return None

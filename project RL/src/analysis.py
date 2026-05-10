import numpy as np
import pandas as pd
from src.utils import timer, logger


# --- БАЗОВЫЙ АНАЛИЗ ---

@timer
@logger
def basic_stats(df):
    return df.describe()


def avg_by_workout(df):
    return df.groupby("workout_type")[["calories_burned", "duration_min"]].mean()


def avg_sleep(df):
    return df["sleep_hours"].mean()


def avg_protein(df):
    return df["protein_g"].mean()


def avg_weight(df):
    return df["weight_kg"].mean()


def weight_change(df):
    return df["weight_kg"].iloc[-1] - df["weight_kg"].iloc[0]


def strength_progress(df):
    return {
        "bench_press": df["bench_press_kg"].iloc[-1] - df["bench_press_kg"].iloc[0],
        "squat": df["squat_kg"].iloc[-1] - df["squat_kg"].iloc[0],
        "deadlift": df["deadlift_kg"].iloc[-1] - df["deadlift_kg"].iloc[0],
    }


def avg_mood(df):
    return df["mood"].mean()


def max_calories_day(df):
    row = df.loc[df["calories_burned"].idxmax()]
    return {
        "date": row["date"],
        "calories": row["calories_burned"],
        "workout": row["workout_type"],
    }


def min_energy_day(df):
    row = df.loc[df["energy_level"].idxmin()]
    return {
        "date": row["date"],
        "energy": row["energy_level"],
        "workout": row["workout_type"],
    }


# --- NUMPY ---

def numpy_stats(df):
    return {
        "median_calories": np.median(df["calories_burned"]),
        "std_duration": np.std(df["duration_min"]),
        "percentile_90_calories": np.percentile(df["calories_burned"], 90),
    }


# --- ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ ---

def sleep_vs_energy(df):
    return df.groupby(pd.cut(df["sleep_hours"], bins=3))["energy_level"].mean()
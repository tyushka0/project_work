import pandas as pd

from src.analysis import (
    avg_sleep,
    avg_protein,
    avg_weight,
    weight_change,
    avg_mood,
)


def test_avg_sleep():
    df = pd.DataFrame({
        "sleep_hours": [6, 8, 7]
    })

    assert avg_sleep(df) == 7


def test_avg_protein():
    df = pd.DataFrame({
        "protein_g": [100, 150, 200]
    })

    assert avg_protein(df) == 150


def test_avg_weight():
    df = pd.DataFrame({
        "weight_kg": [70, 80, 90]
    })

    assert avg_weight(df) == 80


def test_weight_change():
    df = pd.DataFrame({
        "weight_kg": [70, 75]
    })

    assert weight_change(df) == 5


def test_avg_mood():
    df = pd.DataFrame({
        "mood": [6, 8, 10]
    })

    assert avg_mood(df) == 8
import argparse

from src.data_loader import load_data
from src.analysis import (
    basic_stats,
    avg_by_workout,
    avg_sleep,
    avg_protein,
    avg_weight,
    weight_change,
    strength_progress,
    avg_mood,
    max_calories_day,
    min_energy_day,
    numpy_stats,
)

df = load_data("gym_dataset.csv")

parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    help="Команды: stats, workout, progress, numpy, mood"
)

args = parser.parse_args()


if args.command == "stats":
    print("📊 BASIC STATS")
    print(basic_stats(df))

    print("\n😴 AVG SLEEP:", avg_sleep(df))
    print("🍗 AVG PROTEIN:", avg_protein(df))
    print("⚖️ AVG WEIGHT:", avg_weight(df))


elif args.command == "workout":
    print("🏋️ AVG BY WORKOUT")
    print(avg_by_workout(df))

    print("\n🔥 MAX CALORIES DAY")
    print(max_calories_day(df))


elif args.command == "progress":
    print("📈 WEIGHT CHANGE")
    print(weight_change(df))

    print("\n🏋️ STRENGTH PROGRESS")
    print(strength_progress(df))


elif args.command == "numpy":
    print("🧮 NUMPY STATS")
    print(numpy_stats(df))


elif args.command == "mood":
    print("😊 AVG MOOD")
    print(avg_mood(df))

    print("\n⚡ MIN ENERGY DAY")
    print(min_energy_day(df))


else:
    print("❌ Unknown command")
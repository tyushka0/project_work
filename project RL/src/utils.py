import time


# --- ДЕКОРАТОРЫ ---

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Время:", round(time.time() - start, 4))
        return result
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print("Запуск функции:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# --- ГЕНЕРАТОРЫ ---

def chunk_reader(df, size):
    for i in range(0, len(df), size):
        yield df.iloc[i:i + size]


def workout_generator(df):
    for _, row in df.iterrows():
        yield row
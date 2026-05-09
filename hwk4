import pickle
import os

def cache(filename, use_named=False):

    def decorator(func):
        cache_dict = {}
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                cache_dict = pickle.load(f)
            print(f"Загружен кэш из {filename}")

        def wrapper(*args, **kwargs):
            if use_named:
                key = tuple(sorted(kwargs.items()))
            else:
                key = args

            if key in cache_dict:
                print(f"Результат для {func.__name__}{args} взят из кэша")
                return cache_dict[key]

            result = func(*args, **kwargs)
            cache_dict[key] = result

            with open(filename, 'wb') as f:
                pickle.dump(cache_dict, f)

            print(f"Результат для {func.__name__}{args} вычислен и сохранён")
            return result

        return wrapper

    return decorator


print("позиционные аргументы")
@cache('sum_cache.pkl', use_named=False)
def sum(a, b):
    return a + b
print(sum(5, 3))
print(sum(5, 3))  # Из кэша
print(sum(3, 5))  # Новый ключ (3,5) - вычислится
print(sum(2, 4))
print(sum(4, 2))  # Новый ключ (4,2) - вычислится

print("\nименновынные аргументы")

@cache('named_cache.pkl', use_named=True)
def sum_named(a, b):
    return a + b

print(sum_named(a=5, b=3))
print(sum_named(b=3, a=5))
print(sum_named(5, 3))

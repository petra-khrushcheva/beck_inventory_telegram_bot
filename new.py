import pathlib


# env_file = f"{pathlib.Path(__file__).parent()}"
a = f"{pathlib.Path(__file__).parents[1]}/.env"

print(a)

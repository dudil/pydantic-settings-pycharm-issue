# pylint: disable=C0111,R0903
from pydantic import BaseSettings


class AppSettings(BaseSettings):
    first_name: str
    last_name: str


def print_hi():
    app_settings = AppSettings(_env_file="dev.env")
    print(f"Hi, {app_settings.first_name} {app_settings.first_name}!")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi()

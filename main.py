import pandas as pd


class User:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        print("Hello.")

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age


def main():
    # 保存
    # user = User("yamada", 20)
    # print(f"name={user.get_name()}, age={user.get_age()}")
    # pd.to_pickle(user, "user.pkl")

    # 読み出し
    user = pd.read_pickle("user.pkl")
    print(f"name={user.get_name()}, age={user.get_age()}")


if __name__ == "__main__":
    main()

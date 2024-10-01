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
    yamada = User("yamada", 20)
    print(f"name={yamada.get_name()}, age={yamada.get_age()}")


if __name__ == "__main__":
    main()

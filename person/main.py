from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    last: str
    last_name: str = field(init=False)

    def __post_init__(self):
        self.last_name = self.name + " " + self.last

    def __str__(self) -> str:
        return f"{self.last_name}"


def main() -> int:
    p = Person("Luciana", "Mena")
    print(p)
    return 0


if __name__ == "__main__":
    main()

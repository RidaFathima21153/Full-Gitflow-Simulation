def greet(name: str) -> str:
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty")

    return f"Hello, {name}!"
def goodbye(name: str) -> str:
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty")

    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("Gitflow Developer"))
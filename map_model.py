class MapModel:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def __str__(self):
        return f"key={self.key} + value={self.value}"

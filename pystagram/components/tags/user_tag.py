from pystagram.components.tags.tag import Tag


class UserTag(Tag):
    def __init__(self, username: str, x: float, y: float):
        self.username = username
        self.x = x
        self.y = y

    def dict(self) -> dict:
        return {
            "username": self.username,
            "x": self.x,
            "y": self.y
        }

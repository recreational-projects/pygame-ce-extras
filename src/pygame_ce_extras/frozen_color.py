"""Module implementing the `FrozenColor` class."""

from typing import Any, Self

import pygame as pg


class FrozenColor(pg.Color):
    """A frozen subclass of `pygame.Color`."""

    def __init__(self, *args, **kwargs: dict[str, Any]) -> None:
        """Create a `FrozenColor` instance."""
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b}, {self.a})"

    def __setattr__(self, name: str, value: pg.Color | tuple[int, ...]) -> None:
        err_msg = f"Cannot set attribute on a `{self.__class__.__name__}` instance"
        raise AttributeError(err_msg)

    def with_alpha(self, alpha: int) -> Self:
        """Return a new `FrozenColor` with `alpha` set to the given value."""
        return FrozenColor(self.r, self.g, self.b, alpha)

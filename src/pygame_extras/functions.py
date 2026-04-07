from __future__ import annotations

from typing import TYPE_CHECKING

import pygame as pg

if TYPE_CHECKING:
    from pathlib import Path


def blit(
    *,
    surface: pg.Surface,
    source: pg.Surface,
    dest: pg.typing.Point = (0, 0),
    area: pg.typing.RectLike | None = None,
) -> pg.Rect:
    """Draws `source` to `surface`.

    Wraps Pygame's blit, but requires `dest` to have length 2.
    This prevents unexpected results when `dest` is passed concatenated tuples in error.
    """
    if len(dest) != 2:  # noqa: PLR2004
        err_msg = f"`dest` must be length 2. Got {len(dest)}: {dest}"
        raise TypeError(err_msg)

    return surface.blit(source=source, dest=dest, area=area)


def load_svg(filepath: Path, size: tuple[int, int]) -> pg.Surface:
    """TODO: Docstring."""
    glyph = pg.image.load_sized_svg(file=filepath, size=size)
    glyph.fill(pg.Color("white"), special_flags=pg.BLEND_RGB_ADD)
    surface = pg.Surface(size, pg.SRCALPHA)
    blit(surface=surface, source=glyph)
    return surface

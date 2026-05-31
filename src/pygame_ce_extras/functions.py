"""Module implementing helper functions."""

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
    """Draws `source` onto `surface`.

    Wraps `pygame.Surface.blit`, but requires keyword arguments,
    and optional `dest` to have length 2.
    This prevents unexpected results when `dest` is passed concatenated tuples in error.
    """
    if len(dest) != 2:  # noqa: PLR2004
        err_msg = f"`dest` must be length 2. Got {len(dest)}: {dest}"
        raise TypeError(err_msg)

    return surface.blit(source=source, dest=dest, area=area)


def icon_from_svg(
    *,
    filepath: Path,
    size: int = 24,
    scale_factor: float = 1,
    foreground_color: pg.typing.ColorLike | None = None,
    background_color: pg.typing.ColorLike | None = None,
) -> pg.Surface:
    """Generate a square icon image from an SVG file, with optional circular background.

    Args:
    ----
    filepath:
        Path to the SVG file to load.

    size:
        Size of the overall image.

    scale_factor:
        The SVG image is scaled by this factor and centered.

    foreground_color:
        Color to apply to the SVG image.
        If `None` (default), original colors are kept.

    background_color:
        Color to fill a background circle.
        If `None` (default), no background is drawn.

    Returns
    -------
    `pg.Surface`

    """
    glyph_size_ = size * scale_factor
    glyph = pg.image.load_sized_svg(file=filepath, size=(glyph_size_, glyph_size_))
    if foreground_color:
        glyph.fill(pg.Color("white"), special_flags=pg.BLEND_RGB_ADD)
        glyph.fill(foreground_color, special_flags=pg.BLEND_RGB_MULT)

    surface_ = pg.Surface(size=(size, size), flags=pg.SRCALPHA)
    if background_color:
        radius_ = size // 2
        pg.draw.aacircle(
            surface=surface_,
            color=background_color,
            center=(radius_, radius_),
            radius=radius_,
            width=0,
        )
    glyph_dest_ = (size - glyph_size_) // 2
    blit(surface=surface_, source=glyph, dest=(glyph_dest_, glyph_dest_))
    return surface_

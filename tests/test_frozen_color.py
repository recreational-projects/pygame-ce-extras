import pygame as pg

from pygame_ce_extras import FrozenColor


def test_create__from_name() -> None:
    # arrange
    # act
    frozen_red = FrozenColor("red")
    # assert
    assert frozen_red == pg.Color("red")


def test_create__from_self() -> None:
    # arrange
    frozen_blue = FrozenColor("blue")
    # act
    frozen_blue2 = FrozenColor(frozen_blue)
    # assert
    assert frozen_blue2 == frozen_blue


def test_with_alpha() -> None:
    # arrange
    frozen_green = FrozenColor("green")
    # act
    frozen_green_a = frozen_green.with_alpha(128)
    # assert
    assert frozen_green_a == pg.Color(0, 255, 0, 128)

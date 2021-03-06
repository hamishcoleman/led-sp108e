import pytest
import commands
import structures


def test_frame():
    with pytest.raises(ValueError):
        # data too long
        commands.frame(4, b'\x01\x02\x03\x04')

    assert b'\x38\x00\x00\x00\x7f\x83' == commands.frame(0x7f, None)
    assert b'\x38\x80\x00\x00\x0f\x83' == commands.frame(0xf, b'\x80')
    assert b'\x38\x01\x20\x44\x01\x83' == commands.frame(1, b'\x01\x20\x44')


def test_speed():
    assert b'\x38\x64\x00\x00\x03\x83' == commands.speed(100)


def test_get_device_name():
    assert b'\x38\x00\x00\x00\x77\x83' == commands.get_device_name()


def test_check_device():
    with pytest.raises(AttributeError):
        commands.check_device(None)

    assert b'\x38\x30\x20\x10\xd5\x83' == commands.check_device(0x102030)


def test_mode_change():
    assert b'\x38\x00\x00\x00\x06\x83' \
        == commands.mode_change(commands.MODE_AUTO)

    assert b'\x38\xcd\x00\x00\x2c\x83' \
        == commands.mode_change(commands.MODE_METEOR)


def test_sync():
    assert b'\x38\x00\x00\x00\x10\x83' == commands.sync()


def test_set_ic_model():
    assert b'\x38\x1d\x00\x00\x1c\x83' == commands.set_ic_model(0x1d)


def test_color():
    rgb = structures.RGB(0x10, 0x20, 0x30)
    assert b'\x38\x10\x20\x30\x22\x83' == commands.color(rgb)


def test_brightness():
    assert b'\x38\x45\x00\x00\x2a\x83' == commands.brightness(0x45)


def test_dot_count():
    assert b'\x38\x23\x01\x00\x2d\x83' == commands.dot_count(0x123)


def test_sec_count():
    assert b'\x38\x06\x00\x00\x2e\x83' == commands.sec_count(6)

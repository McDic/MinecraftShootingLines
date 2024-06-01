import typing

from .constants import DEFAULT_BLOCK_MODIFICATION_LIMIT, MINECRAFT_NAMESPACE_PREFIX
from .errors import DatapackError


def create_command(*args: typing.Any) -> str:
    """
    Create a single Minecraft command from given `args`.
    """
    return " ".join(str(arg) for arg in args)


def fill(
    x1: int,
    y1: int,
    z1: int,
    x2: int,
    y2: int,
    z2: int,
    block: str,
    replace_block: str | None = None,
) -> str:
    """
    Directly create `fill` command.
    If the volume is only 1 block, then use `setblock` instead.
    """
    block = (
        block
        if block.startswith(MINECRAFT_NAMESPACE_PREFIX) or (":" in block)
        else MINECRAFT_NAMESPACE_PREFIX + block
    )
    if x1 == x2 and y1 == y2 and z1 == z2:
        return create_command("setblock", x1, y1, z1, block)
    else:
        args = [
            "fill",
            min(x1, x2),
            min(y1, y2),
            min(z1, z2),
            max(x1, x2),
            max(y1, y2),
            max(z1, z2),
            block,
        ]
        if replace_block:
            args += ["replace", replace_block]
        return create_command(*args)


def fills(
    x1: int,
    y1: int,
    z1: int,
    x2: int,
    y2: int,
    z2: int,
    block: str,
    *args,
    limit: int = DEFAULT_BLOCK_MODIFICATION_LIMIT,
    **kwargs,
) -> typing.Generator[str, None, None]:
    """
    Create multiple `fill` commands by recursive methods,
    in case total volume exceeds the limit.
    """
    if limit < DEFAULT_BLOCK_MODIFICATION_LIMIT:
        raise DatapackError(f"Given limit = {limit} is too small")

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    z1, z2 = min(z1, z2), max(z1, z2)
    x_length = x2 - x1 + 1
    y_length = y2 - y1 + 1
    z_length = z2 - z1 + 1

    max_length = max(x_length, y_length, z_length)
    if x_length * y_length * z_length <= limit:
        yield fill(x1, y1, z1, x2, y2, z2, block, *args, **kwargs)
    elif max_length == x_length:
        x_mid = (x1 + x2) // 2
        yield from fills(x1, y1, z1, x_mid, y2, z2, block, limit=limit, *args, **kwargs)
        yield from fills(
            x_mid + 1, y1, z1, x2, y2, z2, block, limit=limit, *args, **kwargs
        )
    elif max_length == y_length:
        y_mid = (y1 + y2) // 2
        yield from fills(x1, y1, z1, x2, y_mid, z2, block, limit=limit, *args, **kwargs)
        yield from fills(
            x1, y_mid + 1, z1, x2, y2, z2, block, limit=limit, *args, **kwargs
        )
    else:
        z_mid = (z1 + z2) // 2
        yield from fills(x1, y1, z1, x2, y2, z_mid, block, limit=limit, *args, **kwargs)
        yield from fills(
            x1, y1, z_mid + 1, x2, y2, z2, block, limit=limit, *args, **kwargs
        )


def border_fills(
    x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, block: str, *args, **kwargs
) -> typing.Generator[str, None, None]:
    """
    Fills outline of `[x1, y1, z1]` to `[x2, y2, z2]`.
    """
    if x1 == x2 or z1 == z2:
        raise DatapackError(
            "Given range cannot be border-filled; (x1 = %d, x2 = %d, z1 = %d, z2 = %d)"
            % (x1, x2, z1, z2)
        )

    x1, x2 = min(x1, x2), max(x1, x2)
    z1, z2 = min(z1, z2), max(z1, z2)
    yield from fills(x1, y1, z1, x1, y2, z2 - 1, block, *args, **kwargs)
    yield from fills(x1, y1, z2, x2 - 1, y2, z2, block, *args, **kwargs)
    yield from fills(x2, y1, z2, x2, y2, z1 + 1, block, *args, **kwargs)
    yield from fills(x2, y1, z1, x1 + 1, y2, z2, block, *args, **kwargs)

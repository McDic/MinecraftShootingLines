import typing

from .constants import DEFAULT_BLOCK_MODIFICATION_LIMIT, MINECRAFT_NAMESPACE_PREFIX
from .errors import DatapackError


def fill(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, block: str) -> str:
    """
    Directly create `fill` command.
    """
    return (
        f"fill {min(x1, x2)} {min(y1, y2)} {min(z1, z2)} "
        f"{max(x1, x2)} {max(y1, y2)} {max(z1, z2)} "
        + (
            block
            if block.startswith(MINECRAFT_NAMESPACE_PREFIX)
            else MINECRAFT_NAMESPACE_PREFIX + block
        )
    )


def fills(
    x1: int,
    y1: int,
    z1: int,
    x2: int,
    y2: int,
    z2: int,
    block: str,
    limit: int = DEFAULT_BLOCK_MODIFICATION_LIMIT,
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
        yield fill(x1, y1, z1, x2, y2, z2, block)
    elif max_length == x_length:
        x_mid = (x1 + x2) // 2
        yield from fills(x1, y1, z1, x_mid, y2, z2, block, limit=limit)
        yield from fills(x_mid + 1, y1, z1, x2, y2, z2, block, limit=limit)
    elif max_length == y_length:
        y_mid = (y1 + y2) // 2
        yield from fills(x1, y1, z1, x2, y_mid, z2, block, limit=limit)
        yield from fills(x1, y_mid + 1, z1, x2, y2, z2, block, limit=limit)
    else:
        z_mid = (z1 + z2) // 2
        yield from fills(x1, y1, z1, x2, y2, z_mid, block, limit=limit)
        yield from fills(x1, y1, z_mid + 1, x2, y2, z2, block, limit=limit)

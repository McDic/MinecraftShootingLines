import typing

from common import MCFunction, raw_commands, utils
from common.constants import AVAILABLE_COLORS

LEFT_END: typing.Final[int] = -64
RIGHT_END: typing.Final[int] = 63
Y_HIGH: typing.Final[int] = 255


def concrete(color: AVAILABLE_COLORS) -> str:
    return "minecraft:%s_concrete" % (color,)


def main():
    """
    Generate map creation.
    """
    create_map_function = MCFunction(
        utils.get_datapack_path_auto(), "shooting_lines", "reset", "common", "map"
    )
    create_map_function.add_commands(
        # "# Remove everything",
        # raw_commands.fills(
        #     LEFT_END - 2,
        #     -64,
        #     LEFT_END - 2,
        #     RIGHT_END + 2,
        #     Y_HIGH,
        #     RIGHT_END + 2,
        #     "air",
        # ),
        "# Outer area is black",
        raw_commands.fills(
            LEFT_END - 2,
            0,
            LEFT_END - 2,
            RIGHT_END + 2,
            1,
            RIGHT_END + 2,
            concrete("black"),
        ),
        "# Inner area is white",
        raw_commands.fills(
            LEFT_END + 4,
            1,
            LEFT_END + 4,
            RIGHT_END - 4,
            1,
            RIGHT_END - 4,
            concrete("white"),
        ),
        "# Wall barriers",
        raw_commands.fills(
            LEFT_END - 2,
            2,
            LEFT_END - 2,
            LEFT_END - 2,
            Y_HIGH,
            RIGHT_END + 2,
            "barrier",
        ),
        raw_commands.fills(
            LEFT_END - 2,
            2,
            RIGHT_END + 2,
            RIGHT_END + 2,
            Y_HIGH,
            RIGHT_END + 2,
            "barrier",
        ),
        raw_commands.fills(
            RIGHT_END + 2,
            2,
            RIGHT_END + 2,
            RIGHT_END + 2,
            Y_HIGH,
            LEFT_END - 2,
            "barrier",
        ),
        raw_commands.fills(
            RIGHT_END + 2,
            2,
            LEFT_END - 2,
            LEFT_END - 2,
            Y_HIGH,
            LEFT_END - 2,
            "barrier",
        ),
        "# Standing barriers",
        *(
            raw_commands.fills(
                LEFT_END - 2,
                y,
                LEFT_END - 2,
                RIGHT_END + 2,
                y,
                RIGHT_END + 2,
                "barrier",
            )
            for y in range(40, 160, 20)
        ),
    )
    create_map_function.write()


if __name__ == "__main__":
    utils.do_basic_logging_config()
    main()

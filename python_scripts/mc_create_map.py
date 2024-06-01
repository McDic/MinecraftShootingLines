import typing

from common import MCFunction, raw_commands, utils
from common.constants import AVAILABLE_BLOCK_COLORS, LEFT_END, RIGHT_END

Y_HIGH: typing.Final[int] = 255


def concrete(color: AVAILABLE_BLOCK_COLORS) -> str:
    return "minecraft:%s_concrete" % (color,)


def main():
    """
    Generate map creation.

    - `y=1`: Visible board
    - `y=0`: Temporary calculation states
    """
    reset_map_bottom_visible_function = MCFunction(
        utils.get_datapack_path_auto(),
        "shooting_lines",
        "reset",
        "common",
        "map_bottom_visible",
    )
    reset_map_bottom_hidden_function = MCFunction(
        utils.get_datapack_path_auto(),
        "shooting_lines",
        "reset",
        "common",
        "map_bottom_hidden",
    )
    reset_map_barrier_function = MCFunction(
        utils.get_datapack_path_auto(),
        "shooting_lines",
        "reset",
        "common",
        "map_barriers",
    )

    reset_map_bottom_visible_function.add_commands(
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
        "# y=1 -> visible board",
        "# y=0 -> fixed constant to determine inner/outer area",
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
        "# Border area is gray",
        raw_commands.fills(
            LEFT_END + 3,
            0,
            LEFT_END + 3,
            RIGHT_END - 3,
            1,
            RIGHT_END - 3,
            concrete("light_gray"),
        ),
        *[
            raw_commands.fill(x, 0, z, x, 0, z, concrete("black"))
            for x in [LEFT_END + 3, RIGHT_END - 3]
            for z in [LEFT_END + 3, RIGHT_END - 3]
        ],
        "# Inner area is also black",
        raw_commands.fills(
            LEFT_END + 4,
            0,
            LEFT_END + 4,
            RIGHT_END - 4,
            1,
            RIGHT_END - 4,
            concrete("black"),
        ),
    )

    reset_map_bottom_hidden_function.add_commands(
        raw_commands.fills(
            LEFT_END - 2, -1, LEFT_END - 2, RIGHT_END + 2, -10, RIGHT_END + 2, "air"
        )
    )

    reset_map_barrier_function.add_commands(
        "# Wall barriers",
        raw_commands.fills(
            LEFT_END - 2,
            2,
            LEFT_END - 2,
            LEFT_END - 2,
            Y_HIGH,
            RIGHT_END + 2,
            concrete("black"),
        ),
        raw_commands.fills(
            LEFT_END - 2,
            2,
            RIGHT_END + 2,
            RIGHT_END + 2,
            Y_HIGH,
            RIGHT_END + 2,
            concrete("black"),
        ),
        raw_commands.fills(
            RIGHT_END + 2,
            2,
            RIGHT_END + 2,
            RIGHT_END + 2,
            Y_HIGH,
            LEFT_END - 2,
            concrete("black"),
        ),
        raw_commands.fills(
            RIGHT_END + 2,
            2,
            LEFT_END - 2,
            LEFT_END - 2,
            Y_HIGH,
            LEFT_END - 2,
            concrete("black"),
        ),
        "# Standing barriers",
        *(
            raw_commands.fills(
                LEFT_END - 1,
                y,
                LEFT_END - 1,
                RIGHT_END + 1,
                y,
                RIGHT_END + 1,
                "barrier",
            )
            for y in range(20, 160, 20)
        ),
    )
    reset_map_bottom_visible_function.write()
    reset_map_bottom_hidden_function.write()
    reset_map_barrier_function.write()


if __name__ == "__main__":
    utils.do_basic_logging_config()
    main()

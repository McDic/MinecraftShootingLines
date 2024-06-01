from common import MCFunction, raw_commands, utils
from common.constants import LEFT_END, RIGHT_END


def main():
    """
    Generate outline reservation related functions.
    """
    reset_outline_reservation_function = MCFunction(
        utils.get_datapack_path_auto(),
        "shooting_lines",
        "game",
        "select",
        "occupy",
        "reset_reservations",
    )
    reset_outline_reservation_function.add_commands(
        raw_commands.border_fills(
            LEFT_END + 3,
            -1,
            LEFT_END + 3,
            RIGHT_END - 3,
            -1,
            RIGHT_END - 3,
            "minecraft:air",
            replace_block="#shooting_lines:outline/reserved",
        )
    )
    reset_outline_reservation_function.write()


if __name__ == "__main__":
    utils.do_basic_logging_config()
    main()

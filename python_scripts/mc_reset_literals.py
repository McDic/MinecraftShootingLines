from common import MCFunction, utils


def set_literal(i: int) -> str:
    return f"scoreboard players set ${i} literal_numbers {i}"


def main():
    """
    Generate resetting literals.
    """
    reset_literal_function = MCFunction(
        utils.get_datapack_path_auto(),
        "shooting_lines",
        "reset",
        "common",
        "scoreboard_literals",
    )
    reset_literal_function.add_command(set_literal(0))
    for base_num in range(1, 501):
        reset_literal_function.add_command(set_literal(base_num))
        reset_literal_function.add_command(set_literal(-base_num))
    reset_literal_function.write()


if __name__ == "__main__":
    utils.do_basic_config()
    main()

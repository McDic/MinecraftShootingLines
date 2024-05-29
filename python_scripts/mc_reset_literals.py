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
    reset_literal_function.add_commands(set_literal(i) for i in range(-500, 501))
    reset_literal_function.write()


if __name__ == "__main__":
    utils.do_basic_logging_config()
    main()

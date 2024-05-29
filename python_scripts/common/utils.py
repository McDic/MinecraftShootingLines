import logging
from pathlib import Path


def get_datapack_path_auto() -> Path:
    # source_path = ../python_scripts/common/utils.py
    source_path = Path(__file__).resolve()
    return (
        source_path.parent.parent.parent
        / "shooting_lines"
        / "datapacks"
        / "shooting_lines"
    )


def do_basic_logging_config():
    """
    Do basic logging configs.
    """
    logging.basicConfig(
        encoding="utf-8",
        level=logging.DEBUG,
        format="[%(asctime)s][%(levelname)7s]" "[%(filename)s:%(lineno)d] %(message)s",
    )

import logging
from pathlib import Path

from .constants import GENERATED_MCFUNCTION_PREFIX
from .errors import DatapackError


logger = logging.getLogger("mcfunc")


class MCFunction:
    """
    Indicates mcfunction. Every mcfunction generated
    by this class will have `generated` as suffix folder.
    """

    def __init__(self, datapack_path: Path | str, namespace: str, *path: str):
        assert len(path) > 0, "Given path is empty"
        path = path[:-1] + ("generated", path[-1])

        datapack_path = Path(datapack_path)
        assert datapack_path.exists(), \
            f"Given datapack path {datapack_path} does not exist"

        self._function_name: str = f"{namespace}:{"/".join(path)}"
        self._commands: list[str] = []
        self._locked: bool = False

        self._path = datapack_path / "data" / namespace / "functions"
        for p in path[:-1]:
            self._path = self._path / p
        self._path = self._path / f"{path[-1]}.mcfunction"

    @property
    def name(self):
        """
        The name of this function in Minecraft commands.
        """
        return self._function_name

    def raise_if_locked(self):
        if self._locked:
            raise DatapackError(
                f"This MCFunction({self.name}) is already locked"
            )

    def add_command(self, command: str):
        """
        Add given command to this function.
        If given command is a comment, there is no effect.
        """
        self.raise_if_locked()
        command = command.strip()
        if command.startswith("#"):
            return
        self._commands.append(command)

    def write(self):
        """
        Lock this function and write it to target file.
        """
        self.raise_if_locked()
        self._locked = True

        if self._path.is_file():
            with open(self._path) as command_file:
                first_line = command_file.readline().strip()
                if GENERATED_MCFUNCTION_PREFIX != first_line:
                    raise DatapackError(
                        "The target .mcfunction file already "
                        "exists as non-generated file; "
                        "Better to not overwrite this."
                    )

        if not self._path.parent.exists():
            self._path.parent.mkdir(parents=True)

        logger.info("Writing commands on %s..", self._path)
        with open(self._path, "w") as command_file:
            command_file.write(GENERATED_MCFUNCTION_PREFIX)
            command_file.write("\n")
            for command in self._commands:
                command_file.write(command)
                command_file.write("\n")

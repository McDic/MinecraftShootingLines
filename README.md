# Shooting Lines

This repository is made to backup some parts of my map "Shooting Lines", including

- Data pack
- Resource pack
- Some automation scripts to generate mcfunction files
- Other resources

## Running server

When you run the server with [MinecraftLinux](https://github.com/McDic/MinecraftLinux),
I recommend you to run following script to run the server.

```bash
./run.sh --dir (THIS_DIRECTORY) -v 1.20 --Xmx 4G --nohup
```

## Auto-generating commands

Some files are excluded from git because they have large number of lines.
To generate those files yourself, run `python_scripts/run_all.sh`.

## Directory structure

```
- shooting_lines (World folder)
    - datapacks
        - shooting_lines (Data pack folder)
- python_scripts (Python scripts used in map making to do some automation stuffs)
```

## Block Layers

Note that all layers can have `minecraft:air` blocks
and it is not listed in `Possible Blocks` section.

| Y value | Purposes | Possible Blocks |
| :---: | :---: | :---: |
| 20, 40, 60, ... | Standing floor | Barrier |
| 1 | Visible board | White, Black concretes |
| 0 | Determine inside/outside | White, Black, Gray concretes |
| -1 | Directional dependencies | Brown glazed terracotta |
| -2 | Copied states (Temporary calculation) | Sandstones |
| -3 | Recursive search flags | Bedrock |

## Data Storages

All data storages are saved under `sl` namespace.

- `sl:temp_args`: List of temporary args.
    When the function wants to create temporary arguments,
    then it prepends some value to the list,
    then delete the first element when the usage is finished.

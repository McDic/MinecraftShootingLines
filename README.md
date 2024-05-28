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

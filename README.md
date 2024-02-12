# Download and install QuPath versions for Linux

This is a simple python script to download QuPath releases for Linux to the
current directory. It also adds execute permissions to the main file,
and adds QuPath to your applications menu, launcher, etc, with the correct icon.

## Usage

Download the python script, make it executable
(`chmod +x download-qupath-version.py`) and run it. You can specify a version
or simply default to the latest release:

```bash
./download-qupath-version.py -v latest
```

or display help, in case I've added arguments that haven't been documented yet:

```bash
./download-qupath-version.py --help
```

You may also want to add QuPath to your `$PATH`, for example by running
in the current directory (for `latest`):

```bash
ln -s $(pwd)/latest/bin/QuPath /usr/local/bin/QuPath
```

or for an arbitrary version:

```bash
ln -s $(pwd)/v0.4.3/bin/QuPath /usr/local/bin/QuPath
```


## Details

Uses a few python modules:

- requests
- argparse
- sys
- wget
- os

Installation is handled by creating a `.desktop` file in `~/.local/share/applications`,
linking to the current directory.

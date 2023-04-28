#!/usr/bin/env python3

import requests
import argparse
import sys
import wget
import os

parser = argparse.ArgumentParser(
    prog='DownloadQuPath',
    description='Download a specified version of QuPath'
)
parser.add_argument('-v', '--version', default = "latest")
args = parser.parse_args()
version = args.version

print(f"Downloading QuPath, version: {version}")

url = 'https://api.github.com/repos/qupath/qupath/releases'
headers = {"X-GitHub-Api-Version": "2022-11-28", "Accept": "application/vnd.github+json"}
res = requests.get(url, headers=headers)

releases = res.json()
versions = [release["tag_name"] for release in releases]

if version == "latest":
    version = versions[0]
else:
    if not versions.contains(version):
        print("Version not found")
        sys.exit()

release = [release for release in releases if release["tag_name"] == version][0]
linux_asset = [asset for asset in release["assets"] if "Linux" in asset["name"]]
download_url = linux_asset[0]["browser_download_url"]

tarfile = f"qupath-{version}.tar.xz"
wget.download(download_url, tarfile)
os.system(f"tar -xJf {tarfile}")

os.rename("QuPath", version)

os.remove(tarfile)

print(f"Finished downloading QuPath, version: {version}")

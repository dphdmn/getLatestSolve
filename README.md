
# Slidysim Latest Solve Script

This is a Python script to fetch the latest solve from the Slidysim database ([slidysim.com](https://slidysim.com)).

It outputs solve information and a link for replay, generated using ([betterLeaderboard](https://github.com/dphdmn/betterLeaderboard)).

## Usage

1. Create a batch file with the following content in one of your PATH folders:

```
@echo off
cd path\to\slidysim\
python getLatest.py
pause
```

Replace `path\to\slidysim\` with the path to your Slidysim directory.

2. Save the batch file with a name like "latest.bat".

3. Put the `getLatest.py` script in your Slidysim directory.

4. Whenever you want to fetch the latest solve, press Win+R, then type "latest" (or the name you chose for your batch file), and press Enter. You will get the latest solve information and a link for replay.

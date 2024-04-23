
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

### Example output

```6x3 sliding puzzle solved in 1.808s with 52 moves 28.761 tps
1 15 16 6 5 0/7 14 17 8 3 11/13 10 9 2 4 12
R2U2RDLUR2DLDLURDRUL3UR2D2LU2RD2LU2L2D2RULUR2D2LULU
0, 0, 30, 60, 84, 136, 188, 278, 316, 346, 376, 390, 420, 458, 510, 570, 600, 624, 668, 706, 780, 840, 938, 1028, 1036, 1066, 1096, 1118, 1148, 1178, 1216, 1254, 1277, 1298, 1350, 1380, 1426, 1456, 1470, 1500, 1530, 1560, 1584, 1606, 1636, 1681, 1688, 1710, 1726, 1764, 1770, 1808
Today's date: 2024-04-24
https://dphdmn.github.io/betterLeaderboard/?r=eNotjzGuxCAMRK9ipY60jAGb9CmpIqVa7f2v8WesL8EDj83YfI%2FHX3%2Fu%2FT5%2Bbx338%2B6uyLcS4mZA9V%2Fc73GarwycdsAwDWFh09onDcOQtqwb8AHZ7DI3qs5X33YaV%2BcO7jVOQw9iLVom0cGwDyGFi2XDhcnsBG8z67ngNIhgIhuLc5UncXVqaF6sBi2KlwhIxyiqKVxd4VPzeKZ4Se%2BzifLFcNWMWdQImK3Yi1GsH4WGQVTfWCjKLTU9snwyVJnls9r6%2Ff4AkcZMlA%3D%3D
```

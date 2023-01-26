import wget
import math


def bar_custom(current, total, width=80):
    width = 30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" \
        % (current / total * 100, percent_bar, current, total)
    return progress


def download(url, out_path="."):
    wget.download(url, out=out_path, bar=bar_custom)

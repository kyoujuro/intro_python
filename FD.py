
import glob

filepath = ' '
splitsize = 100
fname, ext = filepath.rsplit('.', 1)
i = 0
written = False
with open(filepath) as files:
    while True:
        outfilepath = "{}{}.{}".format(fname, i, ext)
        with open(outfilepath, 'w') as outfile:
            for line in (files.readline() for _ in range(splitsize)):
                outfile.write(line)
            written = bool(line)
        if not written:
            break
        i += 1


resultpath = ''
readfile = glob.glob("*.csv")
with open(resultpath, "wb") as outfile:
    for i in readfile:
        with open(i, "rb") as infile:
            outfile.write(infile.read())


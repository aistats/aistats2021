import os
import sys
folderpath = os.path.abspath(".")
print(folderpath)
for subdir, dir, files in os.walk(folderpath):
    print(subdir)
    for file in files:
        print(file)
        if file.endswith(".pdf"):
            filepath = os.path.join(subdir, file)
            infile = filepath
            outfile = filepath.replace(".pdf", ".png")
            #os.system("inkscape -l {} {}".format(outfile, infile))
            os.system("convert -density 150 {} -quality 90 {}".format(infile, outfile))
        if file.endswith(".ai"):
            filepath = os.path.join(subdir, file)
            infile = filepath
            outfile = filepath.replace(".ai", ".png")
            #os.system("inkscape -l {} {}".format(outfile, infile))
            os.system("convert -density 150 {} -quality 90 {}".format(infile, outfile))
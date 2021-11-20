"""
Split an image into small square pieces of side `SIZE`
and save them to disk individually.
"""

from PIL import Image
import os
import glob

# -------------------------------------------
# Edit these parameters as required
INFILES = glob.glob('test/4J7A0149.JPG')
CREATE_DIRS = True
SIZE = 128
OFFSETS = [(0, 0) for f in INFILES]
# -------------------------------------------

if __name__ == '__main__' :

    if not INFILES :
        print("Warning : No files were processed")

    for addr, off in zip(INFILES, OFFSETS):
        fname, ext = os.path.splitext(addr)
        loc, fname = os.path.split(fname)
        if CREATE_DIRS :
            prf = os.path.join(loc,fname)
            if not os.path.isdir(prf) :
                os.mkdir(prf)
            OUT_PREFIX = f"./{prf}/"
        else :
            OUT_PREFIX = f"./{fname}_"

        src = Image.open(addr)
        
        for ix, x in enumerate(range(off[0], src.width-SIZE+1, SIZE)):
            for iy, y in enumerate(range(off[1], src.height-SIZE+1, SIZE)):
                section = src.crop((x, y, x+SIZE, y+SIZE))
                section.save(OUT_PREFIX + f"{ix}_{iy}" + ext)

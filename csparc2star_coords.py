import argparse
import numpy as np
from pyem import metadata, star
import os
import sys

def main(args):
    try:
        inputFile = args.input
        cs = np.load(inputFile)
    except:
        print("Error in read input file")
        sys.exit(1)
    
    outputFolder = args.output
    if outputFolder[-1] == "/":
        outputFolder = outputFolder.split("/")[0]
    os.makedirs(args.output)
    
    # coordinate X and Y should be exchanged from cryosparc to relion
    df = metadata.parse_cryosparc_2_cs(cs, swapxy=True)
    # extract unique micrograph name
    micrographName = set(df['rlnMicrographName'])
    # column labels of relion 3.0 manualpick star file
    starColumns = ['rlnCoordinateX', 'rlnCoordinateY', 'rlnClassNumber', 'rlnAnglePsi', 'rlnAutopickFigureOfMerit']

    for i in micrographName:
        # extract micrograph name from the path and remove the ".mrc" of it
        starName = i.split('/')[-1].split('.')[0]
        # extract coordinate from the data frame
        starContent = df.loc[df['rlnMicrographName'] == i].loc[:, ['rlnCoordinateX', 'rlnCoordinateY']]
        # fill the other 3 columns with "-999"
        starContent = starContent.reindex(columns=starColumns).fillna(-999)
        # write star file with suffix of "_manualpick.star"
        star.write_star_table(outputFolder+"/"+starName+"_manualpick.star", starContent)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="particles .cs file exported from cryosparc")
    parser.add_argument("-o", "--output", default="Movies", help="output folder of relion manual pick star file")
    args = parser.parse_args()
    main(args)
    print("all star files are exported to", args.output)
    
    

    

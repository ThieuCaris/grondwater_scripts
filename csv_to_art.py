# script to rename the .csv files to .art files while keeping the name the same.

import sys
import os
from pathlib import Path


source_path = 'G:\\projecten\\WBN\python_scripts\\cm_naar_meter\\gecorrigeerde_csv_bestanden'
target_path = 'G:\\projecten\\WBN\python_scripts\\cm_naar_meter\\gecorrigeerde_art_bestanden'

for root, dirs, files in os.walk(source_path):
    
    # loop over the .csv files in the files collection
    for ori_csv_file in files:

        ori_path = os.path.join(root, ori_csv_file)

        p = Path(ori_path)

        # name without extension
        ori_file_name = p.stem

        # str.format(".art") 
        new_file_name = ori_file_name + ".art"
        
        complete_target_path = str(target_path + "\\" + new_file_name)
                
        os.rename(ori_path, complete_target_path)

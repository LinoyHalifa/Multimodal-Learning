# print("hi")
# exit(0)

# to avoid packeges warnings

import warnings
warnings.filterwarnings("ignore")


import sys
import os
from datetime import datetime, timedelta
import time

start_time = datetime.now()
print(f"\nBen11 *****Run started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

names = ['AVT' ,'VT']
#names = ['VT']
#Single model is not allowed  ['A', 'V','T']  # 'A' for audio, 'V' for video, 'T' for text

#names = ['AVT']

#topn = [1 , 2]
topn = [2]
#topn = [ 1]
epocs = 100


        
for i in range(1, 2):
    temp_time = datetime.now()
    print(f"\nBen12*****Full loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")

    runj=0
    #print(f"Ben13=== run  {i}  ===")

    for name in names:
        #print(f"Fusion type: {name}")
        temp_time = datetime.now()
        #print(f"\n*****name loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")


        for top in topn:
            temp_time = datetime.now()
            #rint(f"\nBen13*****topn loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
            runj=runj+1
            print(f"Ben10 loop {i} run  {runj} Fusion type: {name} topn: {top} started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")
            #print(f"Ben15 === run  {runj}  in loop {i}===")
            cmd = (
                f"python -u main-release_Ben_Multi_Final.py "
                f"--model attention_topn "
                f"--feat_type utt "
                f"--dataset MER2025 "
                f"--fusion_topn {top} "
                f"--fusion_modality {name} "
                f"--gpu 0 "
                f"--epochs {epocs}"
            )
            print("Ben16",cmd)
            startrun= datetime.now()
            os.system(cmd)
            endrun= datetime.now()
            duration = endrun - startrun
            print(f"\nBen 17*****Run {runj} started at {startrun} and took {duration}")
            print(f"Ben 18Run {runj} started at {startrun} run {epocs} epocs and took {duration}")



end_time =  datetime.now()
duration = end_time - start_time
print(f"Script started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Script ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

print(f"Run duration is: {str(duration)}")

print(f"Total loops run: {i}")
print("Finish")
sys.exit(0)

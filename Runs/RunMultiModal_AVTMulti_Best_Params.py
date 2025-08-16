# to avoid packeges warnings

import warnings
warnings.filterwarnings("ignore")

import sys
import os
from datetime import datetime, timedelta
import time

#pyScript= "main-release_Ben_Multi_Final_Control.py"
pyScript= "main-release_Ben_Multi_Final_Control.py"
#names = ['AVT' ,'AV','AT','VT']
#topn = [1 , 2]
epocssss= 10
#epocs = [20]
Lrate = [0.0001]
Dropout = [0.5]
Hidden_Dim = [256]

runj=0

for HD in Hidden_Dim:
    startrun = datetime.now()
    print(f"\nBen20 *****Run started at {startrun.strftime('%Y-%m-%d %H:%M:%S')}")
    runj=runj+1

    print(f"Ben51 run {runj} _epochs 20 _hidden_dim= {HD} _dropout 0.5 _lr 0.0001")
    cmd = (
       f"python -u {pyScript} "
       f"--model attention_topn "
       f"--feat_type utt "
       f"--dataset MER2025 "
       f"--fusion_topn 2 "
       f"--fusion_modality AVT "
       f"--gpu 0 "
       f"--epochs 20 "
       f"--hidden_dim {HD} "
       f"--dropout 0.5 "
       f"--lr 0.0001 "
           )
    print("Ben51",cmd)
    #time.sleep(3)
    os.system(cmd)
    endrun= datetime.now()
    duration = endrun - startrun
    print(f"Ben51 Run {runj} started at {startrun} run {HD} hidden_dim and run duration {duration}")









        
# for i in range(1, 2):
#     temp_time = datetime.now()
#     print(f"\nBen12*****Full loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")

#     runj=0
#     #print(f"Ben13=== run  {i}  ===")

#     for name in names:
#         #print(f"Fusion type: {name}")
#         temp_time = datetime.now()
#         #print(f"\n*****name loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")


#         for top in topn:
#             temp_time = datetime.now()
#             #rint(f"\nBen13*****topn loop started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
#             runj=runj+1
#             print(f"Ben10 loop {i} run  {runj} Fusion type: {name} topn: {top} started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}")
#             #print(f"Ben15 === run  {runj}  in loop {i}===")
#             cmd = (
#                 f"python -u main-release_Ben_Multi_Final_Control.py "
#                 f"--model attention_topn "
#                 f"--feat_type utt "
#                 f"--dataset MER2025 "
#                 f"--fusion_topn {top} "
#                 f"--fusion_modality {name} "
#                 f"--gpu 0 "
#                 f"--epochs {epocs} "
#                 f"--hidden_dim 64 "
#                 f"--dropout 0.2 "
#                 f"--lr 0.001 "
#             )

#             startrun= datetime.now()
#             os.system(cmd)
#             endrun= datetime.now()
#             duration = endrun - startrun
#            # print(f"\nBen 17*****Run {runj} started at {startrun} and took {duration}")
#            # print(f"Ben21 Run {runj} started at {startrun} run {epocs} epocs and took {duration}")
#             print("Ben16",cmd)
#             print(f"Ben20 loop {i} run  {runj} Fusion type: {name} topn: {top} started at {temp_time.strftime('%Y-%m-%d %H:%M:%S')}run {epocs} epocs and took {duration}")

# end_time =  datetime.now()
# duration = end_time - start_time
# print(f"Script started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
# print(f"Script ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

# print(f"Run duration is: {str(duration)}")

# print(f"Total loops run: {i}")
# print("Finish")
# sys.exit(0)

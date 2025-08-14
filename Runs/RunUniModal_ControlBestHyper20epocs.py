# F:\Bentzi__add_on\run\run-Unimodal_Cont_paramtxt.txt
#                                 RunUniModal_Control.py
#python -u "F:\Bentzi__add_on\run\RunUniModal_Control.py" *>&1 | Tee-Object -FilePath "F:\Bentzi__add_on\Logs\RunUniModal_Control.py_Log.txt"
#                                                                                      F:\Bentzi__add_on\Logs\RunUniModal_Control.py_Log.txt




# import subprocess
import os
import sys
from datetime import datetime
import argparse
import time


pyScript= "main-release_Ben_uni_Final_Control.py"

epocs= 20
Lr=0.001
Dropout=0.2
HD=64
#epocs = [20]
# Lrate = [0.0001]
# Dropout = [0.5]
# Hidden_Dim = [ 128, 256]

Script_start_time = datetime.now()
# #script params
# parser = argparse.ArgumentParser()
# parser.add_argument('--epochs', type=int, default=None, metavar='E', help='number of epochs')
# parser.add_argument('--uni_feature', type=str, default=None, help='audio feature name')
# args = parser.parse_args()
# #args = parser.parse_args()

# epocs = args.epochs
#Uni_feature = args.uni_feature 


# print (f"epocs are:{epocs}")
#print (f"uni feature is:{Uni_feature}")

Audio_Model1="chinese-hubert-base-UTT"
Audio_Model2="chinese-hubert-large-UTT"


Text_Model1="chinese-roberta-wwm-ext-UTT"
Text_Model2="chinese-roberta-wwm-ext-large-UTT"



Video_Model1="clip-vit-large-patch14-UTT"
Video_Model2="clip-vit-base-patch32-UTT"


ModelsArry = [Audio_Model1, Audio_Model2, Text_Model1, Text_Model2, Video_Model1, Video_Model2]
# print (f"**** run Uni Array :",  ModelsArry)
# for each_model in ModelsArry: print(f"Uni feature is: {each_model}")
# # run uni model



#ModelsArry = [Audio_Model1, Audio_Model2, Text_Model1, Text_Model2]
#ModelsArry = [Video_Model1, Video_Model2]
print (f"* run Uni Array :",  ModelsArry)
runj=0
for each_model in ModelsArry:
    runj=runj+1
    print(f"Ben91 Run {runj} Uni feature is: {each_model}")
    Model_start_time = datetime.now()
    #Model_start_time = datetime.now()
    #print (f"*****   ===")
    print(f"Ben51 Run {runj} Uni feature is: {each_model} started at: {Model_start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    cmd = (
               f"python -u {pyScript} "

                f"--model attention "
                f"--feat_type utt "
                f"--dataset MER2025 "
                f"--audio_feature {each_model} "
                f"--text_feature {each_model}  "
                f"--video_feature {each_model}  "
                f"--epochs {epocs} "
                f"--gpu 0 "
                f"--hidden_dim {HD} "
                f"--dropout {Dropout} "
                f"--lr {Lr} "
                #f"--debug  "
            )
    print("Ben71",cmd)
    time.sleep(2)

       #f"--debug  "
    os.system(cmd)
    endrun= datetime.now()
    duration = endrun - Model_start_time

    print(f"Ben51 Run {runj} epocs: {epocs} duration : {duration}   started at {Model_start_time}")

    # Model_end_time =  datetime.now()
    # duration = Model_end_time - Model_start_time
    # print(f"\n***Model started at: {Model_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    # print(f"\n***Model ended at: {Model_end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    # print(f"\n***Model run duration is: {str(duration)}")

#os.system(cmd)
Script_end_time =  datetime.now()
duration = Script_end_time - Script_start_time
print(f"\n****Script started at: {Script_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n****Script ended at: {Script_end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n*****Script run duration is: {str(duration)}")


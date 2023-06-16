#import required packages
from glob import glob
# modules for copying files
import os
import shutil

print("Hi")

# #####MEW#######
# #get all MEW 2017 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MEW/2017/'
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/MEW/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2017 MEW are copied successfully")

# #get all MEW 2018 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MEW/2018/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2018 MEW are copied successfully")

# #get all MEW 2019 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MEW/2019/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2019 MEW are copied successfully")

# #get all MEW 2022 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MEW/2022/101_WSCT_MEW_DS/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2022 MEW are copied successfully")

# ####new photos###
# #get all of the more recent MEW photos
# mew_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/MEW/Trail Cam/4_20_2023/101_WSCT_MEW_LowerCam/*')

# #copy 2023 photos
# for i in mew_recent:
#    shutil.copy(i, target)
# print("MEW 2023 files are copied successfully")

# #copy photos from the UPPER camera
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/MEW_upper/'
# #get all of the more recent MEW photos
# mew_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/MEW/Trail Cam/6_2_2022/TRANSMIT/*')

# #copy 2022 photos
# for i in mew_22:
#    shutil.copy(i, target)
# print("2022 MEW upper cam files are copied successfully")

# #get all of the more recent MEW photos
# mew_23 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/MEW/Trail Cam/4_20_2023/Spypoint_MEW_UpperCam/DCIM/TRANSMIT/*')

# #copy 2022 photos
# for i in mew_23:
#    shutil.copy(i, target)
# print("2023 MEW upper cam files are copied successfully")

# #####CLD#######
# #get all CLD 2017 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/CLD/2017/'
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/CLD/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2017 CLD are copied successfully")

# #provide folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/CLD/2018/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2018 CLD are copied successfully")

# ####new photos###
# #get all of the more recent CLD photos
# cld_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/CLD/Trail Cam/6_1_2022/*/*')

# #copy 2022 photos
# for i in cld_22:
#    shutil.copy(i, target)
# print("2022 CLD files are copied successfully")

# #get all of the more recent CLD photos
# cld_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/CLD/Trail Cam/4_20_2023/DCIM/*/*')

# #copy 2023 photos
# for i in cld_recent:
#    shutil.copy(i, target)
# print("CLD 2023 files are copied successfully")

# #####WHT#######
# #get all WHT 2017 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/WHT/2017/'
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/WHT/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2017 WHT are copied successfully")

# ####new photos###
# #get all of the more recent WHT photos
# wht_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/WHT/Trail Cam/6_1_2022/*/*')

# #copy 2022 photos
# for i in wht_22:
#    shutil.copy(i, target)
# print("2022 WHT files are copied successfully")

# #get all of the more recent WHT photos
# wht_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/WHT/Trail Cam/4_19_2023/DCIM/*/*')

# #copy 2023 photos
# for i in wht_recent:
#    shutil.copy(i, target)
# print("WHT 2023 files are copied successfully")

# #####BYS#######
# #get all BYS 2017 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/BYS/2017/'
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/BYS/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2017 BYS are copied successfully")

# #get all BYS 2018 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/BYS/2018/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2018 BYS are copied successfully")

# #get all BYS 2019 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/BYS/2019/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2019 BYS are copied successfully")

# #get all BYS 2022 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/BYS/2022/101_WSCT/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2022 first half BYS are copied successfully")

# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/BYS/2022/102_WSCT/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("2022 second half BYS are copied successfully")


# ####new photos###
# #get all of the more recent BYS photos
# bys_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/BYS/Trail Cam/10_22_downloads/*/*')

# #copy 2022 photos
# for i in bys_22:
#    shutil.copy(i, target)
# print("2022 BYS files are copied successfully")

# #get all of the more recent BYS photos
# bys_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/BYS/Trail Cam/4_18_23/DCIM/*/*')

# #copy 2023 photos
# for i in bys_recent:
#    shutil.copy(i, target)
# print("BYS 2023 files are copied successfully")

#####MLL#######
#get all MLL 2017 photos
#Providing the folder path
origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MLL/2017/'
target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/MLL/'

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
   shutil.copy(origin+file_name, target+file_name)
print("2017 MLL are copied successfully")

#get all MLL 2018 photos
#Providing the folder path
origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MLL/2018/'

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
   shutil.copy(origin+file_name, target+file_name)
print("2018 MLL are copied successfully")

#get all MLL 2019 photos
#Providing the folder path
origin = '/data/CW3E_data/CW3E_Timelapse_Archive/MLL/2019/'

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
   shutil.copy(origin+file_name, target+file_name)
print("2019 MLL are copied successfully")

####new photos###
#get all of the more recent MLL photos
mll_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/MLL/Trail Cam/6_1_2022/*/*')

#copy 2022 photos
for i in mll_22:
   shutil.copy(i, target)
print("2022 MLL files are copied successfully")

#get all of the more recent MLL photos
mll_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/MLL/Trail Cam/4_18_2023/*/*')

#copy 2023 photos
for i in mll_recent:
   shutil.copy(i, target)
print("MLL 2023 files are copied successfully")



#####PRY#######
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/PRY/2017/'
# target = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/PRY/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("Files are copied successfully")

# #get all PRY 2018 photos
# #Providing the folder path
# origin = '/data/CW3E_data/CW3E_Timelapse_Archive/PRY/2018/'

# # Fetching the list of all the files
# files = os.listdir(origin)

# # Fetching all the files to directory
# for file_name in files:
#    shutil.copy(origin+file_name, target+file_name)
# print("Files are copied successfully")


# #get all of the more recent PRY photos
# pry_22 = glob('/data/CW3E_data/CW3E_Streamflow_Archive/PRY/Trail Cam/6_1_2022/*/*')
# print(pry_22)

# #copy 2022 photos
# for i in pry_22:
#    shutil.copy(i, target)
# print("Files are copied successfully")

# #get all of the more recent PRY photos
# pry_recent =  glob('/data/CW3E_data/CW3E_Streamflow_Archive/PRY/Trail Cam/4_19_2023/DCIM/*/*')
# print(pry_recent)

# #copy 2023 photos
# for i in pry_recent:
#    shutil.copy(i, target)
# print("Files are copied successfully")
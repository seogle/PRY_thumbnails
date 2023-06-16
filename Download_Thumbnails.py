from glob import glob
from PIL import Image
#read in paths of cropped photos
PRY_paths = glob('/Volumes/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/PRY/*') #get all the path names of the cropped PRY photos

#create thumbnails and save them
save_path = '/Users/cloudy-guest/Documents/GitHub/PRY_thumbnails/Thumbnails/PRY/'
MAX_SIZE = (204.8,115.2)
for i in PRY_paths:
    str_split = i.split('/') #split path name so can get file name
    last_name = str_split[-1] #find file name
    img = Image.open(i)
    img.thumbnail(MAX_SIZE)
    img.save(save_path+last_name)
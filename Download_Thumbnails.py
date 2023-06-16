from glob import glob
from PIL import Image
#read in paths of cropped photos
PRY_paths = glob('/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/PRY_cropped/*') #get all the path names of the cropped PRY photos
print(PRY_paths)
#create thumbnails and save them
save_path = '/data/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/thumbnails/PRY/'

for i in PRY_paths:
    str_split = i.split('/') #split path name so can get file name
    last_name = str_split[-1] #find file name
    img = Image.open(i)
    img.thumbnail((100,120))
    img.save(save_path+last_name)
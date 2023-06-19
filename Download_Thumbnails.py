from glob import glob
from PIL import Image as Im
from exif import Image
import pandas as pd
#read in paths of cropped photos
PRY_paths = glob('/Volumes/CW3E_data/CW3E_Streamflow_Archive/All_RR_Field_Cam_Photos/PRY/*') #get all the path names of the cropped PRY photos

#create thumbnails and save them
save_path = '/Volumes/seogle/code/PRY_thumbnails/PRY_all/'
MAX_SIZE = (204.8,115.2)
data = {}
data['path']= []
data['date'] = []
for i in PRY_paths:
    str_split = i.split('/') #split path name so can get file name
    last_name = str_split[-1] #find file name
    img = Im.open(i)
    img.thumbnail(MAX_SIZE)
    img.save(save_path+last_name)
    img_bi = Image(i) #get binary of image file so can get date
    date = img_bi.get('datetime_original') #extract date
    data['path'].append(i)
    data['date'].append(date)
path_date_PRY = pd.DataFrame({'date':data['date'], 'path':data['path']})
path_date_PRY.to_csv('/Volumes/seogle/code/PRY_thumbnails/PRY_path_date.csv')

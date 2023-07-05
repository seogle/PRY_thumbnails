library(tidyverse)
library(plotly)
library(data.table)

#Plot with labels and NWM

#load manually labeled PRY photo data
water_data <- read.csv('/Users/cloudy-guest/Library/CloudStorage/GoogleDrive-seogle@ucsd.edu/Shared drives/Sarah_Ogle_PhD/russian_river/code/output_data_from_code/date_water_labeled.csv',header= TRUE)
water_data$date <- ymd_hms(water_data$date,tz = "America/Los_Angeles") #get timezone
water_data$datehour <- round_date(with_tz(water_data$date, tz = "GMT"), unit = "hour") #convert to GMT, hourly
names(water_data)[2] <- "water"

#load labels of photos by ML algorithm
water_data_ML <- read.csv('/Volumes/seogle/code/ML_photo_process/output_data_image_labels/all_PRY_photos_probs.csv')
water_data_ML$date <- ymd_hms(water_data_ML$date,tz = "America/Los_Angeles") #get time zone
water_data_ML$datehour <- round_date(with_tz(water_data_ML$date, tz = "GMT"), unit = "hour") #convert to GMT, hourly
names(water_data_ML)[3] <- "water" #name the label column "label"

#high prob label
#load labels of photos by ML algorithm
water_data_ML <- read.csv('/Volumes/seogle/code/ML_photo_process/output_data_image_labels/PRY_medium_prob_labels.csv')
water_data_ML$date <- ymd_hms(water_data_ML$date,tz = "America/Los_Angeles") #get time zone
water_data_ML$datehour <- round_date(with_tz(water_data_ML$date, tz = "GMT"), unit = "hour") #convert to GMT, hourly
names(water_data_ML)[3] <- "water" #name the label column "label"

nwm <- read.csv('/Users/cloudy-guest/Downloads/PRY_NWM_flow.csv') #load NWM data
nwm$time<- ymd_hms(nwm$time)
nwm$datehour <- round_date(with_tz(nwm$time,tz = "GMT"), unit = "hour")

#load PRY data
PRY <- read.csv('/Volumes/CW3E_data/CW3E_Streamflow_Archive/Data/All_Barocorrected_Level/PRY_Barocorrected_H.csv')
PRY$TIMESTAMP.UTC <- strptime(PRY$TIMESTAMP.UTC, format = "%Y-%m-%d %H:%M:%S", tz = "GMT") #format data
PRY$datehour <- round_date(PRY$TIMESTAMP.UTC, unit = "hour") #round to nearest hour for datehour column
#names(lodata)[1] <-"datehour"

#load all of PRY path and photo data and format dates so that we have an hourly date in GMT
PRY_photo_path <- read.csv('/Volumes/seogle/code/PRY_thumbnails/PRY_path_date.csv')
PRY_photo_path$date <- ymd_hms(PRY_photo_path$date,tz = "America/Los_Angeles") #get time zone
PRY_photo_path$datehour <- round_date(with_tz(PRY_photo_path$date, tz = "GMT"), unit = "hour") #convert to GMT, hourly


#create a dataset that merges the PRY level data and the labels
im_water_data <- merge(PRY, water_data_ML,by="datehour") #merge labeled photos with barocorrected level data for PRY
#merge all photo paths with PRY dataset so that every time that has a corresponding photo is matched
PRY_plus_photos <- merge(PRY, PRY_photo_path, by = "datehour")
#create a dataset that merges the nwm and the labeled photos
im_water_nwm_data <- merge(im_water_data,nwm,by=("datehour")) #merge this with nwm data
#merge PRY level and NWM
nwm_all <- merge(PRY,nwm, by=("datehour")) #merge barocorrected level with NWM

#make data tables for values so that all can be plotted at once
PRY_level_photo_path <- data.table(timestamp = as.POSIXct(PRY_plus_photos$TIMESTAMP.UTC), timehour = as.POSIXct(PRY_plus_photos$datehour), location = PRY_plus_photos$path, unit = "cm", type = "photo", value = PRY_plus_photos$level.corrected.cm)
PRY_table <- data.table(timestamp = as.POSIXct(PRY$TIMESTAMP.UTC), timehour = as.POSIXct(PRY$datehour), location = "PRY", unit = "cm", type = "level", value = PRY$level.corrected.cm)
PRY_labeled_table <- data.table(timestamp = as.POSIXct(im_water_data$datehour), timehour = as.POSIXct(im_water_data$datehour), location = im_water_data$path, unit = im_water_data$water, type = "ML", value = im_water_data$level.corrected.cm)
PRY_all <- rbind(PRY_table,PRY_labeled_table, PRY_level_photo_path)

setwd("/Volumes/")

#also plot the level for all points 
PRY_labeled <- ggplot(data = PRY_all,aes(as.POSIXct(timestamp),value, text = timestamp,key = gsub("^.*\\/", "", location)))+
  geom_line(data = subset(PRY_all, type == "level"), color = "black")+
  geom_point(data = subset(PRY_all, type == "photo"), color = "black")+
  geom_point(data = subset(PRY_all, type == "ML" ),aes(as.POSIXct(timestamp),value, color = as.factor(unit)))+
  scale_color_manual(values = c("High Water" = "#32E0E6", "Low Water" = "#3F16C6", "No Water" = "#F9BF5B"))+
  xlab("Year") + ylab("Stream Level (cm)")+labs(title = "PRY Barocorrected Level Labeled by Machine Learning Algorithm Using Field Camera Photos", color = "Machine Learning Labels")+
  theme_light()
ggplotly(PRY_labeled)
pry_ggplot <- ggplotly(PRY_labeled, tooltip = "text") %>% partial_bundle() 
pry_ggplot

#'/Volumes/' + d.points[0].data.text;
pry_ggplot %>% htmlwidgets::onRender("
    function(el, x) {
      // when hovering over an element, do something
      el.on('plotly_hover', function(d) {
        
        // extract tooltip text
        console.log(d)
        p = d.points[0].pointIndex;
        path = d.points[0].data.key[p]
        console.log(p)
        console.log(path)
        // image is stored locally
        image_location = 'https://raw.githubusercontent.com/seogle/PRY_thumbnails/main/PRY_all/' + path
        console.log(image_location);
    
        // define image to be shown
        var img = {
          // location of image
          source: image_location, 
          // top-left corner
          x: 0.4,
          y: 1,
          sizex: 0.2,
          sizey: 0.2,
          xref: 'paper',
          yref: 'paper'
        };

        // show image and annotation 
        Plotly.relayout(el.id, {
            images: [img] 
        });
      })
    }
    ")


PRY_labeled <- ggplot(PRY_all,aes(as.POSIXct(datehour),level.corrected.cm, text = datehour, key = substring(path,77)))+
  geom_point(aes(color = as.factor(water)), )+
  xlab("Year") + ylab("Stream Level (cm)")+labs(title = "PRY Barocorrected Level Labeled by Machine Learning Algorithm Using Field Camera Photos")+
  theme_light()
ggplotly(PRY_labeled)
pry_ggplot <- ggplotly(PRY_labeled, tooltip = "text") %>% partial_bundle() 
pry_ggplot


PRY_nwm <- ggplot() + 
  geom_point(data = nwm_all,aes(datehour,level.corrected.cm),colour = "blue")+
  geom_point(data = nwm_all,aes(datehour,streamflow), colour = "cyan")
ggplotly(PRY_nwm)

ggplot(data = nwm_water_data,aes(datehour,streamflow,colour = as.numeric(water), label = "High water = 2, Low water = 1, No water = 0")) +
  geom_point(aes(size = level.corrected.cm, label = "Measured Stream Level"))+
  ggtitle("National Water Model Colored by Photo Labels")+
  xlab('Date') + ylab('Streamflow (cfs)')+
  theme_light()


ggplot(data = nwm_water_data,aes(datehour,level.corrected.cm,colour = as.numeric(water))) +
  geom_point(aes(size = streamflow))+
  theme(legend.title = element_text("Water?"))+
  xlab("Date") + ylab("Level (cm)")+
  theme_light()


#compare temperature
drw_temp <- na.omit(drw_temp)
temp_both <- merge(drw_temp, cold, by = "TIMESTAMP")
ggplot(temp_both,aes(TIMESTAMP,airtempavg-Temp..C.))+
  geom_point()

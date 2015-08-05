# NOAA_events_Automation
Files and directories used to automate the collection of NOAA event files and make a .txt file called FLARE_LIST that lists details of all of the flares.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    AFTER DOWNLOADING PERFORM THE FOLLOWING:
    
      1) in line 132 of the NOAA_events_collector.py file in the NOAA_events folder 
          replace *************** with your email address
      
      2) run the following programs in order:
            -"NOAA_events_collector.py" in the NOAA_events directory
            -"flare_list_creator.py" in the repository home directory
      
      
      

Only able to download the data from the past 30 days.          
Older data avaliable upon request



Description of files:

    -functions.py:
            contains all of the funcitons that are used in the other files
            
    -flare_list_creator.py:
            creates the list of flares called FLARE_LIST.txt
            
    -flare_list_updater.py:
            can be used to automate the process of updating FLARE_LIST.txt
            
    -NOAA_README.txt(in NOAA_events directory):
        contains information about the NOAA events files
        
    -NOAA_events_collector.py(in NOAA_events directory):
            can be used to automate the collection of NOAA events files
            
    -NOAA_organizer.py(in NOAA_events directory):
            can be used to organize 'YYYY'_events folders (good to run if older files are downloaded)

    




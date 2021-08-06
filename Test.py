import youtube_dl
import csv
import os
#import glob
#import pandas as pd

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}

def mp3_from_link(link,dir,count):
    try:
        os.mkdir(dir)
    except:
        pass
    ydl_opts['outtmpl']= f"{dir}/{count}.%(ext)s"

    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


with open("Raag_Taal_keyorscala.csv") as csv_file:
    #extension = 'csv'
    #allfile = [i for i in glob.glob('*.{}'.format(extension))]
    
    
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count != 0:
            mp3_from_link(row[1],row[0],line_count)
        line_count += 1
      
      #combine all files in the list
    #combined_csv = pd.concat([pd.read_csv(f) for f in allfile ])
#export to csv
    #combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')  


            
        
    
    
    
    

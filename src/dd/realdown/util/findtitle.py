#-*- coding:utf-8 -*-
import random
def findtitle_sync(infile):
    if infile.find("<title>") >= 0 or infile.find("<title>") >= 0:
        staflag = infile.index("<title>")
        endflag = infile.index("</title>")
        return infile[staflag+7:endflag]
    else:
        return "news_"+random.choice('abcdefghijklmnopqrstuvwxyzABCDEFJHIJKMLNOPQRSTUVWXYZ&#%^*f')
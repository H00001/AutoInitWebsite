#-*- coding:utf-8 -*-
from LikList import lknks
import time
def writeIndex(inmsgtitle,bp):
    print("inint indexing")
    wrindexhinstance = open(bp+'index.html', 'w+', encoding='utf-8')
    wrindexhinstance.write("<!DOCTYPE html>\n<html>\n<head><meta name='TTUNION_verify' content='ffc06baa246dc3d79e4fbb73f95cda44'><meta charset=\"UTF-8\"><title>"+inmsgtitle+"</title>"+'''
        <style>
        #headdiv
        {
            height:300px;
            border-radius: 10px;
	    padding:10px;
	    color:#008769;
            margin: auto;
            background: #f1f1f1;
        }
        #maindiv
        { 
            margin-top:50px;
            padding:10px;
            border-radius: 10px;
            margin: auto;
            background: #f1f1f1;
        }
        a
        {
            color: black;
            text-decoration: none;
            font-family: arial;

        }
	.nearblock
	{
	    width:100%;
	   
	}
</style>
                                                                              
     '''+"</head><body>")
    wrindexhinstance.write("<meta charset=\"UTF-8\">")
    wrindexhinstance.write("<div class=\"nearblock\" id=\"headdiv\">"+'''<img src="http://taobao.gunplan.top/newslogo.png">
'''+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+ '</div>'+"</div><div class=\"nearblock\" id=\"maindiv\">")
    for onetitle in lknks:
        wrindexhinstance.write("<h2><a href=\"fil_n\\" + onetitle[0] + ".html\">" + onetitle[1]+ "</a></h2><br/>")
        pass
    wrindexhinstance.write("</div><div class=\"nearblock\" id=\"footdiv\"></div>")
    print("inint index succeed")
    wrindexhinstance.close()

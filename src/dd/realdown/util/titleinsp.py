#-*- coding:utf-8 -*-
def titleinsp(titin):
    if titin is None:
        return titin
    else:
        return titin.replace(" ", "").replace("title:", "").replace('\'', '').replace(',', '').\
            replace('/', '和').replace("|", "-").replace(" ", "-").replace("\r\n", "").replace("\t", "").\
		replace('&#x3d','=')
		

def maintextinsp(tin):
    return tin.replace("&quot", "\"").replace("title:", "").replace("&lt", "<").replace("&gt", ">").\
                        replace(";", "").replace("content:'", "").replace("content: '", "").\
			replace('&#x3D','=')

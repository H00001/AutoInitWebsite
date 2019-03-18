# -*- coding: utf-8 -*-

import sys

from cleanmodel import deleteFile
from real_download import doDownTouTiao
from real_download import mkdir
from writeIndex import writeIndex

from src.DownControl import getArticleInfoFromTouTiao
from src.printstd import PRINT_STD

isSil = False


def downloadLists(art_info, base_path, group):
    for once_article in art_info:
        print(once_article)
        if once_article[0].startswith("http://toutiao.com/group"):
            doDownTouTiao(once_article,base_path)
        # thread = threading.Thread(target=doDown, args=(once_article, base_path))
        # thread.setDaemon(True)
        # thread.start()


if __name__ == '__main__':
    configfilename="default.ini"
    try:
        if sys.argv[1]=="-sil":
            PRINT_STD.isSil = True
        elif sys.argv[1]=="-c":
            configfilename=sys.argv[2]
        if sys.argv[3]=="-sil":
            PRINT_STD.isSil = True
    except:
        pass
    absPath = sys.path[0] + "/"   #find the path
    try:
        input_file = open(absPath+'conf.d/'+configfilename, 'r', encoding="utf-8")
    except:
        PRINT_STD.E('conf.d/'+configfilename+" is not exist\n")
        exit(-23235)
    for line in input_file:
        if line.startswith("base_path"):
            base_path = line.replace("base_path=", "").replace("\n", "")
        elif line.startswith("findword"):
            findword = line.replace("findword=", "").replace("\n", "")
        elif line.startswith("count"):
            count = line.replace("count=", "").replace("\n", "")
        elif line.startswith("#"):
            PRINT_STD.P(line)
        else:
            pass
    if not 'base_path' in locals().keys() or not 'findword' in locals().keys() or not 'count' in locals().keys():
        print("see the conf.d/defautl.ini file and check it")
        exit(-1)
    elif base_path is None or findword is None or count is None:
        print("see the conf.d/defautl.ini file and check it")
        exit(-2)
    if base_path.endswith('/'):
        pass
    else:
        base_path = base_path + "/"
    mkdir(base_path + "fil_n")
    deleteFile(base_path + "fil_n", isSil)
    itle = 0
    while itle < int(count):
        artile_info = getArticleInfoFromTouTiao(findword, itle)
        downloadLists(artile_info, base_path, itle / 20)
        itle += 20
    writeIndex(findword, base_path)
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#
# from imp import reload
import sys
# from setuptools.compat import execfile

from Renren import SuperRenren
import time, os

def main():
    # dl, dg = {}, {}
    # execfile('user.txt', dg, dl)
    # try:
    #     username = dl['username']
    #     password = dl['password']
    #     cookie = dl['cookie']
    # except:
    #     pass

    renren = SuperRenren()
#    test
#    renren.Create('18911029092', 'THUcst)(')
#    renren.DownloadAlbumInfo(['415604935'], path = 'y:/info', threadnum = 7)
#    print "?"
#    raw_input()
    
    f=open('user.txt')
    for username in f:
        print 'login using ' + username
        if renren.Create(username, 'THUcst)('):
            list = renren.GetFriendList()
            fi=open('y:/1.txt','a')
            for l in list:
                print l[0]
                fi.write((l[0] + " " + l[1] + '\n').encode("utf-8"))
                renren.DownloadAlbumInfo([l[0]], path = 'y:/info', threadnum = 7)
            fi.close()
        else:
            print 'login failed.'
        # renren.PostMsg(time.asctime())
        # renren.PostGroupMsg('387635422', '%s' % time.asctime())
        # renren.DownloadAlbum('333982368', 'sss') 
        # renren.DownloadAlbum('285201751', 'cai')
#        renren.DownloadAlbum('339106868', 'y:/') 
		# renren.DownloadAllFriendsAlbums(path = 'y:/albums',threadnumber=100)
    
if __name__ == '__main__':
    main()
    

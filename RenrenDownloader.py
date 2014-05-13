#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#
# from imp import reload
import sys
import codecs
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
        if username[0] == '#': continue
        print 'login using ' + username
        if renren.Create(username, 'THUcst)('):
            f2 = open('lc_filter.txt')
            for l in f2:
                renren.DownloadAlbum(l.strip(),'y:/albums',threadnum = 1)
            # list = renren.GetFriendList()
            # fi=open('y:/'+unicode(renren.requester.GetUserId())+'.txt','w')
            # for l in list:
            #     # print l[1].encode('gb18030')
            #     fi.write(l[0] + " ")
            #     fi.write(l[1])
            #     fi.write('\n')
            # fi.close()
            # renren.DownloadAlbumInfo([i[0] for i in list], path = 'y:/info', threadnum = 7)
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
    

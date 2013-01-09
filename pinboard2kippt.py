#!/usr/bin/env python
"""Pinboard2Kippt

Module to transfer your bookmarks from Pinboard to Kippt.

"""
import pinboard
import kippt.kippt as kippt

__version__ = "1.0"
__license__ = "BSD"
__copyright__ = "Copyright 2013, David Caplan"
__author__ = "David Caplan <http://www.davecap.com/>"


class Pinboard2Kippt():
    def __init__(self, pinboard_user, pinboard_pass,
                       kippt_user, kippt_api_token):
        self.pinboard = pinboard.connect(username=pinboard_user,
                                         password=pinboard_pass)
        self.kippt = kippt.user(kippt_user, kippt_api_token)
        if not self.kippt.checkAuth():
            raise Exception('Kippt credentials are invalid.')

    def transfer(self):
        print 'Getting Pinboard posts...'
        posts = self.pinboard.posts()
        print 'Transferring to Kippt...'
        for post in posts:
            print post['description']
            self.kippt.addClip(post['href'],
                               title=post['description'],
                               notes=', '.join(post['tags']))

if __name__ == '__main__':
    pass

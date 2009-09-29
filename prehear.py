#schedule.py
# vim: ts=4: sw=4:et:sts:ai
# See README

import rb, rhythmdb
import gtk, pygtk, gobject
from time import strftime, localtime

class Prehear (rb.Plugin):
    def __init__(self):
        rb.Plugin.__init__(self)

    def activate(self, shell):
        self.shell = shell
        self.db = shell.props.db
        self.player = self.shell.get_player()

    def deactivate(self, shell):
        del self.shell
        del self.player
        del self.db

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'valerio cosentino'

import Tkinter as tk
from helper.comment_helper import FacebookCommentHelper


class FacebookCommentHelperGui(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize_gui()
        self.title("FB Comment Helper")
        self._comment_helper = None

        self.mainloop()

    def initialize_gui(self):
        # SELECT TOKEN
        labelToken = tk.Label(self, text=u"Token", anchor="w")
        labelToken.grid(column=0, row=1, sticky='W')

        self.token = tk.StringVar()
        self.tokenValue = tk.Entry(self, textvariable=self.token, width=60)
        self.tokenValue.grid(column=1, row=1, sticky='W')

        # SELECT TARGET USER
        labelUser = tk.Label(self, text=u"Target User", anchor="w")
        labelUser.grid(column=0, row=2, sticky='W')

        self.user = tk.StringVar()
        self.userValue = tk.Entry(self, textvariable=self.user, width=60)
        self.userValue.grid(column=1, row=2, sticky='W')

        #empty label
        emptyLabel = tk.Label(self, anchor="w")
        emptyLabel.grid(column=0, row=3, sticky='WE')

        #BUTTON START
        self.buttonStart = tk.Button(self, text=u"Launch Browser", command=self.validator)
        self.buttonStart.grid(column=0, row=4, sticky="WE")

        #BUTTON NEXT
        self.buttonNext = tk.Button(self, text=u"Get Next Comment", command=self.process_next_comment)
        self.buttonNext.config(state=tk.DISABLED)
        self.buttonNext.grid(column=1, row=4, sticky="WE")

        self.resizable(True, False)

    def validator(self):
        flag = True

        if self.token.get() == "" or self.token.get() == "token cannot be null":
            self.token.set("token cannot be null")
            flag = False

        if self.user.get() == ""or self.user.get() == "target user cannot be null":
            self.user.set("target user cannot be null")
            flag = False

        if flag:
            self.buttonStart.config(state=tk.DISABLED)
            self.start_helper()

    def process_next_comment(self):
        self._comment_helper.process_next_comment()

    def start_helper(self):
        self._comment_helper = FacebookCommentHelper(self.token.get(), self.user.get())

        loop = True
        while loop:
            if not self._comment_helper.comments_queue_is_empty():
                self.buttonNext.config(state=tk.NORMAL)
                break

    def destroy(self):
        self.title("FB Comment Helper is closing..it may take some time!")
        self.buttonNext.config(state=tk.DISABLED)
        if self._comment_helper:
            self._comment_helper.stop_activity()
        self.quit()

if __name__ == '__main__':
    FacebookCommentHelperGui()


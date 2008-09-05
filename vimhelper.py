# vimhelper.py
# Companion to pysmell.vim
# Copyright (C) 2008 Orestis Markou
# All rights reserved
# E-mail: orestis@orestis.gr

# pysmell v0.2
# http://orestis.gr

# Released subject to the BSD License 

def findBase(vim):
    row, col = vim.current.window.cursor
    line = vim.current.buffer[row-1]
    index = col
    # col points at the end of the completed string
    # so col-1 is the last character of base
    while index > 0:
        index -= 1
        if line[index] in '. ':
            index += 1
            break
    return index #this is zero based :S
    
def findWord(vim, origCol, origLine):
    # vim moves the cursor and deletes the text by the time we are called
    # so we need the original position and the original line...
    index = origCol
    while index > 0:
        index -= 1
        if origLine[index] == ' ':
            index +=1
            break
    cword = origLine[index:origCol]
    return cword

    

#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

import random

class Book:
    def __init__(self,path=""):
        self.book={}
        if path!="": self.import_book(path)
        
    def import_book(self,path):
        with open(path) as fp:
            line=fp.readline()
            while line:
                line=line.strip()
                line=line.split(" ")
                move=line[-1]
                line=line[:-1]
                line=' '.join(line)
                book_move=self.book.get(line)
                if book_move: self.book[line].append(move)
                else: self.book[line]=[move]
                line=fp.readline()
        fp.close()
 
    def get_move(self,line):
        book_move=self.book.get(line)
        if book_move: return book_move[random.randint(0,len(book_move)-1)]
        return ()

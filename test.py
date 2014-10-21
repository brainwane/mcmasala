#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import spitouthtml
import codecs

def test_this_works():
    assert(True)

class TestUnicode():
    def setup_method(self, method):
        self.slug_name = 'hello.html'
        self.data = u"""Mazari, Abu ʿAbd Allah Muhammad al-
                    Mlapa III
                    Andrade, Mário Pinto de
                    Bayram al-Khaʾmis, Mohamed
                    Be’alu Girma
                    Bédié, Henri-Konan
                    Obama, Barack, Sr.
                    Okwei
                    Marie Curie
                    Cleopatra
                    Gandhi, Indira
                    Madikizela-Mandela, Winnie
                    """

    def test_unicode_writing_tests(self):
        spitouthtml.write_page(self.data,self.slug_name)
        # assert - read it, check that it is actually readable
        with codecs.open(self.slug_name, encoding='utf-8', mode='r') as f:
            assert(f.read() == self.data)


    def teardown_method(self, method):
        ''' remove file'''
        os.remove(self.slug_name)
        pass

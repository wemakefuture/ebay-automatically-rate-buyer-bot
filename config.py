#!/usr/bin/env python
# -*- coding: utf-8 -*-


#utf8 cause i am german
#download chromedriver and put it into the folder of the config.py (remove in ebay.py the .exe if running on MAC or linux)


from .ebay import ebay

username = 'yourusername'
password = 'yourpassword'


#changce them to whatever --> dis is german
ratings = ('WOW bester Käufer!!bis demnächst :)','Supersupersupersupersuper guter Käufer,bis demnächst :)','Immer wieder gerne <3!! bis demnächst :)')
#put your ratings here, one will be picked by random


eb = ebay()
eb.login(username, password)
eb.rate()
eb.reallyrate(ratings)
eb.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'APICV'
SITENAME = u'#ConPI14'
SITEURL = 'http://congreso.profesoresinformatica.es'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = u'es'

#GOOGLE_ANALYTICS = 'UA-XXXXXXXX-X'

# Use RSS
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = None
FEED_MAX_ITEMS = 30

SINGLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
RELATIVE_URLS = True
 
MENUITEMS = (('Congreso', 'congreso.html'),
             ('Programa', 'programa.html'),
             (u'Inscripción', 'inscripcion.html'),
             ('2013', 'http://profesoresinformatica.es/'),
             )

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Blogroll
LINKS =  (('APICV', 'http://apicv.es/'),
          ('GVA', 'http://www.gva.es/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/pnapi_es'),
          ('github', 'http://github.com/pnapi'),)

DEFAULT_PAGINATION = 10

THEME = "themes/bootstrap3"
BOOTSTRAP_THEME = "flatly"

# static paths will be copied under the same name
STATIC_PATHS = ["static", 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# plugin configuration
#PLUGIN_PATH = 'plugins'
#PLUGINS = ['html_rst_directive']

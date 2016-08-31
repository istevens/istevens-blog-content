#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Stevens'
SITENAME = u'Yes, This Is Ian Stevens'
THEME = 'theme'
CSS_FILE = 'style.css'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
]

PATH = 'content'

STATIC_PATHS = [
    'static/robots.txt',
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
}

TIMEZONE = 'EST5EDT'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

INDEX_SAVE_AS = 'blog_index.html'
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}', '{base_name}/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

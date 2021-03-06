#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

attribVersion_261757124092690704 = pycopia.XML.POM.XMLAttribute(u'version', 1, 11, None)




# 
# Rich Site Summary (RSS) 0.91 official DTD, proposed.
# RSS is an XML vocabulary for describing
# metadata about websites, and enabling the display of
# "channels" on the "My Netscape" website.
# RSS Info can be found at http://my.netscape.com/publish/
# XML Info can be found at http://www.w3.org/XML/ 
# copyright Netscape Communications, 1999
# Dan Libby - danda@netscape.com
# Based on RSS DTD originally created by
# Lars Marius Garshol - larsga@ifi.uio.no.
# $Id$
# 


class Rss(pycopia.XML.POM.ElementNode):
	ATTRIBUTES = {
         u'version': attribVersion_261757124092690704, 
         }
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	KWATTRIBUTES = {
         'version': attribVersion_261757124092690704, 
         }
	_name = u'rss'



_Root = Rss



#  must be "0.91"> 


class Channel(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'channel'


class Title(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'title'


class Description(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'description'


class Link(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'link'


class Image(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'image'


class Url(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'url'


class Item(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'item'


class Textinput(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'textinput'


class Name(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'name'


class Rating(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'rating'


class Language(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'language'


class Width(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'width'


class Height(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'height'


class Copyright(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'copyright'


class Pubdate(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'pubDate'


class Lastbuilddate(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'lastBuildDate'


class Docs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'docs'


class Managingeditor(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'managingEditor'


class Webmaster(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'webMaster'


class Hour(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'hour'


class Day(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'day'


class Skiphours(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'skipHours'


class Skipdays(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'skipDays'


# 
# Copied from HTML 3.2 DTD, with modifications (removed CDATA)
# http://www.w3.org/TR/REC-html32.html#dtd
# =============== BEGIN ===================
# 


#  
# Character Entities for ISO Latin-1
# (C) International Organization for Standardization 1986
# Permission to copy in any form is granted for use with
# conforming SGML systems and applications as defined in
# ISO 8879, provided this notice is included in all copies.
# This has been extended for use with HTML to cover the full
# set of codes in the range 160-255 decimal.
# 


#  Character entity set. Typical invocation:
# <!ENTITY % ISOlat1 PUBLIC
# "ISO 8879-1986//ENTITIES Added Latin 1//EN//HTML">
# %ISOlat1;
# 


#  no-break space 


#  inverted exclamation mark 


#  cent sign 


#  pound sterling sign 


#  general currency sign 


#  yen sign 


#  broken (vertical) bar 


#  section sign 


#  umlaut (dieresis) 


#  copyright sign 


#  ordinal indicator, feminine 


#  angle quotation mark, left 


#  not sign 


#  soft hyphen 


#  registered sign 


#  macron 


#  degree sign 


#  plus-or-minus sign 


#  superscript two 


#  superscript three 


#  acute accent 


#  micro sign 


#  pilcrow (paragraph sign) 


#  middle dot 


#  cedilla 


#  superscript one 


#  ordinal indicator, masculine 


#  angle quotation mark, right 


#  fraction one-quarter 


#  fraction one-half 


#  fraction three-quarters 


#  inverted question mark 


#  capital A, grave accent 


#  capital A, acute accent 


#  capital A, circumflex accent 


#  capital A, tilde 


#  capital A, dieresis or umlaut mark 


#  capital A, ring 


#  capital AE diphthong (ligature) 


#  capital C, cedilla 


#  capital E, grave accent 


#  capital E, acute accent 


#  capital E, circumflex accent 


#  capital E, dieresis or umlaut mark 


#  capital I, grave accent 


#  capital I, acute accent 


#  capital I, circumflex accent 


#  capital I, dieresis or umlaut mark 


#  capital Eth, Icelandic 


#  capital N, tilde 


#  capital O, grave accent 


#  capital O, acute accent 


#  capital O, circumflex accent 


#  capital O, tilde 


#  capital O, dieresis or umlaut mark 


#  multiply sign 


#  capital O, slash 


#  capital U, grave accent 


#  capital U, acute accent 


#  capital U, circumflex accent 


#  capital U, dieresis or umlaut mark 


#  capital Y, acute accent 


#  capital THORN, Icelandic 


#  small sharp s, German (sz ligature) 


#  small a, grave accent 


#  small a, acute accent 


#  small a, circumflex accent 


#  small a, tilde 


#  small a, dieresis or umlaut mark 


#  small a, ring 


#  small ae diphthong (ligature) 


#  small c, cedilla 


#  small e, grave accent 


#  small e, acute accent 


#  small e, circumflex accent 


#  small e, dieresis or umlaut mark 


#  small i, grave accent 


#  small i, acute accent 


#  small i, circumflex accent 


#  small i, dieresis or umlaut mark 


#  small eth, Icelandic 


#  small n, tilde 


#  small o, grave accent 


#  small o, acute accent 


#  small o, circumflex accent 


#  small o, tilde 


#  small o, dieresis or umlaut mark 


#  divide sign 


#  small o, slash 


#  small u, grave accent 


#  small u, acute accent 


#  small u, circumflex accent 


#  small u, dieresis or umlaut mark 


#  small y, acute accent 


#  small thorn, Icelandic 


#  small y, dieresis or umlaut mark 


# 
# Copied from HTML 3.2 DTD, with modifications (removed CDATA)
# http://www.w3.org/TR/REC-html32.html#dtd
# ================= END ===================
# 


GENERAL_ENTITIES = {   'AElig': u'\xc6',
    'Aacute': u'\xc1',
    'Acirc': u'\xc2',
    'Agrave': u'\xc0',
    'Aring': u'\xc5',
    'Atilde': u'\xc3',
    'Auml': u'\xc4',
    'Ccedil': u'\xc7',
    'ETH': u'\xd0',
    'Eacute': u'\xc9',
    'Ecirc': u'\xca',
    'Egrave': u'\xc8',
    'Euml': u'\xcb',
    'Iacute': u'\xcd',
    'Icirc': u'\xce',
    'Igrave': u'\xcc',
    'Iuml': u'\xcf',
    'Ntilde': u'\xd1',
    'Oacute': u'\xd3',
    'Ocirc': u'\xd4',
    'Ograve': u'\xd2',
    'Oslash': u'\xd8',
    'Otilde': u'\xd5',
    'Ouml': u'\xd6',
    'THORN': u'\xde',
    'Uacute': u'\xda',
    'Ucirc': u'\xdb',
    'Ugrave': u'\xd9',
    'Uuml': u'\xdc',
    'Yacute': u'\xdd',
    'aacute': u'\xe1',
    'acirc': u'\xe2',
    'acute': u'\xb4',
    'aelig': u'\xe6',
    'agrave': u'\xe0',
    'aring': u'\xe5',
    'atilde': u'\xe3',
    'auml': u'\xe4',
    'brvbar': u'\xa6',
    'ccedil': u'\xe7',
    'cedil': u'\xb8',
    'cent': u'\xa2',
    'copy': u'\xa9',
    'curren': u'\xa4',
    'deg': u'\xb0',
    'divide': u'\xf7',
    'eacute': u'\xe9',
    'ecirc': u'\xea',
    'egrave': u'\xe8',
    'eth': u'\xf0',
    'euml': u'\xeb',
    'frac12': u'\xbd',
    'frac14': u'\xbc',
    'frac34': u'\xbe',
    'iacute': u'\xed',
    'icirc': u'\xee',
    'iexcl': u'\xa1',
    'igrave': u'\xec',
    'iquest': u'\xbf',
    'iuml': u'\xef',
    'laquo': u'\xab',
    'macr': u'\xaf',
    'micro': u'\xb5',
    'middot': u'\xb7',
    'nbsp': u'\xa0',
    'not': u'\xac',
    'ntilde': u'\xf1',
    'oacute': u'\xf3',
    'ocirc': u'\xf4',
    'ograve': u'\xf2',
    'ordf': u'\xaa',
    'ordm': u'\xba',
    'oslash': u'\xf8',
    'otilde': u'\xf5',
    'ouml': u'\xf6',
    'para': u'\xb6',
    'plusmn': u'\xb1',
    'pound': u'\xa3',
    'raquo': u'\xbb',
    'reg': u'\xae',
    'sect': u'\xa7',
    'shy': u'\xad',
    'sup1': u'\xb9',
    'sup2': u'\xb2',
    'sup3': u'\xb3',
    'szlig': u'\xdf',
    'thorn': u'\xfe',
    'times': u'\xd7',
    'uacute': u'\xfa',
    'ucirc': u'\xfb',
    'ugrave': u'\xf9',
    'uml': u'\xa8',
    'uuml': u'\xfc',
    'yacute': u'\xfd',
    'yen': u'\xa5',
    'yuml': u'\xff'}

# Cache for dynamic classes for this dtd.


_CLASSCACHE = {}



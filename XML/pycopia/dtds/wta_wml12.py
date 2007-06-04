#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

# 
# Wireless Telephony Applications Wireless Markup Language (WTA-WML) Document Type Definition.
# WTA-WML is an XML language. Typical usage:
# <?xml version="1.0"?>
# <!DOCTYPE wta-wml PUBLIC "-//WAPFORUM//DTD WTA-WML 1.2//EN"
#     "http://www.wapforum.org/DTD/wta-wml12.dtd">
# <wta-wml>
# ...
# </wta-wml>
# 


# 
# Wireless Markup Language (WML) Document Type Definition.
# WML is an XML language. Typical usage:
#    <?xml version="1.0"?>
#    <!DOCTYPE wml PUBLIC "-//WAPFORUM//DTD WML 1.2//EN"
#    "http://www.wapforum.org/DTD/wml12.dtd">
#    <wml>
#    ...
#    </wml>
# 
#    Terms and conditions of use are available from the Wireless  Application Protocol Forum
#    Ltd. web site at http://www.wapforum.org/docs/copyright.htm.
# 
# 


#  [0-9]+ for pixels or [0-9]+"%" for
#                                         
# percentage length 


#  attribute value possibly containing
#                                          variable references 


#  URI, URL or URN designating a hypertext
#                                          node. May contain variable references 


#  a number, with format [0-9]+ 


#  media type. May contain variable
#                                          references 


#  flow covers "card-level" elements, such as text and images 


#  Task types 


#  Navigation and event elements 


# ================ Decks and Cards ================


class Wml(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'wml'


#  card intrinsic events 


#  card field types 


class Card(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('newcontext', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('ordered', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'true'), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('onenterforward', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('onenterbackward', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('ontimer', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'card'


# ================ Event Bindings ================


class Do(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('type', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('optional', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'do'


class Onevent(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('type', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'onevent'


# ================ Deck-level declarations ================


class Head(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'head'


class Template(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('onenterforward', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('onenterbackward', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('ontimer', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'template'


class Access(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('domain', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('path', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'access'


class Meta(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('http-equiv', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('forua', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('content', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('scheme', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'meta'


# ================ Tasks ================


class Go(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('href', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('sendreferer', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('method', pycopia.XML.POM.Enumeration(['post', 'get']), 13, u'get'), 
         pycopia.XML.POM.XMLAttribute('enctype', 1, 13, u'application/x-www-form-urlencoded'), 
         pycopia.XML.POM.XMLAttribute('accept-charset', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'go'


class Prev(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'prev'


class Refresh(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'refresh'


class Noop(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'noop'


# ================ postfield ================


class Postfield(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'postfield'


# ================ variables ================


class Setvar(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'setvar'


# ================ Card Fields ================


class Select(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('iname', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('ivalue', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('multiple', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('tabindex', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'select'


class Optgroup(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'optgroup'


class Option(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('onpick', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'option'


class Input(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('type', pycopia.XML.POM.Enumeration(['text', 'password']), 13, u'text'), 
         pycopia.XML.POM.XMLAttribute('value', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('format', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('emptyok', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         pycopia.XML.POM.XMLAttribute('size', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('maxlength', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('tabindex', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('accesskey', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'input'


class Fieldset(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'fieldset'


class Timer(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'timer'


# ================ Images ================


class Img(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('alt', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('src', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('localsrc', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('vspace', 1, 13, u'0'), 
         pycopia.XML.POM.XMLAttribute('hspace', 1, 13, u'0'), 
         pycopia.XML.POM.XMLAttribute('align', pycopia.XML.POM.Enumeration(['top', 'middle', 'bottom']), 13, u'bottom'), 
         pycopia.XML.POM.XMLAttribute('height', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('width', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'img'


# ================ Anchor ================


class Anchor(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('accesskey', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'anchor'


class A(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('href', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('accesskey', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'a'


# ================ Tables ================


class Table(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('title', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('align', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('columns', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'table'


class Tr(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'tr'


class Td(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'td'


# ================ Text layout and line breaks ================


class Em(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'em'


class Strong(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'strong'


class B(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'b'


class I(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'i'


class U(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'u'


class Big(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'big'


class Small(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'small'


class P(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('align', pycopia.XML.POM.Enumeration(['left', 'right', 'center']), 13, u'left'), 
         pycopia.XML.POM.XMLAttribute('mode', pycopia.XML.POM.Enumeration(['wrap', 'nowrap']), 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'p'


class Br(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'br'


class Pre(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:space', 1, 14, u'preserve'), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'pre'


#  quotation mark 


#  ampersand 


#  apostrophe 


#  less than 


#  greater than 


#  non-breaking space 


#  soft hyphen (discretionary hyphen) 


class Wta_wml(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('class', 1, 12, None), 
         ])
	_name = u'wta-wml'



Root = Wta_wml



GENERAL_ENTITIES = {u'gt': u'>', u'quot': u'"', u'shy': u'\xad', u'lt': u'&#60;', u'nbsp': u'\xa0', u'amp': u'&#38;', u'apos': u"'"}

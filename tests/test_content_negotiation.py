# -*- coding: utf-8 -*-

from urest.content_negotiation import MediaType, parse_media_range, parse_and_sort_media_range


def test_media_range_as_string():
    mediatype = MediaType(type="text", subtype="html", q=0.8,
                          params={"charset": "iso-8859-1"})

    assert str(mediatype) == "text/html;charset=iso-8859-1"


def test_parse_media_range():
    media_type, = parse_media_range("text/html;charset=iso-8859-1;q=0.8")

    assert media_type.type == "text"
    assert media_type.subtype == "html"
    assert media_type.q == 0.8
    assert media_type.params["charset"] == "iso-8859-1"


def test_parse_and_sort_media_range():
    media_types = parse_and_sort_media_range(
        "text/*, text/html, text/html;level=1, */*")

    assert str(media_types[0]) == "text/html;level=1"
    assert str(media_types[1]) == "text/html"
    assert str(media_types[2]) == "text/*"
    assert str(media_types[3]) == "*/*"

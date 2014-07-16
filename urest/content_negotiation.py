# -*- coding: utf-8 -*-


class MediaType:
    """Representation of a media type defined in a media range.

    For more information on media ranges see:
    http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

    :param type: String with the type.
    :param subtype: String with the subtype.
    :param params: Dict of attribute-value pairs.
    :param q: Value of the relative quality factor. Must be between 0 and 1.
    """
    def __init__(self, type="*", subtype="*", params=None, q=1):
        self.type = type.strip()
        self.subtype = subtype.strip()
        if params is None:
            params = {}
        self.params = params
        self.q = float(q)

    @property
    def params(self):
        return dict(self._params)

    @params.setter
    def params(self, params):
        self._params = sorted(tuple(params.items()))

    def __str__(self):
        text = "{0.type}/{0.subtype}".format(self)
        params = self.params
        if params:
            params = {"{}={}".format(key, value) for key, value in params.items()}
            text = "{};{}".format(text, ";".join(params))

        return text

    def __lt__(self, other):
        if self == other:
            return False

        if self.q != other.q:
            return self.q < other.q

        if self.type == "*":
            return other.type != "*"

        if self.subtype == "*":
            return other.subtype != "*"

        return len(self.params) < len(other.params)

    def __gt__(self, other):
        if self == other:
            return False
        return not self < other

    def __eq__(self, other):
        return (self.type == other.type and
                self.subtype == other.subtype and
                self.q == other.q and
                self.params == other.params)


def parse_media_range(string):
    """Parse a media range string.

    :param string: Media range string.

    :return: List of `MediaType` instances.
    """
    result = []
    for media_type in string.split(","):
        parts = media_type.split(";")
        type_subtype = parts[0].split("/")
        if len(type_subtype) == 1:
            type = subtype = type_subtype
        else:
            type, subtype = type_subtype

        params = dict(p.split("=") for p in parts[1:])
        q = params.pop("q", 1)

        result.append(MediaType(type, subtype, params, q))

    return result


def parse_and_sort_media_range(media_range):
    media_types = parse_media_range(media_range)
    return sorted(media_types, reverse=True)

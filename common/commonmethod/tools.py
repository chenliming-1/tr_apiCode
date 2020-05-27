import re


def indent(s, indent=4):
    """
    对字符串进行缩进，s为需要缩进的文本，indent缩进的字符，默认为4格
    """
    # This regexp matches the start of non-blank lines:
    return re.sub('(?m)^(?!$)', indent * ' ', s)


# print(indent(""))

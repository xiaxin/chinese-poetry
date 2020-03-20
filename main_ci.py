# -*- coding: utf-8 -*-
import six, os, io
from zhconv import convert_for_mw


if six.PY2:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

POETRY_DIRECTORY = './chinese-poetry/ci/'

def trans(name):

    file_path = os.path.join(POETRY_DIRECTORY, name)

    if os.path.isdir(file_path):
        print file_path + " is dir"
        return
    if name[-4:] != "json":
        return

    raw = io.open(file_path, 'r', encoding='utf-8').read()

    if six.PY2:
        content = convert_for_mw(unicode(raw), 'zh-cn')
    else:
        content = convert_for_mw(raw, 'zh-cn')

    output_path = os.path.join('./ci/', name)

    with open(output_path, 'w') as f:
        f.write(content)
    
    


list(map(trans, os.listdir(POETRY_DIRECTORY)))

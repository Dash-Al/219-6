#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Создать уникальное имя файла

import pathlib
def tree(directory):
   print(f'+ {directory}')
   for path in sorted(directory.rglob('*')):
       depth = len(path.relative_to(directory).parts)
       spacer = '   ' * depth
       print(f'{spacer}+ {path.name}')

# -*- encoding: utf-8 -*-
# @ModuleName: __init__.py
# @Author：龚远琪
# @Date：2019/11/4 11:31
from .addpapertype import addPaperType
from .editpapertype import editPaperType
from .getpapertype import getPaperType
from .getpapertypebyperiod import getPaperTypeByPeriod
from .getpapertypelist import getPaperTypeList

__all__ = ['addPaperType', 'editPaperType', 'getPaperType', 'getPaperTypeByPeriod', 'getPaperTypeList']

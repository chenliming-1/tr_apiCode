#!Date：2019/02/20 17:15
# !@Author：龚远琪

from .sign import sign
from .resource import resource
from .uploadfile import uploadfile
from .createrelation import createrelation, randbusinessId, urldata
from .deleterelation import deleterelation
from .videopage import videopage

__all__ = ['sign', 'resource', 'uploadfile', 'createrelation', 'randbusinessId', 'urldata', 'deleterelation', 'videopage']
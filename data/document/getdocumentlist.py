from common.commonmethod import *
from histudy import *
from module import *

getDocumentList={
    "url": f'{sysURL}tr/api/tr/v1/documents/page',
    "headers":{
            "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
        },
    "params": {
            "currentPage": "1",
            "pageSize": "20",
            "periodId": "10002",
            "subjectId": "8",
            "parentId": "0"
        },"method": "GET"
}














#!Date：2019/02/22 11:28
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *

insertexplanation = {
    "url": f'{sysURL}tr/api/item/explanation',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "wordbody": {
        "audios": [],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": randMethod.getNumByRange(0, 120),
        "itemAnswer": {
            "answer": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemContent": {
            "content": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p>AT_"+randMethod.getMessage(300)+"</p>",
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

    "latexbody": {
        "audios": [],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": randMethod.getNumByRange(0, 120),
        "itemAnswer": {
            "answer": "<p>AT_已知函数~$y = f\left( x \\right)$ 的图象与函数~$y = {a^x}\left( {a > 0\\text{且}a \\ne 1} \\right)$ 的图象关于直线~$y = x$ 对称，记~$g\left( x \\right) = f\left( x \\right)\left[ {f\left( x \\right) + f\left( 2 \\right) - 1} \\right]$．若~$y = g\left( x \\right)$ 在区间~$\left[ {\dfrac{1}{2},2} \\right]$ 上是增函数，则实数~$a$ 的取值范围是~($\qquad$)</p>",
            "pictures": []
        },
        "itemContent": {
            "content": "<p>AT_齐鲁之士$\\underset{\\bullet}从$之者数十百人 从：$\\underline{\hspace{2cm}}$</p><p><br></p>"
                       r"<p>$城\underset{\bullet}{阙}（\qquad）	\underset{\bullet}{宦}游人（\qquad）	\underset{\bullet}{歧}路（\qquad）准\underset{\bullet}{噶}尔（\qquad）	山居秋\underset{\bullet}{暝}（\qquad） 	开轩面场\underset{\bullet}{圃}（\qquad）$</p>",
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p>AT_当~$a > 0$，$b > 0$ 时，设任意~${x_1}$，${x_2} \in R$，${x_1} < {x_2}$，</p><p><br></p>"
                      "<p>则~$f\left( {{x_1}} \\right) - f\left( {{x_2}} \\right) = a\left( {{2^{{x_1}}} - {2^{{x_2}}}} \\right) + b\left( {{3^{{x_1}}} - {3^{{x_2}}}} \\right)$</p><p><br></p>"
                      "<p>$\\because {2^{{x_1}}} < {2^{{x_2}}}$，$a > 0$，$\\therefore a\left( {{2^{{x_1}}} - {2^{{x_2}}}} \\right) < 0$</p><p><br></p>"
                      "<p>$\\because {3^{{x_1}}} < {3^{{x_2}}}$，$b > 0$，$\\therefore b\left( {{3^{{x_1}}} - {3^{{x_2}}}} \\right) < 0$</p><p><br></p>"
                      "<p>$\\therefore f\left( {{x_1}} \\right) - f\left( {{x_2}} \\right) < 0$，函数~$f\left( x \\right)$ 在~$R$ 上是增函数．</p><p><br></p>"
                      "<p>同理可证，当~$a < 0$，$b < 0$时，$f\left( x \\right) $ 为减函数.</p>",
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

    "typebody": {
        "audios": [],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": randMethod.getNumByRange(0, 120),
        "itemAnswer": {
            "answer": "<p><strong><s><em><u>AT_"+randMethod.getMessage(200)+"</u></em></s></strong></p>",
            "pictures": []
        },
        "itemContent": {
            "content": "<p><strong><s><em><u>AT_"+randMethod.getMessage(200)+"</u></em></s></strong></p>",
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p><strong><s><em><u>AT_"+randMethod.getMessage(300)+"</u></em></s></strong></p>",
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

    "picturebody": {
        "audios": [],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": randMethod.getNumByRange(0, 120),
        "itemAnswer": {
            "answer": '<p>AT_'+randMethod.getMessage(100),
            "pictures": []
        },
        "itemContent": {
            "content": "<p>AT_"+randMethod.getMessage(100),
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p>AT_"+randMethod.getMessage(200),
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

    "durationerror": {
        "audios": [],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": 121,
        "itemAnswer": {
            "answer": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemContent": {
            "content": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p>AT_"+randMethod.getMessage(300)+"</p>",
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

    "audiobody": {
        "audios": [{0: []}],
        "diffLevelCode": randdata.getdifflevel(),
        "duration": randMethod.getNumByRange(0, 120),
        "itemAnswer": {
            "answer": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemContent": {
            "content": "<p>AT_"+randMethod.getMessage(200)+"</p>",
            "pictures": []
        },
        "itemDetail": {
            "detail": "<p>AT_"+randMethod.getMessage(300)+"</p>",
            "pictures": []
        },
        "periodId": randdata.getperiod(),
        "productCode": randdata.getproductline(),
        "regionId": randdata.getregion(),
        "sourceDepartmentId": 9001,
        "subjectId": randdata.getsubject(),
        "videos": [],
        "yearCode": randdata.getyear()
    },

}
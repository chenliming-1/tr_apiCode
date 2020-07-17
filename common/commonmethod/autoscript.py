import os
from har2case.core import HarParser
import json
from common.commonmethod import cookie
from common.commonmethod.tools import indent


# 需要写一个方法遍历去找这个文件下面的所有的har文件，然后用将这些所有的json转化成接口


def _gen_script(scriptname):
    pass


def _gen_import_package():
    str = "import unittest" + "\n"
    str = str + "from common.commonmethod import cookie, todict" + "\n"
    str = str + "from histudy import request, randMethod, log" + "\n"
    str = str + "import os" + "\n"
    return str


def _gen_1_class_name(scriptname):
    return f"class Test" + scriptname.capitalize() + "(unittest.TestCase)" + f":"


def _gen_2_class_method():
    return "@classmethod"


def _gen_3_setup_method():
    return "def setUpClass(cls) -> None:"


def _gen_4_init_data(jsonname):
    # json_init = f"    self.data = todict.data('../../data/{jsonname}.json')" + "\n"
    json_init = indent(
        "cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', '" + jsonname + ".json'))") + "\n"
    json_init = json_init + indent("cls.data['request']['headers']['Cookie'] = cookie", 8) + "\n"
    return json_init


def _gen_5_test_script(moudlename, scriptname):
    # 取json之前的文件名称，就是循环中的filename
    script_method = indent("def test_" + scriptname + "(self):") + "\n"
    script_method = script_method + indent("global res", 8) + "\n"
    script_method = script_method + indent("try:", 8) + "\n"
    script_method = script_method + indent(
        "res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])",
        12) + "\n"
    script_method = script_method + indent("except Exception as error:", 8) + "\n"
    script_method = script_method + indent(
        "log.info(f'" + moudlename + "/test_" + scriptname + ": FAIL, error is {error}')", 12) + "\n"
    script_method = script_method + indent("finally:", 8) + "\n"
    script_method = script_method + indent("self.assertEqual(200, res.status_code)", 12) + "\n"
    script_method = script_method + indent("log.info('" + moudlename + "/test_" + scriptname + ": SUCCESS！')",
                                           12) + "\n"
    return script_method


def gen_auto_script(jsonname, modulename, scriptname):
    str_data = _gen_import_package() + "\n\n"
    str_data = str_data + _gen_1_class_name(scriptname) + "\n"
    str_data = str_data + indent(" ", 3) + _gen_2_class_method() + "\n"
    str_data = str_data + indent(" ", 3) + _gen_3_setup_method() + "\n"
    str_data = str_data + indent(" ", 3) + _gen_4_init_data(jsonname) + "\n"
    str_data = str_data + _gen_5_test_script(modulename, scriptname) + "\n"
    str_data = str_data + _gen_teardown()
    return str_data


def _gen_teardown():
    teardown = indent(" ", 3) + _gen_2_class_method() + "\n"
    teardown = teardown + indent("def tearDownClass(cls) -> None:") + "\n"
    teardown = teardown + indent("pass", 8)
    return teardown


def test_make_testcase_v2():
    """
    1、将.har文件转换成json文件；
    2、自动生成脚本（测试用例）
    :return:
    """
    global testcase, files
    filepath = "../../archives"
    if os.path.exists(filepath):
        file_list = os.listdir(filepath)
        if file_list is not []:
            for files in file_list:
                if files != '__init__.py' and files != '__pycache__':
                    har_path = os.path.join(os.path.dirname(__file__), filepath, files)
                    harparser = HarParser(har_path)
                    testcase = harparser._make_testcase("v2")
                    testcase["request"]["headers"]["Cookie"] = cookie
                    filename = files[0:-4]
                    file_to_list = filename.split("_", 1)
                    # print(file_to_list)
                    if os.path.isfile("../../data/" + filename + '.json'):
                        pass
                    else:
                        with open("../../data/" + filename + '.json', 'w', encoding='utf-8') as f:
                            json.dump(testcase, f, indent=4, ensure_ascii=False)
                            f.close()
                    if os.path.exists("../../testcase/" + file_to_list[0]) is False:
                        os.mkdir("../../testcase/" + file_to_list[0])
                        with open(f"../../testcase/{file_to_list[0]}/__init__.py", 'w', encoding='utf-8') as fr:
                            fr.close()
                    if os.path.isfile(f"../../testcase/{file_to_list[0]}/test_{file_to_list[1]}.py"):
                        pass
                    else:
                        auto_testscript = gen_auto_script(filename, file_to_list[0], file_to_list[1])
                        with open(f"../../testcase/{file_to_list[0]}/test_{file_to_list[1]}.py", 'w',
                                  encoding='utf-8') as fr:
                            fr.write(auto_testscript)
                            fr.close()
        else:
            raise FileNotFoundError(f"文件列表为空，无文件")
    else:
        raise FileNotFoundError(f"{filepath}:文件路径不存在")


if __name__ == '__main__':
    test_make_testcase_v2()

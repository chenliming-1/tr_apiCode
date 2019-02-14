#!Date：2018/10/12 11:26
# !@Author：练素琼
from module import *


class init:
    @staticmethod
    def run():
        subprocess.run("pip install -r requirements.txt")


    @staticmethod
    def download_beautifulreport():
        packages_path = os.path.join(os.path.dirname(sys.executable), 'lib', 'site-packages', 'BeautifulReport')
        if not os.path.exists(packages_path):
            subprocess.run(['git', 'clone', 'https://github.com/TesterlifeRaymond/BeautifulReport.git', packages_path])


if __name__ == '__main__':
    init.run()
    init.download_beautifulreport()

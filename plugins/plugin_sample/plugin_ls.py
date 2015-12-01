# coding: utf-8

import os
import subprocess
import cocos
import cocos_project

from argparse      import ArgumentParser
from MultiLanguage import MultiLanguage

class PluginLs(cocos.CCPlugin):
    
    @staticmethod
    def plugin_name():
        return "plugin_ls"
    
    @staticmethod
    def brief_description():
        return "指定されたプラットフォームのルートをlsするだけのサンプル"
    
    def parse_args(self, argv):
        parser = ArgumentParser(prog="cocos %s" % self.__class__.plugin_name(), description=self.__class__.brief_description())
        parser.add_argument("-p", "--platform", dest="platform", help=MultiLanguage.get_string('COCOS_HELP_ARG_PLATFORM'))
        
        (args, unknown) = parser.parse_known_args(argv)
        
        return args
    
    def init(self, args):
        self._project   = cocos_project.Project(os.path.abspath(os.getcwd()))
        self._platforms = cocos_project.Platforms(self._project, args.platform)
    
    def run(self, argv, dependencies):
        args = self.parse_args(argv)
        self.init(args)
        subprocess.call("ls %s" % self._platforms.project_path(), shell=True)

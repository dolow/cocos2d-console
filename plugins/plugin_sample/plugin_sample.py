# coding: utf-8

import cocos

class PluginSample(cocos.CCPlugin):
    
    @staticmethod
    def plugin_name():
        return "plugin_sample"
    
    @staticmethod
    def brief_description():
        return "プラグイン作成のサンプルです"
    
    def parse_args(self, argv):
        pass
    
    def run(self, argv, dependencies):
        print("this is sample")

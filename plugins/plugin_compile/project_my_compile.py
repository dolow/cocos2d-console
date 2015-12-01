#!/usr/bin/python
# coding: utf-8

__docformat__ = 'restructuredtext'

import project_compile

class CCPluginMyCompile(project_compile.CCPluginCompile):

    @staticmethod
    def plugin_name():
        return "my_compile"

    @staticmethod
    def brief_description():
        return "compileをカスタマイズするサンプル"

    def _add_custom_options(self, parser):
        super(CCPluginMyCompile, self)._add_custom_options(parser)
        from argparse import ArgumentParser
        parser.add_argument("--sample", dest="sample", help="カスタム引数追加のサンプル")

    def run(self, argv, dependencies):
        print("this is customized compile")
        super(CCPluginMyCompile, self).run(argv, dependencies)

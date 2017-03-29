#!/usr/bin/python
from plasTeX import Command,Environment

class myBold(Command):
    args = 'text:str'
    def invoke(self, tex):
        Command.invoke(self, tex)
class iframe(Command):
    args = 'width:str height:str src:str'
    def invoke(self,tex):
        Command.invoke(self, tex)
class collapse(Environment):
    args = 'text:str'
class modalbox(Environment):
    args = 'text:str'
class floating(Environment):
    args = 'float:str'
    def invoke(self, tex):
        Environment.invoke(self, tex)
#!/usr/bin/env python

import cmd
import readline
import subprocess

from igita.commands import system
from igita.commands import system_output
from igita.commands import commands

from igita.history import init_history

class Igita(cmd.Cmd):
    prompt = "igita >> "
    
    def default(self, line):
        self.shell.git(line)

    def emptyline(self):
        self.do_ls('')
    
    def do_git(self, line):
        self.default(line)

    def complete_git(self, text, line, begidx, endidx):
        git_cmds = self.shell.git_cmds
        if not text:
            return git_cmds
        else:
            return [command for command in git_cmds if command.startswith(text) ]

    def do_ls(self, line):
        self.shell.ls(line)
            
    def do_cd(self, line):
        self.shell.cd(line)
    
    def do_hist(self, line):
        self.shell.hist(line, self.history)
        
    def do_echo(self, line):
        self.shell.echo(line)
        
    def do_python(self, line):
        self.shell.python(line, self)
    
    def do_quit(self, line):
        self.shell.quit(self.history)
    
    def do_q(self, line):
        self.do_quit(line)

    def do_EOF(self, line):
        print ''
        self.do_quit(line)

    def preloop(self):
        self.shell = commands()
    
        self.FNULL = open('/dev/null', 'w')
        if system('git', 'rev-parse --show-toplevel', stdout=self.FNULL, stderr=self.FNULL):
            print "This does not seem to be a git repository"
            quit()
        
        self.history = init_history(readline)
        
if __name__ == '__main__':
    Igita().cmdloop()


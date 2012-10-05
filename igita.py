#!/usr/bin/env python

import cmd
import re
import readline
import subprocess

from igita.commands import commands
from igita.core import system
from igita.history import init_history

class Igita(cmd.Cmd):

    # cmd.Cmd overwrites

    prompt = "igita >> "

    def preloop(self):
        self.shell = commands()

        for self.shell.

        self.FNULL = open('/dev/null', 'w')
        if system('git', 'rev-parse --show-toplevel', stdout=self.FNULL, stderr=self.FNULL):
            print "This does not seem to be a git repository"
            quit()
        try:
            if system('git-achievements', 'status', stdout=self.FNULL, stderr=self.FNULL) == 0:
                self.shell.git_call = 'git-achievements'
        except OSError, err:
            pass            
        
        self.history = init_history(readline)

    def precmd(self, line):
        def sub_fun(match):
            return str(self.shell.scope.get(match.groups()[0]))

        return re.sub(
            r'\$(\S+)',
            sub_fun,
            line
        )

    def default(self, line):
        self.do_git(line)

    def emptyline(self):
        self.do_ls('')

    def do_EOF(self, line):
        print ''
        self.do_quit(line)

    # Commands and completes

    def complete_git(self, text, line, begidx, endidx):
        git_cmds = self.shell.git_cmds
        if not text:
            return git_cmds
        else:
            return [command for command in git_cmds if command.startswith(text) ]

    def do_q(self, line):
        self.do_quit(line)
        

if __name__ == '__main__':
    Igita().cmdloop()


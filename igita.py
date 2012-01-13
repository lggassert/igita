#!/usr/bin/env python

import cmd
import re
import readline
import subprocess

from igita.commands import shell
from igita.commands import shell_output
from igita.commands import Commands

class Igita(cmd.Cmd):
    prompt = "igita >> "
    
    git_cmds = [
        'add',
        'archive',
        'branch',
        'cat-file',
        'checkout',
        'clone',
        'commit',
        'config',
        'diff',
        'fetch',
        'fsck',
        'gc',
        'grep',
        'init',
        'instaweb',
        'log',
        'ls-tree',
        'merge',
        'prune',
        'pull',
        'push',
        'remote',
        'reset',
        'rm',
        'show',
        'stash',
        'status',
        'tag',
    ]
    
    hist_file = ''
    FNULL = ''
    
    def default(self, line):
        shell('git', line)
    
    def do_git(self, line):
        self.default(line)

    def complete_git(self, text, line, begidx, endidx):
        if not text:
            return self.git_cmds
        else:
            return [cmd for cmd in self.git_cmds if cmd.startswith(text) ]

    def do_ls(self, line):
        Commands().ls(line)
            
    def do_cd(self, line):
        shell('git', 'checkout ' + line)
    
    def do_quit(self, line):
        readline.write_history_file(self.hist_file)
        quit()
    
    def do_q(self, line):
        self.do_quit(line)

    def do_EOF(self, line):
        print ''
        self.do_quit(line)

    def emptyline(self):
        self.do_ls('')

    def preloop(self):
        self.FNULL = open('/dev/null', 'w')
        if shell('git', 'rev-parse --show-toplevel', stdout=self.FNULL, stderr=self.FNULL):
            print "This does not seem to be a git repository"
            quit()
            
        self.hist_file = shell_output('git', 'rev-parse --show-toplevel').strip()
        self.hist_file += '/.igita_history'
        
        open(self.hist_file, 'a').close()
        readline.set_history_length(1000)
        readline.read_history_file(self.hist_file)
        
if __name__ == '__main__':
    Igita().cmdloop()


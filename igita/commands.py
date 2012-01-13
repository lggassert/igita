import code

from core import system
from history import init_history

def commands():
    class Commands:
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
            
        def cd(self, line):
            system('git', 'checkout ' + line)

        def echo(self, line):
            print line
            
        def edit(self, line):
            system('vim', line)
            
        def git(self, line):
            system('git', line)
            
        def hist(self, line, history):
            print history.print_(line)
            
        def ls(self, line):
            system('git', 'status ' + line)
            
        def python(self, line, igitaInst):
            igitaInst.history.save()
            igitaInst.history.clear()
            code.interact(local={'igita' : igitaInst})
            igitaInst.history = init_history(igitaInst.history.handler)
            
        def quit(self, history):
            history.save()
            quit()
            
    return Commands()

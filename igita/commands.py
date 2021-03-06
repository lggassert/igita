import code

from core import system
from history import init_history
from scope import scope

def commands():
    class Commands:
        git_call = 'git'
        editor = 'vim'
    
        scope = scope()
    
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
            system(self.git_call, 'checkout ' + line)

        def echo(self, line):
            print line
            
        def edit(self, line):
            system(editor, line)
            
        def git(self, line):
            system(self.git_call, line)
            
        def hist(self, line, history):
            print history.print_(line)
            
        def ls(self, line):
            system(self.git_call, 'status ' + line)
            
        def python(self, line, igitaInst):
            igitaInst.history.save()
            igitaInst.history.clear()
            code.interact(local={'igita' : igitaInst})
            igitaInst.history = init_history(igitaInst.history.handler)
            
        def set(self, line):
            match = line.strip().split()
            if len(match)%2:
                print "Missing value for variable {}".format(match[-1])
                return
            for i in range(0, len(match) - 1, 2):
                self.scope.set(match[i], match[i + 1])
            
        def quit(self, history):
            history.save()
            quit()
            
    return Commands()

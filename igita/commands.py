import code
import subprocess
import re

def _params(command, line):
        params = []
        
        if command:
            params.append(command)
        
        do_break = 0
        for i, x in enumerate(re.split('"', line)):
            if do_break: break
            if i%2:
                param = '"%s"' % x
                params.append(param)
            else:
                for j, y in enumerate(re.split("'", x)):
                    if do_break: break
                    if j%2:
                        param = '"%s"' % y
                        params.append(param)
                    else:
                        for k, z  in enumerate(re.split('\|', y)):
                            if k%2:
                                do_break = 1
                                break
                            else:
                                for s in z.split():
                                    params.append(s)
        return params

def system(command, line, **kwargs):
        params = _params(command, line)
        return subprocess.call(
            params,
            stdout=kwargs.get('stdout', None),
            stderr=kwargs.get('stderr', None),
        )
        
def system_output(command, line, **kwargs):
        params = _params(command, line)
        return subprocess.check_output(
            params,
            stderr=kwargs.get('stderr', None),
        )

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

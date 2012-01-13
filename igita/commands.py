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

def shell(command, line, **kwargs):
        params = _params(command, line)
        return subprocess.call(
            params,
            stdout=kwargs.get('stdout', None),
            stderr=kwargs.get('stderr', None),
        )
        
def shell_output(command, line, **kwargs):
        params = _params(command, line)
        return subprocess.check_output(
            params,
            stderr=kwargs.get('stderr', None),
        )
        
class Commands:
    def ls(self, line):
        shell('git', 'status ' + line)

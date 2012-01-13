import readline

from commands import system_output
    
def init_history(handler):
    class History():
        def _get_filename(self):
            return system_output(
                'git',
                'rev-parse --show-toplevel'
            ).strip() + '/.igita_history'

        def __init__(self, **kwargs):
            self.lenght = kwargs.get('lenght', 1000)
            self.handler = kwargs.get('handler', readline)
            self.filename = kwargs.get('filename', self._get_filename())
            open(self.filename, 'a').close()
            self.handler.set_history_length(self.lenght)
            self.handler.read_history_file(self.filename)
        
        def save(self):
            self.handler.write_history_file(self.filename)
            
        def clear(self):
            self.handler.clear_history()
            
        def print_(self, line):
            resp = ""
            
            start = 1
            end = 0
            max_ = handler.get_current_history_length()
            
            if not 0 < end <= max_:
                end = max_
            
            format_string = ' {{:{}}}: {{}}\n'.format(len(str(end)))
            for i in range(start, end+1):
                resp += format_string.format(i, handler.get_history_item(i))
            return resp[:-1]
    
    return History(
        handler=handler,
    )

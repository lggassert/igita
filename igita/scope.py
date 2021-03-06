def scope():
    class Scope:
        _scope = {}  
        
        def set(self, var, value):
            self._scope[var] = value
            return value
            
        def unset(self, var):
            del self._scope[var]
            
        def get(self, var):
            return self._scope.get(var, '')
            
    return Scope()

def scope():
    class Scope:
        _scope = {'PORRA' : 1}  
        
        def set(var, value):
            self._scope[var] = value
            return value
            
        def unset(var):
            del self._scope[var]
            
        def get(self, var):
            return self._scope.get(var, '')
            
    return Scope()

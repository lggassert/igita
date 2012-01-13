igita - Interative Git Application
==================================

Commands
--------

igita easily responds to any valid git command. Just type:

        >> <command>

when you'd normally type (on a regular shell):

        >> git <command>

For convenience, igita implements some other calls:

*       _git_ - for when you forget you're using igita
*       _cd_ - the same as 'git checkout'
*       _ls_ - the same as 'git status'
*       _hist_ - shows igita's history
*       _edit_ - edit a file (currently uses VIM)
*       _python_ - opens a python interpreter
*       _echo_ - prints something, will be used to inspect variables at some point
*       _quit_ **or** _q_ - exits igita (**EOF** works too)

**NOTE:** igita no longer responds to system calls.

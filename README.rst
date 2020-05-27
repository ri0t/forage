
Forage Tool
===========

A simple tool to execute commands on given folders.
Via spur, forage is capable of doing that over ssh, too.

You could probably do all that with xargs or find.

Very handy when working on organizations with a non-monolithic repository structure!

It has some safety measures included - but be very careful, as this tool allows
(possibly) unprecedented in-the-foot-shooting.

Installation
============

Installation doesn't require much more than invoking the provided ``setup.py``.
Be crazy and individualistic by installing it into your global environment:

``python setup.py install``

You can also be a little more careful by using a virtual environment, of course.

Application Examples
====================

I mostly use this with git to work on many repositories at once.

git
---

A short word of warning: If you use forage with git, be extra careful!
Always check with ``git diff --cached`` before you actually commit!

Get a quick glance at the status of a lot of repositories:

``forage -o -q -h -p -r "git status -s" repos | less``

Commit with a message:

``forage -o -q -h -p -r "git commit -m {{replace}}" --cmd-replace "Your commit message" repos | less``

Some other useful commands with the forage / git combination:

See changes to commit:
``git diff --cachced``

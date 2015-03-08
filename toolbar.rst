Toolbar
=======
A Toolbar typically provides common shortcuts to features of an application (e.g. open file, find, zoom) and is usually displayed above the main content of the application.

=======
Methods
=======
Widgets are inserted into the Toolbar using::

  toolbar.insertWidget(action, widget)

Separators allowing widgets to be grouped neatly are inserted with::

  toolbar.insertSeparator(action)

Newly-created Toolbar widgets have a handle on the left which provides for detaching the toolbar and allowing the user to position it elsewhere. This can be disabled via::

  toolbar.setMovable(movable)

When the *movable* is set to ``False``, the grab handle is hidden and the Toolbar is not able to be moved.

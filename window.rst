Window
======
The Window is typically the base of every graphical application, and is used to display other widgets.

===========
Constructor
===========
Construction of the Window is done using::

  window = QWindow()

=======
Methods
=======
The title of the Window, which is usually displayed by the Window Manager can be set using::

  window.setTitle(title)

Window objects can also be minimised or maximised programatically using::

  window.showMinimized()
  window.showMaximized()

Alternatively, some applications will want a fullscreen mode::

  window.showFullScreen()

If the window is set to minimised, maximised or fullscreen, it can be restored to a normal state by::

  window.setNormal()

Minimum widths and heights are enforceable with::

  window.setMinimumWidth(width)
  window.setMaximumWidth(width)
  window.setMinimumHeight(height)
  window.setMaximumHeight(height)

A specific width and/or height can also be declared via::

  window.setWidth(width)
  window.setHeight(height)

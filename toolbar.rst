Toolbar
=======
A Toolbar typically provides common shortcuts to features of an application (e.g. open file, find, zoom) and is usually displayed above the main content of the application.

=======
Methods
=======
Widgets are inserted into the Toolbar using::

  toolbar.addWidget(widget)
  toolbar.insertWidget(action, widget)

The *action* parameter within the ``.insertWidget()`` method should be set to an appropriate :doc:`action` object.

Separators allowing widgets to be grouped neatly are attached to the Toolbar with::

  toolbar.addSeparator()
  toolbar.insertSeparator(action)

All items within the Toolbar can be cleared using::

  toolbar.clear()

By default, Toolbar widgets are usually horizontally orientated. The orientation can be set with::

  toolbar.setOrientation(orientation)

The *orientation* value should be set vertically or horizontally with one of the following:

* ``Qt::Vertical``
* ``Qt::Horizontal``

Newly-created Toolbar widgets have a handle on the left which provides for detaching the toolbar and allowing the user to position it elsewhere. This can be disabled via::

  toolbar.setMovable(movable)

When the *movable* is set to ``False``, the grab handle is hidden and the Toolbar is not able to be moved.

In some cases, it may be useful to allow the Toolbar to be floated in its own window::

  toolbar.setFloatable(floatable)

The widget associated with an Action object can be found using::

  toolbar.widgetForAction(action)

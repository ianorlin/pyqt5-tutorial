MenuBar
=======
A MenuBar provides a horizontal bar which is used as a container for other widgets. Typically these will be Button and Menu combinations which provide additional options for the application functionality.

===========
Constructor
===========
The MenuBar can be constructed using::

  menubar = QMenuBar()

=======
Methods
=======
Actions, which perform an associated function when clicked can be added to the MenuBar with a simple text label::

  action = menubar.addAction(label)

When the Action is defined, it is also returned allowing the use of methods defined in the :doc:`action` documentation.

Alternatively, if a menu should be displayed on click with many options, the following can be called::

  menu = menubar.addMenu(label)

As with the Action example, adding a menu returns a :doc:`menu` item.

Items are also removable by::

  menubar.removeAction(action)

The *action* value should be set to the name of the Action to be removed.

Separators are supported by the MenuBar with::

  menubar.addSeparator()

All the actions specified for the MenuBar may be cleared via::

  menubar.clear()

=======
Example
=======
Below is an example of an MenuBar. This also contains examples of the Action and Menu widgets as they are closely associated with the MenuBar.

.. literalinclude:: _examples/menubar.py

Download: :download:`MenuBar <_examples/menubar.py>`

ToolBox
=======
The ToolBox widget is a container which displays groups of items separated by tabs, with the item consisting of the text identifying the item, and an optional icon. The ToolBox is commonly used in applications where there are too many items to place in a :doc:`toolbar`.

===========
Constructor
===========
The ComboBox widget is created by defining::

  toolbox = QToolBox()

=======
Methods
=======
Items can be added to the ToolBox via two methods::

  toolbox.addItem(child, label)
  toolbox.addItem(child, icon, label)
  toolbox.insertItem(index, child, label)
  toolbox.insertItem(index, child, icon, label)

The *child* parameter is the widget to be added to the ToolBox. The *label* value is the item name to be displayed on the ToolBox. An *icon* can also be added to each item using the :doc:`qicon` object. The ``.insertItem()`` method also takes an *index* parameter which indicates the position at which the child should be added.

Items can also be removed::

  toolbox.removeItem(index)

The *index* value indicates the position of the child widget to be removed, with ``0`` indicating the first item.

It may be useful to get the active item index or widget with the methods::

  toolbox.currentIndex()
  toolbox.currentWidget()

The number of items contained in the ToolBox can be fetched using::

  toolbox.count()

To disable (grey-out) an item and prevent it being accessed, call::

  toolbox.setItemEnabled(index, state)

The *index* value indicates which item is to be disabled and the state, when set to ``False`` will disable the item.

Item attributes can also be changed after add/insert with::

  toolbox.setText(index, label)
  toolbox.setIcon(index, icon)

A tooltip, which is displayed when the user hovers over a child, can be associated with each item::

  toolbox.setToolTip(index, text)

The *index* value indicates the child which is to receive the tooltip. The *text* value is the string of text to be attached.

The text, icon and tooltip can also be retrieved from the ToolBox by calling::

  toolbox.itemText(index)
  toolbox.itemIcon(index)
  toolbox.itemToolTip(index)

The *index* value should be set to the number of the item which is to be retrieved.

To find the index number for a given child widget call::

  toolbox.indexOf(widget)

Alternatively, the widget for a given index number is found using::

  toolbox.widget(index)

=======
Example
=======
Below is an example of an ToolBox:

.. literalinclude:: _examples/toolbox.py

Download: :download:`ToolBox <_examples/toolbox.py>`

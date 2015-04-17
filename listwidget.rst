ListWidget
==========
A ListWidget is a simple list widget which provides an easy way to display a number of items, of which one or more can be selected.

===========
Constructor
===========
Constructing the ListWidget is done by::

  listwidget = QListWidget()

=======
Methods
=======
Item can be added to the ListWidget via several different methods::

  listwidget.addItem(text)
  listwidget.addItem(item)
  listwidget.addItems(text, text, ...)
  listwidget.insertItem(row, text)
  listwidget.insertItem(row, item)
  listwidget.insertItems(row, text, text, ...)

The first method takes a string of text as the parameter and adds it to the list. The second method takes a :doc:`listwidgetitem` as a parameter to display. The final method takes several strings of text and adds each one as a single item to the ListWidget. The 'insert' methods work in the same way, with the additional integer value indicating the row at which the item is to be added.



The number of items currently in the list can be retrieved with::

  count = listwidget.count()

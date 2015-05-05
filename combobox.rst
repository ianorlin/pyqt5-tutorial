ComboBox
========
A ComboBox provides a dropdown menu attached to a button, providing a list of options of which one can be selected by the user.

===========
Constructor
===========
The ComboBox widget is created by defining::

  combobox = QComboBox()

=======
Methods
=======
Individual items are added to the ComboBox using the methods::

  combobox.addItem(text)
  combobox.insertItem(index, text)

The *text* value should be set to the string of text which is to be added to the ComboBox. The ``.insertItem()`` method also allows for an *index* value to be specified which indicates where the item will be inserted.

An alternative is to add multiple items with a single method::

  combobox.addItems(text, text, text...)
  combobox.insertItems(index, text, text, text...)

Separators can be inserted into a specific position within the ComboBox popup with::

  comobbox.insertSeparator(index)

Removal of items is done with the method::

  combobox.removeItem(index)

The currently selected index or text is retrievable with the following::

  combobox.currentIndex()
  combobox.currentText()

To retrieve the number of items held within the ComboBox use::

  combobox.count()

The number of items permissable in the ComboBox is set by::

  combobox.maxCount(count)

The *count* value should be an integer value indicating the limit. If the number of items added is greater than the maximum amount, the extra items are truncated.

The ComboBox popup menu can be shown or hidden programmatically with::

  combobox.showPopup()
  combobox.hidePopup()

=======
Example
=======
Below is an example of an ComboBox:

.. literalinclude:: _examples/combobox.py

Download: :download:`ComboBox <_examples/combobox.py>`

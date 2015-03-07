CheckBox
========
A CheckBox provides a checked or unchecked state, indicated via a tick in a box. These are commonly used to indicate when a feature is enabled.

===========
Constructor
===========
Constructing the CheckBox is done with the following statement::

  checkbox = QCheckBox(label)

The *label* parameter is optional. When included, the CheckBox will be displayed with an associated textual label, typically indicating the function of the widget.

=======
Methods
=======
The text associated with the CheckBox can be set after construction by calling::

  checkbox.setText(text)

Adjusting the CheckBox state programmatically is done with the method::

  checkbox.setChecked(checked)

When *checked* is set to ``True``, the CheckBox will contain a ticket in the box.

To get the state of the CheckBox, use::

  checked = checkbox.isChecked()

A tick in the CheckBox will return ``True`` from the method, while ``False`` is returned when the CheckBox is unchecked.

=======
Example
=======
Below is an example of an CheckBox:

.. literalinclude:: _examples/checkbox.py

Download: :download:`CheckBox <_examples/checkbox.py>`

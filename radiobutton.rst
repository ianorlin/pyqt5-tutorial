RadioButton
===========
The RadioButton is a toggable button, which is typically used in conjunction with other RadioButton's with only one of the buttons able to be selected at any one time.

===========
Constructor
===========
The constructor used for building the RadioButton is::

  radiobutton = QRadioButton(label)

=======
Methods
=======
Text can be changed within the RadioButton via::

  radiobutton.setLabel(text)

To set a RadioButton to be checked, use::

  radiobutton.setChecked(checked)

When *checked* is set to ``True``, the defined RadioButton will be active.

Determining whether the RadioButton is active or not is done by::

  checked = radiobutton.isChecked()

By default, all RadioButton widgets within the window will be assigned to the same group. This will cause problems if there are multiple batches of buttons which have different intents. To resolve this issue, read about the :doc:`ButtonGroup` object.

=======
Example
=======
Below is an example of an RadioButton:

.. literalinclude:: _examples/radiobutton.py

Download: :download:`RadioButton <_examples/radiobutton.py>`

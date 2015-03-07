PushButton
==========
The PushButton is often used to get the program to do something with the user simply having to press a button. This could be starting a download or deleting a file.

===========
Constructor
===========
The PushButton is constructed using::

  pushbutton = QPushButton(label)

The *label* string can be left out if not required, or set to the text which should be shown on top of the button.

=======
Methods
=======
The label displayed on the button can be changed after widget construction by::

  pushbutton.setText(label)

By default, the button is shown with a well-defined border making it appeared raised up from the surface of the window beneath. It is possible however to give the button a flat appearance via::

  pushbutton.setFlat(flat)

When *flat* is set to ``True``, the button does not appear raised.

To check whether a button has been set to flat or not, call::

  flat = pushbutton.isFlat()

=======
Signals
=======
One of the common functions of a button is to be clicked by the user, and perform an associated action. This is done by connecting the clicked signal of the button to the appropriate function::

  pushbutton.clicked.connect(button_clicked_function)

=======
Example
=======
Below is an example of an PushButton:

.. literalinclude:: _examples/pushbutton.py

Download: :download:`PushButton <_examples/pushbutton.py>`

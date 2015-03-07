Label
=====
The Label widget is used to display text to the user. This can be anything from one-word labels indicating the purpose of another widget, to single sentences, to multi-line, multi-paragraph blocks of text.

===========
Constructor
===========
Label widgets are constructed via the constructor::

  label = QLabel(text)

The *text* parameter can either be left-out, with the text optionally being specified later, or defined at construction time.

=======
Methods
=======
To set or change the text after construction, call::

  label.text(text)

=======
Example
=======
Below is an example of an Label:

.. literalinclude:: _examples/label.py

Download: :download:`Label <_examples/label.py>`

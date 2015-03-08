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

  label.setText(text)

Text can also be retrieved from the Label via::

  text = label.text()

Alignment defaults for the Label is to position text to the left of the label, and central vertically. This can be customised::

  label.setAlignment(alignment)

The *alignment* parameter specifies where to place the text both horizontally and vertically. The horizontal constants are:

* ``Qt.AlignLeft``
* ``Qt.AlignHCenter``
* ``Qt.AlignRight``
* ``Qt.AlignJustify``

To set the vertical alignment position:

* ``Qt.AlignTop``
* ``Qt.AlignVCenter``
* ``Qt.AlignBottom``
* ``Qt.AlignBaseline``

If both horizontal and vertical alignments are needed, the constants should be separated by a pipe ``|``.

The Label widget also allows wrapping of text if there are multiple lines. This can be enabled using the method::

  label.setWordWrap(word_wrap)

When *word_wrap* is set to ``True``, the text will be wrapped into the space allocated for the widget.

The margin size on a Label is zero initially. Custom margin settings are allowed by specifying the size in pixels::

  label.setMargin(margin)

Indents can also be applied to the Label text by specifying the indent amount in pixels::

  label.setIndent(indent)

Mnemonic keyboard shortcuts are an important part of accessibility and speed when using an application. They are identified by the presence of an underscore beneath a letter in the label. Some widgets however can not display a mnemonic character, so a Label can be paired with the other widget. This allows focus to be transferred to the other widget from the Label when the shortcut key is used.

  label.setBuddy(widget)

The *widget* parameter is the name of the widget to be paired with the Label.

=======
Example
=======
Below is an example of an Label:

.. literalinclude:: _examples/label.py

Download: :download:`Label <_examples/label.py>`

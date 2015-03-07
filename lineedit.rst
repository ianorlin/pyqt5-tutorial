LineEdit
========
The LineEdit widget is a one-line text entry widget used to receive textual input from the user. Example use cases include the user entering their name or their password.

=======
Methods
=======
By default, the LineEdit has no text displayed within the widget. In some cases it may be useful to have a prepopulated string which can be set with::

  lineedit.setText(text)
  lineedit.insert(text)

Both of the methods overwrite any existing text.

Text is also retrieved from the widget by::

  text = lineedit.text()

Another useful feature is to show placeholder text in the LineEdit, which indicates the widgets purpose::

  lineedit.setPlaceholderText(text)

To prevent the user from modifying the content of the LineEdit, call::

  lineedit.setReadOnly(read_only)

When *read_only* is set to ``True``, the widget will not allow its content to be modified.

The default setting of the LineEdit is to allow 32767 characters to be entered into the field. This can be limited by::

  lineedit.setMaxLength(length)

=======
Example
=======
Below is an example of an LineEdit:

.. literalinclude:: _examples/lineedit.py

Download: :download:`LineEdit <_examples/lineedit.py>`

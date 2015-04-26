PlainTextEdit
=============
The PlainTextEdit widget is optimised to display plain text content.

If the application is to display formatted text, the :doc:`textedit` widget should be used.

===========
Constructor
===========
The PlainTextEdit widget is constructed by using::

  plaintextedit = QPlainTextEdit()

=======
Methods
=======
Text is inserted into the PlainTextEdit by either of the following methods::

  plaintextedit.appendPlainText(text)
  plaintextedit.insertPlainText(text)

The ``.appendPlainText()`` method adds the new text to the end of the current text block whereas the ``.insertPlainText()`` method adds the text at the cursor position.

By default, the text in the PlainTextEdit can be modified by the user. It can however be used as a read-only widget with::

  plaintextedit.setReadOnly(read_only)

When *read_only* is set to ``True``, the user will only be able to navigate through the text.

The read-only state of the widget can also be retrieved using::

  read_only = plaintextedit.isReadOnly()

Placeholder text can be placed into the PlainTextEdit with::

  plaintextedit.placeholderText(text)

The *text* specified will only be shown in the widget when there is no text loaded.

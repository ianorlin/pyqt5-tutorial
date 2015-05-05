GroupBox
========
The GroupBox provides a tidy way to group items, with the container featuring a title label and bordering frame.

It should be noted that the GroupBox can only contain one widget itself, with the intention of other containers such as a :doc:`box`.

===========
Constructor
===========
The constructor for a GroupBox is::

  groupbox = QGroupBox(title)

The *title* parameter should be set with the string of text to display.

=======
Methods
=======
The title applied to the GroupBox can be set using::

  groupbox.setTitle(title)

A widget is added to the GroupBox with::

  groupbox.setLayout(child)

The alignment of children within the GroupBox is settable via::

  groupbox.setAlignment(alignment)

By default, the alignment is set to the left-edge, however it can be customised with the *alignment* value being set to one of the following::

  * ``Qt::AlignLeft``
  * ``Qt::AlignRight``
  * ``Qt::AlignHCenter``

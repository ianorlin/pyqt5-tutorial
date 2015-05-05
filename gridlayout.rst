GridLayout
==========
The GridLayout widget provides a container which allows widgets to be laid out in a dynamically sized grid.

===========
Constructor
===========
The constructor for the GridLayout is::

  gridlayout = QGridLayout()

=======
Methods
=======
Items are added to the GridLayout using::

  gridlayout.addWidget(widget)
  gridlayout.addWidget(widget, row, column)
  gridlayout.addWidget(widget, row, column, rowspan, columnspan, alignment)

The *widget* parameter indicates the widget which is to be added to the GridLayout at *row* and *column*. The row and column values work on a coordinate-like system, with 0 and 0 indicating top-left. The *rowspan* and *columnspan* values indicate how many rows or columns the widget should span. Finally, the *alignment* parameter should be set to one of the following:

* ``Qt::AlignmentLeft``
* ``Qt::AlignmentRight``
* ``Qt::AlignmentHCenter``
* ``Qt::AlignmentJustify``

A layout is added to the GridLayout using alternative methods::

  gridlayout.addLayout(widget)
  gridlayout.addLayout(widget, row, column)
  gridlayout.addLayout(widget, row, column, rowspan, columnspan, alignment)

Retrieving the item at a given position is done with the method::

  gridlayout.itemAtPosition(row, column)

There is no spacing between rows and columns by default. This can be adjusted via::

  gridlayout.setSpacing(spacing)

Alternatively, vertical and horizontal spacing can be specified separately using::

  gridlayout.setHorizontalSpacing(spacing)
  gridlayout.setVerticalSpacing(spacing)

The *spacing* parameter should be set to an integer number indicating the number of pixels spacing which should be displayed.

The number of rows and columns can be obtained from the container with::

  gridlayout.rowCount()
  gridlayout.columnCount()

Calendar
========
The Calender widget provides a way to select a date and show a date to the user.

===========
Constructor
===========
The Calendar is constructed using the call::

  calendar = QCalendarWidget()

=======
Methods
=======
A number of functions are available for changing the date relative to the current date with::

  calendar.showToday()
  calendar.showSelectedDate()
  calendar.showNextMonth()
  calendar.showNextYear()
  calendar.showPreviousMonth()
  calendar.showPreviousYear()

The selected date can be retrieved from the Calendar with::

  calendar.selectedDate()

This returns a :doc:`qdate` object which contains a number of associated methods for retrieving the date.

The current page, determined by the specified month and year can be set via::

  calendar.setCurrentPage(month, year)

The minimum and maximum dates viewable within the Calendar can be set with::

  calendar.minimumDate(date)
  calendar.maximumDate(date)

The *date* object should also be a :doc:`qdate` object.

By default, the Calendar allows the date to be changed. It is possible to prevent the Calendar from being changed using::

  calendar.setDateEditEnabled(enabled)

When *enabled* is set to ``False``, the user is no longer able to modify the Calendar.

The view of the Calendar can be customised by showing or hiding both the grid lines and navigation bar::

  calendar.isGridVisible(visible)
  calendar.isNavigationBarVisible(visible)

=======
Signals
=======
When the date selection is changed, either by the user changing the date or by programmatically changing the date, the ``.selectionChanged()`` signal is emitted.

=======
Example
=======
Below is an example of an Calendar:

.. literalinclude:: _examples/calendar.py

Download: :download:`Calendar <_examples/calendar.py>`

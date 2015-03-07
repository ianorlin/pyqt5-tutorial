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
By default, the Calendar allows the date to be changed. It is possible to prevent the Calendar from being changed using::

  calendar.setDateEditEnabled(enabled)

When *enabled* is set to ``False``, the user is no longer able to modify the Calendar.

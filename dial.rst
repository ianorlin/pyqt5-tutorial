Dial
====
The Dial widget provides a :doc:`range` object which takes the form of a control knob. Its design is similar to a volume knob on a music system.

===========
Constructor
===========
The Dial widget is created by defining::

  dial = QDial()

=======
Methods
=======
The minimum and maximum values of the Dial are set by::

  dial.minimum(minimum)
  dial.maximum(maximum)

To set the value of the Dial programmatically, call::

  dial.setValue(value)

Retrieving the value set on the Dial is done using::

  value = dial.value()

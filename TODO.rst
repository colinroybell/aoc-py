=====
TO DO 
=====

* Automatic input handler for string input. It is passed either a filename, or a list of strings, and we return an iterator
* Probable class hierarchy, which can give a prefix function for data (and other things if we need it)
* Utility functions for some general use cases - maybe survey 2015 for typical inputs?
* Work out pytest selection mechanisms/marking, and how to do things reasonably generically
* Find a good linting solution

* think about bringup vs functional vs regression testing.


====== 
pytest
======

pytest xfail is usual semantic for a test that is expected to fail, so think I'm fine at the minute for regressions. Having a pass for bringup tests is less good. Maybe have them commented out as a stub? Or skip?

Durations seem very random. Is there a more reliable means of timing?



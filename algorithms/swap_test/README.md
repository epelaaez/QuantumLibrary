# Swap test
The swap test can tell us if two registers are in the same state without measuring them. However, it cannot tell us what state they are in.

**TODO: explain circuit**

The circuit looks like this:

![circuit](https://user-images.githubusercontent.com/63567458/102344325-0538f900-3f9c-11eb-87aa-dcfb800d299a.jpg)

The more times we observe |1> as the output, the more certain we can be that the two registers are in the same state. The moment we get the state |0> as an output, we can be certain that the registers are **not** in an identical state.<sup>[1](#footnote_1)</sup>

The histogram for this implementation of the swap test looks like this (we get the state |1> 100% of the time since the two registers are set to the same state):

![histogram](https://user-images.githubusercontent.com/63567458/102344351-0ec26100-3f9c-11eb-87b2-347cc3f75a13.jpg)

<a name="footnote_1">1</a>: Note that to account for errors in the quantum computer itself we can allow some occurences of the state |0> and still be certain that the two registers are in the same state.

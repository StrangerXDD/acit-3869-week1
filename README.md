
Okay, it's time to warm up with a fairly simple algorithmic problem.

## Problem Statement

In the file called `solution.py`, you will modify the function called `our_shared_values`.

This function `our_shared_values` should take in two parameters, both lists of strings, which I will call `left` and `right`.

It should also return an list of strings, as follows:
* any word that occurs in *both* `left` and `right` should occur in the output
* the number of times a word appears in the output should be the minimum of the number of times it appears in `left` and `right`

The answer list may be in *any order*.

## How To Run The Tests

```bash
python3 -m unittest -v test.py
```


## Example 1

```python
our_shared_values(
    ['one', 'two', 'two', 'two', 'three'],
    ['four', 'two', 'three', 'two', 'zero'],
)
```

The words "one", "four", and "zero" do not appear in both parameters, so none of those words will appear in the output.  The word "three" is in each parameter once, so the output should include a single "three".  The word "two" appears 3x in the first param, and 2x in the second param, so that means it should appear 2x in the output.

Any of the following would be acceptable outputs for this example:

```python
['two', 'two', 'three']
['two', 'three', 'two']
['three', 'two', 'two']
```


## Example 2

```python
our_shared_values(
    ['one', 'two', 'two', 'two', 'three'],
    [],
)
```

This is a very simple edge case.  There are no words that appear in both lists, so the answer must be an empty list, `[]`.

Can you think of other edge cases?  Are any of them trickier than this one?  Let me know!
##### Module for returning word pairs from text strings

##### Example:

```python
>>> from trw_text_string import TextString
>>> string_example = """Hello, I like nuts. Do you like nuts? No? Are you sure?
                        Why don't you like nuts? Are you nuts? I like you"""
>>> text_string_object = TextString(string_example)
>>> text_string_object.return_word_pairs()
are you: 2
like nuts: 3
you like: 3
i like: 2
```

##### Installation:

<p> In order to install text_string: </p>

```python
pip install trw_text_string
```

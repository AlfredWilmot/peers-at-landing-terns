# Learn Design Patterns
(because your future sanity depends on it!)

### Setup Instructions

- Prepare a basic venv:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- Ensure you're using the right python binary associated with the venv:
    ```bash
    which python
    ```
    (should be something like): 
    > /home/loki/Desktop/ldp/.venv/python
- Check which python version you're using:
    ```bash
    python --version
    ```
    (mine is):
    > Python 3.8.10
- Install requirements with venv sources to finish setting it up:
    ```bash
    pip install -r requirements.txt
    ```

### References

--- 
[Abstract Base Classes vs Protocols](https://www.youtube.com/watch?v=xvb5hGLoK0A)
```python
'Abstract Base Classes' (abc) rely on "nominal typing" -> explicit typing
via inheritance (concrete implementation of ABC inherits from the ABC)

'Protocols' rely on "structural typing" (aka duck-typing) -> Python
interprets the structure of objects that are used with protolcs:
if they have the same properties/ methods as specified by the protocol,
then they are treated as that protocol.
A protocol defined an expected interface, there is no inheritance here.
```
---

[Advanced Exception Handling](https://www.youtube.com/watch?v=ZsvftkbbrR0)
```python

```

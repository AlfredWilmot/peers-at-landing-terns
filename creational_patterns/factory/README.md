# Factory design patterns
Client requests instance of an object without knowning the implementation
details.

### `factory method`
A single method is used to track which objects are created,
instead of letting the client code create objects via direct class instantiations.
This centralizes object creation which simplifies tracking these instances.

Django uses the `factory method` for creating different types of fields in a web form.

Each factory method logically groups the creation of objects that have similar properties.

Decouples the creation and usage of objects.

Changes to the factory method should not require changes of the (client) code that uses it.




### `abstract factory`

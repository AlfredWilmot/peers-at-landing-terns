"""
Taken from the observer pattern wikipedia article:
https://en.wikipedia.org/wiki/Observer_pattern

    - The subject maintains a list of its dependents (observers),
        automatically notifying them of any state changes.
    - subjects are "event streams", while observers are "events sinks"
    - a very basic behavioural pattern that can be extended by
        message queueing systems.

"""
class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)


if __name__ == "__main__":
    subject = Observable()
    observer = Observer(subject)
    subject.notify_observers("test", kw="python")

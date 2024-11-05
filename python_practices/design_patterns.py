class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
print(Singleton() is Singleton()) # True

#Structural Pattern: Adapter
#The Adapter pattern allows incompatible interfaces to work together by wrapping an existing class with a new interface.
class EuropeanSocket:
    def voltage(self): return 230
class USASocket:
    def voltage(self): return 120
class Adapter:
    def __init__(self, socket): self.socket = socket
    def voltage(self): return self.socket.voltage()
# allows incompatible interfaces to work together by wrapping an existing class with a new interface.
european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
print(adapter.voltage())  # Output: 230

# Behavioral Pattern: Observer
# The Observer pattern defines a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.
class Subject:
    def __init__(self): self._observers = []
    def attach(self, observer): self._observers.append(observer)
    def notify(self, message): [ observer.update(message) for observer in self._observers]
class Observer:
    def update(self, message): print(f"Received message: {message}")
# Usage
subject = Subject()
subject.attach(Observer())
subject.attach(Observer())
subject.notify("Hello, Observers!") ## Twice : # Received message: Hello, Observers!
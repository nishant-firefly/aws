class Example:
    @classmethod
    def class_method(cls):
        print("Class method called")

    @staticmethod
    def static_method():
        print("Static method called")
Example.class_method()  # Class method called, take cls.
Example.static_method()  # Static method called

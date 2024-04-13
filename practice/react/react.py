class InputCell:
    def __init__(self, initial_value):
        # Initialize the value and set of observers
        self._value = initial_value
        self._observers = set()

    @property
    def value(self):
        # Getter for the value property
        return self._value

    @value.setter
    def value(self, new_value):
        # Setter for the value property
        self._value = new_value
        # Notify observers upon value change
        for observer in self._observers:
            observer.compute()

    def register_observer(self, observer):
        # Add observer to the set of observers
        self._observers.add(observer)

    def compute(self):
        # Placeholder method for computing the value of InputCell
        pass


class ComputeCell:
    def __init__(self, inputs, compute_function):
        # Initialize inputs, compute function, callbacks, and value
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = set()
        self._value = None
        self._start_observing_ultimate_observables()
        self.compute()

    @property
    def value(self):
        # Getter for the value property
        return self._value

    @value.setter
    def value(self, computed_value):
        # Setter for the value property
        self._value = computed_value
        # Notify callbacks upon value change
        for callback in self.callbacks:
            callback(self.value)

    def add_callback(self, callback):
        # Add callback to the set of callbacks
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        # Remove callback from the set of callbacks
        self.callbacks.discard(callback)

    def _start_observing_ultimate_observables(self):
        # Method to start observing ultimate observables
        def ultimate_observables(inputs):
            for input_ in inputs:
                if isinstance(input_, ComputeCell):
                    yield from ultimate_observables(input_.inputs)
                else:  # InputCell
                    yield input_

        for ultimate_observable in ultimate_observables(self.inputs):
            ultimate_observable.register_observer(self)

    def compute(self):
        # Compute the value based on inputs and compute function
        for input_ in self.inputs:
            input_.compute()
        computed_value = self.compute_function([input_.value for input_ in self.inputs])
        # Update value if computed value differs
        if computed_value != self.value:
            self.value = computed_value

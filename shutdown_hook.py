import threading


class ShutdownHook:

    def __init__(self, shutdown_callback):
        self._shutdown_callback = shutdown_callback
        self._condition = threading.Condition()
        self._terminated = False
        self._shutdown_thread = threading.Thread(target=self.await_termination, name='shutdown-thread', daemon=True)

    def start(self):
        self._shutdown_thread.start()

    def await_termination(self):
        while not self._terminated:
            with self._condition:
                self._condition.wait()

        self._shutdown_callback()

    def shutdown(self):
        with self._condition:
            self._terminated = True
            self._condition.notify_all()

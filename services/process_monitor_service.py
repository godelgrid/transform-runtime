import logging
import threading
import time

logger = logging.getLogger(__name__)


class ProcessMonitorService:

    def __init__(self):
        self._last_health_check = time.time()
        self._health_lock = threading.Lock()
        self._terminated = False
        self._monitor_thread = threading.Thread(target=self.monitor_process, name='process-monitor-thread', daemon=True)

    def start(self, shutdown_hook):
        self._shutdown_hook = shutdown_hook
        self._monitor_thread.start()

    def update_health_check(self):
        with self._health_lock:
            self._last_health_check = time.time()

    def shutdown(self):
        self._terminated = True

    def await_shutdown(self, timeout):
        self._monitor_thread.join(timeout=timeout)

    def monitor_process(self):
        while not self._terminated:
            current_time = time.time()
            exit_runtime = False
            with self._health_lock:
                if current_time - self._last_health_check > 300:  # More than 5 minutes
                    # Process has been abandoned; shutdown now
                    exit_runtime = True
            if exit_runtime:
                logger.error(
                    'Shutting down transform runtime due to inactivity. Runtime has been possibly abandoned.')
                self._shutdown_hook.shutdown()
                break
            time.sleep(5)


PROCESS_MONITOR_SERVICE = ProcessMonitorService()

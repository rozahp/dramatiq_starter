import logging
import watchdog.events
import watchdog.observers

# project imports
from . import tasks

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    # Create a task for every created file in watch path
    def on_created(self, event):
        self.logger.debug("File created - % s." % event.src_path)
        #print("Watchdog received created event - % s." % event.src_path)

        # submitt a task with delay or not
        tasks.process_task.send_with_options(args=(str(event.src_path),), delay=5000)
        tasks.process_task.send(str(event.src_path))

    def on_modified(self, event):
        self.logger.debug("File modified - % s." % event.src_path)
        #print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now

# function for starting the Observer
def startObserver(src_path):
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    return observer

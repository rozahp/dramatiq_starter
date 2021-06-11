import dramatiq
from dramatiq.brokers.redis import RedisBroker
import logging
import time
import config

logger = logging.getLogger(__name__)

conf = config.Config()
redis_broker = RedisBroker(host=conf.REDIS_URL)#, middleware=[]) # middleware = [] to remove prometheus
dramatiq.set_broker(redis_broker)

# first task
@dramatiq.actor
def process_task(path):
    logger.debug("got the path: "+str(path))
    time.sleep(5) # sleep before processing file
    return None # no result backend


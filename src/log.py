import logging

def get_log(name):
    log = logging.getLogger(name)
    formatter = logging.Formatter("%(asctime)s| %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    log.setLevel(logging.INFO)
    return log
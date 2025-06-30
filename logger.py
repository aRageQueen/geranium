import logging

def get_logger(name="leak_fingerprint", logfile="log.txt"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
        logger.addHandler(ch)

        # File handler
        fh = logging.FileHandler(logfile)
        fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(fh)

        logger.setLevel(logging.INFO)
    return logger

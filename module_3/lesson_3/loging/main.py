import logging

logging.basicConfig(filename="test.logs", level=logging.NOTSET, format="%(levelname)s - %(message)s %(asctime)s")

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')

# Logger(info)
# Logger(debug)
# Logger(warning)
# Logger(error)
# Logger(critical)

base_log = ""
info_logger = logging.getLogger("info")
debug_logger = logging.getLogger("debug")
warning_logger = logging.getLogger("warning")
error_logger = logging.getLogger("error")
critical_logger = logging.getLogger("critical")
info_logger.setLevel(level=logging.INFO)
debug_logger.setLevel(level=1)
warning_logger.setLevel(level=1)
error_logger.setLevel(level=1)
critical_logger.setLevel(level=1)


# handlers
info_handler = logging.FileHandler(filename=base_log+'info.log')
debug_handler = logging.FileHandler(filename=base_log+'debug.log')
critical_logger = logging.FileHandler(filename=base_log+'critical.log')
warning_logger = logging.FileHandler(filename=base_log+'warning.log')
error_logger = logging.FileHandler(filename=base_log+'error.log')
info_handler.setLevel(level=logging.INFO)
debug_handler.setLevel(level=1)
warning_logger.setLevel(level=1)
error_logger.setLevel(level=1)
critical_logger.setLevel(level=1)



# formats
f1 = logging.Formatter("%(levelname)s-%(name)s-%(message)s-%(asctime)s")
f2 = logging.Formatter("%(levelname)s-%(name)s-%(message)s")
f3 = logging.Formatter("%(levelname)s-%(name)s-%(message)s")
f4 = logging.Formatter("%(levelname)s-%(name)s-%(message)s")
f5 = logging.Formatter("%(levelname)s-%(name)s-%(message)s")

info_handler.setFormatter(f1)
debug_handler.setFormatter(f2)
warning_logger.setFormatter(f3)
error_logger.setFormatter(f4)
critical_logger.setFormatter(f5)


info_logger.addHandler(info_handler)
debug_logger.addHandler(debug_handler)
warning_logger.addHandler(warning_logger)
error_logger.addHandler(error_logger)
critical_logger.addHandler(critical_logger)



info_logger.info("Success !")
debug_logger.debug("Debug success !")

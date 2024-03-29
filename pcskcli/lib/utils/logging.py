"""
Configures a logger
"""
import logging


class CliLogger:
    @staticmethod
    def configure_logger(logger, formatter, level):
        """
        Configure a Logger with the formatter provided.
        Parameters
        ----------
        logger logging.getLogger
            Logger to configure
        formatter logging.formatter
            Formatter for the logger
        Returns
        -------
        None
        """
        log_stream_handler = logging.StreamHandler()
        log_stream_handler.setLevel(logging.DEBUG)
        log_stream_handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.propagate = False
        logger.addHandler(log_stream_handler)

    @staticmethod
    def configure_null_logger(logger):
        """
        Configure a Logger with a NullHandler
        Useful for libraries that do not follow: https://docs.python.org/3.6/howto/logging.html#configuring-logging-for-a-library
        Parameters
        ----------
        logger logging.getLogger
            Logger to configure
        Returns
        -------
        None
        """
        logger.propagate = False
        logger.addHandler(logging.NullHandler())
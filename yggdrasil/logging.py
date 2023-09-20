def add_log_level_arg(parser):
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Set the log level, options: DEBUG, INFO, WARNING, ERROR, CRITICAL; default: INFO",
    )
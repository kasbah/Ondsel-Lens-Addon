LOG_PREFIX = "(log)"

class MockConsole:
    @staticmethod
    def PrintLog(arg: str) -> None:
        print(LOG_PREFIX, arg)

    @staticmethod
    def PrintMessage(arg: str) -> None:
        print(LOG_PREFIX, arg)

    @staticmethod
    def PrintWarning(arg: str) -> None:
        print(LOG_PREFIX, arg)

    @staticmethod
    def PrintError(arg: str) -> None:
        print(LOG_PREFIX, arg)

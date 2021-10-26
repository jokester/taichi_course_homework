import logging, sys
from typing import List, Union
import datetime

def create_logger(src) -> logging.Logger:

    formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    screen_handler = logging.StreamHandler(stream=sys.stderr)
    screen_handler.setFormatter(formatter)

    logger = logging.Logger(name=src, level=logging.DEBUG)
    logger.addHandler(screen_handler)
    return logger

logging.getLogger().setLevel(logging.DEBUG)

class FpsMeter():
    def __init__(self, identifier: str, numFrames = 30) -> None:
        self._identifier = identifier
        self._timestamps = List[float]()
        self._numFrames = numFrames
        self._logger = create_logger(identifier)

        self.shouldBeReporting = False

    async def startReport(self)-> None:
        self.shouldBeReporting = True
        while self.shouldBeReporting:
            fps = self.fps()
            if fps is not None:
                self._logger("Stream(%s) fps=%f"%(self._identifier, fps))


    async def stopReport(self) -> None:
        self.shouldBeReporting = False

    def onFrame(self) -> None:
        self._timestamps.append( datetime.datetime.utcnow().timestamp() )
        if len(self._timestamps) > self._numFrames:
            self._timestamps = self._timestamps[1:]
        
    def fps(self) -> Union[float, None]:
        if len(self._timestamps) == self._numFrames:
            return self._numFrames / float(self._timestamps[0] - self._timestamps[self._numFrames-1])
        return None


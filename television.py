class Television:
    """
    A class for the functionality of a TV remote.
    Global variables for minimum and maximum volume, and the minimum and
    maximum channel.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method for setting the default values for the private status,
        muted, channel, and volume variables.
        """
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Method for turning the TV on and off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method for muting and unmuting the TV.
        """
        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase TV channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease TV channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


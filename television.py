class Television:
    """
    Sets the minimum and maximum range for volume
    Sets the minimum and maximum number of channels
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__ (self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns the power on and off
        """
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self):
        """
        Mutes and unmutes the television
        """
        if self.status == False:
            return
        elif self.muted == False:
            self.muted = True
        else:
            self.muted = False

    def channel_up(self):
        """
        Changes to the next channel
        If it is already the last channel, goes back to the first channel
        """
        if self.status == False:
            return
        elif self.channel == Television.MAX_CHANNEL:
            self.channel = Television.MIN_CHANNEL
        else:
            self.channel += 1

    def channel_down(self):
        """
        Changes to the previous channel
        If it is already the first channel, goes to the last channel"
        """
        if self.status == False:
            return
        elif self.channel == Television.MIN_CHANNEL:
            self.channel = Television.MAX_CHANNEL
        else:
            self.channel -= 1

    def volume_up(self):
        """
        Increases the volume unless it is already at a maximum
        Unmutes if TV is muted
        """
        if self.status == False:
            return
        elif self.muted == True:
            self.muted = False
            if self.volume == Television.MAX_VOLUME:
                return
            else:
                self.volume += 1
        else:
            if self.volume == Television.MAX_VOLUME:
                return
            else:
                self.volume += 1

    def volume_down(self):
        """
        Decreases the volume unless it is already at the minimum
        Unmutes if muted
        """
        if self.status == False:
            return
        elif self.muted == True:
            self.muted = False
            if self.volume == Television.MIN_VOLUME:
                return
            else:
                self.volume -= 1
        else:
            if self.volume == Television.MIN_VOLUME:
                return
            else:
                self.volume -= 1

    def __str__(self):
        """
        Returns status of television: Power (on or off), channel number and volume
        """
        if self.muted == True:
            return f'Power = [{self.status}], Channel = [{self.channel}], Volume = [0]'

        return f'Power = [{self.status}], Channel = [{self.channel}], Volume = [{self.volume}]'
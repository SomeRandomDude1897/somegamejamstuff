class Animation:
    def __init__(self, frames):
        self.frames = frames
        self.current_frame = 0
    def MoveFrame(self):
        self.current_frame += 1
        if self.current_frame == len(self.frames):
            self.current_frame = 0
    def GetFrame(self):
        return self.frames[self.current_frame]
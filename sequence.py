class Sequence:
    # waves_dir = f""
    # waves = []
    # audio = 
    patterns = []
    name = ""
    length_bars = 0
    length_time = 0
    BPM = 140

    def set_time():
        length_time = (60 * 4 * length_bars) / BPM
        
    # def set_bars():
        # length_bars = ()
        # pass

    def set_bars():
        length_bars = 0
        for pattern in patterns:
            length_bars += pattern.length_bars
            
    
    def __init__(self, patterns, name, BPM):
        # self.waves_dir = waves_dir
        self.patterns = patterns
        self.name = name
        self.BPM = BPM
        set_time()
        set_bars()

    def __init__(self):
        self = self

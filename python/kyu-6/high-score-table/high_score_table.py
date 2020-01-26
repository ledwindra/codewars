class HighScoreTable:
    
    def __init__(self, limit_size):
        self.limit_size = limit_size
        self.scores = []
    
    def update(self, value):

        self.scores.append(value)

        if len(self.scores) > self.limit_size:
            self.scores.remove(min(self.scores))

        return self.scores.sort(reverse=True)

    def reset(self):
        
        return self.scores.clear()
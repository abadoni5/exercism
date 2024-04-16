"""
Scale Generator - This class, Scale, is designed to generate musical scales based on a given tonic note.
It utilizes a chromatic scale with both sharp and flat keys. The chromatic method
returns a list of notes in the scale based on the given intervals. The intervals are
specified as a string where 'm' stands for minor, 'M' for major, and 'A' for augmented.
The get_scale method generates the appropriate scale based on the key signature, 
which can be either sharp or flat, and the get_keysig method determines the key 
signature based on the tonic note provided.
"""
 
class Scale:
    NOTES = ["A", "AB", "B", "C", "CD", "D", "DE", "E", "F", "FG", "G", "GA"]
    SEL_SHARP = ["C", "a", "G", "D", "A", "E", "B", "e", "b"]
    
    def __init__(self, tonic):
        self.tonic = tonic
 
    def chromatic(self):
        return self.interval()
 
    def interval(self, intervals="".join(["m" for note in NOTES[:-1]])):
        scale = self.get_scale(self.get_keysig())
        result = []
        result.append(self.tonic.capitalize())
        index = scale.index(self.tonic.capitalize())
        for interval in intervals:
            if interval == "m":
                index += 1
            if interval == "M":
                index += 2
            if interval == "A":
                index += 3
            index = index%len(scale)
            result.append(scale[index])
        return result
 
    def get_scale(self, keysig):
        scale = []
        for note in self.NOTES:
            if len(note) == 1:
                scale.append(note)
            elif keysig == "Flat":
                scale.append("".join([note[1], "b"]))
            else:
                scale.append("".join([note[0], "#"]))
        return scale
 
    def get_keysig(self):
        if self.tonic in self.SEL_SHARP or self.tonic[-1] == "#":
            return "Sharp"
        return "Flat"
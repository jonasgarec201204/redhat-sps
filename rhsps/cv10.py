class ReverseString:
    def __init__(self, string):
        self.string = string;
    def reverse(self):
        final_string = ""
        for i in range(1, len(self.string)+1):
            final_string += self.string[-i]
        return final_string

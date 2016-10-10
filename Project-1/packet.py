class packet():
    def __init__(self, data, generated_at, sent_at,
                 pushed_out_at, bit_length):
        self.data = data
        self.generated_at = generated_at
        self.sent_at = sent_at
        self.pushed_out_at = pushed_out_at
        self.bit_length = bit_length

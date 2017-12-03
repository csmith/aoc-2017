import math
with open('data/03.txt', 'r') as file:
    square = int(file.readline().strip())
    # The maximum number in each ring in the spiral is 1, 9, 25, 49, 81, etc
    ring = math.ceil((math.sqrt(square)+1)/2.)
    # Calculate the numbers at the cardinal points (N/E/S/W) for that ring
    cardinals = [4*ring**2 - 11*ring + 8, 4*ring**2 - 9*ring + 6, 4*ring**2 - 7*ring + 4, 4*ring**2 - 5*ring + 2]
    # Distance "around" is the smallest difference between the input and one of the cardinals
    around = min(abs(c - square) for c in cardinals)
    # Plus the distance "inwards" is ring - 1
    print(f'Part one: {around+ring-1}')

    # There's no sensible way to calculate part two, and I can't be bothered writing
    # something to generate the sequence after I spent so much time avoiding doing that
    # for part one, so ¯\_(ツ)_/¯
    print('Part two: See table at https://oeis.org/A141481')

    # Bits of working:

    # Ring --> Max
    # 1         1
    # 2         9
    # 3         25
    # 4         49
    # n         (n+(n-1))^2  ==> (2n-1)^2

    # m = (2n-1)^2
    # sqrt(m) = 2n-1
    # (sqrt(m)+1)/2 = n

    # https://oeis.org/A054552
    # 197 196 195 194 193 192 191 190 189 188 187 186 185 184 183
    # 198 145 144 143 142 141 140 139 138 137 136 135 134 133 182
    # 199 146 101 100  99  98  97  96  95  94  93  92  91 132 181
    # 200 147 102  65  64  63  62  61  60  59  58  57  90 131 180
    # 201 148 103  66  37  36  35  34  33  32  31  56  89 130 179
    # 202 149 104  67  38  17  16  15  14  13  30  55  88 129 178
    # 203 150 105  68  39  18   5   4   3  12  29  54  87 128 177
    # 204 151 106  69  40  19   6   1   2  11  28  53  86 127 176
    # 205 152 107  70  41  20   7   8   9  10  27  52  85 126 175
    # 206 153 108  71  42  21  22  23  24  25  26  51  84 125 174
    # 207 154 109  72  43  44  45  46  47  48  49  50  83 124 173
    # 208 155 110  73  74  75  76  77  78  79  80  81  82 123 172
    # 209 156 111 112 113 114 115 116 117 118 119 120 121 122 171
    # 210 157 158 159 160 161 162 163 164 165 166 167 168 169 170
    # 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225

    # Ring --> Key points
    # 1         1, 1, 1, 1
    # 2         2, 4, 6, 8
    # 3         11, 15, 19, 23
    # 4         28, 34, 40, 46

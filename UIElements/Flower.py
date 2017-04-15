class Flower:

    line_front = range(8, 19) + range(113, 163)
    line_back = range(513, 583)[::-1]
    
    leaf_right_front = range(90, 112)[::-1]
    leaf_right_back = range(66, 91)
    leaf_left_front = range(19, 39)
    leaf_left_back = range(38, 63)[::-1]
    
    seeds = range(463, 513)

    l1 = range(163, 190)
    l2 = range(193, 221)
    l3 = range(222, 251)
    l4 = range(251, 280)
    l5 = range(281, 310)
    l6 = range(312, 341)
    l7 = range(342, 370)
    l8 = range(370, 401)
    l9 = range(402, 432)
    l10 = range(432, 462)

    bottom_to_top_cols = [[234, 235, 236, 237, 238, 264, 265, 266, 233, 239, 263, 267, 206, 207, 208, 209, 232, 240, 241, 262, 268, 205, 210, 231, 242, 261, 269, 204, 211, 212, 230, 243, 260, 270, 203, 213, 214, 229, 244, 259, 271, 272, 202, 215, 228, 245, 258, 273, 201, 216, 217, 227, 246, 257, 274, 292],
                        [199, 200, 218, 226, 247, 256, 275, 276, 291, 293, 180, 181, 182, 198, 219, 225, 248, 249, 255, 277, 289, 290, 294, 178, 179, 183, 184, 185, 197, 220, 224, 250, 254, 278, 279, 288, 295, 177, 186, 196, 221, 223, 251, 253, 280, 287, 296, 176, 187, 188, 195, 285, 286, 297, 173, 174, 175, 189, 190, 194, 282, 283, 284, 298, 299, 300, 468, 481, 490, 170, 171, 172, 191, 193, 301, 302, 303, 304, 467, 488, 492, 512],
                        [167, 168, 169, 305, 306, 307, 308, 487, 491, 497, 506, 163, 164, 165, 166, 309, 310, 311, 453, 454, 455, 476, 477, 502, 505, 449, 450, 451, 452, 456, 457, 464, 480, 489, 499, 500, 448, 458, 459, 460, 461, 469, 474, 484, 496, 510, 313, 314, 315, 316, 317, 447, 465, 466, 493, 318, 319, 320, 321, 322, 323, 446, 494, 495, 503, 507, 324, 445, 475, 478, 479, 483, 486, 511, 325, 340, 434, 435, 436, 444, 473, 504],
                        [326, 339, 437, 438, 439, 440, 441, 442, 443, 470, 471, 472, 482, 498, 508, 327, 328, 329, 330, 331, 336, 337, 338, 342, 431, 485, 501, 509, 332, 333, 334, 335, 343, 370, 372, 402, 429, 430, 344, 369, 373, 400, 403, 427, 428, 345, 367, 368, 374, 399, 404, 426, 346, 364, 365, 366, 375, 398, 405, 425, 347, 363, 376, 396, 397, 406, 424, 348, 360, 361, 362, 377, 378, 395, 407, 423],
                        [349, 359, 379, 394, 408, 409, 422, 350, 357, 358, 380, 393, 410, 421, 351, 356, 381, 392, 411, 412, 420, 352, 353, 354, 355, 382, 391, 413, 419, 383, 390, 414, 417, 418, 384, 389, 415, 416, 385, 386, 387, 388]]


    def __init__(self):
        self.clear()

    def get_array(self):
        return self.arr

    def get_leaves(self):
        return self.l1 + self.l2 + self.l3 + self.l4 + self.l5 + self.l6 + self.l7 + self.l8 + self.l9 + self.l10

    def get_leaves_array(self):
        return [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10]

    def get_seeds(self):
        return range(463, 513)

    def get_all_indexes(self):
        return self.get_leaves() + self.get_seeds()

    def clear(self):
        self.arr = [0, 0, 0] * 583

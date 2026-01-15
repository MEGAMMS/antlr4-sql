# Generated from grammar/SQLParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,120,600,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,1,5,1,91,8,1,10,1,
        12,1,94,9,1,1,2,1,2,3,2,98,8,2,4,2,100,8,2,11,2,12,2,101,1,2,3,2,
        105,8,2,1,2,3,2,108,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,117,8,3,
        1,4,1,4,1,4,1,4,3,4,123,8,4,1,5,1,5,1,5,1,5,3,5,129,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,141,8,7,10,7,12,7,144,9,7,1,
        8,1,8,1,8,5,8,149,8,8,10,8,12,8,152,9,8,1,9,1,9,1,9,1,9,3,9,158,
        8,9,1,9,1,9,3,9,162,8,9,1,9,3,9,165,8,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,180,8,10,3,10,182,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,204,8,11,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,14,3,14,214,8,14,1,14,1,14,3,14,218,8,14,
        1,14,1,14,3,14,222,8,14,1,14,1,14,1,14,1,14,5,14,228,8,14,10,14,
        12,14,231,9,14,1,14,1,14,3,14,235,8,14,1,14,1,14,1,14,3,14,240,8,
        14,1,14,1,14,3,14,244,8,14,3,14,246,8,14,1,14,1,14,1,14,3,14,251,
        8,14,1,15,1,15,1,15,1,15,5,15,257,8,15,10,15,12,15,260,9,15,3,15,
        262,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,
        274,8,16,1,16,3,16,277,8,16,3,16,279,8,16,1,17,1,17,3,17,283,8,17,
        1,17,3,17,286,8,17,1,17,1,17,1,17,1,17,3,17,292,8,17,1,17,3,17,295,
        8,17,3,17,297,8,17,1,18,3,18,300,8,18,1,18,3,18,303,8,18,1,18,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,313,8,19,10,19,12,19,316,9,
        19,1,20,1,20,3,20,320,8,20,1,20,1,20,1,20,3,20,325,8,20,5,20,327,
        8,20,10,20,12,20,330,9,20,1,21,1,21,3,21,334,8,21,1,21,1,21,1,21,
        1,21,1,21,3,21,341,8,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,349,8,
        21,1,22,1,22,1,22,5,22,354,8,22,10,22,12,22,357,9,22,1,23,1,23,1,
        23,5,23,362,8,23,10,23,12,23,365,9,23,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,373,8,24,1,25,1,25,1,25,5,25,378,8,25,10,25,12,25,381,9,
        25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,391,8,26,1,27,1,
        27,3,27,395,8,27,1,27,1,27,1,27,3,27,400,8,27,1,28,1,28,1,28,1,29,
        1,29,1,29,5,29,408,8,29,10,29,12,29,411,9,29,1,30,1,30,3,30,415,
        8,30,1,30,1,30,1,30,3,30,420,8,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,3,32,431,8,32,5,32,433,8,32,10,32,12,32,436,9,32,
        1,32,1,32,1,32,1,32,1,32,1,32,3,32,444,8,32,5,32,446,8,32,10,32,
        12,32,449,9,32,1,32,1,32,1,32,1,32,1,32,3,32,456,8,32,5,32,458,8,
        32,10,32,12,32,461,9,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,469,8,
        32,3,32,471,8,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,3,34,480,8,34,
        1,34,1,34,3,34,484,8,34,1,34,1,34,1,34,5,34,489,8,34,10,34,12,34,
        492,9,34,3,34,494,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,4,36,521,8,36,11,36,12,36,522,1,36,1,36,3,36,527,
        8,36,1,36,1,36,1,36,1,36,3,36,533,8,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,3,36,559,8,36,1,36,1,36,1,36,1,36,
        3,36,565,8,36,1,36,1,36,5,36,569,8,36,10,36,12,36,572,9,36,1,37,
        1,37,1,37,3,37,577,8,37,1,37,1,37,1,38,1,38,1,38,3,38,584,8,38,1,
        39,1,39,1,39,5,39,589,8,39,10,39,12,39,592,9,39,1,40,1,40,1,41,1,
        41,1,42,1,42,1,42,0,1,72,43,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,0,12,2,0,18,18,25,26,2,0,67,71,77,77,2,0,29,
        30,61,63,1,0,36,37,1,0,67,70,1,0,82,84,1,0,80,81,2,0,72,74,77,79,
        1,0,6,7,2,0,115,116,118,118,4,0,38,38,94,96,98,98,106,107,1,0,112,
        113,658,0,86,1,0,0,0,2,92,1,0,0,0,4,107,1,0,0,0,6,116,1,0,0,0,8,
        122,1,0,0,0,10,128,1,0,0,0,12,130,1,0,0,0,14,137,1,0,0,0,16,145,
        1,0,0,0,18,153,1,0,0,0,20,181,1,0,0,0,22,203,1,0,0,0,24,205,1,0,
        0,0,26,209,1,0,0,0,28,213,1,0,0,0,30,261,1,0,0,0,32,278,1,0,0,0,
        34,296,1,0,0,0,36,299,1,0,0,0,38,309,1,0,0,0,40,317,1,0,0,0,42,331,
        1,0,0,0,44,350,1,0,0,0,46,358,1,0,0,0,48,366,1,0,0,0,50,374,1,0,
        0,0,52,390,1,0,0,0,54,392,1,0,0,0,56,401,1,0,0,0,58,404,1,0,0,0,
        60,412,1,0,0,0,62,421,1,0,0,0,64,470,1,0,0,0,66,472,1,0,0,0,68,475,
        1,0,0,0,70,495,1,0,0,0,72,532,1,0,0,0,74,573,1,0,0,0,76,583,1,0,
        0,0,78,585,1,0,0,0,80,593,1,0,0,0,82,595,1,0,0,0,84,597,1,0,0,0,
        86,87,3,2,1,0,87,88,5,0,0,1,88,1,1,0,0,0,89,91,3,4,2,0,90,89,1,0,
        0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,3,1,0,0,0,94,92,
        1,0,0,0,95,97,3,6,3,0,96,98,5,91,0,0,97,96,1,0,0,0,97,98,1,0,0,0,
        98,100,1,0,0,0,99,95,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,104,1,0,0,0,103,105,5,2,0,0,104,103,1,0,0,0,104,
        105,1,0,0,0,105,108,1,0,0,0,106,108,5,2,0,0,107,99,1,0,0,0,107,106,
        1,0,0,0,108,5,1,0,0,0,109,117,3,8,4,0,110,117,3,10,5,0,111,117,3,
        64,32,0,112,117,3,66,33,0,113,117,3,56,28,0,114,117,3,62,31,0,115,
        117,3,68,34,0,116,109,1,0,0,0,116,110,1,0,0,0,116,111,1,0,0,0,116,
        112,1,0,0,0,116,113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,
        7,1,0,0,0,118,123,3,12,6,0,119,123,3,22,11,0,120,123,3,24,12,0,121,
        123,3,26,13,0,122,118,1,0,0,0,122,119,1,0,0,0,122,120,1,0,0,0,122,
        121,1,0,0,0,123,9,1,0,0,0,124,129,3,28,14,0,125,129,3,42,21,0,126,
        129,3,48,24,0,127,129,3,54,27,0,128,124,1,0,0,0,128,125,1,0,0,0,
        128,126,1,0,0,0,128,127,1,0,0,0,129,11,1,0,0,0,130,131,5,17,0,0,
        131,132,5,18,0,0,132,133,3,78,39,0,133,134,5,92,0,0,134,135,3,14,
        7,0,135,136,5,93,0,0,136,13,1,0,0,0,137,142,3,16,8,0,138,139,5,89,
        0,0,139,141,3,16,8,0,140,138,1,0,0,0,141,144,1,0,0,0,142,140,1,0,
        0,0,142,143,1,0,0,0,143,15,1,0,0,0,144,142,1,0,0,0,145,146,3,80,
        40,0,146,150,3,18,9,0,147,149,3,20,10,0,148,147,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,17,1,0,0,0,152,150,1,
        0,0,0,153,164,3,80,40,0,154,157,5,92,0,0,155,158,5,95,0,0,156,158,
        3,80,40,0,157,155,1,0,0,0,157,156,1,0,0,0,158,161,1,0,0,0,159,160,
        5,89,0,0,160,162,5,95,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,163,
        1,0,0,0,163,165,5,93,0,0,164,154,1,0,0,0,164,165,1,0,0,0,165,19,
        1,0,0,0,166,167,5,8,0,0,167,182,5,38,0,0,168,182,5,38,0,0,169,170,
        5,21,0,0,170,182,5,22,0,0,171,172,5,54,0,0,172,182,3,72,36,0,173,
        179,5,55,0,0,174,175,5,92,0,0,175,176,5,95,0,0,176,177,5,89,0,0,
        177,178,5,95,0,0,178,180,5,93,0,0,179,174,1,0,0,0,179,180,1,0,0,
        0,180,182,1,0,0,0,181,166,1,0,0,0,181,168,1,0,0,0,181,169,1,0,0,
        0,181,171,1,0,0,0,181,173,1,0,0,0,182,21,1,0,0,0,183,184,5,19,0,
        0,184,185,5,18,0,0,185,186,3,78,39,0,186,187,5,23,0,0,187,188,3,
        16,8,0,188,204,1,0,0,0,189,190,5,19,0,0,190,191,5,18,0,0,191,192,
        3,78,39,0,192,193,5,20,0,0,193,194,5,24,0,0,194,195,3,80,40,0,195,
        204,1,0,0,0,196,197,5,19,0,0,197,198,5,18,0,0,198,199,3,78,39,0,
        199,200,5,19,0,0,200,201,5,24,0,0,201,202,3,16,8,0,202,204,1,0,0,
        0,203,183,1,0,0,0,203,189,1,0,0,0,203,196,1,0,0,0,204,23,1,0,0,0,
        205,206,5,20,0,0,206,207,7,0,0,0,207,208,3,78,39,0,208,25,1,0,0,
        0,209,210,5,27,0,0,210,211,3,80,40,0,211,27,1,0,0,0,212,214,3,70,
        35,0,213,212,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,217,5,3,
        0,0,216,218,5,10,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,221,1,0,
        0,0,219,220,5,56,0,0,220,222,5,95,0,0,221,219,1,0,0,0,221,222,1,
        0,0,0,222,223,1,0,0,0,223,245,3,30,15,0,224,225,5,4,0,0,225,229,
        3,34,17,0,226,228,3,36,18,0,227,226,1,0,0,0,228,231,1,0,0,0,229,
        227,1,0,0,0,229,230,1,0,0,0,230,234,1,0,0,0,231,229,1,0,0,0,232,
        233,5,5,0,0,233,235,3,72,36,0,234,232,1,0,0,0,234,235,1,0,0,0,235,
        239,1,0,0,0,236,237,5,32,0,0,237,238,5,33,0,0,238,240,3,38,19,0,
        239,236,1,0,0,0,239,240,1,0,0,0,240,243,1,0,0,0,241,242,5,34,0,0,
        242,244,3,72,36,0,243,241,1,0,0,0,243,244,1,0,0,0,244,246,1,0,0,
        0,245,224,1,0,0,0,245,246,1,0,0,0,246,250,1,0,0,0,247,248,5,35,0,
        0,248,249,5,33,0,0,249,251,3,40,20,0,250,247,1,0,0,0,250,251,1,0,
        0,0,251,29,1,0,0,0,252,262,5,82,0,0,253,258,3,32,16,0,254,255,5,
        89,0,0,255,257,3,32,16,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,
        1,0,0,0,258,259,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,261,252,
        1,0,0,0,261,253,1,0,0,0,262,31,1,0,0,0,263,264,3,84,42,0,264,265,
        7,1,0,0,265,266,3,72,36,0,266,279,1,0,0,0,267,268,3,80,40,0,268,
        269,5,77,0,0,269,270,3,72,36,0,270,279,1,0,0,0,271,276,3,72,36,0,
        272,274,5,9,0,0,273,272,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,
        275,277,3,80,40,0,276,273,1,0,0,0,276,277,1,0,0,0,277,279,1,0,0,
        0,278,263,1,0,0,0,278,267,1,0,0,0,278,271,1,0,0,0,279,33,1,0,0,0,
        280,285,3,78,39,0,281,283,5,9,0,0,282,281,1,0,0,0,282,283,1,0,0,
        0,283,284,1,0,0,0,284,286,3,80,40,0,285,282,1,0,0,0,285,286,1,0,
        0,0,286,297,1,0,0,0,287,288,5,92,0,0,288,289,3,28,14,0,289,294,5,
        93,0,0,290,292,5,9,0,0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,1,
        0,0,0,293,295,3,80,40,0,294,291,1,0,0,0,294,295,1,0,0,0,295,297,
        1,0,0,0,296,280,1,0,0,0,296,287,1,0,0,0,297,35,1,0,0,0,298,300,7,
        2,0,0,299,298,1,0,0,0,299,300,1,0,0,0,300,302,1,0,0,0,301,303,5,
        64,0,0,302,301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,5,
        28,0,0,305,306,3,34,17,0,306,307,5,31,0,0,307,308,3,72,36,0,308,
        37,1,0,0,0,309,314,3,72,36,0,310,311,5,89,0,0,311,313,3,72,36,0,
        312,310,1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,
        315,39,1,0,0,0,316,314,1,0,0,0,317,319,3,72,36,0,318,320,7,3,0,0,
        319,318,1,0,0,0,319,320,1,0,0,0,320,328,1,0,0,0,321,322,5,89,0,0,
        322,324,3,72,36,0,323,325,7,3,0,0,324,323,1,0,0,0,324,325,1,0,0,
        0,325,327,1,0,0,0,326,321,1,0,0,0,327,330,1,0,0,0,328,326,1,0,0,
        0,328,329,1,0,0,0,329,41,1,0,0,0,330,328,1,0,0,0,331,333,5,11,0,
        0,332,334,5,12,0,0,333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,
        0,335,340,3,78,39,0,336,337,5,92,0,0,337,338,3,44,22,0,338,339,5,
        93,0,0,339,341,1,0,0,0,340,336,1,0,0,0,340,341,1,0,0,0,341,348,1,
        0,0,0,342,343,5,13,0,0,343,344,5,92,0,0,344,345,3,46,23,0,345,346,
        5,93,0,0,346,349,1,0,0,0,347,349,3,28,14,0,348,342,1,0,0,0,348,347,
        1,0,0,0,349,43,1,0,0,0,350,355,3,80,40,0,351,352,5,89,0,0,352,354,
        3,80,40,0,353,351,1,0,0,0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,
        1,0,0,0,356,45,1,0,0,0,357,355,1,0,0,0,358,363,3,72,36,0,359,360,
        5,89,0,0,360,362,3,72,36,0,361,359,1,0,0,0,362,365,1,0,0,0,363,361,
        1,0,0,0,363,364,1,0,0,0,364,47,1,0,0,0,365,363,1,0,0,0,366,367,5,
        14,0,0,367,368,3,78,39,0,368,369,5,15,0,0,369,372,3,50,25,0,370,
        371,5,5,0,0,371,373,3,72,36,0,372,370,1,0,0,0,372,373,1,0,0,0,373,
        49,1,0,0,0,374,379,3,52,26,0,375,376,5,89,0,0,376,378,3,52,26,0,
        377,375,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,380,1,0,0,0,
        380,51,1,0,0,0,381,379,1,0,0,0,382,383,3,80,40,0,383,384,5,77,0,
        0,384,385,3,72,36,0,385,391,1,0,0,0,386,387,3,80,40,0,387,388,7,
        4,0,0,388,389,3,72,36,0,389,391,1,0,0,0,390,382,1,0,0,0,390,386,
        1,0,0,0,391,53,1,0,0,0,392,394,5,16,0,0,393,395,5,4,0,0,394,393,
        1,0,0,0,394,395,1,0,0,0,395,396,1,0,0,0,396,399,3,78,39,0,397,398,
        5,5,0,0,398,400,3,72,36,0,399,397,1,0,0,0,399,400,1,0,0,0,400,55,
        1,0,0,0,401,402,5,1,0,0,402,403,3,58,29,0,403,57,1,0,0,0,404,409,
        3,60,30,0,405,406,5,89,0,0,406,408,3,60,30,0,407,405,1,0,0,0,408,
        411,1,0,0,0,409,407,1,0,0,0,409,410,1,0,0,0,410,59,1,0,0,0,411,409,
        1,0,0,0,412,414,5,113,0,0,413,415,5,9,0,0,414,413,1,0,0,0,414,415,
        1,0,0,0,415,416,1,0,0,0,416,419,3,18,9,0,417,418,5,77,0,0,418,420,
        3,72,36,0,419,417,1,0,0,0,419,420,1,0,0,0,420,61,1,0,0,0,421,422,
        5,15,0,0,422,423,3,84,42,0,423,424,7,1,0,0,424,425,3,72,36,0,425,
        63,1,0,0,0,426,427,5,41,0,0,427,434,5,50,0,0,428,430,3,6,3,0,429,
        431,5,91,0,0,430,429,1,0,0,0,430,431,1,0,0,0,431,433,1,0,0,0,432,
        428,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,435,
        437,1,0,0,0,436,434,1,0,0,0,437,438,5,42,0,0,438,439,5,50,0,0,439,
        440,5,41,0,0,440,447,5,51,0,0,441,443,3,6,3,0,442,444,5,91,0,0,443,
        442,1,0,0,0,443,444,1,0,0,0,444,446,1,0,0,0,445,441,1,0,0,0,446,
        449,1,0,0,0,447,445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,449,
        447,1,0,0,0,450,451,5,42,0,0,451,471,5,51,0,0,452,459,5,41,0,0,453,
        455,3,6,3,0,454,456,5,91,0,0,455,454,1,0,0,0,455,456,1,0,0,0,456,
        458,1,0,0,0,457,453,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,
        460,1,0,0,0,460,462,1,0,0,0,461,459,1,0,0,0,462,471,5,42,0,0,463,
        464,5,49,0,0,464,465,3,72,36,0,465,468,3,6,3,0,466,467,5,46,0,0,
        467,469,3,6,3,0,468,466,1,0,0,0,468,469,1,0,0,0,469,471,1,0,0,0,
        470,426,1,0,0,0,470,452,1,0,0,0,470,463,1,0,0,0,471,65,1,0,0,0,472,
        473,5,53,0,0,473,474,3,72,36,0,474,67,1,0,0,0,475,479,5,52,0,0,476,
        477,3,84,42,0,477,478,5,77,0,0,478,480,1,0,0,0,479,476,1,0,0,0,479,
        480,1,0,0,0,480,483,1,0,0,0,481,484,3,78,39,0,482,484,3,84,42,0,
        483,481,1,0,0,0,483,482,1,0,0,0,484,493,1,0,0,0,485,490,3,72,36,
        0,486,487,5,89,0,0,487,489,3,72,36,0,488,486,1,0,0,0,489,492,1,0,
        0,0,490,488,1,0,0,0,490,491,1,0,0,0,491,494,1,0,0,0,492,490,1,0,
        0,0,493,485,1,0,0,0,493,494,1,0,0,0,494,69,1,0,0,0,495,496,5,58,
        0,0,496,497,3,80,40,0,497,498,5,9,0,0,498,499,5,92,0,0,499,500,3,
        28,14,0,500,501,5,93,0,0,501,71,1,0,0,0,502,503,6,36,-1,0,503,504,
        5,92,0,0,504,505,3,72,36,0,505,506,5,93,0,0,506,533,1,0,0,0,507,
        508,5,8,0,0,508,533,3,72,36,13,509,510,5,47,0,0,510,511,5,92,0,0,
        511,512,3,28,14,0,512,513,5,93,0,0,513,533,1,0,0,0,514,520,5,43,
        0,0,515,516,5,44,0,0,516,517,3,72,36,0,517,518,5,45,0,0,518,519,
        3,72,36,0,519,521,1,0,0,0,520,515,1,0,0,0,521,522,1,0,0,0,522,520,
        1,0,0,0,522,523,1,0,0,0,523,526,1,0,0,0,524,525,5,46,0,0,525,527,
        3,72,36,0,526,524,1,0,0,0,526,527,1,0,0,0,527,528,1,0,0,0,528,529,
        5,42,0,0,529,533,1,0,0,0,530,533,3,74,37,0,531,533,3,76,38,0,532,
        502,1,0,0,0,532,507,1,0,0,0,532,509,1,0,0,0,532,514,1,0,0,0,532,
        530,1,0,0,0,532,531,1,0,0,0,533,570,1,0,0,0,534,535,10,12,0,0,535,
        536,7,5,0,0,536,569,3,72,36,13,537,538,10,11,0,0,538,539,7,6,0,0,
        539,569,3,72,36,12,540,541,10,10,0,0,541,542,7,7,0,0,542,569,3,72,
        36,11,543,544,10,9,0,0,544,545,5,66,0,0,545,569,3,72,36,10,546,547,
        10,8,0,0,547,548,7,8,0,0,548,569,3,72,36,9,549,550,10,7,0,0,550,
        551,5,39,0,0,551,569,5,38,0,0,552,553,10,6,0,0,553,554,5,39,0,0,
        554,555,5,8,0,0,555,569,5,38,0,0,556,558,10,5,0,0,557,559,5,8,0,
        0,558,557,1,0,0,0,558,559,1,0,0,0,559,560,1,0,0,0,560,561,5,48,0,
        0,561,564,5,92,0,0,562,565,3,46,23,0,563,565,3,28,14,0,564,562,1,
        0,0,0,564,563,1,0,0,0,565,566,1,0,0,0,566,567,5,93,0,0,567,569,1,
        0,0,0,568,534,1,0,0,0,568,537,1,0,0,0,568,540,1,0,0,0,568,543,1,
        0,0,0,568,546,1,0,0,0,568,549,1,0,0,0,568,552,1,0,0,0,568,556,1,
        0,0,0,569,572,1,0,0,0,570,568,1,0,0,0,570,571,1,0,0,0,571,73,1,0,
        0,0,572,570,1,0,0,0,573,574,3,80,40,0,574,576,5,92,0,0,575,577,3,
        46,23,0,576,575,1,0,0,0,576,577,1,0,0,0,577,578,1,0,0,0,578,579,
        5,93,0,0,579,75,1,0,0,0,580,584,3,78,39,0,581,584,3,82,41,0,582,
        584,3,84,42,0,583,580,1,0,0,0,583,581,1,0,0,0,583,582,1,0,0,0,584,
        77,1,0,0,0,585,590,3,80,40,0,586,587,5,90,0,0,587,589,3,80,40,0,
        588,586,1,0,0,0,589,592,1,0,0,0,590,588,1,0,0,0,590,591,1,0,0,0,
        591,79,1,0,0,0,592,590,1,0,0,0,593,594,7,9,0,0,594,81,1,0,0,0,595,
        596,7,10,0,0,596,83,1,0,0,0,597,598,7,11,0,0,598,85,1,0,0,0,76,92,
        97,101,104,107,116,122,128,142,150,157,161,164,179,181,203,213,217,
        221,229,234,239,243,245,250,258,261,273,276,278,282,285,291,294,
        296,299,302,314,319,324,328,333,340,348,355,363,372,379,390,394,
        399,409,414,419,430,434,443,447,455,459,468,470,479,483,490,493,
        522,526,532,558,564,568,570,576,583,590
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'>='", "'<='", "<INVALID>", 
                     "'!<'", "'!>'", "'='", "'>'", "'<'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", "'~'", "','", 
                     "'.'", "';'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*/'" ]

    symbolicNames = [ "<INVALID>", "DECLARE", "GO", "SELECT", "FROM", "WHERE", 
                      "AND", "OR", "NOT", "AS", "DISTINCT", "INSERT", "INTO", 
                      "VALUES", "UPDATE", "SET", "DELETE", "CREATE", "TABLE", 
                      "ALTER", "DROP", "PRIMARY", "KEY", "ADD", "COLUMN", 
                      "VIEW", "PROCEDURE", "USE", "JOIN", "INNER", "LEFT", 
                      "ON", "GROUP", "BY", "HAVING", "ORDER", "ASC", "DESC", 
                      "NULL", "IS", "UNION", "BEGIN", "END", "CASE", "WHEN", 
                      "THEN", "ELSE", "EXISTS", "IN", "IF", "TRY", "CATCH", 
                      "EXEC", "PRINT", "DEFAULT", "IDENTITY", "TOP", "OUTPUT", 
                      "WITH", "OVER", "PARTITION", "RIGHT", "FULL", "CROSS", 
                      "OUTER", "BETWEEN", "LIKE", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                      "STAR_ASSIGN", "SLASH_ASSIGN", "PERCENT_ASSIGN", "GE", 
                      "LE", "NEQ", "NOT_LESS", "NOT_GREATER", "EQ", "GT", 
                      "LT", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
                      "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT", "COMMA", 
                      "DOT", "SEMI", "LPAREN", "RPAREN", "FLOAT", "INT", 
                      "NSTRING", "UNCLOSED_NSTRING_EOF", "STRING", "UNCLOSED_STRING_EOF", 
                      "LINE_COMMENT", "BLOCK_COMMENT_START", "NESTED_BLOCK_START", 
                      "BLOCK_COMMENT_END", "COMMENT_TEXT", "UNTERMINATED_BLOCK_COMMENT", 
                      "TRUE", "FALSE", "HEX_LITERAL", "INVALID_HEX_LITERAL", 
                      "BIT_STRING", "INVALID_BIT_STRING", "GLOBAL_VAR", 
                      "LOCAL_VAR", "TEMP_ID", "BRACKET_ID", "DQUOTED_ID", 
                      "UNCLOSED_BRACKET_ID", "ID", "WS", "ERROR_CHAR" ]

    RULE_root = 0
    RULE_sql_script = 1
    RULE_batch = 2
    RULE_sql_statement = 3
    RULE_ddl_statement = 4
    RULE_dml_statement = 5
    RULE_create_statement = 6
    RULE_column_def_list = 7
    RULE_column_def = 8
    RULE_data_type = 9
    RULE_column_constraint = 10
    RULE_alter_statement = 11
    RULE_drop_statement = 12
    RULE_use_statement = 13
    RULE_select_statement = 14
    RULE_select_list = 15
    RULE_select_item = 16
    RULE_table_source = 17
    RULE_join_part = 18
    RULE_group_list = 19
    RULE_order_list = 20
    RULE_insert_statement = 21
    RULE_column_list = 22
    RULE_expression_list = 23
    RULE_update_statement = 24
    RULE_assignment_list = 25
    RULE_assignment = 26
    RULE_delete_statement = 27
    RULE_declare_statement = 28
    RULE_declare_list = 29
    RULE_declare_item = 30
    RULE_set_statement = 31
    RULE_control_flow_statement = 32
    RULE_print_statement = 33
    RULE_execute_statement = 34
    RULE_with_expression = 35
    RULE_expression = 36
    RULE_function_call = 37
    RULE_atom = 38
    RULE_table_name = 39
    RULE_id_name = 40
    RULE_constant = 41
    RULE_variable = 42

    ruleNames =  [ "root", "sql_script", "batch", "sql_statement", "ddl_statement", 
                   "dml_statement", "create_statement", "column_def_list", 
                   "column_def", "data_type", "column_constraint", "alter_statement", 
                   "drop_statement", "use_statement", "select_statement", 
                   "select_list", "select_item", "table_source", "join_part", 
                   "group_list", "order_list", "insert_statement", "column_list", 
                   "expression_list", "update_statement", "assignment_list", 
                   "assignment", "delete_statement", "declare_statement", 
                   "declare_list", "declare_item", "set_statement", "control_flow_statement", 
                   "print_statement", "execute_statement", "with_expression", 
                   "expression", "function_call", "atom", "table_name", 
                   "id_name", "constant", "variable" ]

    EOF = Token.EOF
    DECLARE=1
    GO=2
    SELECT=3
    FROM=4
    WHERE=5
    AND=6
    OR=7
    NOT=8
    AS=9
    DISTINCT=10
    INSERT=11
    INTO=12
    VALUES=13
    UPDATE=14
    SET=15
    DELETE=16
    CREATE=17
    TABLE=18
    ALTER=19
    DROP=20
    PRIMARY=21
    KEY=22
    ADD=23
    COLUMN=24
    VIEW=25
    PROCEDURE=26
    USE=27
    JOIN=28
    INNER=29
    LEFT=30
    ON=31
    GROUP=32
    BY=33
    HAVING=34
    ORDER=35
    ASC=36
    DESC=37
    NULL=38
    IS=39
    UNION=40
    BEGIN=41
    END=42
    CASE=43
    WHEN=44
    THEN=45
    ELSE=46
    EXISTS=47
    IN=48
    IF=49
    TRY=50
    CATCH=51
    EXEC=52
    PRINT=53
    DEFAULT=54
    IDENTITY=55
    TOP=56
    OUTPUT=57
    WITH=58
    OVER=59
    PARTITION=60
    RIGHT=61
    FULL=62
    CROSS=63
    OUTER=64
    BETWEEN=65
    LIKE=66
    PLUS_ASSIGN=67
    MINUS_ASSIGN=68
    STAR_ASSIGN=69
    SLASH_ASSIGN=70
    PERCENT_ASSIGN=71
    GE=72
    LE=73
    NEQ=74
    NOT_LESS=75
    NOT_GREATER=76
    EQ=77
    GT=78
    LT=79
    PLUS=80
    MINUS=81
    STAR=82
    SLASH=83
    PERCENT=84
    BIT_AND=85
    BIT_OR=86
    BIT_XOR=87
    BIT_NOT=88
    COMMA=89
    DOT=90
    SEMI=91
    LPAREN=92
    RPAREN=93
    FLOAT=94
    INT=95
    NSTRING=96
    UNCLOSED_NSTRING_EOF=97
    STRING=98
    UNCLOSED_STRING_EOF=99
    LINE_COMMENT=100
    BLOCK_COMMENT_START=101
    NESTED_BLOCK_START=102
    BLOCK_COMMENT_END=103
    COMMENT_TEXT=104
    UNTERMINATED_BLOCK_COMMENT=105
    TRUE=106
    FALSE=107
    HEX_LITERAL=108
    INVALID_HEX_LITERAL=109
    BIT_STRING=110
    INVALID_BIT_STRING=111
    GLOBAL_VAR=112
    LOCAL_VAR=113
    TEMP_ID=114
    BRACKET_ID=115
    DQUOTED_ID=116
    UNCLOSED_BRACKET_ID=117
    ID=118
    WS=119
    ERROR_CHAR=120

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sql_script(self):
            return self.getTypedRuleContext(SQLParser.Sql_scriptContext,0)


        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SQLParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.sql_script()
            self.state = 87
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_scriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def batch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.BatchContext)
            else:
                return self.getTypedRuleContext(SQLParser.BatchContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_sql_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_script" ):
                listener.enterSql_script(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_script" ):
                listener.exitSql_script(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_script" ):
                return visitor.visitSql_script(self)
            else:
                return visitor.visitChildren(self)




    def sql_script(self):

        localctx = SQLParser.Sql_scriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sql_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 302306324146538510) != 0):
                self.state = 89
                self.batch()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_batch

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatementBatchContext(BatchContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.BatchContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sql_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Sql_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Sql_statementContext,i)

        def GO(self):
            return self.getToken(SQLParser.GO, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.SEMI)
            else:
                return self.getToken(SQLParser.SEMI, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementBatch" ):
                listener.enterStatementBatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementBatch" ):
                listener.exitStatementBatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementBatch" ):
                return visitor.visitStatementBatch(self)
            else:
                return visitor.visitChildren(self)


    class EmptyGoContext(BatchContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.BatchContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GO(self):
            return self.getToken(SQLParser.GO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyGo" ):
                listener.enterEmptyGo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyGo" ):
                listener.exitEmptyGo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyGo" ):
                return visitor.visitEmptyGo(self)
            else:
                return visitor.visitChildren(self)



    def batch(self):

        localctx = SQLParser.BatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_batch)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 11, 14, 15, 16, 17, 19, 20, 27, 41, 49, 52, 53, 58]:
                localctx = SQLParser.StatementBatchContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 95
                        self.sql_statement()
                        self.state = 97
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==91:
                            self.state = 96
                            self.match(SQLParser.SEMI)



                    else:
                        raise NoViableAltException(self)
                    self.state = 101 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.match(SQLParser.GO)


                pass
            elif token in [2]:
                localctx = SQLParser.EmptyGoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(SQLParser.GO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ddl_statement(self):
            return self.getTypedRuleContext(SQLParser.Ddl_statementContext,0)


        def dml_statement(self):
            return self.getTypedRuleContext(SQLParser.Dml_statementContext,0)


        def control_flow_statement(self):
            return self.getTypedRuleContext(SQLParser.Control_flow_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(SQLParser.Print_statementContext,0)


        def declare_statement(self):
            return self.getTypedRuleContext(SQLParser.Declare_statementContext,0)


        def set_statement(self):
            return self.getTypedRuleContext(SQLParser.Set_statementContext,0)


        def execute_statement(self):
            return self.getTypedRuleContext(SQLParser.Execute_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_sql_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_statement" ):
                listener.enterSql_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_statement" ):
                listener.exitSql_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_statement" ):
                return visitor.visitSql_statement(self)
            else:
                return visitor.visitChildren(self)




    def sql_statement(self):

        localctx = SQLParser.Sql_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sql_statement)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 19, 20, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.ddl_statement()
                pass
            elif token in [3, 11, 14, 16, 58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.dml_statement()
                pass
            elif token in [41, 49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.control_flow_statement()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.print_statement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.declare_statement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.set_statement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.execute_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ddl_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create_statement(self):
            return self.getTypedRuleContext(SQLParser.Create_statementContext,0)


        def alter_statement(self):
            return self.getTypedRuleContext(SQLParser.Alter_statementContext,0)


        def drop_statement(self):
            return self.getTypedRuleContext(SQLParser.Drop_statementContext,0)


        def use_statement(self):
            return self.getTypedRuleContext(SQLParser.Use_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_ddl_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdl_statement" ):
                listener.enterDdl_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdl_statement" ):
                listener.exitDdl_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdl_statement" ):
                return visitor.visitDdl_statement(self)
            else:
                return visitor.visitChildren(self)




    def ddl_statement(self):

        localctx = SQLParser.Ddl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ddl_statement)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.create_statement()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.alter_statement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.drop_statement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.use_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dml_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def insert_statement(self):
            return self.getTypedRuleContext(SQLParser.Insert_statementContext,0)


        def update_statement(self):
            return self.getTypedRuleContext(SQLParser.Update_statementContext,0)


        def delete_statement(self):
            return self.getTypedRuleContext(SQLParser.Delete_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_dml_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDml_statement" ):
                listener.enterDml_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDml_statement" ):
                listener.exitDml_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDml_statement" ):
                return visitor.visitDml_statement(self)
            else:
                return visitor.visitChildren(self)




    def dml_statement(self):

        localctx = SQLParser.Dml_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dml_statement)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.select_statement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.insert_statement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.update_statement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.delete_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def column_def_list(self):
            return self.getTypedRuleContext(SQLParser.Column_def_listContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_create_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_statement" ):
                listener.enterCreate_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_statement" ):
                listener.exitCreate_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_statement" ):
                return visitor.visitCreate_statement(self)
            else:
                return visitor.visitChildren(self)




    def create_statement(self):

        localctx = SQLParser.Create_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_create_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SQLParser.CREATE)
            self.state = 131
            self.match(SQLParser.TABLE)
            self.state = 132
            self.table_name()
            self.state = 133
            self.match(SQLParser.LPAREN)
            self.state = 134
            self.column_def_list()
            self.state = 135
            self.match(SQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Column_defContext)
            else:
                return self.getTypedRuleContext(SQLParser.Column_defContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_column_def_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_def_list" ):
                listener.enterColumn_def_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_def_list" ):
                listener.exitColumn_def_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_def_list" ):
                return visitor.visitColumn_def_list(self)
            else:
                return visitor.visitChildren(self)




    def column_def_list(self):

        localctx = SQLParser.Column_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_column_def_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.column_def()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 138
                self.match(SQLParser.COMMA)
                self.state = 139
                self.column_def()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def data_type(self):
            return self.getTypedRuleContext(SQLParser.Data_typeContext,0)


        def column_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Column_constraintContext)
            else:
                return self.getTypedRuleContext(SQLParser.Column_constraintContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_column_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_def" ):
                listener.enterColumn_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_def" ):
                listener.exitColumn_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_def" ):
                return visitor.visitColumn_def(self)
            else:
                return visitor.visitChildren(self)




    def column_def(self):

        localctx = SQLParser.Column_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_column_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.id_name()
            self.state = 146
            self.data_type()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 54043470408450304) != 0):
                self.state = 147
                self.column_constraint()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Id_nameContext)
            else:
                return self.getTypedRuleContext(SQLParser.Id_nameContext,i)


        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.INT)
            else:
                return self.getToken(SQLParser.INT, i)

        def COMMA(self):
            return self.getToken(SQLParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = SQLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.id_name()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 154
                self.match(SQLParser.LPAREN)
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [95]:
                    self.state = 155
                    self.match(SQLParser.INT)
                    pass
                elif token in [115, 116, 118]:
                    self.state = 156
                    self.id_name()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==89:
                    self.state = 159
                    self.match(SQLParser.COMMA)
                    self.state = 160
                    self.match(SQLParser.INT)


                self.state = 163
                self.match(SQLParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def PRIMARY(self):
            return self.getToken(SQLParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(SQLParser.KEY, 0)

        def DEFAULT(self):
            return self.getToken(SQLParser.DEFAULT, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def IDENTITY(self):
            return self.getToken(SQLParser.IDENTITY, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.INT)
            else:
                return self.getToken(SQLParser.INT, i)

        def COMMA(self):
            return self.getToken(SQLParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_column_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_constraint" ):
                listener.enterColumn_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_constraint" ):
                listener.exitColumn_constraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_constraint" ):
                return visitor.visitColumn_constraint(self)
            else:
                return visitor.visitChildren(self)




    def column_constraint(self):

        localctx = SQLParser.Column_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_column_constraint)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(SQLParser.NOT)
                self.state = 167
                self.match(SQLParser.NULL)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(SQLParser.NULL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.match(SQLParser.PRIMARY)
                self.state = 170
                self.match(SQLParser.KEY)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.match(SQLParser.DEFAULT)
                self.state = 172
                self.expression(0)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.match(SQLParser.IDENTITY)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==92:
                    self.state = 174
                    self.match(SQLParser.LPAREN)
                    self.state = 175
                    self.match(SQLParser.INT)
                    self.state = 176
                    self.match(SQLParser.COMMA)
                    self.state = 177
                    self.match(SQLParser.INT)
                    self.state = 178
                    self.match(SQLParser.RPAREN)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alter_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_alter_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AlterDropContext(Alter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Alter_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALTER(self):
            return self.getToken(SQLParser.ALTER, 0)
        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)
        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)
        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)
        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlterDrop" ):
                listener.enterAlterDrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlterDrop" ):
                listener.exitAlterDrop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlterDrop" ):
                return visitor.visitAlterDrop(self)
            else:
                return visitor.visitChildren(self)


    class AlterAddContext(Alter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Alter_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALTER(self):
            return self.getToken(SQLParser.ALTER, 0)
        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)
        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)

        def ADD(self):
            return self.getToken(SQLParser.ADD, 0)
        def column_def(self):
            return self.getTypedRuleContext(SQLParser.Column_defContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlterAdd" ):
                listener.enterAlterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlterAdd" ):
                listener.exitAlterAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlterAdd" ):
                return visitor.visitAlterAdd(self)
            else:
                return visitor.visitChildren(self)


    class AlterModifyContext(Alter_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Alter_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALTER(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.ALTER)
            else:
                return self.getToken(SQLParser.ALTER, i)
        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)
        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)
        def column_def(self):
            return self.getTypedRuleContext(SQLParser.Column_defContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlterModify" ):
                listener.enterAlterModify(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlterModify" ):
                listener.exitAlterModify(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlterModify" ):
                return visitor.visitAlterModify(self)
            else:
                return visitor.visitChildren(self)



    def alter_statement(self):

        localctx = SQLParser.Alter_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alter_statement)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = SQLParser.AlterAddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(SQLParser.ALTER)
                self.state = 184
                self.match(SQLParser.TABLE)
                self.state = 185
                self.table_name()
                self.state = 186
                self.match(SQLParser.ADD)
                self.state = 187
                self.column_def()
                pass

            elif la_ == 2:
                localctx = SQLParser.AlterDropContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(SQLParser.ALTER)
                self.state = 190
                self.match(SQLParser.TABLE)
                self.state = 191
                self.table_name()
                self.state = 192
                self.match(SQLParser.DROP)
                self.state = 193
                self.match(SQLParser.COLUMN)
                self.state = 194
                self.id_name()
                pass

            elif la_ == 3:
                localctx = SQLParser.AlterModifyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(SQLParser.ALTER)
                self.state = 197
                self.match(SQLParser.TABLE)
                self.state = 198
                self.table_name()
                self.state = 199
                self.match(SQLParser.ALTER)
                self.state = 200
                self.match(SQLParser.COLUMN)
                self.state = 201
                self.column_def()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Drop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def VIEW(self):
            return self.getToken(SQLParser.VIEW, 0)

        def PROCEDURE(self):
            return self.getToken(SQLParser.PROCEDURE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_drop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop_statement" ):
                listener.enterDrop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop_statement" ):
                listener.exitDrop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrop_statement" ):
                return visitor.visitDrop_statement(self)
            else:
                return visitor.visitChildren(self)




    def drop_statement(self):

        localctx = SQLParser.Drop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_drop_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(SQLParser.DROP)
            self.state = 206
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 100925440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 207
            self.table_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Use_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(SQLParser.USE, 0)

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_use_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUse_statement" ):
                listener.enterUse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUse_statement" ):
                listener.exitUse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUse_statement" ):
                return visitor.visitUse_statement(self)
            else:
                return visitor.visitChildren(self)




    def use_statement(self):

        localctx = SQLParser.Use_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_use_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(SQLParser.USE)
            self.state = 210
            self.id_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def select_list(self):
            return self.getTypedRuleContext(SQLParser.Select_listContext,0)


        def with_expression(self):
            return self.getTypedRuleContext(SQLParser.With_expressionContext,0)


        def DISTINCT(self):
            return self.getToken(SQLParser.DISTINCT, 0)

        def TOP(self):
            return self.getToken(SQLParser.TOP, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def table_source(self):
            return self.getTypedRuleContext(SQLParser.Table_sourceContext,0)


        def ORDER(self):
            return self.getToken(SQLParser.ORDER, 0)

        def BY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.BY)
            else:
                return self.getToken(SQLParser.BY, i)

        def order_list(self):
            return self.getTypedRuleContext(SQLParser.Order_listContext,0)


        def join_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Join_partContext)
            else:
                return self.getTypedRuleContext(SQLParser.Join_partContext,i)


        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def GROUP(self):
            return self.getToken(SQLParser.GROUP, 0)

        def group_list(self):
            return self.getTypedRuleContext(SQLParser.Group_listContext,0)


        def HAVING(self):
            return self.getToken(SQLParser.HAVING, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_select_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_statement" ):
                listener.enterSelect_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_statement" ):
                listener.exitSelect_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_statement" ):
                return visitor.visitSelect_statement(self)
            else:
                return visitor.visitChildren(self)




    def select_statement(self):

        localctx = SQLParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 212
                self.with_expression()


            self.state = 215
            self.match(SQLParser.SELECT)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 216
                self.match(SQLParser.DISTINCT)


            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 219
                self.match(SQLParser.TOP)
                self.state = 220
                self.match(SQLParser.INT)


            self.state = 223
            self.select_list()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 224
                self.match(SQLParser.FROM)
                self.state = 225
                self.table_source()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 28)) & ~0x3f) == 0 and ((1 << (_la - 28)) & 128849018887) != 0):
                    self.state = 226
                    self.join_part()
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 232
                    self.match(SQLParser.WHERE)
                    self.state = 233
                    self.expression(0)


                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 236
                    self.match(SQLParser.GROUP)
                    self.state = 237
                    self.match(SQLParser.BY)
                    self.state = 238
                    self.group_list()


                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 241
                    self.match(SQLParser.HAVING)
                    self.state = 242
                    self.expression(0)




            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 247
                self.match(SQLParser.ORDER)
                self.state = 248
                self.match(SQLParser.BY)
                self.state = 249
                self.order_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(SQLParser.STAR, 0)

        def select_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Select_itemContext)
            else:
                return self.getTypedRuleContext(SQLParser.Select_itemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_select_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_list" ):
                listener.enterSelect_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_list" ):
                listener.exitSelect_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_list" ):
                return visitor.visitSelect_list(self)
            else:
                return visitor.visitChildren(self)




    def select_list(self):

        localctx = SQLParser.Select_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_select_list)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [82]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(SQLParser.STAR)
                pass
            elif token in [8, 38, 43, 47, 92, 94, 95, 96, 98, 106, 107, 112, 113, 115, 116, 118]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.select_item()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==89:
                    self.state = 254
                    self.match(SQLParser.COMMA)
                    self.state = 255
                    self.select_item()
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_select_item

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectAliasAssignmentContext(Select_itemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Select_itemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)

        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)
        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectAliasAssignment" ):
                listener.enterSelectAliasAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectAliasAssignment" ):
                listener.exitSelectAliasAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectAliasAssignment" ):
                return visitor.visitSelectAliasAssignment(self)
            else:
                return visitor.visitChildren(self)


    class SelectExpressionContext(Select_itemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Select_itemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)

        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectExpression" ):
                listener.enterSelectExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectExpression" ):
                listener.exitSelectExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectExpression" ):
                return visitor.visitSelectExpression(self)
            else:
                return visitor.visitChildren(self)


    class SelectVarAssignmentContext(Select_itemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.Select_itemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(SQLParser.VariableContext,0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)
        def PLUS_ASSIGN(self):
            return self.getToken(SQLParser.PLUS_ASSIGN, 0)
        def MINUS_ASSIGN(self):
            return self.getToken(SQLParser.MINUS_ASSIGN, 0)
        def STAR_ASSIGN(self):
            return self.getToken(SQLParser.STAR_ASSIGN, 0)
        def SLASH_ASSIGN(self):
            return self.getToken(SQLParser.SLASH_ASSIGN, 0)
        def PERCENT_ASSIGN(self):
            return self.getToken(SQLParser.PERCENT_ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectVarAssignment" ):
                listener.enterSelectVarAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectVarAssignment" ):
                listener.exitSelectVarAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectVarAssignment" ):
                return visitor.visitSelectVarAssignment(self)
            else:
                return visitor.visitChildren(self)



    def select_item(self):

        localctx = SQLParser.Select_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_select_item)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = SQLParser.SelectVarAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.variable()
                self.state = 264
                _la = self._input.LA(1)
                if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 1055) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = SQLParser.SelectAliasAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.id_name()
                self.state = 268
                self.match(SQLParser.EQ)
                self.state = 269
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = SQLParser.SelectExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.expression(0)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9 or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & 11) != 0):
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 272
                        self.match(SQLParser.AS)


                    self.state = 275
                    self.id_name()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_sourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_table_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_source" ):
                listener.enterTable_source(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_source" ):
                listener.exitTable_source(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_source" ):
                return visitor.visitTable_source(self)
            else:
                return visitor.visitChildren(self)




    def table_source(self):

        localctx = SQLParser.Table_sourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_table_source)
        self._la = 0 # Token type
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [115, 116, 118]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.table_name()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9 or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & 11) != 0):
                    self.state = 282
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 281
                        self.match(SQLParser.AS)


                    self.state = 284
                    self.id_name()


                pass
            elif token in [92]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(SQLParser.LPAREN)
                self.state = 288
                self.select_statement()
                self.state = 289
                self.match(SQLParser.RPAREN)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9 or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & 11) != 0):
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==9:
                        self.state = 290
                        self.match(SQLParser.AS)


                    self.state = 293
                    self.id_name()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_source(self):
            return self.getTypedRuleContext(SQLParser.Table_sourceContext,0)


        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def OUTER(self):
            return self.getToken(SQLParser.OUTER, 0)

        def INNER(self):
            return self.getToken(SQLParser.INNER, 0)

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(SQLParser.FULL, 0)

        def CROSS(self):
            return self.getToken(SQLParser.CROSS, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_join_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_part" ):
                listener.enterJoin_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_part" ):
                listener.exitJoin_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoin_part" ):
                return visitor.visitJoin_part(self)
            else:
                return visitor.visitChildren(self)




    def join_part(self):

        localctx = SQLParser.Join_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_join_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -2305843007603081216) != 0):
                self.state = 298
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -2305843007603081216) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 301
                self.match(SQLParser.OUTER)


            self.state = 304
            self.match(SQLParser.JOIN)
            self.state = 305
            self.table_source()
            self.state = 306
            self.match(SQLParser.ON)
            self.state = 307
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_group_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_list" ):
                listener.enterGroup_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_list" ):
                listener.exitGroup_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup_list" ):
                return visitor.visitGroup_list(self)
            else:
                return visitor.visitChildren(self)




    def group_list(self):

        localctx = SQLParser.Group_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_group_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expression(0)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 310
                self.match(SQLParser.COMMA)
                self.state = 311
                self.expression(0)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def ASC(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.ASC)
            else:
                return self.getToken(SQLParser.ASC, i)

        def DESC(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.DESC)
            else:
                return self.getToken(SQLParser.DESC, i)

        def getRuleIndex(self):
            return SQLParser.RULE_order_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_list" ):
                listener.enterOrder_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_list" ):
                listener.exitOrder_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrder_list" ):
                return visitor.visitOrder_list(self)
            else:
                return visitor.visitChildren(self)




    def order_list(self):

        localctx = SQLParser.Order_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_order_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expression(0)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36 or _la==37:
                self.state = 318
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 321
                self.match(SQLParser.COMMA)
                self.state = 322
                self.expression(0)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36 or _la==37:
                    self.state = 323
                    _la = self._input.LA(1)
                    if not(_la==36 or _la==37):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.LPAREN)
            else:
                return self.getToken(SQLParser.LPAREN, i)

        def expression_list(self):
            return self.getTypedRuleContext(SQLParser.Expression_listContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.RPAREN)
            else:
                return self.getToken(SQLParser.RPAREN, i)

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def column_list(self):
            return self.getTypedRuleContext(SQLParser.Column_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_insert_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_statement" ):
                listener.enterInsert_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_statement" ):
                listener.exitInsert_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_statement" ):
                return visitor.visitInsert_statement(self)
            else:
                return visitor.visitChildren(self)




    def insert_statement(self):

        localctx = SQLParser.Insert_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_insert_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(SQLParser.INSERT)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 332
                self.match(SQLParser.INTO)


            self.state = 335
            self.table_name()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 336
                self.match(SQLParser.LPAREN)
                self.state = 337
                self.column_list()
                self.state = 338
                self.match(SQLParser.RPAREN)


            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 342
                self.match(SQLParser.VALUES)
                self.state = 343
                self.match(SQLParser.LPAREN)
                self.state = 344
                self.expression_list()
                self.state = 345
                self.match(SQLParser.RPAREN)
                pass
            elif token in [3, 58]:
                self.state = 347
                self.select_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Id_nameContext)
            else:
                return self.getTypedRuleContext(SQLParser.Id_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_list" ):
                return visitor.visitColumn_list(self)
            else:
                return visitor.visitChildren(self)




    def column_list(self):

        localctx = SQLParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.id_name()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 351
                self.match(SQLParser.COMMA)
                self.state = 352
                self.id_name()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = SQLParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.expression(0)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 359
                self.match(SQLParser.COMMA)
                self.state = 360
                self.expression(0)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(SQLParser.UPDATE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def assignment_list(self):
            return self.getTypedRuleContext(SQLParser.Assignment_listContext,0)


        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_update_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate_statement" ):
                listener.enterUpdate_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate_statement" ):
                listener.exitUpdate_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_statement" ):
                return visitor.visitUpdate_statement(self)
            else:
                return visitor.visitChildren(self)




    def update_statement(self):

        localctx = SQLParser.Update_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_update_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(SQLParser.UPDATE)
            self.state = 367
            self.table_name()
            self.state = 368
            self.match(SQLParser.SET)
            self.state = 369
            self.assignment_list()
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 370
                self.match(SQLParser.WHERE)
                self.state = 371
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SQLParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_assignment_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_list" ):
                listener.enterAssignment_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_list" ):
                listener.exitAssignment_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_list" ):
                return visitor.visitAssignment_list(self)
            else:
                return visitor.visitChildren(self)




    def assignment_list(self):

        localctx = SQLParser.Assignment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.assignment()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 375
                self.match(SQLParser.COMMA)
                self.state = 376
                self.assignment()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def PLUS_ASSIGN(self):
            return self.getToken(SQLParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(SQLParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(SQLParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(SQLParser.SLASH_ASSIGN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SQLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.id_name()
                self.state = 383
                self.match(SQLParser.EQ)
                self.state = 384
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.id_name()
                self.state = 387
                _la = self._input.LA(1)
                if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 388
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delete_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SQLParser.DELETE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_delete_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_statement" ):
                listener.enterDelete_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_statement" ):
                listener.exitDelete_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_statement" ):
                return visitor.visitDelete_statement(self)
            else:
                return visitor.visitChildren(self)




    def delete_statement(self):

        localctx = SQLParser.Delete_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_delete_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(SQLParser.DELETE)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 393
                self.match(SQLParser.FROM)


            self.state = 396
            self.table_name()
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 397
                self.match(SQLParser.WHERE)
                self.state = 398
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(SQLParser.DECLARE, 0)

        def declare_list(self):
            return self.getTypedRuleContext(SQLParser.Declare_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_declare_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_statement" ):
                listener.enterDeclare_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_statement" ):
                listener.exitDeclare_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_statement" ):
                return visitor.visitDeclare_statement(self)
            else:
                return visitor.visitChildren(self)




    def declare_statement(self):

        localctx = SQLParser.Declare_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_declare_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(SQLParser.DECLARE)
            self.state = 402
            self.declare_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Declare_itemContext)
            else:
                return self.getTypedRuleContext(SQLParser.Declare_itemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_declare_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_list" ):
                listener.enterDeclare_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_list" ):
                listener.exitDeclare_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_list" ):
                return visitor.visitDeclare_list(self)
            else:
                return visitor.visitChildren(self)




    def declare_list(self):

        localctx = SQLParser.Declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_declare_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.declare_item()
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==89:
                self.state = 405
                self.match(SQLParser.COMMA)
                self.state = 406
                self.declare_item()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCAL_VAR(self):
            return self.getToken(SQLParser.LOCAL_VAR, 0)

        def data_type(self):
            return self.getTypedRuleContext(SQLParser.Data_typeContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_declare_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_item" ):
                listener.enterDeclare_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_item" ):
                listener.exitDeclare_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_item" ):
                return visitor.visitDeclare_item(self)
            else:
                return visitor.visitChildren(self)




    def declare_item(self):

        localctx = SQLParser.Declare_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_declare_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(SQLParser.LOCAL_VAR)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 413
                self.match(SQLParser.AS)


            self.state = 416
            self.data_type()
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 417
                self.match(SQLParser.EQ)
                self.state = 418
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def variable(self):
            return self.getTypedRuleContext(SQLParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(SQLParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(SQLParser.MINUS_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(SQLParser.STAR_ASSIGN, 0)

        def SLASH_ASSIGN(self):
            return self.getToken(SQLParser.SLASH_ASSIGN, 0)

        def PERCENT_ASSIGN(self):
            return self.getToken(SQLParser.PERCENT_ASSIGN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_set_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_statement" ):
                listener.enterSet_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_statement" ):
                listener.exitSet_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_statement" ):
                return visitor.visitSet_statement(self)
            else:
                return visitor.visitChildren(self)




    def set_statement(self):

        localctx = SQLParser.Set_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_set_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(SQLParser.SET)
            self.state = 422
            self.variable()
            self.state = 423
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 1055) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 424
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_flow_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.BEGIN)
            else:
                return self.getToken(SQLParser.BEGIN, i)

        def TRY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TRY)
            else:
                return self.getToken(SQLParser.TRY, i)

        def END(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.END)
            else:
                return self.getToken(SQLParser.END, i)

        def CATCH(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.CATCH)
            else:
                return self.getToken(SQLParser.CATCH, i)

        def sql_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Sql_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Sql_statementContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.SEMI)
            else:
                return self.getToken(SQLParser.SEMI, i)

        def IF(self):
            return self.getToken(SQLParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def ELSE(self):
            return self.getToken(SQLParser.ELSE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_control_flow_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl_flow_statement" ):
                listener.enterControl_flow_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl_flow_statement" ):
                listener.exitControl_flow_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_flow_statement" ):
                return visitor.visitControl_flow_statement(self)
            else:
                return visitor.visitChildren(self)




    def control_flow_statement(self):

        localctx = SQLParser.Control_flow_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_control_flow_statement)
        self._la = 0 # Token type
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(SQLParser.BEGIN)
                self.state = 427
                self.match(SQLParser.TRY)
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 302306324146538506) != 0):
                    self.state = 428
                    self.sql_statement()
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==91:
                        self.state = 429
                        self.match(SQLParser.SEMI)


                    self.state = 436
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 437
                self.match(SQLParser.END)
                self.state = 438
                self.match(SQLParser.TRY)
                self.state = 439
                self.match(SQLParser.BEGIN)
                self.state = 440
                self.match(SQLParser.CATCH)
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 302306324146538506) != 0):
                    self.state = 441
                    self.sql_statement()
                    self.state = 443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==91:
                        self.state = 442
                        self.match(SQLParser.SEMI)


                    self.state = 449
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 450
                self.match(SQLParser.END)
                self.state = 451
                self.match(SQLParser.CATCH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(SQLParser.BEGIN)
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 302306324146538506) != 0):
                    self.state = 453
                    self.sql_statement()
                    self.state = 455
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==91:
                        self.state = 454
                        self.match(SQLParser.SEMI)


                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 462
                self.match(SQLParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.match(SQLParser.IF)
                self.state = 464
                self.expression(0)
                self.state = 465
                self.sql_statement()
                self.state = 468
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 466
                    self.match(SQLParser.ELSE)
                    self.state = 467
                    self.sql_statement()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(SQLParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = SQLParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(SQLParser.PRINT)
            self.state = 473
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Execute_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXEC(self):
            return self.getToken(SQLParser.EXEC, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.VariableContext)
            else:
                return self.getTypedRuleContext(SQLParser.VariableContext,i)


        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_execute_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecute_statement" ):
                listener.enterExecute_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecute_statement" ):
                listener.exitExecute_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecute_statement" ):
                return visitor.visitExecute_statement(self)
            else:
                return visitor.visitChildren(self)




    def execute_statement(self):

        localctx = SQLParser.Execute_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_execute_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(SQLParser.EXEC)
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 476
                self.variable()
                self.state = 477
                self.match(SQLParser.EQ)


            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [115, 116, 118]:
                self.state = 481
                self.table_name()
                pass
            elif token in [112, 113]:
                self.state = 482
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 149808459284736) != 0) or ((((_la - 92)) & ~0x3f) == 0 and ((1 << (_la - 92)) & 95469661) != 0):
                self.state = 485
                self.expression(0)
                self.state = 490
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==89:
                    self.state = 486
                    self.match(SQLParser.COMMA)
                    self.state = 487
                    self.expression(0)
                    self.state = 492
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class With_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(SQLParser.WITH, 0)

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_with_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWith_expression" ):
                listener.enterWith_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWith_expression" ):
                listener.exitWith_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWith_expression" ):
                return visitor.visitWith_expression(self)
            else:
                return visitor.visitChildren(self)




    def with_expression(self):

        localctx = SQLParser.With_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_with_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(SQLParser.WITH)
            self.state = 496
            self.id_name()
            self.state = 497
            self.match(SQLParser.AS)
            self.state = 498
            self.match(SQLParser.LPAREN)
            self.state = 499
            self.select_statement()
            self.state = 500
            self.match(SQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LikeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def LIKE(self):
            return self.getToken(SQLParser.LIKE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLikeExpr" ):
                listener.enterLikeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLikeExpr" ):
                listener.exitLikeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLikeExpr" ):
                return visitor.visitLikeExpr(self)
            else:
                return visitor.visitChildren(self)


    class IsNotNullExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def IS(self):
            return self.getToken(SQLParser.IS, 0)
        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)
        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsNotNullExpr" ):
                listener.enterIsNotNullExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsNotNullExpr" ):
                listener.exitIsNotNullExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsNotNullExpr" ):
                return visitor.visitIsNotNullExpr(self)
            else:
                return visitor.visitChildren(self)


    class IsNullExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def IS(self):
            return self.getToken(SQLParser.IS, 0)
        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsNullExpr" ):
                listener.enterIsNullExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsNullExpr" ):
                listener.exitIsNullExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsNullExpr" ):
                return visitor.visitIsNullExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(SQLParser.EQ, 0)
        def NEQ(self):
            return self.getToken(SQLParser.NEQ, 0)
        def GT(self):
            return self.getToken(SQLParser.GT, 0)
        def LT(self):
            return self.getToken(SQLParser.LT, 0)
        def GE(self):
            return self.getToken(SQLParser.GE, 0)
        def LE(self):
            return self.getToken(SQLParser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(SQLParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def STAR(self):
            return self.getToken(SQLParser.STAR, 0)
        def SLASH(self):
            return self.getToken(SQLParser.SLASH, 0)
        def PERCENT(self):
            return self.getToken(SQLParser.PERCENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(SQLParser.Function_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(SQLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SQLParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class InExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def IN(self):
            return self.getToken(SQLParser.IN, 0)
        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)
        def expression_list(self):
            return self.getTypedRuleContext(SQLParser.Expression_listContext,0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpr" ):
                listener.enterInExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpr" ):
                listener.exitInExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInExpr" ):
                return visitor.visitInExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class CaseExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(SQLParser.CASE, 0)
        def END(self):
            return self.getToken(SQLParser.END, 0)
        def WHEN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.WHEN)
            else:
                return self.getToken(SQLParser.WHEN, i)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.THEN)
            else:
                return self.getToken(SQLParser.THEN, i)
        def ELSE(self):
            return self.getToken(SQLParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExpr" ):
                listener.enterCaseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExpr" ):
                listener.exitCaseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseExpr" ):
                return visitor.visitCaseExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(SQLParser.AND, 0)
        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExistsExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)
        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)
        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistsExpr" ):
                listener.enterExistsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistsExpr" ):
                listener.exitExistsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistsExpr" ):
                return visitor.visitExistsExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                localctx = SQLParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 503
                self.match(SQLParser.LPAREN)
                self.state = 504
                self.expression(0)
                self.state = 505
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SQLParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 507
                self.match(SQLParser.NOT)
                self.state = 508
                self.expression(13)
                pass

            elif la_ == 3:
                localctx = SQLParser.ExistsExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 509
                self.match(SQLParser.EXISTS)
                self.state = 510
                self.match(SQLParser.LPAREN)
                self.state = 511
                self.select_statement()
                self.state = 512
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = SQLParser.CaseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 514
                self.match(SQLParser.CASE)
                self.state = 520 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 515
                    self.match(SQLParser.WHEN)
                    self.state = 516
                    self.expression(0)
                    self.state = 517
                    self.match(SQLParser.THEN)
                    self.state = 518
                    self.expression(0)
                    self.state = 522 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==44):
                        break

                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 524
                    self.match(SQLParser.ELSE)
                    self.state = 525
                    self.expression(0)


                self.state = 528
                self.match(SQLParser.END)
                pass

            elif la_ == 5:
                localctx = SQLParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 530
                self.function_call()
                pass

            elif la_ == 6:
                localctx = SQLParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 531
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 570
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 568
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                    if la_ == 1:
                        localctx = SQLParser.MultiplicativeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 534
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 535
                        _la = self._input.LA(1)
                        if not(((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & 7) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 536
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = SQLParser.AdditiveExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 537
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 538
                        _la = self._input.LA(1)
                        if not(_la==80 or _la==81):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 539
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = SQLParser.ComparisonExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 540
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 541
                        _la = self._input.LA(1)
                        if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 231) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 542
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = SQLParser.LikeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 543
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 544
                        self.match(SQLParser.LIKE)
                        self.state = 545
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = SQLParser.LogicalExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 546
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 547
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 548
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = SQLParser.IsNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 549
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 550
                        self.match(SQLParser.IS)
                        self.state = 551
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 7:
                        localctx = SQLParser.IsNotNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 552
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 553
                        self.match(SQLParser.IS)
                        self.state = 554
                        self.match(SQLParser.NOT)
                        self.state = 555
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 8:
                        localctx = SQLParser.InExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 556
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 558
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==8:
                            self.state = 557
                            self.match(SQLParser.NOT)


                        self.state = 560
                        self.match(SQLParser.IN)
                        self.state = 561
                        self.match(SQLParser.LPAREN)
                        self.state = 564
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [8, 38, 43, 47, 92, 94, 95, 96, 98, 106, 107, 112, 113, 115, 116, 118]:
                            self.state = 562
                            self.expression_list()
                            pass
                        elif token in [3, 58]:
                            self.state = 563
                            self.select_statement()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 566
                        self.match(SQLParser.RPAREN)
                        pass

             
                self.state = 572
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SQLParser.Expression_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = SQLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.id_name()
            self.state = 574
            self.match(SQLParser.LPAREN)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 149808459284736) != 0) or ((((_la - 92)) & ~0x3f) == 0 and ((1 << (_la - 92)) & 95469661) != 0):
                self.state = 575
                self.expression_list()


            self.state = 578
            self.match(SQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def constant(self):
            return self.getTypedRuleContext(SQLParser.ConstantContext,0)


        def variable(self):
            return self.getTypedRuleContext(SQLParser.VariableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SQLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_atom)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [115, 116, 118]:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.table_name()
                pass
            elif token in [38, 94, 95, 96, 98, 106, 107]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.constant()
                pass
            elif token in [112, 113]:
                self.enterOuterAlt(localctx, 3)
                self.state = 582
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Id_nameContext)
            else:
                return self.getTypedRuleContext(SQLParser.Id_nameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.DOT)
            else:
                return self.getToken(SQLParser.DOT, i)

        def getRuleIndex(self):
            return SQLParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_name" ):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = SQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.id_name()
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 586
                    self.match(SQLParser.DOT)
                    self.state = 587
                    self.id_name() 
                self.state = 592
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SQLParser.ID, 0)

        def BRACKET_ID(self):
            return self.getToken(SQLParser.BRACKET_ID, 0)

        def DQUOTED_ID(self):
            return self.getToken(SQLParser.DQUOTED_ID, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_id_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_name" ):
                listener.enterId_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_name" ):
                listener.exitId_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_name" ):
                return visitor.visitId_name(self)
            else:
                return visitor.visitChildren(self)




    def id_name(self):

        localctx = SQLParser.Id_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_id_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            _la = self._input.LA(1)
            if not(((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & 11) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SQLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(SQLParser.STRING, 0)

        def NSTRING(self):
            return self.getToken(SQLParser.NSTRING, 0)

        def TRUE(self):
            return self.getToken(SQLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SQLParser.FALSE, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = SQLParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            _la = self._input.LA(1)
            if not(_la==38 or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & 12311) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GLOBAL_VAR(self):
            return self.getToken(SQLParser.GLOBAL_VAR, 0)

        def LOCAL_VAR(self):
            return self.getToken(SQLParser.LOCAL_VAR, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = SQLParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            _la = self._input.LA(1)
            if not(_la==112 or _la==113):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         





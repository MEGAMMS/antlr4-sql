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
        4,1,128,700,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,1,0,1,0,1,0,1,1,5,1,99,8,1,10,1,12,1,102,9,1,1,2,1,2,3,2,
        106,8,2,4,2,108,8,2,11,2,12,2,109,1,2,1,2,3,2,114,8,2,3,2,116,8,
        2,1,2,1,2,3,2,120,8,2,3,2,122,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,131,8,3,1,4,1,4,1,4,1,4,1,4,3,4,138,8,4,1,5,1,5,1,5,1,5,3,5,144,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,156,8,7,10,7,12,
        7,159,9,7,1,8,1,8,3,8,163,8,8,1,9,1,9,1,9,5,9,168,8,9,10,9,12,9,
        171,9,9,1,10,1,10,3,10,175,8,10,1,10,1,10,1,10,3,10,180,8,10,1,10,
        3,10,183,8,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,191,8,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,206,
        8,10,1,10,1,10,1,10,1,10,1,10,3,10,213,8,10,1,11,1,11,1,11,1,11,
        3,11,219,8,11,1,11,1,11,3,11,223,8,11,1,11,3,11,226,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,3,12,234,8,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,244,8,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,252,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,274,8,13,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,3,17,288,8,17,
        1,17,1,17,3,17,292,8,17,1,17,1,17,3,17,296,8,17,1,17,1,17,1,17,1,
        17,5,17,302,8,17,10,17,12,17,305,9,17,1,17,1,17,3,17,309,8,17,1,
        17,1,17,1,17,3,17,314,8,17,1,17,1,17,3,17,318,8,17,3,17,320,8,17,
        1,17,1,17,1,17,3,17,325,8,17,1,18,1,18,1,18,1,18,5,18,331,8,18,10,
        18,12,18,334,9,18,3,18,336,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,348,8,19,1,19,3,19,351,8,19,3,19,353,8,19,
        1,20,1,20,3,20,357,8,20,1,20,3,20,360,8,20,1,20,1,20,1,20,1,20,3,
        20,366,8,20,1,20,3,20,369,8,20,3,20,371,8,20,1,21,3,21,374,8,21,
        1,21,3,21,377,8,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,5,22,
        387,8,22,10,22,12,22,390,9,22,1,23,1,23,3,23,394,8,23,1,23,1,23,
        1,23,3,23,399,8,23,5,23,401,8,23,10,23,12,23,404,9,23,1,24,1,24,
        3,24,408,8,24,1,24,1,24,1,24,1,24,1,24,3,24,415,8,24,1,24,1,24,1,
        24,1,24,5,24,421,8,24,10,24,12,24,424,9,24,1,24,3,24,427,8,24,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,5,26,436,8,26,10,26,12,26,439,9,
        26,1,27,1,27,1,27,5,27,444,8,27,10,27,12,27,447,9,27,1,28,1,28,1,
        28,1,28,1,28,1,28,3,28,455,8,28,1,29,1,29,1,29,5,29,460,8,29,10,
        29,12,29,463,9,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,473,
        8,30,1,31,1,31,3,31,477,8,31,1,31,1,31,1,31,3,31,482,8,31,1,32,1,
        32,1,32,1,33,1,33,1,33,5,33,490,8,33,10,33,12,33,493,9,33,1,34,1,
        34,3,34,497,8,34,1,34,1,34,1,34,3,34,502,8,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,3,36,513,8,36,5,36,515,8,36,10,36,12,36,
        518,9,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,526,8,36,5,36,528,8,
        36,10,36,12,36,531,9,36,1,36,1,36,1,36,1,36,1,36,3,36,538,8,36,5,
        36,540,8,36,10,36,12,36,543,9,36,1,36,1,36,1,36,1,36,1,36,1,36,3,
        36,551,8,36,3,36,553,8,36,1,37,1,37,1,37,1,38,1,38,1,38,1,38,3,38,
        562,8,38,1,38,1,38,3,38,566,8,38,1,38,1,38,1,38,5,38,571,8,38,10,
        38,12,38,574,9,38,3,38,576,8,38,1,39,1,39,1,39,1,39,1,39,1,39,1,
        39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,4,40,609,
        8,40,11,40,12,40,610,1,40,1,40,3,40,615,8,40,1,40,1,40,1,40,1,40,
        3,40,621,8,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,631,8,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,643,8,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,3,40,659,8,40,1,40,1,40,1,40,1,40,3,40,665,8,40,1,40,1,40,
        5,40,669,8,40,10,40,12,40,672,9,40,1,41,1,41,1,41,3,41,677,8,41,
        1,41,1,41,1,42,1,42,1,42,3,42,684,8,42,1,43,1,43,1,43,5,43,689,8,
        43,10,43,12,43,692,9,43,1,44,1,44,1,45,1,45,1,46,1,46,1,46,0,1,80,
        47,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,0,13,1,0,36,37,2,0,19,19,26,27,2,0,75,79,85,85,2,0,30,31,
        69,71,1,0,44,45,1,0,75,78,1,0,88,89,1,0,90,92,2,0,80,82,85,87,1,
        0,7,8,3,0,106,106,123,124,126,126,4,0,46,46,102,104,106,106,114,
        115,1,0,120,121,773,0,94,1,0,0,0,2,100,1,0,0,0,4,121,1,0,0,0,6,130,
        1,0,0,0,8,137,1,0,0,0,10,143,1,0,0,0,12,145,1,0,0,0,14,152,1,0,0,
        0,16,162,1,0,0,0,18,164,1,0,0,0,20,212,1,0,0,0,22,214,1,0,0,0,24,
        251,1,0,0,0,26,273,1,0,0,0,28,275,1,0,0,0,30,279,1,0,0,0,32,283,
        1,0,0,0,34,287,1,0,0,0,36,335,1,0,0,0,38,352,1,0,0,0,40,370,1,0,
        0,0,42,373,1,0,0,0,44,383,1,0,0,0,46,391,1,0,0,0,48,405,1,0,0,0,
        50,428,1,0,0,0,52,432,1,0,0,0,54,440,1,0,0,0,56,448,1,0,0,0,58,456,
        1,0,0,0,60,472,1,0,0,0,62,474,1,0,0,0,64,483,1,0,0,0,66,486,1,0,
        0,0,68,494,1,0,0,0,70,503,1,0,0,0,72,552,1,0,0,0,74,554,1,0,0,0,
        76,557,1,0,0,0,78,577,1,0,0,0,80,620,1,0,0,0,82,673,1,0,0,0,84,683,
        1,0,0,0,86,685,1,0,0,0,88,693,1,0,0,0,90,695,1,0,0,0,92,697,1,0,
        0,0,94,95,3,2,1,0,95,96,5,0,0,1,96,1,1,0,0,0,97,99,3,4,2,0,98,97,
        1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,3,1,0,
        0,0,102,100,1,0,0,0,103,105,3,6,3,0,104,106,5,99,0,0,105,104,1,0,
        0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,103,1,0,0,0,108,109,1,0,
        0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,115,1,0,0,0,111,113,5,2,
        0,0,112,114,5,99,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,116,1,0,
        0,0,115,111,1,0,0,0,115,116,1,0,0,0,116,122,1,0,0,0,117,119,5,2,
        0,0,118,120,5,99,0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,122,1,0,
        0,0,121,107,1,0,0,0,121,117,1,0,0,0,122,5,1,0,0,0,123,131,3,8,4,
        0,124,131,3,10,5,0,125,131,3,72,36,0,126,131,3,74,37,0,127,131,3,
        64,32,0,128,131,3,70,35,0,129,131,3,76,38,0,130,123,1,0,0,0,130,
        124,1,0,0,0,130,125,1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,0,130,
        128,1,0,0,0,130,129,1,0,0,0,131,7,1,0,0,0,132,138,3,12,6,0,133,138,
        3,26,13,0,134,138,3,28,14,0,135,138,3,30,15,0,136,138,3,32,16,0,
        137,132,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,0,0,0,
        137,136,1,0,0,0,138,9,1,0,0,0,139,144,3,34,17,0,140,144,3,48,24,
        0,141,144,3,56,28,0,142,144,3,62,31,0,143,139,1,0,0,0,143,140,1,
        0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,11,1,0,0,0,145,146,5,18,
        0,0,146,147,5,19,0,0,147,148,3,86,43,0,148,149,5,100,0,0,149,150,
        3,14,7,0,150,151,5,101,0,0,151,13,1,0,0,0,152,157,3,16,8,0,153,154,
        5,97,0,0,154,156,3,16,8,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,15,1,0,0,0,159,157,1,0,0,0,160,163,3,
        18,9,0,161,163,3,20,10,0,162,160,1,0,0,0,162,161,1,0,0,0,163,17,
        1,0,0,0,164,165,3,88,44,0,165,169,3,22,11,0,166,168,3,24,12,0,167,
        166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,
        19,1,0,0,0,171,169,1,0,0,0,172,173,5,38,0,0,173,175,3,88,44,0,174,
        172,1,0,0,0,174,175,1,0,0,0,175,179,1,0,0,0,176,177,5,22,0,0,177,
        180,5,23,0,0,178,180,5,40,0,0,179,176,1,0,0,0,179,178,1,0,0,0,180,
        182,1,0,0,0,181,183,7,0,0,0,182,181,1,0,0,0,182,183,1,0,0,0,183,
        184,1,0,0,0,184,185,5,100,0,0,185,186,3,52,26,0,186,187,5,101,0,
        0,187,213,1,0,0,0,188,189,5,38,0,0,189,191,3,88,44,0,190,188,1,0,
        0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,42,0,0,193,194,5,23,
        0,0,194,195,5,100,0,0,195,196,3,52,26,0,196,197,5,101,0,0,197,198,
        5,39,0,0,198,199,3,86,43,0,199,200,5,100,0,0,200,201,3,52,26,0,201,
        202,5,101,0,0,202,213,1,0,0,0,203,204,5,38,0,0,204,206,3,88,44,0,
        205,203,1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,207,208,5,41,0,0,
        208,209,5,100,0,0,209,210,3,80,40,0,210,211,5,101,0,0,211,213,1,
        0,0,0,212,174,1,0,0,0,212,190,1,0,0,0,212,205,1,0,0,0,213,21,1,0,
        0,0,214,225,3,88,44,0,215,218,5,100,0,0,216,219,5,103,0,0,217,219,
        3,88,44,0,218,216,1,0,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,221,
        5,97,0,0,221,223,5,103,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,224,
        1,0,0,0,224,226,5,101,0,0,225,215,1,0,0,0,225,226,1,0,0,0,226,23,
        1,0,0,0,227,228,5,9,0,0,228,252,5,46,0,0,229,252,5,46,0,0,230,231,
        5,22,0,0,231,233,5,23,0,0,232,234,7,0,0,0,233,232,1,0,0,0,233,234,
        1,0,0,0,234,252,1,0,0,0,235,236,5,62,0,0,236,252,3,80,40,0,237,243,
        5,63,0,0,238,239,5,100,0,0,239,240,5,103,0,0,240,241,5,97,0,0,241,
        242,5,103,0,0,242,244,5,101,0,0,243,238,1,0,0,0,243,244,1,0,0,0,
        244,252,1,0,0,0,245,246,5,39,0,0,246,247,3,86,43,0,247,248,5,100,
        0,0,248,249,3,88,44,0,249,250,5,101,0,0,250,252,1,0,0,0,251,227,
        1,0,0,0,251,229,1,0,0,0,251,230,1,0,0,0,251,235,1,0,0,0,251,237,
        1,0,0,0,251,245,1,0,0,0,252,25,1,0,0,0,253,254,5,20,0,0,254,255,
        5,19,0,0,255,256,3,86,43,0,256,257,5,24,0,0,257,258,3,18,9,0,258,
        274,1,0,0,0,259,260,5,20,0,0,260,261,5,19,0,0,261,262,3,86,43,0,
        262,263,5,21,0,0,263,264,5,25,0,0,264,265,3,88,44,0,265,274,1,0,
        0,0,266,267,5,20,0,0,267,268,5,19,0,0,268,269,3,86,43,0,269,270,
        5,20,0,0,270,271,5,25,0,0,271,272,3,18,9,0,272,274,1,0,0,0,273,253,
        1,0,0,0,273,259,1,0,0,0,273,266,1,0,0,0,274,27,1,0,0,0,275,276,5,
        21,0,0,276,277,7,1,0,0,277,278,3,86,43,0,278,29,1,0,0,0,279,280,
        5,3,0,0,280,281,5,19,0,0,281,282,3,86,43,0,282,31,1,0,0,0,283,284,
        5,28,0,0,284,285,3,88,44,0,285,33,1,0,0,0,286,288,3,78,39,0,287,
        286,1,0,0,0,287,288,1,0,0,0,288,289,1,0,0,0,289,291,5,4,0,0,290,
        292,5,11,0,0,291,290,1,0,0,0,291,292,1,0,0,0,292,295,1,0,0,0,293,
        294,5,64,0,0,294,296,5,103,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,
        297,1,0,0,0,297,319,3,36,18,0,298,299,5,5,0,0,299,303,3,40,20,0,
        300,302,3,42,21,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,
        0,303,304,1,0,0,0,304,308,1,0,0,0,305,303,1,0,0,0,306,307,5,6,0,
        0,307,309,3,80,40,0,308,306,1,0,0,0,308,309,1,0,0,0,309,313,1,0,
        0,0,310,311,5,33,0,0,311,312,5,34,0,0,312,314,3,44,22,0,313,310,
        1,0,0,0,313,314,1,0,0,0,314,317,1,0,0,0,315,316,5,35,0,0,316,318,
        3,80,40,0,317,315,1,0,0,0,317,318,1,0,0,0,318,320,1,0,0,0,319,298,
        1,0,0,0,319,320,1,0,0,0,320,324,1,0,0,0,321,322,5,43,0,0,322,323,
        5,34,0,0,323,325,3,46,23,0,324,321,1,0,0,0,324,325,1,0,0,0,325,35,
        1,0,0,0,326,336,5,90,0,0,327,332,3,38,19,0,328,329,5,97,0,0,329,
        331,3,38,19,0,330,328,1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,
        333,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,335,326,1,0,0,0,335,
        327,1,0,0,0,336,37,1,0,0,0,337,338,3,92,46,0,338,339,7,2,0,0,339,
        340,3,80,40,0,340,353,1,0,0,0,341,342,3,88,44,0,342,343,5,85,0,0,
        343,344,3,80,40,0,344,353,1,0,0,0,345,350,3,80,40,0,346,348,5,10,
        0,0,347,346,1,0,0,0,347,348,1,0,0,0,348,349,1,0,0,0,349,351,3,88,
        44,0,350,347,1,0,0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,337,1,0,
        0,0,352,341,1,0,0,0,352,345,1,0,0,0,353,39,1,0,0,0,354,359,3,86,
        43,0,355,357,5,10,0,0,356,355,1,0,0,0,356,357,1,0,0,0,357,358,1,
        0,0,0,358,360,3,88,44,0,359,356,1,0,0,0,359,360,1,0,0,0,360,371,
        1,0,0,0,361,362,5,100,0,0,362,363,3,34,17,0,363,368,5,101,0,0,364,
        366,5,10,0,0,365,364,1,0,0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,
        369,3,88,44,0,368,365,1,0,0,0,368,369,1,0,0,0,369,371,1,0,0,0,370,
        354,1,0,0,0,370,361,1,0,0,0,371,41,1,0,0,0,372,374,7,3,0,0,373,372,
        1,0,0,0,373,374,1,0,0,0,374,376,1,0,0,0,375,377,5,72,0,0,376,375,
        1,0,0,0,376,377,1,0,0,0,377,378,1,0,0,0,378,379,5,29,0,0,379,380,
        3,40,20,0,380,381,5,32,0,0,381,382,3,80,40,0,382,43,1,0,0,0,383,
        388,3,80,40,0,384,385,5,97,0,0,385,387,3,80,40,0,386,384,1,0,0,0,
        387,390,1,0,0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,45,1,0,0,0,390,
        388,1,0,0,0,391,393,3,80,40,0,392,394,7,4,0,0,393,392,1,0,0,0,393,
        394,1,0,0,0,394,402,1,0,0,0,395,396,5,97,0,0,396,398,3,80,40,0,397,
        399,7,4,0,0,398,397,1,0,0,0,398,399,1,0,0,0,399,401,1,0,0,0,400,
        395,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,
        47,1,0,0,0,404,402,1,0,0,0,405,407,5,12,0,0,406,408,5,13,0,0,407,
        406,1,0,0,0,407,408,1,0,0,0,408,409,1,0,0,0,409,414,3,86,43,0,410,
        411,5,100,0,0,411,412,3,52,26,0,412,413,5,101,0,0,413,415,1,0,0,
        0,414,410,1,0,0,0,414,415,1,0,0,0,415,426,1,0,0,0,416,417,5,14,0,
        0,417,422,3,50,25,0,418,419,5,97,0,0,419,421,3,50,25,0,420,418,1,
        0,0,0,421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,427,1,
        0,0,0,424,422,1,0,0,0,425,427,3,34,17,0,426,416,1,0,0,0,426,425,
        1,0,0,0,427,49,1,0,0,0,428,429,5,100,0,0,429,430,3,54,27,0,430,431,
        5,101,0,0,431,51,1,0,0,0,432,437,3,88,44,0,433,434,5,97,0,0,434,
        436,3,88,44,0,435,433,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,
        438,1,0,0,0,438,53,1,0,0,0,439,437,1,0,0,0,440,445,3,80,40,0,441,
        442,5,97,0,0,442,444,3,80,40,0,443,441,1,0,0,0,444,447,1,0,0,0,445,
        443,1,0,0,0,445,446,1,0,0,0,446,55,1,0,0,0,447,445,1,0,0,0,448,449,
        5,15,0,0,449,450,3,86,43,0,450,451,5,16,0,0,451,454,3,58,29,0,452,
        453,5,6,0,0,453,455,3,80,40,0,454,452,1,0,0,0,454,455,1,0,0,0,455,
        57,1,0,0,0,456,461,3,60,30,0,457,458,5,97,0,0,458,460,3,60,30,0,
        459,457,1,0,0,0,460,463,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,
        462,59,1,0,0,0,463,461,1,0,0,0,464,465,3,88,44,0,465,466,5,85,0,
        0,466,467,3,80,40,0,467,473,1,0,0,0,468,469,3,88,44,0,469,470,7,
        5,0,0,470,471,3,80,40,0,471,473,1,0,0,0,472,464,1,0,0,0,472,468,
        1,0,0,0,473,61,1,0,0,0,474,476,5,17,0,0,475,477,5,5,0,0,476,475,
        1,0,0,0,476,477,1,0,0,0,477,478,1,0,0,0,478,481,3,86,43,0,479,480,
        5,6,0,0,480,482,3,80,40,0,481,479,1,0,0,0,481,482,1,0,0,0,482,63,
        1,0,0,0,483,484,5,1,0,0,484,485,3,66,33,0,485,65,1,0,0,0,486,491,
        3,68,34,0,487,488,5,97,0,0,488,490,3,68,34,0,489,487,1,0,0,0,490,
        493,1,0,0,0,491,489,1,0,0,0,491,492,1,0,0,0,492,67,1,0,0,0,493,491,
        1,0,0,0,494,496,5,121,0,0,495,497,5,10,0,0,496,495,1,0,0,0,496,497,
        1,0,0,0,497,498,1,0,0,0,498,501,3,22,11,0,499,500,5,85,0,0,500,502,
        3,80,40,0,501,499,1,0,0,0,501,502,1,0,0,0,502,69,1,0,0,0,503,504,
        5,16,0,0,504,505,3,92,46,0,505,506,7,2,0,0,506,507,3,80,40,0,507,
        71,1,0,0,0,508,509,5,49,0,0,509,516,5,58,0,0,510,512,3,6,3,0,511,
        513,5,99,0,0,512,511,1,0,0,0,512,513,1,0,0,0,513,515,1,0,0,0,514,
        510,1,0,0,0,515,518,1,0,0,0,516,514,1,0,0,0,516,517,1,0,0,0,517,
        519,1,0,0,0,518,516,1,0,0,0,519,520,5,50,0,0,520,521,5,58,0,0,521,
        522,5,49,0,0,522,529,5,59,0,0,523,525,3,6,3,0,524,526,5,99,0,0,525,
        524,1,0,0,0,525,526,1,0,0,0,526,528,1,0,0,0,527,523,1,0,0,0,528,
        531,1,0,0,0,529,527,1,0,0,0,529,530,1,0,0,0,530,532,1,0,0,0,531,
        529,1,0,0,0,532,533,5,50,0,0,533,553,5,59,0,0,534,541,5,49,0,0,535,
        537,3,6,3,0,536,538,5,99,0,0,537,536,1,0,0,0,537,538,1,0,0,0,538,
        540,1,0,0,0,539,535,1,0,0,0,540,543,1,0,0,0,541,539,1,0,0,0,541,
        542,1,0,0,0,542,544,1,0,0,0,543,541,1,0,0,0,544,553,5,50,0,0,545,
        546,5,57,0,0,546,547,3,80,40,0,547,550,3,6,3,0,548,549,5,54,0,0,
        549,551,3,6,3,0,550,548,1,0,0,0,550,551,1,0,0,0,551,553,1,0,0,0,
        552,508,1,0,0,0,552,534,1,0,0,0,552,545,1,0,0,0,553,73,1,0,0,0,554,
        555,5,61,0,0,555,556,3,80,40,0,556,75,1,0,0,0,557,561,5,60,0,0,558,
        559,3,92,46,0,559,560,5,85,0,0,560,562,1,0,0,0,561,558,1,0,0,0,561,
        562,1,0,0,0,562,565,1,0,0,0,563,566,3,86,43,0,564,566,3,92,46,0,
        565,563,1,0,0,0,565,564,1,0,0,0,566,575,1,0,0,0,567,572,3,80,40,
        0,568,569,5,97,0,0,569,571,3,80,40,0,570,568,1,0,0,0,571,574,1,0,
        0,0,572,570,1,0,0,0,572,573,1,0,0,0,573,576,1,0,0,0,574,572,1,0,
        0,0,575,567,1,0,0,0,575,576,1,0,0,0,576,77,1,0,0,0,577,578,5,66,
        0,0,578,579,3,88,44,0,579,580,5,10,0,0,580,581,5,100,0,0,581,582,
        3,34,17,0,582,583,5,101,0,0,583,79,1,0,0,0,584,585,6,40,-1,0,585,
        586,5,100,0,0,586,587,3,80,40,0,587,588,5,101,0,0,588,621,1,0,0,
        0,589,590,7,6,0,0,590,621,3,80,40,16,591,592,5,9,0,0,592,621,3,80,
        40,15,593,594,5,55,0,0,594,595,5,100,0,0,595,596,3,34,17,0,596,597,
        5,101,0,0,597,621,1,0,0,0,598,599,5,100,0,0,599,600,3,34,17,0,600,
        601,5,101,0,0,601,621,1,0,0,0,602,608,5,51,0,0,603,604,5,52,0,0,
        604,605,3,80,40,0,605,606,5,53,0,0,606,607,3,80,40,0,607,609,1,0,
        0,0,608,603,1,0,0,0,609,610,1,0,0,0,610,608,1,0,0,0,610,611,1,0,
        0,0,611,614,1,0,0,0,612,613,5,54,0,0,613,615,3,80,40,0,614,612,1,
        0,0,0,614,615,1,0,0,0,615,616,1,0,0,0,616,617,5,50,0,0,617,621,1,
        0,0,0,618,621,3,82,41,0,619,621,3,84,42,0,620,584,1,0,0,0,620,589,
        1,0,0,0,620,591,1,0,0,0,620,593,1,0,0,0,620,598,1,0,0,0,620,602,
        1,0,0,0,620,618,1,0,0,0,620,619,1,0,0,0,621,670,1,0,0,0,622,623,
        10,14,0,0,623,624,7,7,0,0,624,669,3,80,40,15,625,626,10,13,0,0,626,
        627,7,6,0,0,627,669,3,80,40,14,628,630,10,12,0,0,629,631,5,9,0,0,
        630,629,1,0,0,0,630,631,1,0,0,0,631,632,1,0,0,0,632,633,5,73,0,0,
        633,634,3,80,40,0,634,635,5,7,0,0,635,636,3,80,40,13,636,669,1,0,
        0,0,637,638,10,11,0,0,638,639,7,8,0,0,639,669,3,80,40,12,640,642,
        10,10,0,0,641,643,5,9,0,0,642,641,1,0,0,0,642,643,1,0,0,0,643,644,
        1,0,0,0,644,645,5,74,0,0,645,669,3,80,40,11,646,647,10,9,0,0,647,
        648,7,9,0,0,648,669,3,80,40,10,649,650,10,8,0,0,650,651,5,47,0,0,
        651,669,5,46,0,0,652,653,10,7,0,0,653,654,5,47,0,0,654,655,5,9,0,
        0,655,669,5,46,0,0,656,658,10,6,0,0,657,659,5,9,0,0,658,657,1,0,
        0,0,658,659,1,0,0,0,659,660,1,0,0,0,660,661,5,56,0,0,661,664,5,100,
        0,0,662,665,3,54,27,0,663,665,3,34,17,0,664,662,1,0,0,0,664,663,
        1,0,0,0,665,666,1,0,0,0,666,667,5,101,0,0,667,669,1,0,0,0,668,622,
        1,0,0,0,668,625,1,0,0,0,668,628,1,0,0,0,668,637,1,0,0,0,668,640,
        1,0,0,0,668,646,1,0,0,0,668,649,1,0,0,0,668,652,1,0,0,0,668,656,
        1,0,0,0,669,672,1,0,0,0,670,668,1,0,0,0,670,671,1,0,0,0,671,81,1,
        0,0,0,672,670,1,0,0,0,673,674,3,88,44,0,674,676,5,100,0,0,675,677,
        3,54,27,0,676,675,1,0,0,0,676,677,1,0,0,0,677,678,1,0,0,0,678,679,
        5,101,0,0,679,83,1,0,0,0,680,684,3,86,43,0,681,684,3,90,45,0,682,
        684,3,92,46,0,683,680,1,0,0,0,683,681,1,0,0,0,683,682,1,0,0,0,684,
        85,1,0,0,0,685,690,3,88,44,0,686,687,5,98,0,0,687,689,3,88,44,0,
        688,686,1,0,0,0,689,692,1,0,0,0,690,688,1,0,0,0,690,691,1,0,0,0,
        691,87,1,0,0,0,692,690,1,0,0,0,693,694,7,10,0,0,694,89,1,0,0,0,695,
        696,7,11,0,0,696,91,1,0,0,0,697,698,7,12,0,0,698,93,1,0,0,0,89,100,
        105,109,113,115,119,121,130,137,143,157,162,169,174,179,182,190,
        205,212,218,222,225,233,243,251,273,287,291,295,303,308,313,317,
        319,324,332,335,347,350,352,356,359,365,368,370,373,376,388,393,
        398,402,407,414,422,426,437,445,454,461,472,476,481,491,496,501,
        512,516,525,529,537,541,550,552,561,565,572,575,610,614,620,630,
        642,658,664,668,670,676,683,690
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'>='", "'<='", "<INVALID>", 
                     "'!<'", "'!>'", "'='", "'>'", "'<'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", "'~'", "','", 
                     "'.'", "';'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*/'" ]

    symbolicNames = [ "<INVALID>", "DECLARE", "GO", "TRUNCATE", "SELECT", 
                      "FROM", "WHERE", "AND", "OR", "NOT", "AS", "DISTINCT", 
                      "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE", 
                      "CREATE", "TABLE", "ALTER", "DROP", "PRIMARY", "KEY", 
                      "ADD", "COLUMN", "VIEW", "PROCEDURE", "USE", "JOIN", 
                      "INNER", "LEFT", "ON", "GROUP", "BY", "HAVING", "CLUSTERED", 
                      "NONCLUSTERED", "CONSTRAINT", "REFERENCES", "UNIQUE", 
                      "CHECK", "FOREIGN", "ORDER", "ASC", "DESC", "NULL", 
                      "IS", "UNION", "BEGIN", "END", "CASE", "WHEN", "THEN", 
                      "ELSE", "EXISTS", "IN", "IF", "TRY", "CATCH", "EXEC", 
                      "PRINT", "DEFAULT", "IDENTITY", "TOP", "OUTPUT", "WITH", 
                      "OVER", "PARTITION", "RIGHT", "FULL", "CROSS", "OUTER", 
                      "BETWEEN", "LIKE", "PLUS_ASSIGN", "MINUS_ASSIGN", 
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
    RULE_table_element_list = 7
    RULE_table_element = 8
    RULE_column_def = 9
    RULE_table_constraint = 10
    RULE_data_type = 11
    RULE_column_constraint = 12
    RULE_alter_statement = 13
    RULE_drop_statement = 14
    RULE_truncate_statement = 15
    RULE_use_statement = 16
    RULE_select_statement = 17
    RULE_select_list = 18
    RULE_select_item = 19
    RULE_table_source = 20
    RULE_join_part = 21
    RULE_group_list = 22
    RULE_order_list = 23
    RULE_insert_statement = 24
    RULE_expression_list_parens = 25
    RULE_column_list = 26
    RULE_expression_list = 27
    RULE_update_statement = 28
    RULE_assignment_list = 29
    RULE_assignment = 30
    RULE_delete_statement = 31
    RULE_declare_statement = 32
    RULE_declare_list = 33
    RULE_declare_item = 34
    RULE_set_statement = 35
    RULE_control_flow_statement = 36
    RULE_print_statement = 37
    RULE_execute_statement = 38
    RULE_with_expression = 39
    RULE_expression = 40
    RULE_function_call = 41
    RULE_atom = 42
    RULE_table_name = 43
    RULE_id_name = 44
    RULE_constant = 45
    RULE_variable = 46

    ruleNames =  [ "root", "sql_script", "batch", "sql_statement", "ddl_statement", 
                   "dml_statement", "create_statement", "table_element_list", 
                   "table_element", "column_def", "table_constraint", "data_type", 
                   "column_constraint", "alter_statement", "drop_statement", 
                   "truncate_statement", "use_statement", "select_statement", 
                   "select_list", "select_item", "table_source", "join_part", 
                   "group_list", "order_list", "insert_statement", "expression_list_parens", 
                   "column_list", "expression_list", "update_statement", 
                   "assignment_list", "assignment", "delete_statement", 
                   "declare_statement", "declare_list", "declare_item", 
                   "set_statement", "control_flow_statement", "print_statement", 
                   "execute_statement", "with_expression", "expression", 
                   "function_call", "atom", "table_name", "id_name", "constant", 
                   "variable" ]

    EOF = Token.EOF
    DECLARE=1
    GO=2
    TRUNCATE=3
    SELECT=4
    FROM=5
    WHERE=6
    AND=7
    OR=8
    NOT=9
    AS=10
    DISTINCT=11
    INSERT=12
    INTO=13
    VALUES=14
    UPDATE=15
    SET=16
    DELETE=17
    CREATE=18
    TABLE=19
    ALTER=20
    DROP=21
    PRIMARY=22
    KEY=23
    ADD=24
    COLUMN=25
    VIEW=26
    PROCEDURE=27
    USE=28
    JOIN=29
    INNER=30
    LEFT=31
    ON=32
    GROUP=33
    BY=34
    HAVING=35
    CLUSTERED=36
    NONCLUSTERED=37
    CONSTRAINT=38
    REFERENCES=39
    UNIQUE=40
    CHECK=41
    FOREIGN=42
    ORDER=43
    ASC=44
    DESC=45
    NULL=46
    IS=47
    UNION=48
    BEGIN=49
    END=50
    CASE=51
    WHEN=52
    THEN=53
    ELSE=54
    EXISTS=55
    IN=56
    IF=57
    TRY=58
    CATCH=59
    EXEC=60
    PRINT=61
    DEFAULT=62
    IDENTITY=63
    TOP=64
    OUTPUT=65
    WITH=66
    OVER=67
    PARTITION=68
    RIGHT=69
    FULL=70
    CROSS=71
    OUTER=72
    BETWEEN=73
    LIKE=74
    PLUS_ASSIGN=75
    MINUS_ASSIGN=76
    STAR_ASSIGN=77
    SLASH_ASSIGN=78
    PERCENT_ASSIGN=79
    GE=80
    LE=81
    NEQ=82
    NOT_LESS=83
    NOT_GREATER=84
    EQ=85
    GT=86
    LT=87
    PLUS=88
    MINUS=89
    STAR=90
    SLASH=91
    PERCENT=92
    BIT_AND=93
    BIT_OR=94
    BIT_XOR=95
    BIT_NOT=96
    COMMA=97
    DOT=98
    SEMI=99
    LPAREN=100
    RPAREN=101
    FLOAT=102
    INT=103
    NSTRING=104
    UNCLOSED_NSTRING_EOF=105
    STRING=106
    UNCLOSED_STRING_EOF=107
    LINE_COMMENT=108
    BLOCK_COMMENT_START=109
    NESTED_BLOCK_START=110
    BLOCK_COMMENT_END=111
    COMMENT_TEXT=112
    UNTERMINATED_BLOCK_COMMENT=113
    TRUE=114
    FALSE=115
    HEX_LITERAL=116
    INVALID_HEX_LITERAL=117
    BIT_STRING=118
    INVALID_BIT_STRING=119
    GLOBAL_VAR=120
    LOCAL_VAR=121
    TEMP_ID=122
    BRACKET_ID=123
    DQUOTED_ID=124
    UNCLOSED_BRACKET_ID=125
    ID=126
    WS=127
    ERROR_CHAR=128

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
            self.state = 94
            self.sql_script()
            self.state = 95
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
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3603442652121894942) != 0) or _la==66:
                self.state = 97
                self.batch()
                self.state = 102
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
        def SEMI(self):
            return self.getToken(SQLParser.SEMI, 0)

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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 12, 15, 16, 17, 18, 20, 21, 28, 49, 57, 60, 61, 66]:
                localctx = SQLParser.StatementBatchContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 103
                        self.sql_statement()
                        self.state = 105
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==99:
                            self.state = 104
                            self.match(SQLParser.SEMI)



                    else:
                        raise NoViableAltException(self)
                    self.state = 109 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 115
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 111
                    self.match(SQLParser.GO)
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==99:
                        self.state = 112
                        self.match(SQLParser.SEMI)




                pass
            elif token in [2]:
                localctx = SQLParser.EmptyGoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(SQLParser.GO)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==99:
                    self.state = 118
                    self.match(SQLParser.SEMI)


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
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 18, 20, 21, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.ddl_statement()
                pass
            elif token in [4, 12, 15, 17, 66]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.dml_statement()
                pass
            elif token in [49, 57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.control_flow_statement()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.print_statement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.declare_statement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.set_statement()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
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


        def truncate_statement(self):
            return self.getTypedRuleContext(SQLParser.Truncate_statementContext,0)


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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.create_statement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.alter_statement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.drop_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.truncate_statement()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 66]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.select_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.insert_statement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.update_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
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

        def table_element_list(self):
            return self.getTypedRuleContext(SQLParser.Table_element_listContext,0)


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
            self.state = 145
            self.match(SQLParser.CREATE)
            self.state = 146
            self.match(SQLParser.TABLE)
            self.state = 147
            self.table_name()
            self.state = 148
            self.match(SQLParser.LPAREN)
            self.state = 149
            self.table_element_list()
            self.state = 150
            self.match(SQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Table_elementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Table_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_table_element_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_element_list" ):
                listener.enterTable_element_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_element_list" ):
                listener.exitTable_element_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_element_list" ):
                return visitor.visitTable_element_list(self)
            else:
                return visitor.visitChildren(self)




    def table_element_list(self):

        localctx = SQLParser.Table_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_table_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.table_element()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 153
                self.match(SQLParser.COMMA)
                self.state = 154
                self.table_element()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_def(self):
            return self.getTypedRuleContext(SQLParser.Column_defContext,0)


        def table_constraint(self):
            return self.getTypedRuleContext(SQLParser.Table_constraintContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_element" ):
                listener.enterTable_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_element" ):
                listener.exitTable_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_element" ):
                return visitor.visitTable_element(self)
            else:
                return visitor.visitChildren(self)




    def table_element(self):

        localctx = SQLParser.Table_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_table_element)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [106, 123, 124, 126]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.column_def()
                pass
            elif token in [22, 38, 40, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.table_constraint()
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
        self.enterRule(localctx, 18, self.RULE_column_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.id_name()
            self.state = 165
            self.data_type()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611615099923201536) != 0):
                self.state = 166
                self.column_constraint()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.LPAREN)
            else:
                return self.getToken(SQLParser.LPAREN, i)

        def column_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Column_listContext)
            else:
                return self.getTypedRuleContext(SQLParser.Column_listContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.RPAREN)
            else:
                return self.getToken(SQLParser.RPAREN, i)

        def PRIMARY(self):
            return self.getToken(SQLParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(SQLParser.KEY, 0)

        def UNIQUE(self):
            return self.getToken(SQLParser.UNIQUE, 0)

        def CONSTRAINT(self):
            return self.getToken(SQLParser.CONSTRAINT, 0)

        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


        def CLUSTERED(self):
            return self.getToken(SQLParser.CLUSTERED, 0)

        def NONCLUSTERED(self):
            return self.getToken(SQLParser.NONCLUSTERED, 0)

        def FOREIGN(self):
            return self.getToken(SQLParser.FOREIGN, 0)

        def REFERENCES(self):
            return self.getToken(SQLParser.REFERENCES, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def CHECK(self):
            return self.getToken(SQLParser.CHECK, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_constraint" ):
                listener.enterTable_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_constraint" ):
                listener.exitTable_constraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_constraint" ):
                return visitor.visitTable_constraint(self)
            else:
                return visitor.visitChildren(self)




    def table_constraint(self):

        localctx = SQLParser.Table_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_table_constraint)
        self._la = 0 # Token type
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 172
                    self.match(SQLParser.CONSTRAINT)
                    self.state = 173
                    self.id_name()


                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22]:
                    self.state = 176
                    self.match(SQLParser.PRIMARY)
                    self.state = 177
                    self.match(SQLParser.KEY)
                    pass
                elif token in [40]:
                    self.state = 178
                    self.match(SQLParser.UNIQUE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36 or _la==37:
                    self.state = 181
                    _la = self._input.LA(1)
                    if not(_la==36 or _la==37):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 184
                self.match(SQLParser.LPAREN)
                self.state = 185
                self.column_list()
                self.state = 186
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 188
                    self.match(SQLParser.CONSTRAINT)
                    self.state = 189
                    self.id_name()


                self.state = 192
                self.match(SQLParser.FOREIGN)
                self.state = 193
                self.match(SQLParser.KEY)
                self.state = 194
                self.match(SQLParser.LPAREN)
                self.state = 195
                self.column_list()
                self.state = 196
                self.match(SQLParser.RPAREN)
                self.state = 197
                self.match(SQLParser.REFERENCES)
                self.state = 198
                self.table_name()
                self.state = 199
                self.match(SQLParser.LPAREN)
                self.state = 200
                self.column_list()
                self.state = 201
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 203
                    self.match(SQLParser.CONSTRAINT)
                    self.state = 204
                    self.id_name()


                self.state = 207
                self.match(SQLParser.CHECK)
                self.state = 208
                self.match(SQLParser.LPAREN)
                self.state = 209
                self.expression(0)
                self.state = 210
                self.match(SQLParser.RPAREN)
                pass


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
        self.enterRule(localctx, 22, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.id_name()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==100:
                self.state = 215
                self.match(SQLParser.LPAREN)
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [103]:
                    self.state = 216
                    self.match(SQLParser.INT)
                    pass
                elif token in [106, 123, 124, 126]:
                    self.state = 217
                    self.id_name()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==97:
                    self.state = 220
                    self.match(SQLParser.COMMA)
                    self.state = 221
                    self.match(SQLParser.INT)


                self.state = 224
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

        def CLUSTERED(self):
            return self.getToken(SQLParser.CLUSTERED, 0)

        def NONCLUSTERED(self):
            return self.getToken(SQLParser.NONCLUSTERED, 0)

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

        def REFERENCES(self):
            return self.getToken(SQLParser.REFERENCES, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def id_name(self):
            return self.getTypedRuleContext(SQLParser.Id_nameContext,0)


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
        self.enterRule(localctx, 24, self.RULE_column_constraint)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(SQLParser.NOT)
                self.state = 228
                self.match(SQLParser.NULL)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(SQLParser.NULL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(SQLParser.PRIMARY)
                self.state = 231
                self.match(SQLParser.KEY)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36 or _la==37:
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==36 or _la==37):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(SQLParser.DEFAULT)
                self.state = 236
                self.expression(0)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 5)
                self.state = 237
                self.match(SQLParser.IDENTITY)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==100:
                    self.state = 238
                    self.match(SQLParser.LPAREN)
                    self.state = 239
                    self.match(SQLParser.INT)
                    self.state = 240
                    self.match(SQLParser.COMMA)
                    self.state = 241
                    self.match(SQLParser.INT)
                    self.state = 242
                    self.match(SQLParser.RPAREN)


                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.match(SQLParser.REFERENCES)
                self.state = 246
                self.table_name()
                self.state = 247
                self.match(SQLParser.LPAREN)
                self.state = 248
                self.id_name()
                self.state = 249
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
        self.enterRule(localctx, 26, self.RULE_alter_statement)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = SQLParser.AlterAddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(SQLParser.ALTER)
                self.state = 254
                self.match(SQLParser.TABLE)
                self.state = 255
                self.table_name()
                self.state = 256
                self.match(SQLParser.ADD)
                self.state = 257
                self.column_def()
                pass

            elif la_ == 2:
                localctx = SQLParser.AlterDropContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(SQLParser.ALTER)
                self.state = 260
                self.match(SQLParser.TABLE)
                self.state = 261
                self.table_name()
                self.state = 262
                self.match(SQLParser.DROP)
                self.state = 263
                self.match(SQLParser.COLUMN)
                self.state = 264
                self.id_name()
                pass

            elif la_ == 3:
                localctx = SQLParser.AlterModifyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.match(SQLParser.ALTER)
                self.state = 267
                self.match(SQLParser.TABLE)
                self.state = 268
                self.table_name()
                self.state = 269
                self.match(SQLParser.ALTER)
                self.state = 270
                self.match(SQLParser.COLUMN)
                self.state = 271
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
        self.enterRule(localctx, 28, self.RULE_drop_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(SQLParser.DROP)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 201850880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 277
            self.table_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Truncate_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUNCATE(self):
            return self.getToken(SQLParser.TRUNCATE, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_truncate_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncate_statement" ):
                listener.enterTruncate_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncate_statement" ):
                listener.exitTruncate_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncate_statement" ):
                return visitor.visitTruncate_statement(self)
            else:
                return visitor.visitChildren(self)




    def truncate_statement(self):

        localctx = SQLParser.Truncate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_truncate_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(SQLParser.TRUNCATE)
            self.state = 280
            self.match(SQLParser.TABLE)
            self.state = 281
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
        self.enterRule(localctx, 32, self.RULE_use_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(SQLParser.USE)
            self.state = 284
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
        self.enterRule(localctx, 34, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 286
                self.with_expression()


            self.state = 289
            self.match(SQLParser.SELECT)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 290
                self.match(SQLParser.DISTINCT)


            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 293
                self.match(SQLParser.TOP)
                self.state = 294
                self.match(SQLParser.INT)


            self.state = 297
            self.select_list()
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 298
                self.match(SQLParser.FROM)
                self.state = 299
                self.table_source()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 16492674416647) != 0):
                    self.state = 300
                    self.join_part()
                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 306
                    self.match(SQLParser.WHERE)
                    self.state = 307
                    self.expression(0)


                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 310
                    self.match(SQLParser.GROUP)
                    self.state = 311
                    self.match(SQLParser.BY)
                    self.state = 312
                    self.group_list()


                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 315
                    self.match(SQLParser.HAVING)
                    self.state = 316
                    self.expression(0)




            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 321
                self.match(SQLParser.ORDER)
                self.state = 322
                self.match(SQLParser.BY)
                self.state = 323
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
        self.enterRule(localctx, 36, self.RULE_select_list)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [90]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(SQLParser.STAR)
                pass
            elif token in [9, 46, 51, 55, 88, 89, 100, 102, 103, 104, 106, 114, 115, 120, 121, 123, 124, 126]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.select_item()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==97:
                    self.state = 328
                    self.match(SQLParser.COMMA)
                    self.state = 329
                    self.select_item()
                    self.state = 334
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
        self.enterRule(localctx, 38, self.RULE_select_item)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = SQLParser.SelectVarAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.variable()
                self.state = 338
                _la = self._input.LA(1)
                if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1055) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = SQLParser.SelectAliasAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.id_name()
                self.state = 342
                self.match(SQLParser.EQ)
                self.state = 343
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = SQLParser.SelectExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.expression(0)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & 1441793) != 0):
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 346
                        self.match(SQLParser.AS)


                    self.state = 349
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
        self.enterRule(localctx, 40, self.RULE_table_source)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [106, 123, 124, 126]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.table_name()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & 1441793) != 0):
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 355
                        self.match(SQLParser.AS)


                    self.state = 358
                    self.id_name()


                pass
            elif token in [100]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(SQLParser.LPAREN)
                self.state = 362
                self.select_statement()
                self.state = 363
                self.match(SQLParser.RPAREN)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & 1441793) != 0):
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 364
                        self.match(SQLParser.AS)


                    self.state = 367
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
        self.enterRule(localctx, 42, self.RULE_join_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 3848290697219) != 0):
                self.state = 372
                _la = self._input.LA(1)
                if not(((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 3848290697219) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==72:
                self.state = 375
                self.match(SQLParser.OUTER)


            self.state = 378
            self.match(SQLParser.JOIN)
            self.state = 379
            self.table_source()
            self.state = 380
            self.match(SQLParser.ON)
            self.state = 381
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
        self.enterRule(localctx, 44, self.RULE_group_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expression(0)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 384
                self.match(SQLParser.COMMA)
                self.state = 385
                self.expression(0)
                self.state = 390
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
        self.enterRule(localctx, 46, self.RULE_order_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.expression(0)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44 or _la==45:
                self.state = 392
                _la = self._input.LA(1)
                if not(_la==44 or _la==45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 395
                self.match(SQLParser.COMMA)
                self.state = 396
                self.expression(0)
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44 or _la==45:
                    self.state = 397
                    _la = self._input.LA(1)
                    if not(_la==44 or _la==45):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 404
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

        def expression_list_parens(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Expression_list_parensContext)
            else:
                return self.getTypedRuleContext(SQLParser.Expression_list_parensContext,i)


        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def column_list(self):
            return self.getTypedRuleContext(SQLParser.Column_listContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

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
        self.enterRule(localctx, 48, self.RULE_insert_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(SQLParser.INSERT)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 406
                self.match(SQLParser.INTO)


            self.state = 409
            self.table_name()
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==100:
                self.state = 410
                self.match(SQLParser.LPAREN)
                self.state = 411
                self.column_list()
                self.state = 412
                self.match(SQLParser.RPAREN)


            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 416
                self.match(SQLParser.VALUES)
                self.state = 417
                self.expression_list_parens()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==97:
                    self.state = 418
                    self.match(SQLParser.COMMA)
                    self.state = 419
                    self.expression_list_parens()
                    self.state = 424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [4, 66]:
                self.state = 425
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


    class Expression_list_parensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(SQLParser.Expression_listContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_expression_list_parens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list_parens" ):
                listener.enterExpression_list_parens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list_parens" ):
                listener.exitExpression_list_parens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list_parens" ):
                return visitor.visitExpression_list_parens(self)
            else:
                return visitor.visitChildren(self)




    def expression_list_parens(self):

        localctx = SQLParser.Expression_list_parensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression_list_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(SQLParser.LPAREN)
            self.state = 429
            self.expression_list()
            self.state = 430
            self.match(SQLParser.RPAREN)
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
        self.enterRule(localctx, 52, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.id_name()
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 433
                self.match(SQLParser.COMMA)
                self.state = 434
                self.id_name()
                self.state = 439
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
        self.enterRule(localctx, 54, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.expression(0)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 441
                self.match(SQLParser.COMMA)
                self.state = 442
                self.expression(0)
                self.state = 447
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
        self.enterRule(localctx, 56, self.RULE_update_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(SQLParser.UPDATE)
            self.state = 449
            self.table_name()
            self.state = 450
            self.match(SQLParser.SET)
            self.state = 451
            self.assignment_list()
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 452
                self.match(SQLParser.WHERE)
                self.state = 453
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
        self.enterRule(localctx, 58, self.RULE_assignment_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.assignment()
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 457
                self.match(SQLParser.COMMA)
                self.state = 458
                self.assignment()
                self.state = 463
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
        self.enterRule(localctx, 60, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.id_name()
                self.state = 465
                self.match(SQLParser.EQ)
                self.state = 466
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.id_name()
                self.state = 469
                _la = self._input.LA(1)
                if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 15) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 470
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
        self.enterRule(localctx, 62, self.RULE_delete_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(SQLParser.DELETE)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 475
                self.match(SQLParser.FROM)


            self.state = 478
            self.table_name()
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 479
                self.match(SQLParser.WHERE)
                self.state = 480
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
        self.enterRule(localctx, 64, self.RULE_declare_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(SQLParser.DECLARE)
            self.state = 484
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
        self.enterRule(localctx, 66, self.RULE_declare_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.declare_item()
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==97:
                self.state = 487
                self.match(SQLParser.COMMA)
                self.state = 488
                self.declare_item()
                self.state = 493
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
        self.enterRule(localctx, 68, self.RULE_declare_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(SQLParser.LOCAL_VAR)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 495
                self.match(SQLParser.AS)


            self.state = 498
            self.data_type()
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==85:
                self.state = 499
                self.match(SQLParser.EQ)
                self.state = 500
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
        self.enterRule(localctx, 70, self.RULE_set_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(SQLParser.SET)
            self.state = 504
            self.variable()
            self.state = 505
            _la = self._input.LA(1)
            if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 1055) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 506
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
        self.enterRule(localctx, 72, self.RULE_control_flow_statement)
        self._la = 0 # Token type
        try:
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(SQLParser.BEGIN)
                self.state = 509
                self.match(SQLParser.TRY)
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3603442652121894938) != 0) or _la==66:
                    self.state = 510
                    self.sql_statement()
                    self.state = 512
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==99:
                        self.state = 511
                        self.match(SQLParser.SEMI)


                    self.state = 518
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 519
                self.match(SQLParser.END)
                self.state = 520
                self.match(SQLParser.TRY)
                self.state = 521
                self.match(SQLParser.BEGIN)
                self.state = 522
                self.match(SQLParser.CATCH)
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3603442652121894938) != 0) or _la==66:
                    self.state = 523
                    self.sql_statement()
                    self.state = 525
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==99:
                        self.state = 524
                        self.match(SQLParser.SEMI)


                    self.state = 531
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 532
                self.match(SQLParser.END)
                self.state = 533
                self.match(SQLParser.CATCH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
                self.match(SQLParser.BEGIN)
                self.state = 541
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3603442652121894938) != 0) or _la==66:
                    self.state = 535
                    self.sql_statement()
                    self.state = 537
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==99:
                        self.state = 536
                        self.match(SQLParser.SEMI)


                    self.state = 543
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 544
                self.match(SQLParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 545
                self.match(SQLParser.IF)
                self.state = 546
                self.expression(0)
                self.state = 547
                self.sql_statement()
                self.state = 550
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.match(SQLParser.ELSE)
                    self.state = 549
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
        self.enterRule(localctx, 74, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(SQLParser.PRINT)
            self.state = 555
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
        self.enterRule(localctx, 76, self.RULE_execute_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(SQLParser.EXEC)
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 558
                self.variable()
                self.state = 559
                self.match(SQLParser.EQ)


            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [106, 123, 124, 126]:
                self.state = 563
                self.table_name()
                pass
            elif token in [120, 121]:
                self.state = 564
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 38350965576827392) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & 391043731459) != 0):
                self.state = 567
                self.expression(0)
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==97:
                    self.state = 568
                    self.match(SQLParser.COMMA)
                    self.state = 569
                    self.expression(0)
                    self.state = 574
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
        self.enterRule(localctx, 78, self.RULE_with_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.match(SQLParser.WITH)
            self.state = 578
            self.id_name()
            self.state = 579
            self.match(SQLParser.AS)
            self.state = 580
            self.match(SQLParser.LPAREN)
            self.state = 581
            self.select_statement()
            self.state = 582
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
        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

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


    class BetweenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)
        def AND(self):
            return self.getToken(SQLParser.AND, 0)
        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenExpr" ):
                listener.enterBetweenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenExpr" ):
                listener.exitBetweenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenExpr" ):
                return visitor.visitBetweenExpr(self)
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


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)

        def PLUS(self):
            return self.getToken(SQLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SQLParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
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


    class ScalarSubqueryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SQLParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)
        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarSubqueryExpr" ):
                listener.enterScalarSubqueryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarSubqueryExpr" ):
                listener.exitScalarSubqueryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarSubqueryExpr" ):
                return visitor.visitScalarSubqueryExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                localctx = SQLParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 585
                self.match(SQLParser.LPAREN)
                self.state = 586
                self.expression(0)
                self.state = 587
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SQLParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 589
                _la = self._input.LA(1)
                if not(_la==88 or _la==89):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 590
                self.expression(16)
                pass

            elif la_ == 3:
                localctx = SQLParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 591
                self.match(SQLParser.NOT)
                self.state = 592
                self.expression(15)
                pass

            elif la_ == 4:
                localctx = SQLParser.ExistsExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 593
                self.match(SQLParser.EXISTS)
                self.state = 594
                self.match(SQLParser.LPAREN)
                self.state = 595
                self.select_statement()
                self.state = 596
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = SQLParser.ScalarSubqueryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 598
                self.match(SQLParser.LPAREN)
                self.state = 599
                self.select_statement()
                self.state = 600
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = SQLParser.CaseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 602
                self.match(SQLParser.CASE)
                self.state = 608 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 603
                    self.match(SQLParser.WHEN)
                    self.state = 604
                    self.expression(0)
                    self.state = 605
                    self.match(SQLParser.THEN)
                    self.state = 606
                    self.expression(0)
                    self.state = 610 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==52):
                        break

                self.state = 614
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==54:
                    self.state = 612
                    self.match(SQLParser.ELSE)
                    self.state = 613
                    self.expression(0)


                self.state = 616
                self.match(SQLParser.END)
                pass

            elif la_ == 7:
                localctx = SQLParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 618
                self.function_call()
                pass

            elif la_ == 8:
                localctx = SQLParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 619
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 670
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 668
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                    if la_ == 1:
                        localctx = SQLParser.MultiplicativeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 622
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 623
                        _la = self._input.LA(1)
                        if not(((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & 7) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 624
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = SQLParser.AdditiveExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 625
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 626
                        _la = self._input.LA(1)
                        if not(_la==88 or _la==89):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 627
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = SQLParser.BetweenExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 628
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 630
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 629
                            self.match(SQLParser.NOT)


                        self.state = 632
                        self.match(SQLParser.BETWEEN)
                        self.state = 633
                        self.expression(0)
                        self.state = 634
                        self.match(SQLParser.AND)
                        self.state = 635
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = SQLParser.ComparisonExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 637
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 638
                        _la = self._input.LA(1)
                        if not(((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 231) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 639
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = SQLParser.LikeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 640
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 642
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 641
                            self.match(SQLParser.NOT)


                        self.state = 644
                        self.match(SQLParser.LIKE)
                        self.state = 645
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = SQLParser.LogicalExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 646
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 647
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 648
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = SQLParser.IsNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 649
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 650
                        self.match(SQLParser.IS)
                        self.state = 651
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 8:
                        localctx = SQLParser.IsNotNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 652
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 653
                        self.match(SQLParser.IS)
                        self.state = 654
                        self.match(SQLParser.NOT)
                        self.state = 655
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 9:
                        localctx = SQLParser.InExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 656
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 658
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 657
                            self.match(SQLParser.NOT)


                        self.state = 660
                        self.match(SQLParser.IN)
                        self.state = 661
                        self.match(SQLParser.LPAREN)
                        self.state = 664
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [9, 46, 51, 55, 88, 89, 100, 102, 103, 104, 106, 114, 115, 120, 121, 123, 124, 126]:
                            self.state = 662
                            self.expression_list()
                            pass
                        elif token in [4, 66]:
                            self.state = 663
                            self.select_statement()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 666
                        self.match(SQLParser.RPAREN)
                        pass

             
                self.state = 672
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.id_name()
            self.state = 674
            self.match(SQLParser.LPAREN)
            self.state = 676
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 38350965576827392) != 0) or ((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & 391043731459) != 0):
                self.state = 675
                self.expression_list()


            self.state = 678
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
        self.enterRule(localctx, 84, self.RULE_atom)
        try:
            self.state = 683
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.table_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 681
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 682
                self.variable()
                pass


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
        self.enterRule(localctx, 86, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.id_name()
            self.state = 690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,88,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 686
                    self.match(SQLParser.DOT)
                    self.state = 687
                    self.id_name() 
                self.state = 692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,88,self._ctx)

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

        def STRING(self):
            return self.getToken(SQLParser.STRING, 0)

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
        self.enterRule(localctx, 88, self.RULE_id_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            _la = self._input.LA(1)
            if not(((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & 1441793) != 0)):
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
        self.enterRule(localctx, 90, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            _la = self._input.LA(1)
            if not(_la==46 or ((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & 12311) != 0)):
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
        self.enterRule(localctx, 92, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 697
            _la = self._input.LA(1)
            if not(_la==120 or _la==121):
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
        self._predicates[40] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         





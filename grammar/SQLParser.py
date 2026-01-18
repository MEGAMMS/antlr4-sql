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
        4,1,121,639,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,1,0,
        1,1,5,1,95,8,1,10,1,12,1,98,9,1,1,2,1,2,3,2,102,8,2,4,2,104,8,2,
        11,2,12,2,105,1,2,1,2,3,2,110,8,2,3,2,112,8,2,1,2,1,2,3,2,116,8,
        2,3,2,118,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,127,8,3,1,4,1,4,1,
        4,1,4,1,4,3,4,134,8,4,1,5,1,5,1,5,1,5,3,5,140,8,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,152,8,7,10,7,12,7,155,9,7,1,8,1,8,
        1,8,5,8,160,8,8,10,8,12,8,163,9,8,1,9,1,9,1,9,1,9,3,9,169,8,9,1,
        9,1,9,3,9,173,8,9,1,9,3,9,176,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,191,8,10,3,10,193,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,215,8,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,3,15,229,8,15,1,15,1,
        15,3,15,233,8,15,1,15,1,15,3,15,237,8,15,1,15,1,15,1,15,1,15,5,15,
        243,8,15,10,15,12,15,246,9,15,1,15,1,15,3,15,250,8,15,1,15,1,15,
        1,15,3,15,255,8,15,1,15,1,15,3,15,259,8,15,3,15,261,8,15,1,15,1,
        15,1,15,3,15,266,8,15,1,16,1,16,1,16,1,16,5,16,272,8,16,10,16,12,
        16,275,9,16,3,16,277,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,3,17,289,8,17,1,17,3,17,292,8,17,3,17,294,8,17,1,18,1,
        18,3,18,298,8,18,1,18,3,18,301,8,18,1,18,1,18,1,18,1,18,3,18,307,
        8,18,1,18,3,18,310,8,18,3,18,312,8,18,1,19,3,19,315,8,19,1,19,3,
        19,318,8,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,20,328,8,20,
        10,20,12,20,331,9,20,1,21,1,21,3,21,335,8,21,1,21,1,21,1,21,3,21,
        340,8,21,5,21,342,8,21,10,21,12,21,345,9,21,1,22,1,22,3,22,349,8,
        22,1,22,1,22,1,22,1,22,1,22,3,22,356,8,22,1,22,1,22,1,22,1,22,5,
        22,362,8,22,10,22,12,22,365,9,22,1,22,3,22,368,8,22,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,5,24,377,8,24,10,24,12,24,380,9,24,1,25,1,
        25,1,25,5,25,385,8,25,10,25,12,25,388,9,25,1,26,1,26,1,26,1,26,1,
        26,1,26,3,26,396,8,26,1,27,1,27,1,27,5,27,401,8,27,10,27,12,27,404,
        9,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,414,8,28,1,29,
        1,29,3,29,418,8,29,1,29,1,29,1,29,3,29,423,8,29,1,30,1,30,1,30,1,
        31,1,31,1,31,5,31,431,8,31,10,31,12,31,434,9,31,1,32,1,32,3,32,438,
        8,32,1,32,1,32,1,32,3,32,443,8,32,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,34,3,34,454,8,34,5,34,456,8,34,10,34,12,34,459,9,34,
        1,34,1,34,1,34,1,34,1,34,1,34,3,34,467,8,34,5,34,469,8,34,10,34,
        12,34,472,9,34,1,34,1,34,1,34,1,34,1,34,3,34,479,8,34,5,34,481,8,
        34,10,34,12,34,484,9,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,492,8,
        34,3,34,494,8,34,1,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,503,8,36,
        1,36,1,36,3,36,507,8,36,1,36,1,36,1,36,5,36,512,8,36,10,36,12,36,
        515,9,36,3,36,517,8,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,4,38,548,8,38,11,38,12,38,
        549,1,38,1,38,3,38,554,8,38,1,38,1,38,1,38,1,38,3,38,560,8,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,570,8,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,582,8,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,598,
        8,38,1,38,1,38,1,38,1,38,3,38,604,8,38,1,38,1,38,5,38,608,8,38,10,
        38,12,38,611,9,38,1,39,1,39,1,39,3,39,616,8,39,1,39,1,39,1,40,1,
        40,1,40,3,40,623,8,40,1,41,1,41,1,41,5,41,628,8,41,10,41,12,41,631,
        9,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,0,1,76,45,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,0,12,2,0,19,19,26,
        27,2,0,68,72,78,78,2,0,30,31,62,64,1,0,37,38,1,0,68,71,1,0,83,85,
        1,0,81,82,2,0,73,75,78,80,1,0,7,8,3,0,99,99,116,117,119,119,4,0,
        39,39,95,97,99,99,107,108,1,0,113,114,703,0,90,1,0,0,0,2,96,1,0,
        0,0,4,117,1,0,0,0,6,126,1,0,0,0,8,133,1,0,0,0,10,139,1,0,0,0,12,
        141,1,0,0,0,14,148,1,0,0,0,16,156,1,0,0,0,18,164,1,0,0,0,20,192,
        1,0,0,0,22,214,1,0,0,0,24,216,1,0,0,0,26,220,1,0,0,0,28,224,1,0,
        0,0,30,228,1,0,0,0,32,276,1,0,0,0,34,293,1,0,0,0,36,311,1,0,0,0,
        38,314,1,0,0,0,40,324,1,0,0,0,42,332,1,0,0,0,44,346,1,0,0,0,46,369,
        1,0,0,0,48,373,1,0,0,0,50,381,1,0,0,0,52,389,1,0,0,0,54,397,1,0,
        0,0,56,413,1,0,0,0,58,415,1,0,0,0,60,424,1,0,0,0,62,427,1,0,0,0,
        64,435,1,0,0,0,66,444,1,0,0,0,68,493,1,0,0,0,70,495,1,0,0,0,72,498,
        1,0,0,0,74,518,1,0,0,0,76,559,1,0,0,0,78,612,1,0,0,0,80,622,1,0,
        0,0,82,624,1,0,0,0,84,632,1,0,0,0,86,634,1,0,0,0,88,636,1,0,0,0,
        90,91,3,2,1,0,91,92,5,0,0,1,92,1,1,0,0,0,93,95,3,4,2,0,94,93,1,0,
        0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,3,1,0,0,0,98,96,
        1,0,0,0,99,101,3,6,3,0,100,102,5,92,0,0,101,100,1,0,0,0,101,102,
        1,0,0,0,102,104,1,0,0,0,103,99,1,0,0,0,104,105,1,0,0,0,105,103,1,
        0,0,0,105,106,1,0,0,0,106,111,1,0,0,0,107,109,5,2,0,0,108,110,5,
        92,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,107,1,
        0,0,0,111,112,1,0,0,0,112,118,1,0,0,0,113,115,5,2,0,0,114,116,5,
        92,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,103,1,
        0,0,0,117,113,1,0,0,0,118,5,1,0,0,0,119,127,3,8,4,0,120,127,3,10,
        5,0,121,127,3,68,34,0,122,127,3,70,35,0,123,127,3,60,30,0,124,127,
        3,66,33,0,125,127,3,72,36,0,126,119,1,0,0,0,126,120,1,0,0,0,126,
        121,1,0,0,0,126,122,1,0,0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,
        125,1,0,0,0,127,7,1,0,0,0,128,134,3,12,6,0,129,134,3,22,11,0,130,
        134,3,24,12,0,131,134,3,26,13,0,132,134,3,28,14,0,133,128,1,0,0,
        0,133,129,1,0,0,0,133,130,1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,
        0,134,9,1,0,0,0,135,140,3,30,15,0,136,140,3,44,22,0,137,140,3,52,
        26,0,138,140,3,58,29,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,
        0,0,0,139,138,1,0,0,0,140,11,1,0,0,0,141,142,5,18,0,0,142,143,5,
        19,0,0,143,144,3,82,41,0,144,145,5,93,0,0,145,146,3,14,7,0,146,147,
        5,94,0,0,147,13,1,0,0,0,148,153,3,16,8,0,149,150,5,90,0,0,150,152,
        3,16,8,0,151,149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,
        1,0,0,0,154,15,1,0,0,0,155,153,1,0,0,0,156,157,3,84,42,0,157,161,
        3,18,9,0,158,160,3,20,10,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,
        1,0,0,0,161,162,1,0,0,0,162,17,1,0,0,0,163,161,1,0,0,0,164,175,3,
        84,42,0,165,168,5,93,0,0,166,169,5,96,0,0,167,169,3,84,42,0,168,
        166,1,0,0,0,168,167,1,0,0,0,169,172,1,0,0,0,170,171,5,90,0,0,171,
        173,5,96,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,0,174,
        176,5,94,0,0,175,165,1,0,0,0,175,176,1,0,0,0,176,19,1,0,0,0,177,
        178,5,9,0,0,178,193,5,39,0,0,179,193,5,39,0,0,180,181,5,22,0,0,181,
        193,5,23,0,0,182,183,5,55,0,0,183,193,3,76,38,0,184,190,5,56,0,0,
        185,186,5,93,0,0,186,187,5,96,0,0,187,188,5,90,0,0,188,189,5,96,
        0,0,189,191,5,94,0,0,190,185,1,0,0,0,190,191,1,0,0,0,191,193,1,0,
        0,0,192,177,1,0,0,0,192,179,1,0,0,0,192,180,1,0,0,0,192,182,1,0,
        0,0,192,184,1,0,0,0,193,21,1,0,0,0,194,195,5,20,0,0,195,196,5,19,
        0,0,196,197,3,82,41,0,197,198,5,24,0,0,198,199,3,16,8,0,199,215,
        1,0,0,0,200,201,5,20,0,0,201,202,5,19,0,0,202,203,3,82,41,0,203,
        204,5,21,0,0,204,205,5,25,0,0,205,206,3,84,42,0,206,215,1,0,0,0,
        207,208,5,20,0,0,208,209,5,19,0,0,209,210,3,82,41,0,210,211,5,20,
        0,0,211,212,5,25,0,0,212,213,3,16,8,0,213,215,1,0,0,0,214,194,1,
        0,0,0,214,200,1,0,0,0,214,207,1,0,0,0,215,23,1,0,0,0,216,217,5,21,
        0,0,217,218,7,0,0,0,218,219,3,82,41,0,219,25,1,0,0,0,220,221,5,3,
        0,0,221,222,5,19,0,0,222,223,3,82,41,0,223,27,1,0,0,0,224,225,5,
        28,0,0,225,226,3,84,42,0,226,29,1,0,0,0,227,229,3,74,37,0,228,227,
        1,0,0,0,228,229,1,0,0,0,229,230,1,0,0,0,230,232,5,4,0,0,231,233,
        5,11,0,0,232,231,1,0,0,0,232,233,1,0,0,0,233,236,1,0,0,0,234,235,
        5,57,0,0,235,237,5,96,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,238,
        1,0,0,0,238,260,3,32,16,0,239,240,5,5,0,0,240,244,3,36,18,0,241,
        243,3,38,19,0,242,241,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
        245,1,0,0,0,245,249,1,0,0,0,246,244,1,0,0,0,247,248,5,6,0,0,248,
        250,3,76,38,0,249,247,1,0,0,0,249,250,1,0,0,0,250,254,1,0,0,0,251,
        252,5,33,0,0,252,253,5,34,0,0,253,255,3,40,20,0,254,251,1,0,0,0,
        254,255,1,0,0,0,255,258,1,0,0,0,256,257,5,35,0,0,257,259,3,76,38,
        0,258,256,1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,239,1,0,0,
        0,260,261,1,0,0,0,261,265,1,0,0,0,262,263,5,36,0,0,263,264,5,34,
        0,0,264,266,3,42,21,0,265,262,1,0,0,0,265,266,1,0,0,0,266,31,1,0,
        0,0,267,277,5,83,0,0,268,273,3,34,17,0,269,270,5,90,0,0,270,272,
        3,34,17,0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,276,267,1,0,0,0,276,268,
        1,0,0,0,277,33,1,0,0,0,278,279,3,88,44,0,279,280,7,1,0,0,280,281,
        3,76,38,0,281,294,1,0,0,0,282,283,3,84,42,0,283,284,5,78,0,0,284,
        285,3,76,38,0,285,294,1,0,0,0,286,291,3,76,38,0,287,289,5,10,0,0,
        288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,0,0,0,290,292,3,84,42,
        0,291,288,1,0,0,0,291,292,1,0,0,0,292,294,1,0,0,0,293,278,1,0,0,
        0,293,282,1,0,0,0,293,286,1,0,0,0,294,35,1,0,0,0,295,300,3,82,41,
        0,296,298,5,10,0,0,297,296,1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,
        0,299,301,3,84,42,0,300,297,1,0,0,0,300,301,1,0,0,0,301,312,1,0,
        0,0,302,303,5,93,0,0,303,304,3,30,15,0,304,309,5,94,0,0,305,307,
        5,10,0,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,1,0,0,0,308,310,
        3,84,42,0,309,306,1,0,0,0,309,310,1,0,0,0,310,312,1,0,0,0,311,295,
        1,0,0,0,311,302,1,0,0,0,312,37,1,0,0,0,313,315,7,2,0,0,314,313,1,
        0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,318,5,65,0,0,317,316,1,
        0,0,0,317,318,1,0,0,0,318,319,1,0,0,0,319,320,5,29,0,0,320,321,3,
        36,18,0,321,322,5,32,0,0,322,323,3,76,38,0,323,39,1,0,0,0,324,329,
        3,76,38,0,325,326,5,90,0,0,326,328,3,76,38,0,327,325,1,0,0,0,328,
        331,1,0,0,0,329,327,1,0,0,0,329,330,1,0,0,0,330,41,1,0,0,0,331,329,
        1,0,0,0,332,334,3,76,38,0,333,335,7,3,0,0,334,333,1,0,0,0,334,335,
        1,0,0,0,335,343,1,0,0,0,336,337,5,90,0,0,337,339,3,76,38,0,338,340,
        7,3,0,0,339,338,1,0,0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,336,
        1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,43,1,
        0,0,0,345,343,1,0,0,0,346,348,5,12,0,0,347,349,5,13,0,0,348,347,
        1,0,0,0,348,349,1,0,0,0,349,350,1,0,0,0,350,355,3,82,41,0,351,352,
        5,93,0,0,352,353,3,48,24,0,353,354,5,94,0,0,354,356,1,0,0,0,355,
        351,1,0,0,0,355,356,1,0,0,0,356,367,1,0,0,0,357,358,5,14,0,0,358,
        363,3,46,23,0,359,360,5,90,0,0,360,362,3,46,23,0,361,359,1,0,0,0,
        362,365,1,0,0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,368,1,0,0,0,
        365,363,1,0,0,0,366,368,3,30,15,0,367,357,1,0,0,0,367,366,1,0,0,
        0,368,45,1,0,0,0,369,370,5,93,0,0,370,371,3,50,25,0,371,372,5,94,
        0,0,372,47,1,0,0,0,373,378,3,84,42,0,374,375,5,90,0,0,375,377,3,
        84,42,0,376,374,1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,378,379,
        1,0,0,0,379,49,1,0,0,0,380,378,1,0,0,0,381,386,3,76,38,0,382,383,
        5,90,0,0,383,385,3,76,38,0,384,382,1,0,0,0,385,388,1,0,0,0,386,384,
        1,0,0,0,386,387,1,0,0,0,387,51,1,0,0,0,388,386,1,0,0,0,389,390,5,
        15,0,0,390,391,3,82,41,0,391,392,5,16,0,0,392,395,3,54,27,0,393,
        394,5,6,0,0,394,396,3,76,38,0,395,393,1,0,0,0,395,396,1,0,0,0,396,
        53,1,0,0,0,397,402,3,56,28,0,398,399,5,90,0,0,399,401,3,56,28,0,
        400,398,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,
        403,55,1,0,0,0,404,402,1,0,0,0,405,406,3,84,42,0,406,407,5,78,0,
        0,407,408,3,76,38,0,408,414,1,0,0,0,409,410,3,84,42,0,410,411,7,
        4,0,0,411,412,3,76,38,0,412,414,1,0,0,0,413,405,1,0,0,0,413,409,
        1,0,0,0,414,57,1,0,0,0,415,417,5,17,0,0,416,418,5,5,0,0,417,416,
        1,0,0,0,417,418,1,0,0,0,418,419,1,0,0,0,419,422,3,82,41,0,420,421,
        5,6,0,0,421,423,3,76,38,0,422,420,1,0,0,0,422,423,1,0,0,0,423,59,
        1,0,0,0,424,425,5,1,0,0,425,426,3,62,31,0,426,61,1,0,0,0,427,432,
        3,64,32,0,428,429,5,90,0,0,429,431,3,64,32,0,430,428,1,0,0,0,431,
        434,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,63,1,0,0,0,434,432,
        1,0,0,0,435,437,5,114,0,0,436,438,5,10,0,0,437,436,1,0,0,0,437,438,
        1,0,0,0,438,439,1,0,0,0,439,442,3,18,9,0,440,441,5,78,0,0,441,443,
        3,76,38,0,442,440,1,0,0,0,442,443,1,0,0,0,443,65,1,0,0,0,444,445,
        5,16,0,0,445,446,3,88,44,0,446,447,7,1,0,0,447,448,3,76,38,0,448,
        67,1,0,0,0,449,450,5,42,0,0,450,457,5,51,0,0,451,453,3,6,3,0,452,
        454,5,92,0,0,453,452,1,0,0,0,453,454,1,0,0,0,454,456,1,0,0,0,455,
        451,1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,0,457,458,1,0,0,0,458,
        460,1,0,0,0,459,457,1,0,0,0,460,461,5,43,0,0,461,462,5,51,0,0,462,
        463,5,42,0,0,463,470,5,52,0,0,464,466,3,6,3,0,465,467,5,92,0,0,466,
        465,1,0,0,0,466,467,1,0,0,0,467,469,1,0,0,0,468,464,1,0,0,0,469,
        472,1,0,0,0,470,468,1,0,0,0,470,471,1,0,0,0,471,473,1,0,0,0,472,
        470,1,0,0,0,473,474,5,43,0,0,474,494,5,52,0,0,475,482,5,42,0,0,476,
        478,3,6,3,0,477,479,5,92,0,0,478,477,1,0,0,0,478,479,1,0,0,0,479,
        481,1,0,0,0,480,476,1,0,0,0,481,484,1,0,0,0,482,480,1,0,0,0,482,
        483,1,0,0,0,483,485,1,0,0,0,484,482,1,0,0,0,485,494,5,43,0,0,486,
        487,5,50,0,0,487,488,3,76,38,0,488,491,3,6,3,0,489,490,5,47,0,0,
        490,492,3,6,3,0,491,489,1,0,0,0,491,492,1,0,0,0,492,494,1,0,0,0,
        493,449,1,0,0,0,493,475,1,0,0,0,493,486,1,0,0,0,494,69,1,0,0,0,495,
        496,5,54,0,0,496,497,3,76,38,0,497,71,1,0,0,0,498,502,5,53,0,0,499,
        500,3,88,44,0,500,501,5,78,0,0,501,503,1,0,0,0,502,499,1,0,0,0,502,
        503,1,0,0,0,503,506,1,0,0,0,504,507,3,82,41,0,505,507,3,88,44,0,
        506,504,1,0,0,0,506,505,1,0,0,0,507,516,1,0,0,0,508,513,3,76,38,
        0,509,510,5,90,0,0,510,512,3,76,38,0,511,509,1,0,0,0,512,515,1,0,
        0,0,513,511,1,0,0,0,513,514,1,0,0,0,514,517,1,0,0,0,515,513,1,0,
        0,0,516,508,1,0,0,0,516,517,1,0,0,0,517,73,1,0,0,0,518,519,5,59,
        0,0,519,520,3,84,42,0,520,521,5,10,0,0,521,522,5,93,0,0,522,523,
        3,30,15,0,523,524,5,94,0,0,524,75,1,0,0,0,525,526,6,38,-1,0,526,
        527,5,93,0,0,527,528,3,76,38,0,528,529,5,94,0,0,529,560,1,0,0,0,
        530,531,5,9,0,0,531,560,3,76,38,15,532,533,5,48,0,0,533,534,5,93,
        0,0,534,535,3,30,15,0,535,536,5,94,0,0,536,560,1,0,0,0,537,538,5,
        93,0,0,538,539,3,30,15,0,539,540,5,94,0,0,540,560,1,0,0,0,541,547,
        5,44,0,0,542,543,5,45,0,0,543,544,3,76,38,0,544,545,5,46,0,0,545,
        546,3,76,38,0,546,548,1,0,0,0,547,542,1,0,0,0,548,549,1,0,0,0,549,
        547,1,0,0,0,549,550,1,0,0,0,550,553,1,0,0,0,551,552,5,47,0,0,552,
        554,3,76,38,0,553,551,1,0,0,0,553,554,1,0,0,0,554,555,1,0,0,0,555,
        556,5,43,0,0,556,560,1,0,0,0,557,560,3,78,39,0,558,560,3,80,40,0,
        559,525,1,0,0,0,559,530,1,0,0,0,559,532,1,0,0,0,559,537,1,0,0,0,
        559,541,1,0,0,0,559,557,1,0,0,0,559,558,1,0,0,0,560,609,1,0,0,0,
        561,562,10,14,0,0,562,563,7,5,0,0,563,608,3,76,38,15,564,565,10,
        13,0,0,565,566,7,6,0,0,566,608,3,76,38,14,567,569,10,12,0,0,568,
        570,5,9,0,0,569,568,1,0,0,0,569,570,1,0,0,0,570,571,1,0,0,0,571,
        572,5,66,0,0,572,573,3,76,38,0,573,574,5,7,0,0,574,575,3,76,38,13,
        575,608,1,0,0,0,576,577,10,11,0,0,577,578,7,7,0,0,578,608,3,76,38,
        12,579,581,10,10,0,0,580,582,5,9,0,0,581,580,1,0,0,0,581,582,1,0,
        0,0,582,583,1,0,0,0,583,584,5,67,0,0,584,608,3,76,38,11,585,586,
        10,9,0,0,586,587,7,8,0,0,587,608,3,76,38,10,588,589,10,8,0,0,589,
        590,5,40,0,0,590,608,5,39,0,0,591,592,10,7,0,0,592,593,5,40,0,0,
        593,594,5,9,0,0,594,608,5,39,0,0,595,597,10,6,0,0,596,598,5,9,0,
        0,597,596,1,0,0,0,597,598,1,0,0,0,598,599,1,0,0,0,599,600,5,49,0,
        0,600,603,5,93,0,0,601,604,3,50,25,0,602,604,3,30,15,0,603,601,1,
        0,0,0,603,602,1,0,0,0,604,605,1,0,0,0,605,606,5,94,0,0,606,608,1,
        0,0,0,607,561,1,0,0,0,607,564,1,0,0,0,607,567,1,0,0,0,607,576,1,
        0,0,0,607,579,1,0,0,0,607,585,1,0,0,0,607,588,1,0,0,0,607,591,1,
        0,0,0,607,595,1,0,0,0,608,611,1,0,0,0,609,607,1,0,0,0,609,610,1,
        0,0,0,610,77,1,0,0,0,611,609,1,0,0,0,612,613,3,84,42,0,613,615,5,
        93,0,0,614,616,3,50,25,0,615,614,1,0,0,0,615,616,1,0,0,0,616,617,
        1,0,0,0,617,618,5,94,0,0,618,79,1,0,0,0,619,623,3,82,41,0,620,623,
        3,86,43,0,621,623,3,88,44,0,622,619,1,0,0,0,622,620,1,0,0,0,622,
        621,1,0,0,0,623,81,1,0,0,0,624,629,3,84,42,0,625,626,5,91,0,0,626,
        628,3,84,42,0,627,625,1,0,0,0,628,631,1,0,0,0,629,627,1,0,0,0,629,
        630,1,0,0,0,630,83,1,0,0,0,631,629,1,0,0,0,632,633,7,9,0,0,633,85,
        1,0,0,0,634,635,7,10,0,0,635,87,1,0,0,0,636,637,7,11,0,0,637,89,
        1,0,0,0,81,96,101,105,109,111,115,117,126,133,139,153,161,168,172,
        175,190,192,214,228,232,236,244,249,254,258,260,265,273,276,288,
        291,293,297,300,306,309,311,314,317,329,334,339,343,348,355,363,
        367,378,386,395,402,413,417,422,432,437,442,453,457,466,470,478,
        482,491,493,502,506,513,516,549,553,559,569,581,597,603,607,609,
        615,622,629
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
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'>='", "'<='", 
                     "<INVALID>", "'!<'", "'!>'", "'='", "'>'", "'<'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", "'~'", 
                     "','", "'.'", "';'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*/'" ]

    symbolicNames = [ "<INVALID>", "DECLARE", "GO", "TRUNCATE", "SELECT", 
                      "FROM", "WHERE", "AND", "OR", "NOT", "AS", "DISTINCT", 
                      "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE", 
                      "CREATE", "TABLE", "ALTER", "DROP", "PRIMARY", "KEY", 
                      "ADD", "COLUMN", "VIEW", "PROCEDURE", "USE", "JOIN", 
                      "INNER", "LEFT", "ON", "GROUP", "BY", "HAVING", "ORDER", 
                      "ASC", "DESC", "NULL", "IS", "UNION", "BEGIN", "END", 
                      "CASE", "WHEN", "THEN", "ELSE", "EXISTS", "IN", "IF", 
                      "TRY", "CATCH", "EXEC", "PRINT", "DEFAULT", "IDENTITY", 
                      "TOP", "OUTPUT", "WITH", "OVER", "PARTITION", "RIGHT", 
                      "FULL", "CROSS", "OUTER", "BETWEEN", "LIKE", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", "PERCENT_ASSIGN", 
                      "GE", "LE", "NEQ", "NOT_LESS", "NOT_GREATER", "EQ", 
                      "GT", "LT", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", 
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
    RULE_truncate_statement = 13
    RULE_use_statement = 14
    RULE_select_statement = 15
    RULE_select_list = 16
    RULE_select_item = 17
    RULE_table_source = 18
    RULE_join_part = 19
    RULE_group_list = 20
    RULE_order_list = 21
    RULE_insert_statement = 22
    RULE_expression_list_parens = 23
    RULE_column_list = 24
    RULE_expression_list = 25
    RULE_update_statement = 26
    RULE_assignment_list = 27
    RULE_assignment = 28
    RULE_delete_statement = 29
    RULE_declare_statement = 30
    RULE_declare_list = 31
    RULE_declare_item = 32
    RULE_set_statement = 33
    RULE_control_flow_statement = 34
    RULE_print_statement = 35
    RULE_execute_statement = 36
    RULE_with_expression = 37
    RULE_expression = 38
    RULE_function_call = 39
    RULE_atom = 40
    RULE_table_name = 41
    RULE_id_name = 42
    RULE_constant = 43
    RULE_variable = 44

    ruleNames =  [ "root", "sql_script", "batch", "sql_statement", "ddl_statement", 
                   "dml_statement", "create_statement", "column_def_list", 
                   "column_def", "data_type", "column_constraint", "alter_statement", 
                   "drop_statement", "truncate_statement", "use_statement", 
                   "select_statement", "select_list", "select_item", "table_source", 
                   "join_part", "group_list", "order_list", "insert_statement", 
                   "expression_list_parens", "column_list", "expression_list", 
                   "update_statement", "assignment_list", "assignment", 
                   "delete_statement", "declare_statement", "declare_list", 
                   "declare_item", "set_statement", "control_flow_statement", 
                   "print_statement", "execute_statement", "with_expression", 
                   "expression", "function_call", "atom", "table_name", 
                   "id_name", "constant", "variable" ]

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
    ORDER=36
    ASC=37
    DESC=38
    NULL=39
    IS=40
    UNION=41
    BEGIN=42
    END=43
    CASE=44
    WHEN=45
    THEN=46
    ELSE=47
    EXISTS=48
    IN=49
    IF=50
    TRY=51
    CATCH=52
    EXEC=53
    PRINT=54
    DEFAULT=55
    IDENTITY=56
    TOP=57
    OUTPUT=58
    WITH=59
    OVER=60
    PARTITION=61
    RIGHT=62
    FULL=63
    CROSS=64
    OUTER=65
    BETWEEN=66
    LIKE=67
    PLUS_ASSIGN=68
    MINUS_ASSIGN=69
    STAR_ASSIGN=70
    SLASH_ASSIGN=71
    PERCENT_ASSIGN=72
    GE=73
    LE=74
    NEQ=75
    NOT_LESS=76
    NOT_GREATER=77
    EQ=78
    GT=79
    LT=80
    PLUS=81
    MINUS=82
    STAR=83
    SLASH=84
    PERCENT=85
    BIT_AND=86
    BIT_OR=87
    BIT_XOR=88
    BIT_NOT=89
    COMMA=90
    DOT=91
    SEMI=92
    LPAREN=93
    RPAREN=94
    FLOAT=95
    INT=96
    NSTRING=97
    UNCLOSED_NSTRING_EOF=98
    STRING=99
    UNCLOSED_STRING_EOF=100
    LINE_COMMENT=101
    BLOCK_COMMENT_START=102
    NESTED_BLOCK_START=103
    BLOCK_COMMENT_END=104
    COMMENT_TEXT=105
    UNTERMINATED_BLOCK_COMMENT=106
    TRUE=107
    FALSE=108
    HEX_LITERAL=109
    INVALID_HEX_LITERAL=110
    BIT_STRING=111
    INVALID_BIT_STRING=112
    GLOBAL_VAR=113
    LOCAL_VAR=114
    TEMP_ID=115
    BRACKET_ID=116
    DQUOTED_ID=117
    UNCLOSED_BRACKET_ID=118
    ID=119
    WS=120
    ERROR_CHAR=121

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
            self.state = 90
            self.sql_script()
            self.state = 91
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
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 604612648293077022) != 0):
                self.state = 93
                self.batch()
                self.state = 98
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
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 12, 15, 16, 17, 18, 20, 21, 28, 42, 50, 53, 54, 59]:
                localctx = SQLParser.StatementBatchContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 99
                        self.sql_statement()
                        self.state = 101
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==92:
                            self.state = 100
                            self.match(SQLParser.SEMI)



                    else:
                        raise NoViableAltException(self)
                    self.state = 105 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 107
                    self.match(SQLParser.GO)
                    self.state = 109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==92:
                        self.state = 108
                        self.match(SQLParser.SEMI)




                pass
            elif token in [2]:
                localctx = SQLParser.EmptyGoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(SQLParser.GO)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==92:
                    self.state = 114
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
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 18, 20, 21, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.ddl_statement()
                pass
            elif token in [4, 12, 15, 17, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.dml_statement()
                pass
            elif token in [42, 50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.control_flow_statement()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.print_statement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.declare_statement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 124
                self.set_statement()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 7)
                self.state = 125
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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.create_statement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.alter_statement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.drop_statement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.truncate_statement()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.select_statement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.insert_statement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.update_statement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
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
            self.state = 141
            self.match(SQLParser.CREATE)
            self.state = 142
            self.match(SQLParser.TABLE)
            self.state = 143
            self.table_name()
            self.state = 144
            self.match(SQLParser.LPAREN)
            self.state = 145
            self.column_def_list()
            self.state = 146
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
            self.state = 148
            self.column_def()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 149
                self.match(SQLParser.COMMA)
                self.state = 150
                self.column_def()
                self.state = 155
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
            self.state = 156
            self.id_name()
            self.state = 157
            self.data_type()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 108086940816900608) != 0):
                self.state = 158
                self.column_constraint()
                self.state = 163
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
            self.state = 164
            self.id_name()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==93:
                self.state = 165
                self.match(SQLParser.LPAREN)
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [96]:
                    self.state = 166
                    self.match(SQLParser.INT)
                    pass
                elif token in [99, 116, 117, 119]:
                    self.state = 167
                    self.id_name()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==90:
                    self.state = 170
                    self.match(SQLParser.COMMA)
                    self.state = 171
                    self.match(SQLParser.INT)


                self.state = 174
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
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(SQLParser.NOT)
                self.state = 178
                self.match(SQLParser.NULL)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(SQLParser.NULL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(SQLParser.PRIMARY)
                self.state = 181
                self.match(SQLParser.KEY)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.match(SQLParser.DEFAULT)
                self.state = 183
                self.expression(0)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.match(SQLParser.IDENTITY)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==93:
                    self.state = 185
                    self.match(SQLParser.LPAREN)
                    self.state = 186
                    self.match(SQLParser.INT)
                    self.state = 187
                    self.match(SQLParser.COMMA)
                    self.state = 188
                    self.match(SQLParser.INT)
                    self.state = 189
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
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = SQLParser.AlterAddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(SQLParser.ALTER)
                self.state = 195
                self.match(SQLParser.TABLE)
                self.state = 196
                self.table_name()
                self.state = 197
                self.match(SQLParser.ADD)
                self.state = 198
                self.column_def()
                pass

            elif la_ == 2:
                localctx = SQLParser.AlterDropContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(SQLParser.ALTER)
                self.state = 201
                self.match(SQLParser.TABLE)
                self.state = 202
                self.table_name()
                self.state = 203
                self.match(SQLParser.DROP)
                self.state = 204
                self.match(SQLParser.COLUMN)
                self.state = 205
                self.id_name()
                pass

            elif la_ == 3:
                localctx = SQLParser.AlterModifyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(SQLParser.ALTER)
                self.state = 208
                self.match(SQLParser.TABLE)
                self.state = 209
                self.table_name()
                self.state = 210
                self.match(SQLParser.ALTER)
                self.state = 211
                self.match(SQLParser.COLUMN)
                self.state = 212
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
            self.state = 216
            self.match(SQLParser.DROP)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 201850880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
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
        self.enterRule(localctx, 26, self.RULE_truncate_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(SQLParser.TRUNCATE)
            self.state = 221
            self.match(SQLParser.TABLE)
            self.state = 222
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
        self.enterRule(localctx, 28, self.RULE_use_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(SQLParser.USE)
            self.state = 225
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
        self.enterRule(localctx, 30, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 227
                self.with_expression()


            self.state = 230
            self.match(SQLParser.SELECT)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 231
                self.match(SQLParser.DISTINCT)


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 234
                self.match(SQLParser.TOP)
                self.state = 235
                self.match(SQLParser.INT)


            self.state = 238
            self.select_list()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 239
                self.match(SQLParser.FROM)
                self.state = 240
                self.table_source()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 128849018887) != 0):
                    self.state = 241
                    self.join_part()
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 247
                    self.match(SQLParser.WHERE)
                    self.state = 248
                    self.expression(0)


                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 251
                    self.match(SQLParser.GROUP)
                    self.state = 252
                    self.match(SQLParser.BY)
                    self.state = 253
                    self.group_list()


                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 256
                    self.match(SQLParser.HAVING)
                    self.state = 257
                    self.expression(0)




            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 262
                self.match(SQLParser.ORDER)
                self.state = 263
                self.match(SQLParser.BY)
                self.state = 264
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
        self.enterRule(localctx, 32, self.RULE_select_list)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [83]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(SQLParser.STAR)
                pass
            elif token in [9, 39, 44, 48, 93, 95, 96, 97, 99, 107, 108, 113, 114, 116, 117, 119]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.select_item()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==90:
                    self.state = 269
                    self.match(SQLParser.COMMA)
                    self.state = 270
                    self.select_item()
                    self.state = 275
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
        self.enterRule(localctx, 34, self.RULE_select_item)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = SQLParser.SelectVarAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.variable()
                self.state = 279
                _la = self._input.LA(1)
                if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 1055) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = SQLParser.SelectAliasAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.id_name()
                self.state = 283
                self.match(SQLParser.EQ)
                self.state = 284
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = SQLParser.SelectExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.expression(0)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & 1441793) != 0):
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 287
                        self.match(SQLParser.AS)


                    self.state = 290
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
        self.enterRule(localctx, 36, self.RULE_table_source)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [99, 116, 117, 119]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.table_name()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & 1441793) != 0):
                    self.state = 297
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 296
                        self.match(SQLParser.AS)


                    self.state = 299
                    self.id_name()


                pass
            elif token in [93]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(SQLParser.LPAREN)
                self.state = 303
                self.select_statement()
                self.state = 304
                self.match(SQLParser.RPAREN)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & 1441793) != 0):
                    self.state = 306
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 305
                        self.match(SQLParser.AS)


                    self.state = 308
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
        self.enterRule(localctx, 38, self.RULE_join_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 30064771075) != 0):
                self.state = 313
                _la = self._input.LA(1)
                if not(((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 30064771075) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 316
                self.match(SQLParser.OUTER)


            self.state = 319
            self.match(SQLParser.JOIN)
            self.state = 320
            self.table_source()
            self.state = 321
            self.match(SQLParser.ON)
            self.state = 322
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
        self.enterRule(localctx, 40, self.RULE_group_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.expression(0)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 325
                self.match(SQLParser.COMMA)
                self.state = 326
                self.expression(0)
                self.state = 331
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
        self.enterRule(localctx, 42, self.RULE_order_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.expression(0)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37 or _la==38:
                self.state = 333
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 336
                self.match(SQLParser.COMMA)
                self.state = 337
                self.expression(0)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37 or _la==38:
                    self.state = 338
                    _la = self._input.LA(1)
                    if not(_la==37 or _la==38):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 345
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
        self.enterRule(localctx, 44, self.RULE_insert_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(SQLParser.INSERT)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 347
                self.match(SQLParser.INTO)


            self.state = 350
            self.table_name()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==93:
                self.state = 351
                self.match(SQLParser.LPAREN)
                self.state = 352
                self.column_list()
                self.state = 353
                self.match(SQLParser.RPAREN)


            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 357
                self.match(SQLParser.VALUES)
                self.state = 358
                self.expression_list_parens()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==90:
                    self.state = 359
                    self.match(SQLParser.COMMA)
                    self.state = 360
                    self.expression_list_parens()
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [4, 59]:
                self.state = 366
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
        self.enterRule(localctx, 46, self.RULE_expression_list_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(SQLParser.LPAREN)
            self.state = 370
            self.expression_list()
            self.state = 371
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
        self.enterRule(localctx, 48, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.id_name()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 374
                self.match(SQLParser.COMMA)
                self.state = 375
                self.id_name()
                self.state = 380
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
        self.enterRule(localctx, 50, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expression(0)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 382
                self.match(SQLParser.COMMA)
                self.state = 383
                self.expression(0)
                self.state = 388
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
        self.enterRule(localctx, 52, self.RULE_update_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(SQLParser.UPDATE)
            self.state = 390
            self.table_name()
            self.state = 391
            self.match(SQLParser.SET)
            self.state = 392
            self.assignment_list()
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 393
                self.match(SQLParser.WHERE)
                self.state = 394
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
        self.enterRule(localctx, 54, self.RULE_assignment_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.assignment()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 398
                self.match(SQLParser.COMMA)
                self.state = 399
                self.assignment()
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
        self.enterRule(localctx, 56, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.id_name()
                self.state = 406
                self.match(SQLParser.EQ)
                self.state = 407
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.id_name()
                self.state = 410
                _la = self._input.LA(1)
                if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 15) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
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
        self.enterRule(localctx, 58, self.RULE_delete_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(SQLParser.DELETE)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 416
                self.match(SQLParser.FROM)


            self.state = 419
            self.table_name()
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 420
                self.match(SQLParser.WHERE)
                self.state = 421
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
        self.enterRule(localctx, 60, self.RULE_declare_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(SQLParser.DECLARE)
            self.state = 425
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
        self.enterRule(localctx, 62, self.RULE_declare_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.declare_item()
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==90:
                self.state = 428
                self.match(SQLParser.COMMA)
                self.state = 429
                self.declare_item()
                self.state = 434
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
        self.enterRule(localctx, 64, self.RULE_declare_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(SQLParser.LOCAL_VAR)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 436
                self.match(SQLParser.AS)


            self.state = 439
            self.data_type()
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 440
                self.match(SQLParser.EQ)
                self.state = 441
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
        self.enterRule(localctx, 66, self.RULE_set_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(SQLParser.SET)
            self.state = 445
            self.variable()
            self.state = 446
            _la = self._input.LA(1)
            if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 1055) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 447
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
        self.enterRule(localctx, 68, self.RULE_control_flow_statement)
        self._la = 0 # Token type
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(SQLParser.BEGIN)
                self.state = 450
                self.match(SQLParser.TRY)
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 604612648293077018) != 0):
                    self.state = 451
                    self.sql_statement()
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==92:
                        self.state = 452
                        self.match(SQLParser.SEMI)


                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 460
                self.match(SQLParser.END)
                self.state = 461
                self.match(SQLParser.TRY)
                self.state = 462
                self.match(SQLParser.BEGIN)
                self.state = 463
                self.match(SQLParser.CATCH)
                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 604612648293077018) != 0):
                    self.state = 464
                    self.sql_statement()
                    self.state = 466
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==92:
                        self.state = 465
                        self.match(SQLParser.SEMI)


                    self.state = 472
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 473
                self.match(SQLParser.END)
                self.state = 474
                self.match(SQLParser.CATCH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.match(SQLParser.BEGIN)
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 604612648293077018) != 0):
                    self.state = 476
                    self.sql_statement()
                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==92:
                        self.state = 477
                        self.match(SQLParser.SEMI)


                    self.state = 484
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 485
                self.match(SQLParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.match(SQLParser.IF)
                self.state = 487
                self.expression(0)
                self.state = 488
                self.sql_statement()
                self.state = 491
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 489
                    self.match(SQLParser.ELSE)
                    self.state = 490
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
        self.enterRule(localctx, 70, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(SQLParser.PRINT)
            self.state = 496
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
        self.enterRule(localctx, 72, self.RULE_execute_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(SQLParser.EXEC)
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 499
                self.variable()
                self.state = 500
                self.match(SQLParser.EQ)


            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [99, 116, 117, 119]:
                self.state = 504
                self.table_name()
                pass
            elif token in [113, 114]:
                self.state = 505
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 299616918569472) != 0) or ((((_la - 93)) & ~0x3f) == 0 and ((1 << (_la - 93)) & 95469661) != 0):
                self.state = 508
                self.expression(0)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==90:
                    self.state = 509
                    self.match(SQLParser.COMMA)
                    self.state = 510
                    self.expression(0)
                    self.state = 515
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
        self.enterRule(localctx, 74, self.RULE_with_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(SQLParser.WITH)
            self.state = 519
            self.id_name()
            self.state = 520
            self.match(SQLParser.AS)
            self.state = 521
            self.match(SQLParser.LPAREN)
            self.state = 522
            self.select_statement()
            self.state = 523
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                localctx = SQLParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 526
                self.match(SQLParser.LPAREN)
                self.state = 527
                self.expression(0)
                self.state = 528
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SQLParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 530
                self.match(SQLParser.NOT)
                self.state = 531
                self.expression(15)
                pass

            elif la_ == 3:
                localctx = SQLParser.ExistsExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 532
                self.match(SQLParser.EXISTS)
                self.state = 533
                self.match(SQLParser.LPAREN)
                self.state = 534
                self.select_statement()
                self.state = 535
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = SQLParser.ScalarSubqueryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 537
                self.match(SQLParser.LPAREN)
                self.state = 538
                self.select_statement()
                self.state = 539
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = SQLParser.CaseExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 541
                self.match(SQLParser.CASE)
                self.state = 547 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 542
                    self.match(SQLParser.WHEN)
                    self.state = 543
                    self.expression(0)
                    self.state = 544
                    self.match(SQLParser.THEN)
                    self.state = 545
                    self.expression(0)
                    self.state = 549 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==45):
                        break

                self.state = 553
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 551
                    self.match(SQLParser.ELSE)
                    self.state = 552
                    self.expression(0)


                self.state = 555
                self.match(SQLParser.END)
                pass

            elif la_ == 6:
                localctx = SQLParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 557
                self.function_call()
                pass

            elif la_ == 7:
                localctx = SQLParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 558
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 607
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                    if la_ == 1:
                        localctx = SQLParser.MultiplicativeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 561
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 562
                        _la = self._input.LA(1)
                        if not(((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 7) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 563
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = SQLParser.AdditiveExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 564
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 565
                        _la = self._input.LA(1)
                        if not(_la==81 or _la==82):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 566
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = SQLParser.BetweenExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 567
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 569
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 568
                            self.match(SQLParser.NOT)


                        self.state = 571
                        self.match(SQLParser.BETWEEN)
                        self.state = 572
                        self.expression(0)
                        self.state = 573
                        self.match(SQLParser.AND)
                        self.state = 574
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = SQLParser.ComparisonExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 576
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 577
                        _la = self._input.LA(1)
                        if not(((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 231) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 578
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = SQLParser.LikeExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 579
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 581
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 580
                            self.match(SQLParser.NOT)


                        self.state = 583
                        self.match(SQLParser.LIKE)
                        self.state = 584
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = SQLParser.LogicalExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 585
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 586
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 587
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = SQLParser.IsNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 588
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 589
                        self.match(SQLParser.IS)
                        self.state = 590
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 8:
                        localctx = SQLParser.IsNotNullExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 591
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 592
                        self.match(SQLParser.IS)
                        self.state = 593
                        self.match(SQLParser.NOT)
                        self.state = 594
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 9:
                        localctx = SQLParser.InExprContext(self, SQLParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 595
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 597
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==9:
                            self.state = 596
                            self.match(SQLParser.NOT)


                        self.state = 599
                        self.match(SQLParser.IN)
                        self.state = 600
                        self.match(SQLParser.LPAREN)
                        self.state = 603
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [9, 39, 44, 48, 93, 95, 96, 97, 99, 107, 108, 113, 114, 116, 117, 119]:
                            self.state = 601
                            self.expression_list()
                            pass
                        elif token in [4, 59]:
                            self.state = 602
                            self.select_statement()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 605
                        self.match(SQLParser.RPAREN)
                        pass

             
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.id_name()
            self.state = 613
            self.match(SQLParser.LPAREN)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 299616918569472) != 0) or ((((_la - 93)) & ~0x3f) == 0 and ((1 << (_la - 93)) & 95469661) != 0):
                self.state = 614
                self.expression_list()


            self.state = 617
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
        self.enterRule(localctx, 80, self.RULE_atom)
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.table_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 621
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
        self.enterRule(localctx, 82, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.id_name()
            self.state = 629
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 625
                    self.match(SQLParser.DOT)
                    self.state = 626
                    self.id_name() 
                self.state = 631
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_id_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            _la = self._input.LA(1)
            if not(((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & 1441793) != 0)):
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
        self.enterRule(localctx, 86, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            _la = self._input.LA(1)
            if not(_la==39 or ((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & 12311) != 0)):
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
        self.enterRule(localctx, 88, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            _la = self._input.LA(1)
            if not(_la==113 or _la==114):
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
        self._predicates[38] = self.expression_sempred
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
         





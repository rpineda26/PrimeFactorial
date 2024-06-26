import math
import sys
from controller import *
sys.set_int_max_str_digits(1000000)
"""
@definition: This function tests the naive isPrime function by checking if it returns the correct result for prime and composite numbers
@param: primes - a predefined list of prime numbers
        composites - a predefined list of composite numbers
"""
def test_naive_isPrime(primes, composites):
    for i in range(len(primes)):
        assert naive_isPrime(primes[i]) == True
    for i in range(len(composites)):
        assert naive_isPrime(composites[i]) == False
"""
@definition: This function tests the optimized isPrime function by checking if it returns a false positive for composite numbers
@param: primes - a predefined list of prime numbers
        composites - a predefined list of composite numbers
"""
def test_optimized_isPrime(primes, composites):
    #this test never returns a false negative
    for i in range(len(primes)):
        assert optimized_isPrime(primes[i]) == True
    #count the number of false positives
    count_false_positives = 0
    for i in range(len(composites)):
        try:
            assert optimized_isPrime(composites[i]) == False
        except AssertionError:
            print("optimized_isPrime returned a false positive for", composites[i])
            count_false_positives += 1
    return count_false_positives
"""
@definition: This function tests the optimized isPrime_deterministic function by 
            checking if it doesn't return a false positive for composite numbers
            and if it returns the correct result for prime numbers
@param: primes - a predefined list of prime numbers
        composites - a predefined list of composite numbers
"""
def test_optimized_isPrime_deterministic(primes, composites):
    #this test never returns a false negative
    for i in range(len(primes)):
        assert optimized_isPrime_deterministic(primes[i]) == True
    #count the number of false positives
    count_false_positives = 0
    for i in range(len(composites)):
        try:
            assert optimized_isPrime_deterministic(composites[i]) == False
        except AssertionError:
            print("optimized_isPrime returned a false positive for", composites[i])
            count_false_positives += 1
    return count_false_positives
"""
@definition: This function tests the naive factorial function by comparing it with the math library's factorial function
"""
def test_naive_factorial():
    #998 is the ceiling to prevent exceeding python's recursive depth limit
    for i in range(998):
        #Im trusting the python math library to test my naive factorial function implementation
        assert naive_factorial(i) == math.factorial(i)
"""
@definition: This function tests the optimized factorial function by comparing it with the math library's factorial function
"""
def test_optimized_factorial_should_memoize():
    #998 is the ceiling to prevent exceeding python's recursive depth limit
    for i in range(1200):
        try:
            #Im trusting the python math library to test my optimized factorial function implementation
            actual = optimized_factorial(max=i)
            expected = math.factorial(i)
            assert actual == expected
        except AssertionError:
            print("optimized_factorial returned an incorrect value for: ",i)
def test_optimized_factorial_should_not_memoize():    
    assert optimized_factorial(max=186) == math.factorial(186) 
    
        
def getPrimes():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
              401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
              	503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    return primes
"""
@definition: This function returns a predefined list of composite numbers up to 1000
@returns: a list of composite numbers from 4 to 1000
"""
def getComposites():
    composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50,

51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100,

102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150,

152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 164, 165, 166, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 180, 182, 183, 184, 185, 186, 187, 188, 189, 190, 192, 194, 195, 196, 198, 200,

201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 224, 225, 226, 228, 230, 231, 232, 234, 235, 236, 237, 238, 240, 242, 243, 244, 245, 246, 247, 248, 249,

250, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 270, 272, 273, 274, 275, 276, 278, 279, 280, 282, 284, 285, 286, 287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299,

300, 301, 302, 303, 304, 305, 306, 308, 309, 310, 312, 314, 315, 316, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 332, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343, 344, 345, 346, 348,

350, 351, 352, 354, 355, 356, 357, 358, 360, 361, 362, 363, 364, 365, 366, 368, 369, 370, 371, 372, 374, 375, 376, 377, 378, 380, 381, 382, 384, 385, 386, 387, 388, 390, 391, 392, 393, 394, 395, 396, 398, 399,

400, 402, 403, 404, 405, 406, 407, 408, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 422, 423, 424, 425, 426, 427, 428, 429, 430, 432, 434, 435, 436, 437, 438, 440, 441, 442, 444, 445, 446, 447, 448, 450,

451, 452, 453, 454, 455, 456, 458, 459, 460, 462, 464, 465, 466, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 480, 481, 482, 483, 484, 485, 486, 488, 489, 490, 492, 493, 494, 495, 496, 497, 498, 500,

501, 502, 504, 505, 506, 507, 508, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 522, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 542, 543, 544, 545, 546, 548, 549, 550,

551, 552, 553, 554, 555, 556, 558, 559, 560, 561, 562, 564, 565, 566, 567, 568, 570, 572, 573, 574, 575, 576, 578, 579, 580, 581, 582, 583, 584, 585, 586, 588, 589, 590, 591, 592, 594, 595, 596, 597, 598, 600,

602, 603, 604, 605, 606, 608, 609, 610, 611, 612, 614, 615, 616, 618, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 632, 633, 634, 635, 636, 637, 638, 639, 640, 642, 644, 645, 646, 648, 649, 650,

651, 652, 654, 655, 656, 657, 658, 660, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 674, 675, 676, 678, 679, 680, 681, 682, 684, 685, 686, 687, 688, 689, 690, 692, 693, 694, 695, 696, 697, 698, 699,

700, 702, 703, 704, 705, 706, 707, 708, 710, 711, 712, 713, 714, 715, 716, 717, 718, 720, 721, 722, 723, 724, 725, 726, 728, 729, 730, 731, 732, 734, 735, 736, 737, 738, 740, 741, 742, 744, 745, 746, 747, 748, 749, 750,

752, 753, 754, 755, 756, 758, 759, 760, 762, 763, 764, 765, 766, 767, 768, 770, 771, 772, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 788, 789, 790, 791, 792, 793, 794, 795, 796, 798, 799,

800, 801, 802, 803, 804, 805, 806, 807, 808, 810, 812, 813, 814, 815, 816, 817, 818, 819, 820, 822, 824, 825, 826, 828, 830, 831, 832, 833, 834, 835, 836, 837, 838, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850,

851, 852, 854, 855, 856, 858, 860, 861, 862, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 878, 879, 880, 882, 884, 885, 886, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900,

901, 902, 903, 904, 905, 906, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 920, 921, 922, 923, 924, 925, 926, 927, 928, 930, 931, 932, 933, 934, 935, 936, 938, 939, 940, 942, 943, 944, 945, 946, 948, 949,

950, 951, 952, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 968, 969, 970, 972, 973, 974, 975, 976, 978, 979, 980, 981, 982, 984, 985, 986, 987, 988, 989, 990, 992, 993, 994, 995, 996, 998, 999, 1000]
    return composites

"""
run the tests, display the results
"""
if __name__ == "__main__":
    test_naive_isPrime(getPrimes(), getComposites())
    print("TEST#1: Naive isPrime test passed")
    count =0
    #because the optimized isPrime is probabilistic, we need to run it multiple times to get an accurate measure of its accuracy
    #note that the measure for accuracy is not the same as the probability of a false positive
    #as I've only counted the number of times the function returns a false positive
    print("TEST#2: Optimized isPrime")
    #test all the composites from 4-1000 a hundred times to check for false positives and if randomness is observed
    for i in range(100): 
        count += test_optimized_isPrime(getPrimes(), getComposites())
    print("TEST#2: Optimized isPrime total tests conducted:", 100*len(getComposites()))
    print("TEST#2: Optimized isPrime false positives:", count)
    print("TEST#2: Optimized isPrime accuracy:",(100*len(getComposites())- count)/(100*len(getComposites())))
    test_naive_factorial()
    print("TEST#3: Naive factorial test passed. Max number: 998")
    print("TEST#4: Optimized isPrime deterministic")
    count =0
    #test all the composites from 4-1000 a hundred times to check for false positives and if randomness is observed
    for i in range(100): 
        count += test_optimized_isPrime_deterministic(getPrimes(), getComposites())
    print("TEST#4: Optimized isPrime deterministic total tests conducted:", 100*len(getComposites()))
    print("TEST#4: Optimized isPrime deterministic false positives:", count)
    print("TEST#4: Optimized isPrime deterministic accuracy:",(100*len(getComposites())- count)/(100*len(getComposites())))
    
    print("TEST#5: Optimized factorial test. Should not access memoization")
    test_optimized_factorial_should_not_memoize()
    print("TEST#5: Optimized factorial test. Max number TESTED: 1200, should access memoization")
    test_optimized_factorial_should_memoize()


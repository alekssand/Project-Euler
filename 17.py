import time
start_time = time.time()

def writeNumbers(low, high):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    numbers = []

    for i in range(low, high+1):
        
        nStringRev = str(i)[::-1]
        number = ''

        if len(nStringRev) > 3:
            number += ones[int(nStringRev[3])] + "thousand"

        if len(nStringRev) > 2 and nStringRev[2] != "0":
            number += ones[int(nStringRev[2])] + "hundred"

            if nStringRev[0:2] != "00":
                number += "and"

        if len(nStringRev) > 1 and nStringRev[1] == "1":
            number += teens[int(nStringRev[0])]

        elif len(nStringRev) > 1:
            number += tens[int(nStringRev[1])] + ones[int(nStringRev[0])]

        else:
            number += ones[int(nStringRev[0])]

        numbers.append(number)
    return numbers

def countDigits(nums):
    total = 0

    for i in nums:
        total += len(i)

    return total

print (countDigits(writeNumbers(1, 1000)))
print("%s seconds" % (time.time() - start_time))
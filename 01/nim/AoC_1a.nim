import strutils

for line in lines "../input":
    var result = 0
    var idx = 0
    for char in line[0 .. line.high]:
        if char == line[(idx+1) mod len(line)]:
            result += parseInt($char)
        idx += 1
    echo result

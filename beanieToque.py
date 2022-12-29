print('Are we working with inches or centimeters?')
units = input()

print('Tell us about your swatch: How many stitches did you cast on?')
swatchStitches = int(input())
print('Tell us about your swatch: What is the width of your swatch?')
swatchWidth = int(input())
print('Tell us about your swatch: How many rows or rounds did you work?')
swatchRows = int(input())
print('Tell us about your swatch: What is the length of your swatch?')
swatchLength = int(input())

stitchesPerUnit = swatchStitches/swatchWidth
rowsPerUnit = swatchRows/swatchLength

print('Head circumference to fit: ')
headCircumference = int(input())

print('choose edge style: ribbed, rolled, or hemmed')
edge = input()

if edge == "ribbed" :
    print('How deep (in inches) would you like the ribbing to be?')
    ribDepth = int(input())
    print('Would you prefer 1x1 or 2x2 ribbing?')
    ribStyle = input()
    if units == "inches" or "in":
        castOnStitchesRaw = int((headCircumference - 1.5) * stitchesPerUnit)
        print({castOnStitchesRaw})
        if ribStyle == "1x1":
            if castOnStitchesRaw % 2 == 0:
                castOnStitches = castOnStitchesRaw
            else :
                castOnStitches = castOnStitchesRaw + 1
        if ribStyle == "2x2" :
            if castOnStitchesRaw % 4 == 0:
                castOnStitches = castOnStitchesRaw
            elif castOnStitchesRaw % 4 == 3:
                castOnStitches = castOnStitchesRaw + 1
            elif castOnStitchesRaw % 4 == 2:
                castOnStitches = castOnStitchesRaw + 2
            elif castOnStitchesRaw % 4 == 1:
                castOnStitches = castOnStitchesRaw + 3
    elif units == "centimeters" or "cm":
        castOnStitchesRaw = int((headCircumference - 3.8) * stitchesPerUnit)
        print({castOnStitchesRaw})
        if ribStyle == "1x1":
            if castOnStitchesRaw % 2 == 0:
                castOnStitches = castOnStitchesRaw
            else:
                castOnStitches = castOnStitchesRaw + 1
        if ribStyle == "2x2":
            if castOnStitchesRaw % 4 == 0:
                castOnStitches = castOnStitchesRaw
            elif castOnStitchesRaw % 4 == 3:
                castOnStitches = castOnStitchesRaw + 1
            elif castOnStitchesRaw % 4 == 2:
                castOnStitches = castOnStitchesRaw + 2
            elif castOnStitchesRaw % 4 == 1:
                castOnStitches = castOnStitchesRaw + 3

print({castOnStitches})


lengthBeforeDecrease = (headCircumference - 16)/1.5 + 4

print({lengthBeforeDecrease})

filename = 'BeanieToque.txt'
f = open(filename, "w")
f.write('Hem/Edge: \n'
f'CO {castOnStitches} stitches, place marker and join in round being careful not to twist.\n' )
f.close()

if edge == "ribbed":
    if ribStyle == "1x1":
        f = open(filename, "a")
        f.write(f'Round 1: *k1 p1* repeat until end of round \n Work ribbing as established until measures {ribDepth} \n')
        f.close()
    else:
        f = open(filename, "a")
        f.write(f'Round 1: *k2 p2* repeat until end of round \n Work ribbing as established until measures {ribDepth} \n')
        f.close()
#elif edge == "rolled":
    #todo build this out
#elif edge == "hemmed" :
    # todo build this out
#else:
    #todo handle error

#main body (for now assumes plain stockinette stitch)
f = open(filename, "a")
f.write(f'Main Body: Knit every round until measures {lengthBeforeDecrease} {units} from CO edge\n')
f.close()

#decrease section
if castOnStitches % 8 == 0:
    placeMarker = (castOnStitches/8)
    f = open(filename, "a")
    f.write(f'Decrease section: \n'
        f'Round 1: *k{placeMarker} pm * repeat across round \n'
            f'Round 2: *k to 2 before marker, k2tog* repeat across round \n'
            f'Round 3: k across round \n'
            f'Repeat rounds 2-3 until 8 stitches remain')
    f.close()
elif castOnStitches % 6 == 0:
    placeMarker = (castOnStitches / 6)
    f = open(filename, "a")
    f.write(f'Decrease section: \n'
            f'Round 1: *k{placeMarker} pm * repeat across round \n'
            f'Round 2: *k to 2 before marker, k2tog* repeat across round \n'
            f'Round 3: k across round \n'
            f'Repeat rounds 2-3 until 8 stitches remain \n')
    f.close()
elif castOnStitches % 10 == 0:
    placeMarker = (castOnStitches / 10)
    f = open(filename, "a")
    f.write(f'Decrease section: \n'
            f'Round 1: *k{placeMarker} pm * repeat across round \n'
            f'Round 2: *k to 2 before marker, k2tog* repeat across round \n'
            f'Round 3: k across round \n'
            f'Repeat rounds 2-3 until 8 stitches remain \n')
    f.close()
else:
    print('unable to calculate decrease rounds. cast on stitches not divisible by 8, 6, or 10.')

f = open(filename, "a")
f.write(f' Cut yarn, thread through remaining live stitches. Draw tight and weave in ends. ')
f.close()
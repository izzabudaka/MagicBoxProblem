Box     = input()
sideLen = len(Box[0])
rows    = {}

# Account for cases where rows are exact inverses
def normalise(row):
  if(row[0]):
    return row
  else:
    for i in range(sideLen):
      row[i] = 1- row[i]
    return row

# pick the row with the least number of flips
def getBestRow(rowArray):
  arrLength = len(rowArray)
  sums = [0] * arrLength
  for i in range(arrLength):
    sums[i] = sum(rowArray[i])
  maxIndex = sums.index(max(sums))
  return (rowArray[maxIndex], sums[maxIndex])

# hash rows
for row in Box:
  row = normalise(row)
  tupledRow = tuple(row)
  if tupledRow in rows:
    rows[tupledRow] += 1
  else:
    rows[tupledRow] = 1

# retrieve most common row with least number of flips
maxVal                      = max(rows.values())
rowKeys                     = [k for k,v in rows.items() if v==maxVal]
(commonRow, flipIndicator)  = getBestRow(rowKeys)
flipIndicator               = sideLen - flipIndicator

# print columns to flip
if flipIndicator > (sideLen/2 + sideLen % 2):
  print [i for i,x in enumerate(commonRow) if x == 1] 
else:
  print [i for i,x in enumerate(commonRow) if x == 0]
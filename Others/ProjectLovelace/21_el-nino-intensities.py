import csv

Data = {}
with open('mei.ext_index.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    next(reader, None)  # skip the header line
    for row in reader:
        Data[int(row[0])] = list(map(float,row[1:]))

It = ('weak', 'moderate', 'strong', 'very strong')

def enso_classification(two_year_period):
    y = int(two_year_period.split('-')[0])
    classification = 'Neither'
    intensity = 'none'
    mei = 0
    data = Data[y] + Data[y+1]
    for i in range(len(data)-5):
        m = min(data[i:i+5])
        M = max(data[i:i+5])
        if m>0.5:
            classification = 'El Nino'
            mei = max(data)
            intensity = It[min(int(2.*(mei-0.5)), len(It)-1)]
            break
        elif M<-0.5:
            classification = 'La Nina'
            mei = min(data)
            intensity = It[min(int(2.*(-mei-0.5)), len(It)-1)]
            break
    return classification, intensity, mei
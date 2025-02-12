def makeEquiDepthBin(data : list,numOfBin : int) -> list[list]:
    
    binDepth = len(data)//numOfBin
    bins=[]
    for i in range(numOfBin):
        start = i*binDepth
        end = (i+1)*binDepth if i < numOfBin - 1 else len(data)
        
        bin = []
        for j in range(start,end):
            bin.append(data[j])
        bins.append(bin)
    return bins


def makeEquiWidthBin(data : list,numOfBin : int) -> list[list]:
    
    dataRange = max(data) - min(data)
    width = dataRange / numOfBin
    bins = [[] for _ in range(numOfBin)]
    edges = []
    for i in range (numOfBin+1):
        edges.append(min(data) + i*width)
    for value in data:
        for j in range (numOfBin):
            if(edges[j] <= value < edges[j+1]):
                bins[j].append(value)
                break
        if (value == edges[-1]):
                bins[-1].append(value)
    return bins 
            

def binByMean(data : list,numOfBin : int,method : str) -> list:
    smoothData = []
    try:
        if method == 'D':
            bins = makeEquiDepthBin(data,numOfBin)
        elif method == 'W':
            bins = makeEquiWidthBin(data,numOfBin)
        else :
            raise Exception ("Invalid method. Please enter 'D' for equi-depth or 'W' for equi-width")
    except Exception as e:
        print("Error: ",e)
    print(f"Orignal data : {data} ")
    print("\nBins Before Smoothing :")
    smoothBins = []
    for bin in bins:
        print(bin)
        mean = round(sum(bin)/len(bin),2)
        binLen = len(bin)
        smoothBin = []
        for i in range(binLen):
            smoothData.append(mean)
            smoothBin.append(mean)
        smoothBins.append(smoothBin)
    print("\nBins After Smoothing : ")
    for bin in smoothBins:
        print(bin)
    print(f"\nSmoothed Data : {smoothData}")
    return smoothData


        
def binByMedian(data : list,numOfBin : int,method : str) -> list:
    smoothData = []
    try:
        if method == 'D':
            bins = makeEquiDepthBin(data,numOfBin)
        elif method == 'W':
            bins = makeEquiWidthBin(data,numOfBin)
        else :
            raise Exception ("Invalid method. Please enter 'D' for equi-depth or 'W' for equi-width")
    except Exception as e:
        print("Error: ",e)
    print(f"Orignal data : {data}")
    print("\nBins Before Smoothing :")
    smoothBins = []
    for bin in bins:
        print(bin)
        binLen = len(bin)
        median = bin[binLen//2] if binLen % 2 != 0 else (bin[binLen//2 - 1] + bin[binLen // 2]) / 2
        smoothBin = []
        for i in range(binLen):
            smoothData.append(median)
            smoothBin.append(median)
        smoothBins.append(smoothBin)
    print("\nBins After Smoothing : ")
    for bin in smoothBins:
        print(bin)
    print(f"\nSmoothed Data : {smoothData}") 
    return smoothData             



def binByBoundary(data : list,numOfBin : int,method : str) -> list:
    smoothData = []
    try:
        if method == 'D':
            bins = makeEquiDepthBin(data,numOfBin)
        elif method == 'W':
            bins = makeEquiWidthBin(data,numOfBin)
        else :
            raise Exception ("Invalid method. Please enter 'D' for equi-depth or 'W' for equi-width")
    except Exception as e:
        print("Error: ",e)
    print(f"Orignal data : {data}")
    print("\nBins Before Smoothing :")
    smoothBins = []
    for bin in bins:
        print(bin)
        binLen = len(bin)
        smoothBin = []
        # mean = round(sum(bin)/len(bin),2)
        minVal = min(bin)
        maxVal = max(bin)
        for i in range(binLen):
            if abs(bin[i]-minVal) <= abs(bin[i]-maxVal):
                smoothData.append(minVal)
                smoothBin.append(minVal)
            else:
                smoothData.append(maxVal)
                smoothBin.append(maxVal)
        smoothBins.append(smoothBin)
    print("\nBins After Smoothing : ")
    for bin in smoothBins:
        print(bin)
    print(f"\nSmoothed Data : {smoothData}")
    return smoothData


        
# Sample data
a = [5, 10, 11, 13, 35, 50, 55, 75, 92, 100, 204, 215]


# Get the number of bins from the user
numofbins = int(input("Enter no. of bins: "))
method = str(input("Enter method for Binning :\n\'D\' for EquiDepth \n\'W\' for EquiWidth\n"))
parameter = str(input("Enter parameter for Binning :\n\'X\' for Mean \n\'M\' for Median \n\'B\' for Boundary\n"))

if(method == 'D'):
    print("\nEquiDepth Binning\n")
    if(parameter == 'X'):
        print("Binning by Mean\n")
        binByMean(a,numofbins,method)
    elif(parameter == 'M'):
        print("Binning by Median\n")
        binByMedian(a,numofbins,method)
    elif(parameter == 'B'):
        print("Binning by Boundary\n")
        binByBoundary(a,numofbins,method)
elif(method == 'W'):
    print("\nEquiWidth Binning\n")
    if(parameter == 'X'):
        print("Binning by Mean\n")
        binByMean(a,numofbins,method)
    elif(parameter == 'M'):
        print("Binning by Median\n")
        binByMedian(a,numofbins,method)
    elif(parameter == 'B'):
        print("Binning by Boundary\n")
        binByBoundary(a,numofbins,method)





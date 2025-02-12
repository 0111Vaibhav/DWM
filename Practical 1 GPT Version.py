def makeEquiDepthBin(data: list, numOfBin: int) -> list[list]:
    """Create bins of equal depth."""
    data.sort()
    binDepth = len(data) // numOfBin
    return [data[i * binDepth: (i + 1) * binDepth] for i in range(numOfBin - 1)] + [data[(numOfBin - 1) * binDepth:]]

def makeEquiWidthBin(data: list, numOfBin: int) -> list[list]:
    """Create bins of equal width."""
    data.sort()
    dataRange = max(data) - min(data)
    width = dataRange / numOfBin
    edges = [min(data) + i * width for i in range(numOfBin + 1)]
    
    bins = [[] for _ in range(numOfBin)]
    for value in data:
        for j in range(numOfBin):
            if edges[j] <= value < edges[j + 1]:
                bins[j].append(value)
                break
        if value == edges[-1]:  # Edge case for max value
            bins[-1].append(value)
    
    return bins

def binning(data: list, numOfBin: int, method: str, parameter: str) -> list:
    """General function to perform binning using Mean, Median, or Boundary methods."""
    try:
        bins = makeEquiDepthBin(data, numOfBin) if method == 'D' else makeEquiWidthBin(data, numOfBin) if method == 'W' else None
        if bins is None:
            raise ValueError("Invalid method. Use 'D' for EquiDepth or 'W' for EquiWidth")
    except Exception as e:
        print(f"Error: {e}")
        return []

    print(f"Original Data: {data}")
    print("\nBins Before Smoothing:")
    for bin in bins:
        print(bin)

    smoothBins = []
    smoothData = []
    
    for bin in bins:
        if parameter == 'X':  # Mean
            smoothValue = round(sum(bin) / len(bin), 2)
        elif parameter == 'M':  # Median
            mid = len(bin) // 2
            smoothValue = bin[mid] if len(bin) % 2 != 0 else round((bin[mid - 1] + bin[mid]) / 2, 2)
        elif parameter == 'B':  # Boundary
            minVal, maxVal = min(bin), max(bin)
            smoothValue = [minVal if abs(x - minVal) <= abs(x - maxVal) else maxVal for x in bin]
        else:
            raise ValueError("Invalid parameter. Use 'X' for Mean, 'M' for Median, or 'B' for Boundary")

        smoothBin = [smoothValue] * len(bin) if isinstance(smoothValue, (int, float)) else smoothValue
        smoothBins.append(smoothBin)
        smoothData.extend(smoothBin)

    print("\nBins After Smoothing:")
    for bin in smoothBins:
        print(bin)
    
    print(f"\nSmoothed Data: {smoothData}")
    return smoothData

# Sample Data
a = [5, 10, 11, 13, 35, 50, 55, 75, 92, 100, 204, 215]

# User Input
numofbins = int(input("Enter no. of bins: "))
method = input("Enter method for Binning:\n'D' for EquiDepth \n'W' for EquiWidth\n")
parameter = input("Enter parameter for Binning:\n'X' for Mean \n'M' for Median \n'B' for Boundary\n")

# Call Binning Function
binning(a, numofbins, method, parameter)

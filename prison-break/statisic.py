from csv import reader
import math


class dataSets:

    def __init__(self, fileName: str, col: int, exCol: int) -> list:
        self.fileName = fileName
        self.col = col
        self.exCol = exCol
        self.dataReal = []

        decode_notation = 'US'

        try:
            file = open(self.fileName)
            try:
                dataset = list(reader(file))[self.exCol:]
                dataReal = []
                for row in dataset:
                    data = row[self.col]
                    if(data != '' and decode_notation):
                        dataReal.append(float(''.join(data[1:].split(','))))
                self.dataReal = dataReal
                self.dataReal.sort()
            except:
                print('failed while parsing the file')
            finally:
                file.close()
        except:
            print('cannot find file')
            raise FileNotFoundError('cannot find file')

    def dataSet(self) -> list:
        return self.dataReal

    def avarage(self) -> int:
        x = sum(self.dataReal) / len(self.dataReal)
        return x

    def median(self) -> int:
        xn = len(self.dataReal)
        # return xn
        if len(self.dataReal) % 2 != 0:
            # return 'ganjil'
            xn = self.checkNum((xn + 1)/2)
            print(xn)
            return self.dataReal[xn]
        else:
            # return 'genap'
            xn = self.checkNum((xn/2 + (xn/2+1))/2)
            # return (xn/2 + (xn/2+1))/2
            print(xn)
            return self.dataReal[xn]

    def checkNum(self, num) -> int:
        if(num - .5 > float(int(num))):
            return self.round_up(num)
        if(num - .5 <= float(int(num))):
            return self.round_down(num)

    def round_down(self, n, decimals=0) -> int:
        multiplier = 10 ** decimals
        return int(math.floor(n * multiplier) / multiplier)

    def truncate(self, n, decimals=0) -> int:
        multiplier = 10 ** decimals
        return int(int(n * multiplier) / multiplier)

    def round_up(self, n, decimals=0) -> int:
        multiplier = 10 ** decimals
        return int(math.ceil(n * multiplier) / multiplier)


myData = dataSets('Product Dataset.csv', 3, 1)
print(myData.median())
print(len(myData.dataSet()))
# price_sum = sum(price_data)

# print(price_sum/len(price_data))

# goal to calculate total prices

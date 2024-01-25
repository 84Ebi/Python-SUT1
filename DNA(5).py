class MrKrabs:
    def __init__(self, data):
        self.data = data

    def process(self):
        result = ""

        if self.data.startswith("m"):
            result = self.processmrkr()

        elif self.data.startswith("sb"):
            result = self.processsp()

        elif self.data.startswith("s") and self.data[1] != "b":
            result = self.processsq()

        elif self.data[-1] == "m":
            self.data = self.data[::-1]
            result = self.processmrkr()

        elif self.data[-1] == "s" and self.data[-2] == "b":
            self.data = self.data[::-1]
            result = self.processsp()

        elif self.data[-1] == "s" and self.data[-2] != "b":
            self.data = self.data[::-1]
            result = self.processsq()

        else:
            result = "invalid input"

        return result

    def processmrkr(self):
        result = self.data.replace("tt", "o")
        tee = self.data[:10].replace("tt", "o")
        return result + tee

    def processsp(self):
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                suba2 = arr[mid:]
                suba1 = arr[:mid]
                mergeSort(suba2)
                mergeSort(suba1)
                i = j = k = 0
                while i < len(suba1) and j < len(suba2):
                    if suba1[i] < suba2[j]:
                        arr[k] = suba1[i]
                        i += 1
                    else:
                        arr[k] = suba2[j]
                        j += 1
                    k += 1
                while i < len(suba1):
                    arr[k] = suba1[i]
                    i += 1
                    k += 1
                while j < len(suba2):
                    arr[k] = suba2[j]
                    j += 1
                    k += 1

        def sortdna(dna):
            length = list(str(len(dna)))
            tmp1 = [int(length[i]) for i in range(len(length))]
            mergeSort(tmp1)
            sortedl = ""
            for i in range(len(tmp1)):
                sortedl += f"{tmp1[i] + 1}" if i == 0 else f"{tmp1[i]}"
            return sortedl

        return sortdna(self.data)

    def processsq(self):
        result = ""
        i = 0
        tmp2 =0
        flag = False
        while i < len(self.data):
            count = 1
            if self.data[i]=="x" and flag==False:
                tmp2+=i
                flag=True
            while i + count < len(self.data) and self.data[i] == self.data[i + count]:
                count += 1

                if count >= 3:
                    break

            if count >= 3:
                result += "(0_0)"
                i += count

            else:
                result += self.data[i]
                i += 1
        if flag==True:
            result+=f"{tmp2}"
        return result


input1 = input()
mrkrab = MrKrabs(input1)
result = mrkrab.process()
print(result)

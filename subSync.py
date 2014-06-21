import re

def synchronizer(filename, offset):
    filename = filename.encode('string-escape')
    myfile = open(filename, "r+")
    lst = myfile.readlines()
    test = r"[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]\,[0-9][0-9][0-9]"
    timeLst = []
    for content in lst:
        if re.findall(test, content) != []:
            timeLst.append(re.findall(test, content))
            
    for elem in timeLst:
        startTime = elem[0][6:8]
        endTime = elem[1][6:8]
        startTime = int(startTime) + offset
        endTime = int(endTime) + offset
        endTime = str(endTime) if endTime > 9 else "0" + str(endTime)
        startTime = str(startTime) if startTime > 9 else "0" + str(startTime)
        elem[0] = elem[0][:6] + str(startTime) + elem[0][8:]
        elem[1] = elem[1][:6] + str(endTime) + elem[1][8:]
        
    count = 0    
    resultLst = []
    for content in lst:
        if re.findall(test, content) != []:
            s = re.findall(test, content)
            for i in range(2):
                content = re.sub(s[i], timeLst[count][i], content)
            count += 1
        resultLst.append(content)
        
    myfile.seek(0, 0)
    myfile.writelines(resultLst)
    myfile.close()

synchronizer("C:\Users\rajiv\Desktop\House of Cards (2013) - 01x01 - Chapter 1.480p.WEBRip.x264-BTN.English.orig.Addic7ed.com.srt", -1)
f = open("main.tex","a")
list = open("list.txt")


Template = open("tekTemplate.txt")
PicTemp = open("tekTemplatePicture.txt")
FirstPage = open("CelesticaTemplate.txt")

PicTempLines = PicTemp.readlines()
TestPoints = list.readlines()
FirstPageLines = FirstPage.readlines()


content = Template.readlines()
# Remember to print out directly you need to add an extra slash for it to print out 




#for line in content:
#    line.replace("Blah")
#    f.write(line)

for someLine in FirstPageLines:
    print(someLine)
    f.write(someLine)
    
f.write("\n")
f.write("\n")

 
for tp in TestPoints:
    f.write("\\newpage\n")
    f.write("\\ThisCenterWallPaper{1}{CelesticaNextPages.pdf}\n")
    tp = tp.replace("\n",'')
    location = tp+"/results.txt"
    figurename = "\\caption{blah}\n"
    figurename = figurename.replace("blah",tp+" Waveform characterestics")
    figurename = figurename.replace("_"," ")
    f.write(figurename)
    f.write("\\begin{table}[h]\n")
    f.write("\\begin{tabular}{llll}\n")
    f.write("\\hline\n")
    f.write("\\multicolumn{1}{|l|}{Parameter} & \\multicolumn{1}{l|}{Specification} & \\multicolumn{1}{l|}{Measured Results} & \\multicolumn{1}{l|}{Status} \\\ \\hline\n")
    TestResults = open(location)
    results = TestResults.readlines()
    for i in range(len(content)):
        results[i] = results[i].replace("\n", '')
        content[i] = content[i].replace("blah", results[i])
        print(content[i])
        f.write(content[i])
    f.write("\n")
    f.write("\\end{tabular} \n")
    f.write("\\end{table} \n")
    print("\n")
    f.write("\n")
    location = tp+"/PicList.txt"
    picnames = open(location)
    
    # setting up Pictures 
    pic = picnames.readlines()
    f.write("\\newpage\n")
    f.write("\\ThisCenterWallPaper{1}{CelesticaNextPages.pdf}\n")
    for i in range(len(PicTempLines)):
        if i == 2:
            f.write("\\newpage\n")
            f.write("\\ThisCenterWallPaper{1}{CelesticaNextPages.pdf}\n")
        pic[i] = pic[i].replace("\n","")
        location = tp +"/"+pic[i]+".png"
        piclocation = PicTempLines[i].replace("BLAH",location)
        f.write(piclocation)
    f.write("\n")
    f.write("\n")
f.write("\\end{document}")

    




PicTempLines[2] = PicTempLines[2].replace("BLAH",TestPoints[0])
print(PicTempLines[2])  

#from pylatex import Document 
f.close()
#
#doc = Document('basic')
#doc.generate_pdf('main',clean_tex=False)
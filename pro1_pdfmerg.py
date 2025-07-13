from PyPDF2 import PdfMerger

ALLPDF =["p1.pdf", "p2.pdf"]
Ourmerger = PdfMerger()

for Newpdf in ALLPDF:
    Ourmerger.append(Newpdf)



Ourmerger.write("HABLUT.PDF")
Ourmerger.close()

print("merger succecfully")
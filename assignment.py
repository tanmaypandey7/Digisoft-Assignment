import pydicom

dcm1=r"dcm files\bmode.dcm"
dcm2=r"dcm files\ttfm.dcm"

dcm_data1 = pydicom.dcmread(dcm1)
dcm_data2 = pydicom.dcmread(dcm2)

temp1=str(dcm_data1)
temp2=str(dcm_data2)

with open(r"text files\bmode.txt", "w") as text_file:
    text_file.write(temp1)

with open(r"text files\ttfm.txt", "w") as text_file:
    text_file.write(temp2)
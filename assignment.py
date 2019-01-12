import pydicom

dcm1=r"C:\Users\Vision\Desktop\Digisoft-Assignment\ttfm.dcm"
dcm2=r"C:\Users\Vision\Desktop\Digisoft-Assignment\bmode.dcm"

dcm_data1 = pydicom.dcmread(dcm1)
dcm_data2 = pydicom.dcmread(dcm2)

temp1=str(dcm_data1)
temp2=str(dcm_data2)

with open("ttfm.txt", "w") as text_file:
    text_file.write(temp1)

with open("bmode.txt", "w") as text_file:
    text_file.write(temp2)
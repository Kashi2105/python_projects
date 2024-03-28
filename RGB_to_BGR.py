import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(7,7))
img_RGB=Image.open(r"C:\Users\yuvra\OneDrive\Desktop\KASHI\kashi_pic.jpg")
fig.add_subplot(1,2,1)
plt.title("Image in RGB")
plt.imshow(img_RGB)
img_data=np.array(img_RGB)
bgr_data=img_data[:,:,::-1]
bgr_image=Image.fromarray(bgr_data)
fig.add_subplot(1,2,2)
plt.title("Image in BGR")
plt.imshow(bgr_image)
plt.show()
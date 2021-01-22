

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
from tkinter import messagebox
import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import cv2





width = 300
height = 300
center = height//1
white = (255, 255, 255)
green = (0, 128, 0)



def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black", width=15)
    draw.line([x1, y1, x2, y2], fill="black", width=15)
    #filename = "capture.bmp"
    #image1.save(filename)




def load_image(filename):
    # filename = "capture.png"
    # image1.save(filename)
    # load the image
    img = load_img('capture.png', grayscale=True, target_size=(28, 28))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


# load an image and predict the class
def result():
    # save the image
    filename = "capture.png"
    image1.save(filename)
    # load the image
    img = load_image('capture.png')
    # load model
    model = load_model('ai_model.h5')
    # predict the class
    digit = model.predict_classes(img)
    messagebox.showinfo("Kết quả", digit[0])




def delete():
    cv.delete("all")
    # if os.path.exists("capture.bmp"):
    #     os.remove("capture.bmp")
    #    messagebox.showwarning("Cảnh báo", "Đã xoá")
    #else:
    #    messagebox.showerror("Lỗi", "File không tồn tại")
    root.update()


    #filename = "capture.png"
    #ilename = "capture1.png"
    #image1.save(filename)
    #img = load_image('cv')

    #img = image1.os.path.exists("cature.png")
    #img.save(img)


    #image1.save(paint())
    #image1.load(cv)
    # load the image


def openfn():
    filename = filedialog.askopenfilename(title='open')

    return filename


def open_img():

    x = openfn()
    cv2 = Image.open(x)
    cv2 = cv2.resize((50, 50), Image.ANTIALIAS)
    cv2 = ImageTk.PhotoImage(cv2)
    panel = Label(root, image=cv2)





    panel.image = cv2
    panel.pack()
    img = load_image('cv2')
    # load model
    model = load_model('ai_model.h5')
    # predict the class
    digit = model.predict_classes(img)
    messagebox.showinfo("Kết quả", digit[0])




# load and prepare the image


#entry point, run the example
root = Tk()
root.title('Nhận diện chữ số viết tay')

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.grid(row=0, column=0)
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)

button1 = Button(root, text="Xoá", command=delete)
button1.pack()
button = Button(root, text="Kết quả", command=result)
button.pack()
btn = Button(root, text='open image', command=open_img).pack()
root.mainloop()


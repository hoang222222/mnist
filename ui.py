from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
from tkinter import messagebox
import os

width = 600
height = 400
center = height // 2
white = (255, 255, 255)
green = (0, 128, 0)


def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_oval(x1, y1, x2, y2, fill="black", width=5)
    draw.line([x1, y1, x2, y2], fill="black", width=5)


def delete():
    cv.delete("all")
    if os.path.exists("capture.png"):
        os.remove("capture.png")
    #    messagebox.showwarning("Cảnh báo", "Đã xoá")
    # else:
    #    messagebox.showerror("Lỗi", "File không tồn tại")


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img("capture.png", grayscale=True, target_size=(28, 28))
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
    # filename =
    image1.save("capture.png")
    # load the image
    img = load_image("capture.png")
    # load model
    model = load_model('ai_model.h5')
    # predict the class
    digit = model.predict_classes(img)
    messagebox.showinfo("Kết quả", digit[0])


# entry point, run the example
root = Tk()
root.title('Nhận diện chữ số viết tay')

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')

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
btn_result = Button(root, text="Kết quả", command=result)
btn_result.pack()
btn_del = Button(root, text="Xoá", command=delete)
btn_del.pack()
root.mainloop()

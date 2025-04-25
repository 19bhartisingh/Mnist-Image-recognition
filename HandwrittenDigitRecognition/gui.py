from keras.models import load_model
from tkinter import *
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import matplotlib.pyplot as plt

model = load_model('mnist.h5')

def predict_digit(img):
    # Resize and convert to grayscale
    img = img.resize((28, 28))
    img = img.convert('L')
    
    # Invert image (black digit on white background)
    img = ImageOps.invert(img)
    
    # Convert to NumPy and threshold
    img = np.array(img)
    img = np.where(img > 100, 255, 0).astype('uint8')

    # Normalize
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Optional debug
    plt.imshow(img.squeeze(), cmap='gray')
    plt.title("Processed Input")
    plt.axis('off')
    plt.show()

    res = model.predict([img])[0]
    return np.argmax(res), max(res)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas_width = 300
        self.canvas_height = 300
        self.x = self.y = 0

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white", cursor="cross")
        self.label = tk.Label(self, text="Draw a digit", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text="Recognize", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)

        self.canvas.grid(row=0, column=0, pady=2, sticky=W)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

        # Image buffer (PIL)
        self.image1 = Image.new("L", (self.canvas_width, self.canvas_height), 'white')
        self.draw = ImageDraw.Draw(self.image1)

    def clear_all(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_width, self.canvas_height], fill="white")

    def classify_handwriting(self):
        # Crop bounding box from image
        bbox = self.image1.getbbox()
        if bbox:
            cropped_img = self.image1.crop(bbox)
        else:
            cropped_img = self.image1

        digit, acc = predict_digit(cropped_img)
        self.label.configure(text=f'{digit}, {int(acc * 100)}%')

    def draw_lines(self, event):
        r = 8  # thicker radius
        self.x = event.x
        self.y = event.y
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black', outline='black')
        self.draw.ellipse([self.x - r, self.y - r, self.x + r, self.y + r], fill='black')


app = App()
mainloop()

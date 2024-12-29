from PIL import Image

# Define dummy functions for the buttons
def func1():
    print("Function 1 executed")

def func2():
    print("Function 2 executed")

def func3():
    print("Function 3 executed")




# Define a dummy function to get a video (placeholder)
def getvideo(width, height):
    # return None
    image = Image.open("drone icon.jpeg")
    print(width, height)
    return image.resize((width, height))
    
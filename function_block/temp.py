from PIL import Image



def func1():
    print("Function 1 executed")

def func2():
    print("Function 2 executed")

def func3():
    print("Function 3 executed")

def btn():
    ...



# Define a dummy function to get a video (placeholder)
def getvideo(width, height):
    image = Image.open("drone icon.jpeg")
    return image.resize((width, height))

# Define a function to get data from the drone swarm server
def get_data(type):
    # should give the bloc the convenient data based on the type, the type is the type of data needed
    data = {}
    return data


    




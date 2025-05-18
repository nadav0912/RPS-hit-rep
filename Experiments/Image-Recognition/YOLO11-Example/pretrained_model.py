from ultralytics import YOLO
import torch

epochs = 10

# Compute on GPU if available, else CPU
if torch.cuda.is_available():
    device = '0'
    print(f'Using GPU, code \'{device}\'')
else:
    device = 'cpu'
    print(f'Using CPU, code \'{device}\'')

# Load a model
model = YOLO("yolo11n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(
    data="hand-keypoints.yaml", 
    epochs=epochs, 
    imgsz=640, 
    device=device
)

# Validate model
metrics = model.val()

'''
This is an example as to how you test the model.
save={bool} - saves the result in the runs/ folder. 
show={bool} - shows you the result file
Change these parameters as you see fit 
'''
#results = model('testImg1.jpg', save=True, show=True)
#results[0].show()


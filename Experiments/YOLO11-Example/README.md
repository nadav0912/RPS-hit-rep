# General information
YOLO11 by ultralytics is an object/image recognition model

In this folder you'll find different examples I've made with simple explanations to guide
through the examples.

Note: datasets/, runs/ folders will be added as you run the code, don't worry those folders are already listed in the .gitignore.


# Files

### hand-keypoints.yaml
Can be ignored<br />
General file necessary to the model that is used in this example<br />
-The file contains information for the model<br />
-The file contains the dataset's download link, it should be downloaded automatically once you run one<br />
 of the examples. If it doesn't you'll have to download it manually and unzip it's files in the
 same structure show at the top of the .yaml file<br />

### pretrained_model.py
A pretrained model, needs to be trained to give results, yolo takes care of everything and even
downloads the datasets.<br />
It's results at the begining are trash because it isn't trained, once trained you can also see
it's progression through the printed parameters of the training model<br />


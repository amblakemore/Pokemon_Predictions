# Pokemon Predictions

https://pokemon-project3.herokuapp.com/


## Data

### Collecting and Cleaning the Data
Using the Kaggle dataset by Lance Zhang, 149 classes of Pokemone from generation one were collected and sorted into their own folders. To prepare the images to train the model, we reviewed and cleaned the images from the original dataset including: any image that was irrelevant to the classification, any image with multiple pokemon in the picture, and any images of a Mega Evolution. The images were then uploaded to Google Drive and were ready to train the model

## Model Deployment

### Machine Learning Model
The maching learning algorithm was created using Google Colab allowing us to train our model with over 7,000 images! Using Tensorflow and Keras, the model was trained, saved, and loaded using Tensorflow, Keras, and Flask (Tensorflow 2.4.1 and Keras 2.3.4).

### Iterations
Using the first model, training accuracy was nearly 100% but validation accuracy was only 30%. The second round of model training resulted in about 75% training accury. It was during this time that the model steadily improved in accuracy and reduce the training and test loss gap.

The second model utilized image augmentation to create new training samples out of existing data to improve the performance and ability of the model to generalized. NOTE: image augmentation was only applied to the training data.

### Heroku Deployment
Using Heroku to deploy our app proved to be convenient and efficient. To deploy the app on Heroku's cloud based platform service, the following steps were taken: 
* Linking Heroku and the Github Repo
* Updated the required files and folder structure to ensure the app deployed correctly
* Using the correct and updated procfile, requirments.txt, slugignore (to save memory)
* Using tensorflow-cpu to stay under the memory limit
* Utilizing .slugignor files for unused files
* Ensuring that the app deployed correctly.

## Conclusions
For the purpose of this project, we went with our version from Round 2 but obviously there is ALOT more that can be done. We do believe one key factor to improving our model is to increase the amount of images for testing and training since we have a large amount of classification. Many suggest each class to contain 1000 images. Currently, we range from 40-70 images per class. Another key item to further tuning is having the resources to run these training models!

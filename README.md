# MeowBot
Discord bot to tell if the given image attached in chat is a cat with confidence of prediction in %.

Uses a 4 layer (12288, 20, 7, 5, 1) neural network implemented from DeepLearning.AI Neural Networks and Deep Learning Week 4 final assignment.

### To host the bot
First clone this repo and install the dependencies
```
pip install discord
pip install numpy
pip install pillow
```
Then run the bot using 
```
python bot.py <TOKEN>
```

### For trying the bot
Message me for link to join my testing server, or the link to invite the bot running on my machine.

### To train the model
Run 
```
python train.py
```
This will take the datasets and utility functions and train the model and store it in parameters.json

I have already trained and stored the parameters in the parameters.json file, but you can try to tweak with the model parameters.
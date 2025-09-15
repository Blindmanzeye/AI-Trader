This is my Ultimate Project to test all of my skills to date, I will pull stock data using IBKR's API, parse the numbers using Numpy and Pandas, then train a pretrained AI specialized in 
Predicting numbers to tweak it to a specific stock, or a classification of stocks (fortune 500, "tech" etc)

Then, I will choose a specific stock, or a group of stocks, run the numbers through my AI to get a prediction on whether to buy or sell. For now, I will only use DRY testing (no money just predict and analyze).

My Dry tests results can be found in the TestLog.txt


The development will happen in 4 stages, each stage has its own folder. 

Stage 1) Pull and Parse Data
Stage 2) Develop Base AI 
Stage 3) Train/Tweak AI
Stage 4) Combine stages 1-3 and Test/Tweak AI further.

In Depth. . . 

Stage 1) Pull and Parse Data
- We will use IKBR's API to pull stock data (This will test my ability to call/use API's)
- We will then Parse the data using various methods and libraries including Numpy and Pandas (This will test my ability to proccess/parse data)
- Then, I will store the data in a file to be used for the later steps (This will test my ability to read/write to files)

Stage 2) Develop Base AI
- I will research what AI to use (This will test my research skills)
- Then, I will use either pytorch, scikit-learn, or both to get it's base, pretrained state, running on my machine (This will test pytorch/scikit-learn ability)
- I will then create a data and data loading class and integrate it with the AI to make sure it gets it's training data (Ability of Class creation and design)
- Once that is set up, I will begin training the AI. (This will test my ability to work with open source models, and my money [gpu :sob:])

Stage 3) Train and Tweak AI
- Once we train it for the first time with a small dataset to make sure it actually trains, We train using a larger dataset
- Tweak our data and dataloader classes to take more data, while increasing the number of epochs we will train for. (Ability of being able to edit working code)
- Then, by using our AI's mean square error, we will change the number of epochs and data per epoch, while watching out for any overfitting (Ability of Mathematical Analysis and AI theory)

Stage 4) Combine and Test
- We will attempt to combine all steps into a major folder. The reason is because I want to modify Stage 1 to get less amounts of Live data, instead of large amounts of past data.
- Also, combining all files will definitly break something
- Then, we will begin possibly our longest stage yet, Extensive Testing. (that's if I dont lose my brain spending months doing stage 3)
- Each test will look at specific sections of the stock market, then have it make a prediction. We will then track that prediction and see if it works out or not, then record our results in TestLog.txt
- Depending on the results of our test, we will either train it more or actually use it for personal financial gain
- This project will be dropped and used as a display of my skill if it doesn't work out for a year of this stage.
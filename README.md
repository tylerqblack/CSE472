# Final Report [LINK](https://docs.google.com/document/d/1O_iEl2x9zU2b3h1-YfiPune_lA1jrv59NLKKLneoFb8/edit):
Detailed content is written in this report!

## Procedure
1. We used 16 features per each extractor in .ipynb
2. Bot_Feature_Extraction.ipynb -> bot_features.pkl
3. Hum_Feature_Extraction.ipynb -> hum_features.pkl
3. Unlabeled_Feature_Extraction.ipynb -> unlabeled_features.pkl
4. Fake_Follower_Classifier.ipynb
+ Train it with KNN, Logistic regression, MLP, Random Forest
+ Train it with self-supervised learning (Label propagation)
5. Final result is about 99% accuracy.

## Papers
1. An enhanced graph‑based semi‑supervised learning algorithm to detect fake users on Twitter
2. THE ART OF SOCIAL BOTS: A REVIEW AND A REFINED TAXONOMY
3. LOBO – Evaluation of Generalization Deficiencies in Twitter Bot Classifiers : https://arxiv.org/abs/1809.09684
4. Better Safe Than Sorry: an Adversarial Approach to improve Social Bot Detection : https://arxiv.org/abs/1904.05132
5. Using Improved Conditional Generative Adversarial Networks to Detect Social Bots on Twitter : https://ieeexplore.ieee.org/document/9006873

## Dataset Download [LINK](https://drive.google.com/drive/folders/157pcedewvyJLXBpxL7y2LJSp3MiGS8tc?usp=sharing) :
Put /datasets directory within the same location of our .ipynb
1. [vendor-purchased-2019](https://botometer.osome.iu.edu/bot-repository/datasets/vendor-purchased-2019/vendor-purchased-2019.tar.gz)
+ This dataset is proposed in "Arming the public with artificial intelligence to counter social bots."
+ Some of profile_image_url_https are not able to access (Page not found)

2. [Fame for sale](https://botometer.osome.iu.edu/bot-repository/datasets/cresci-2015/cresci-2015.csv.tar.gz)
+ E13 and TFP are Human / FSF, INT, and TWT are Bot

3. Unlabeled Tweet user data : We crawl about 830 of twitter user data by using tweepy API.

# Google Doc [LINK](https://docs.google.com/document/d/1O_iEl2x9zU2b3h1-YfiPune_lA1jrv59NLKKLneoFb8/edit)

## Progress
1. Getting two features(friends/follower ratio, is "bot" in user name?) from Bot dataset(vendor-purchased-19) and Human dataset(TFP, E13)
2. Bot_Feature_Extraction.ipynb -> bot_features.pkl
3. Hum_Feature_Extraction.ipynb -> hum_features.pkl
4. Fake_Follower_Classifier.ipynb -> Train KNN and MLP and get evaluation matrix
5. Final result is about 80% accuracy.

## Papers (AI-bot detection)

1. LOBO – Evaluation of Generalization Deficiencies in Twitter Bot Classifiers : https://arxiv.org/abs/1809.09684
2. Better Safe Than Sorry: an Adversarial Approach to improve Social Bot Detection : https://arxiv.org/abs/1904.05132
3. Using Improved Conditional Generative Adversarial Networks to Detect Social Bots on Twitter : https://ieeexplore.ieee.org/document/9006873

Let's see 2&3 when we have some time to expand our model.

## Tutorial (Fake follower detection)
1. https://github.com/lminy/BotDetector
+ This code is from "Fame for sale: efficient detection of fake Twitter followers"
+ There is no dataset directory in this github, and it will be not able to execute.
+ If you want, you can include dataset from this [URL](https://botometer.osome.iu.edu/bot-repository/datasets/cresci-2015/cresci-2015.csv.tar.gz)

## Dataset (Fake follower detection)
1. [vendor-purchased-2019](https://botometer.osome.iu.edu/bot-repository/datasets/vendor-purchased-2019/vendor-purchased-2019.tar.gz)
+ This dataset is proposed in "Arming the public with artificial intelligence to counter social bots."
+ Some of profile_image_url_https are not able to access (Page not found)
2. [Fame for sale](https://botometer.osome.iu.edu/bot-repository/datasets/cresci-2015/cresci-2015.csv.tar.gz)
+ E13 and TFP are Human / FSF, INT, and TWT are Bot
### Sample data [vendor-purchased-2019]
[                                                                               
    {                                                                           
        "created_at": "Tue Jan 09 16:38:26 +0000 2018",                         
        "user": {                                                               
            "follow_request_sent": "false",                                     
            "has_extended_profile": "false",                                    
            "profile_use_background_image": "true",                             
            "id": 53805021,                                                     
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
            "verified": "false",                                                
            "translator_type": "none",                                          
            "profile_text_color": "333333",                                     
            "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "profile_sidebar_fill_color": "DDEEF6",                             
            "is_translator": "false",                                           
            "entities": {                                                       
                "description": {                                                
                    "urls": []                                                  
                }                                                               
            },                                                                  
            "followers_count": 3,                                               
            "profile_sidebar_border_color": "C0DEED",                           
            "id_str": "53805021",                                               
            "default_profile_image": "true",                                    
            "listed_count": 0,                                                  
            "is_translation_enabled": "false",                                  
            "utc_offset": 28800,                                                
            "statuses_count": 8,                                                
            "description": "",                                                  
            "friends_count": 359,                                               
            "location": "",                                                     
            "profile_link_color": "1DA1F2",                                     
            "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
            "notifications": "false",                                           
            "geo_enabled": "false",                                             
            "profile_background_color": "C0DEED",                               
            "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
            "screen_name": "guowei534",                                         
            "lang": "en",                                                       
            "profile_background_tile": "false",                                 
            "favourites_count": 10,                                             
            "name": "pan",                                                      
            "url": "null",                                                      
            "created_at": "Sun Jul 05 01:14:40 +0000 2009",                     
            "contributors_enabled": "false",                                    
            "time_zone": "Beijing",                                             
            "protected": "false",                                               
            "default_profile": "true",                                          
            "following": "false"                                                
        }                                                                       
    }                                                                           
]                

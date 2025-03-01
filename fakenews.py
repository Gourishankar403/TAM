fake_phrases=[
    "You Won't Believe What Happened Next!",
    "This Will Shock You!",
    "The Government Is Hiding This From You!",
    "Doctors Hate This One Simple Trick!",
    "Big Pharma Doesn’t Want You to Know This!",
    "Everything You should Know About  this   Lie!",
    "Elite Globalists Are Controlling the World!",
    "Vaccines Are Poison!",
    "Scientists Have Finally Proven [False Claim]!",
    "Mainstream Media Is Covering Up This Huge Story!",
]

genuine_dict={"International News Agencies":
["BBC News (UK) – https://www.bbc.com/news",
"CNN (USA) – https://www.cnn.com",
"Reuters (UK) – https://www.reuters.com",
"The Associated Press (AP) (USA) – https://apnews.com",
"Al Jazeera (Qatar) – https://www.aljazeera.com",
"Bloomberg News (USA) – https://www.bloomberg.com",
"The Guardian (UK) – https://www.theguardian.com/international",
"The New York Times (USA) – https://www.nytimes.com",
"The Washington Post (USA) – https://www.washingtonpost.com"
"Deutsche Welle (DW) (Germany) – https://www.dw.com/en"],
"European News Outlets":
["France 24 (France) – https://www.france24.com/en",
"The Economist (UK) – https://www.economist.com",
"Euronews (Europe) – https://www.euronews.com",
"Sky News (UK) – https://news.sky.com"],
"American News Outlets":
["CBS News (USA) – https://www.cbsnews.com",
"NBC News (USA) – https://www.nbcnews.com",
"ABC News (USA) – https://abcnews.go.com",
"Fox News (USA) – https://www.foxnews.com (Check for bias in political reporting)"],
"Asian News Outlets":
["Times of India (India) – https://timesofindia.indiatimes.com",
"The Hindu (India) – https://www.thehindu.com",
"NHK World (Japan) – https://www3.nhk.or.jp/nhkworld/en/news",
"South China Morning Post (SCMP) (Hong Kong) – https://www.scmp.com",
"Channel News Asia (CNA) (Singapore) – https://www.channelnewsasia.com",
"The Straits Times (Singapore) – https://www.straitstimes.com"],
"Australian News Outlets":
["Sydney Morning Herald (Australia) – https://www.smh.com.au"]}


#Entering the Headline to guess if the news is genuine or not

new_headline=input("Enter the newsheadline:")

if new_headline  in fake_phrases:
        print("Hight chance of being Fake !! Validate before sharing ")
        choice=input("Do you want websites to validate the news? yes/no")
        if choice=="yes" or "YES":
            for i in genuine_dict:
                for k in genuine_dict[i]:
                    print(k)
        else:
            print("Thanks for using FakeNews Detector Visit again")



else:
    print("Does not contain any phrases that are commonly found in fake news. ")
    choice = input("Do you want websites to validate the news yes/no")

    if choice == "yes" or "YES":
        print("Here are some internationalyy valid websites to check the validity of the news:")
        for i in genuine_dict:
            for k in genuine_dict[i]:
                print(k)
    else:
        print("Thanks for using FakeNews Detector Visit again")

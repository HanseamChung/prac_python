import tweepy

Consumer_Key='QDoNigyZwpfYD6T7LuBzwpYXR'

Consumer_Secret='bhZJ9TP4hAMQuFFTNH55zKCvFMLecWRIf4F8FHHJO3oleUmeaJ'

Access_Token='961407992498290688-PFvqjx9SgQEywGdZeat7IuSAgPYmrpr'

Access_Token_Secret='vdhyliLywdFpxAp6HYW24LdYgkTOkNcnPldknrfaudn0F'

auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)

auth.set_access_token(Access_Token,Access_Token_Secret)

api=tweepy.API(auth)


keyword='네델란드'

result=[]

for i in range(1,3) :
    tweets=api.search(keyword)
    for tweet in tweets:
        result.append(tweet)
print(len(result))
print(type(result[0]))


for i in range(0,len(result)):
    print(result[i])


'''
for i in range(0,len(result)):
    try:
        print(result[i])
    except UnicodeEncodeError:
        print('인코딩 에러입니다.')
        continue

'''        
'''
f=open('tweet2.txt','w')
for i in range(0,len(result)):
    try:
        f.write(str(result[i])+'\n')
    except UnicodeEncodeError:
        print('인코딩 에러입니다.')
        continue
f.close()
'''
              

#!/usr/bin/env python
# coding: utf-8

# # Soccer Team Season Performance Calculator
# ## Hi, are you interested in how your favourite soccer team is performing this season? I am here to help you!
# Follow the instructions and enter the **related information** of the team that you are interested in.
# 

# In[ ]:


teamname = input('Please enter team name')
print('The name of your team is ' + teamname)
GamesWon = int(input('Please enter the the games that your team has won.'))
GamesDrawn = int(input('Please enter the the games that your team has drawn.'))
GamesLost = int(input('Please enter the the games that your team has lost.'))
AveragePoints = (GamesWon * 3 + GamesDrawn * 1 + GamesLost * 0) / (GamesWon + GamesDrawn + GamesLost)
winpercentage = GamesWon / (GamesWon + GamesDrawn + GamesLost) * 100
losepercentage = GamesLost / (GamesWon + GamesDrawn + GamesLost) * 100
print(teamname , ' has an average ' , AveragePoints , ' points per game.')
print(teamname, ' has won', winpercentage, '%', ' of the games')
print(teamname, ' has lost', losepercentage, '%', ' of the games')


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
tdb = pd.read_csv('tennis_stats.csv')

print(tdb.describe())
print(tdb.head())
print(len(tdb))
tdb=tdb.sort_values(by=['Ranking'])

fig = plt.figure()
ax1 = fig.add_subplot(621)
ax2 = fig.add_subplot(622)
ax3 = fig.add_subplot(623)
ax4 = fig.add_subplot(624)
ax5 = fig.add_subplot(625)
ax6 = fig.add_subplot(626)
ax7 = fig.add_subplot(627)


tdb.plot.scatter(x='FirstServe', y='FirstServePointsWon', c='r',ax=ax1)
tdb.plot.scatter(x='FirstServe', y='FirstServeReturnPointsWon', c='g',ax=ax1)
tdb.plot.scatter(x='FirstServe', y='SecondServePointsWon',ax=ax1)
tdb.plot.scatter(x='Ranking', y='Winnings',c='g',ax=ax2)
tdb.plot.scatter(x='Ranking', y='Losses',c='g',ax=ax3)


# perform exploratory analysis here:


X_train, X_test, y_train, y_test = train_test_split(tdb[['Winnings']], tdb[['FirstServePointsWon']], test_size=0.2, random_state=77)

Linmod=LinearRegression()
Linmod.fit(X_train,y_train)
#Score LR training
Linmod.score(X_train, y_train)
prediction=Linmod.predict(X_test)
ax4.scatter(y_test,prediction, alpha=0.4)


X_train, X_test, y_train, y_test = train_test_split(tdb[['Winnings']], tdb[['FirstServeReturnPointsWon']], test_size=0.2, random_state=77)

Linmod=LinearRegression()
Linmod.fit(X_train,y_train)
#Score LR training
Linmod.score(X_train, y_train)
prediction=Linmod.predict(X_test)
ax5.scatter(y_test,prediction, alpha=0.4)

X_train, X_test, y_train, y_test = train_test_split(tdb[['BreakPointsOpportunities']], tdb[['Winnings']], test_size=0.2, random_state=77)
Linmod=LinearRegression()
Linmod.fit(X_train,y_train)
#Score LR training
Linmod.score(X_train, y_train)
prediction=Linmod.predict(X_test)
ax6.scatter(y_test,prediction, alpha=0.4)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(tdb[['BreakPointsOpportunities','FirstServeReturnPointsWon']], tdb[['Winnings']], test_size=0.2, random_state=77)

Linmod=LinearRegression()
Linmod.fit(X_train,y_train)
#Score LR training
Linmod.score(X_train, y_train)
prediction=Linmod.predict(X_test)
ax7.scatter(y_test,prediction, alpha=0.4)
plt.show()









## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:























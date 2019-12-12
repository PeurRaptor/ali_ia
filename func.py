import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.metrics import mean_squared_error,r2_score
#import seaborn as sns
import numpy as np


def returnarray(col2):
        col=[]
        ind=2
        T=str(list(col2))
        for i in range(0,len(T)):
            if T[i]==";":
                col.append(T[ind:i])
                ind=i+1
        return col

def linearregression(x1,y1,x2):#multiple dans lm.fit(x[[1,2,3]],y) ou simple
    lm=LinearRegression()
    lm.fit(x1,y1)
    return lm.predict(x2)#ou return lm pour intercept_ et coef_

def regressionplot(df,Xn,Yn,w,h):# pour voir les données et la fonction linéaire qui les definit
    plt.figure(figsize=(w,h))
    sns.regplot(x=Xn,y=Yn,data=df)
    plt.Ylim(0,)

def residualplot(df,Xn,Yn,w,h):# pour voir la difference entre données predites et données preetablies
    plt.figure(figsize=(w,h))
    sns.residplot(df[Xn],df[Yn],data=df)
    plt.show()

def distributionplot(df,Ypred,Y,w,h):#meme que residual mais pour multiple
    plt.figure(figsize=(w,h))
    act=sns.distplot(Y,hist=False,color="r",label="value")
    sns.distplot(Ypred,hist=False,label="predicted value",ax=act)
    plt.title("actual vs predicted")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    plt.close()

#--------------------------------------POLYNOMIAL   

def PlotPolly(model, independent_variable, dependent_variabble, Name):#model=modelcreation(x,y,n) pour plotter modelcreation
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)
    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('y')

    plt.show()
    plt.close()

def modelcreation(x,y,n):
    f = np.polyfit(x, y, n)
    p = np.poly1d(f)
    return p

def Polynomialtransformation(x,n):#multiple dans lm.fit(x[[1,2,3]],y) ou simple
    pr=PolynomialFeatures(degree=n)
    Ypr=pr.fit_transform(x)
    return Ypr

def pipeline(Input,x,y):#Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
    pipe=Pipeline(Input)
    pipe.fit(x,y)
    return pipe.predict(x)

#on analyse par la suite les erreurs avec rsquared:lm.score(x,y) DOIT ETRE GRANDE et mse:mean_squared_error(df['price'], Yhat) DOIT ETRE PETITE
#------------------model evaluation

#x_train_1,x_test_1,y_train_1,x_train_1=train_test_split(x_data,y_data,test_size=0.4,random_state=1) 

'''from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)
Y_Pred = regressor.predict(X_Test)'''

def linearregressionwithsplit(x,y,test):
    x1,x2,y1,y2=train_test_split(x,y,test_size=test)
    return linearregression(x1,y1,x2) 

def Polynomialregressionwithsplit(x,y,test,n):
    l=LinearRegression()
    p=PolynomialFeatures(degree=n)
    x1,x2,y1,y2=train_test_split(x,y,test_size=test)
    xtr=p.fit_transform(x1)
    xte=p.fit_transform(x2)
    l.fit(xtr,y1)
    #print("degree|rsquared")
    #print(str(n)+"|"+str(l.score(xte, y2)))
    return l.predict(xte)


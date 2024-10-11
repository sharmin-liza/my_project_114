# Example input data


from sklearn.linear_model import LogisticRegression
x=[[1,2],[2,3],[3,4],[4,5],[5,6]]
y=[0,0,1,1,1]
model=LogisticRegression()
model.fit(x,y)
prediction=model.predict([[6,7]])[0]
print(prediction)

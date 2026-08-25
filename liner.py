from sklearn.linear_model import LinearRegression
model=LinearRegression()
x=[[1],[2],[3],[6]]
y=[20,30,40,50]
model.fit(x,y)
hours=float(input(" Enter how many hours you have study"))
predict_marks=model.predict([[hours]])
print(f"you have obatined {hours} studing you have obtained {predict_marks}")
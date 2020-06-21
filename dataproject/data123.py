import pandas as pd
from plotly.offline import  plot
import plotly.express as px
startyear=2005
dataset=pd.read_excel("life_expectancy_years.xlsx")
a=pd.DataFrame(columns=("country","life-exp","year"))
for i in range(startyear,2018):
    b=dataset[['country',i]].copy()
    b['year']=i
    b.columns=['country','life-exp','year',]
    c=a.append(b)
    a=c
dataset=pd.read_excel("income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
x=pd.DataFrame(columns=("country","income","year"))
for i in range(startyear,2018):
    y=dataset[['country',i]].copy()
    y['year']=i
    y.columns=['country','income','year',]
    z=x.append(y)
    x=z
dataset=pd.read_excel("population_total.xlsx")
r=pd.DataFrame(columns=("country","population","year"))
for i in range(startyear,2018):
    s=dataset[['country',i]].copy()
    s['year']=i
    s.columns=['country','population','year']
    t=r.append(s)
    r=t
data= pd.merge(a,x)
data= pd.merge(data,r)
data.to_excel(f"{startyear}到2018人均GDP和人均寿命.xlsx")
dataset=pd.read_excel("2005到2018人均GDP和人均寿命.xlsx")
figure = px.scatter(dataset, x="income", y="life-exp", animation_frame="year",animation_group="country",size="income",color="population",hover_name="country",log_x=True, size_max=45,range_x=[500,200000], range_y=[25,90],labels=dict(income="人均收入(PPP购买力标准)",lifeExp="人均寿命"))
plot(figure)
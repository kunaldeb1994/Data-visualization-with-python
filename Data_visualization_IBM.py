import pandas as pd
import matplotlib.pyplot as plt
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)


project_fie=pd.read_csv('E:\\course era\\Data Visualization With Python\\Topic_Survey_Assignment.csv')
survey=pd.DataFrame(project_fie)
print(survey.head())
survey.rename(columns={'Unnamed: 0':'Technolgies'},inplace= True) #first change the name then set index
survey1=survey.set_index('Technolgies')
print(survey1)

'''creating visualization'''
sur=survey1.sort_values(['Very interested'],ascending=False)
print(sur)


ax=sur.plot(kind='bar',figsize=(15,4),width=0.8,color=['#5cb85c','#5bc0de','#d9534f'])
ax.set_title('Percentage of Respondents Interest in Data Science Areas',fontsize=16)

'''to remove the boundry layer of the graph'''
for spine in plt.gca().spines.values():
    spine.set_visible(False)

ax.set_yticks([])
ax.set_xlabel('',fontsize=14)
for p in (ax.patches):
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.annotate('{:.0%}'.format(height/2233), (x+.5*width, y + height + 0.01),ha='center')
    print('{:.0%}'.format(height/2233), (x+.5*width, y + height + 0.01))

plt.show()
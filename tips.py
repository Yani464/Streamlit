import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

st.write("""
# Исследование по чаевым и его визуализация
""")


tips = pd.read_csv('/Users/nikita/ds_bootcamp/Leaning/datasets/tips.csv')
random_dates = pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-01-31'), size=len(tips)))
tips['time_order'] = random_dates
tips = tips.drop('Unnamed: 0', axis=1)

st.write("""
##  Таблица чаевых по первым 5 заказам
""")
st.write(tips.head())

avg_tip_by_time = tips.groupby('time')['tip'].mean()

plt.figure(figsize=(8, 5))
avg_tip_by_time.plot(kind='bar', color='skyblue')
plt.xlabel('Время дня')
plt.ylabel('Средняя сумма чаевых')
plt.title('Средняя сумма чаевых в зависимости от времени суток')
plt.xticks(rotation=0)
plt.show()

st.pyplot(plt)

plt.figure(figsize=(8, 5))
plt.hist(tips['total_bill'], bins=10, color='green', edgecolor='black', alpha=0.7)
plt.xlabel('Сумма чаевых')
plt.ylabel('Частота')
plt.title('Гистограмма распределения чаевых')
plt.show()

st.pyplot(plt)


plt.figure(figsize=(8, 5))
plt.scatter(tips['total_bill'], tips['tip'], color='red', alpha=0.7)
plt.xlabel('Сумма заказа')
plt.ylabel('Чаевые')
plt.title('График распределения: Сумма заказа и Чаевые')
plt.show()

st.pyplot(plt)



lunch_data = tips[tips['time'] == 'Lunch']
dinner_data = tips[tips['time'] == 'Dinner']
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharey=True)

sns.histplot(lunch_data['tip'], bins=10, color='skyblue', ax=axes[0])
axes[0].set_title('Гистограмма чаевых на завтрак')
axes[0].set_xlabel('Чаевые')
axes[0].set_ylabel('Частота')

sns.histplot(dinner_data['tip'], bins=10, color='salmon', ax=axes[1])
axes[1].set_title('Гистограмма чаевых на ужин')
axes[1].set_xlabel('Чаевые')
axes[1].set_ylabel('Частота')

plt.tight_layout()
plt.show()

st.pyplot(plt)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='tip', y='day', hue='sex', data=tips, palette='viridis', s=100, alpha=0.7)
plt.xlabel('Чаевые')
plt.ylabel('День недели')
plt.title('Чаевые vs День недели с цветом по полу')
plt.show()
st.pyplot(plt)

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', hue='time', data=tips, palette='Set2')

plt.xlabel('День недели')
plt.ylabel('Сумма счета')
plt.title('Сумма счета по дням недели и времени')
plt.show()
st.pyplot(plt)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(tips['total_bill'], tips['tip'], tips['size'], c='skyblue', s=50, alpha=0.7)
plt.show()
st.pyplot(plt)

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips, palette='viridis')
plt.xlabel('День недели')
plt.ylabel('Размер счета')
plt.title('Связь между днем недели и размером счета')
plt.show()
st.pyplot(plt)

tips['time_order'] = pd.to_datetime(tips['time_order'])
df_male = tips[tips['sex'] == 'Male']
df_female = tips[tips['sex'] == 'Female']

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(df_male['total_bill'], df_male['tip'], c=df_male['smoker'].map({'Yes': 'red', 'No': 'blue'}))
plt.title('Scatterplot для мужчин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

plt.subplot(1, 2, 2)
plt.scatter(df_female['total_bill'], df_female['tip'], c=df_female['smoker'].map({'Yes': 'red', 'No': 'blue'}))
plt.title('Scatterplot для женщин')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
st.pyplot(plt)


# plt.figure(figsize=(8, 6))
# sns.heatmap(tips.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
# plt.title('Тепловая карта зависимостей численных переменных')
# st.pyplot(plt)


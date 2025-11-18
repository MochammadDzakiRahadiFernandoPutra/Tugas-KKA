import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nilai_siswa.csv')

print(data.info())
print(data.describe())
print(data.head())

print("rata-rata:", data['Nilai'].mean())
print("median:", data['Nilai'].median())
print("modus:", data['Nilai'].mode()[0])

print(data[data['Matpel'] == 'Matematika'])
print(data[data['Matpel'] == 'Bahasa Indonesia'])
print(data[data['Matpel'] == 'Bahasa Inggris'])
print(data[data['Matpel'] == 'Fisika'])
print(data[data['Matpel'] == 'Produktif'])

print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color=['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd'])
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

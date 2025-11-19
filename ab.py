import matplotlib.pyplot as plt

labels = ['Autism Spectrum', 'Dyslexia', 'Memory Impairment', 'Attention Deficit', 'Other']
sizes = [30, 25, 20, 15, 10]
colors = ['#66b3ff','#99ff99','#ffcc99','#ff9999','#c2c2f0']
explode = (0.1, 0, 0, 0, 0)  # explode first slice

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)
plt.title('User Demographics by Cognitive Disability Type')
plt.axis('equal')
plt.show()

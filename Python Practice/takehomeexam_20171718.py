# Module
import urllib.request
import matplotlib.pyplot as plt

# Function


def tokenize(book):
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def map_book(tokens):
    hash_map = {}

    if tokens is not None:
        for element in tokens:
            # Remove Punctuation
            word = element.replace(",", "")
            word = word.replace(".", "").replace("?", "")

            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None

# Get Text File From Online and Make World Dictionary

print('Wait for a minute')

url = 'http://www.textfiles.com/etext/FICTION/lesms10.txt'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

k = tokenize(text.upper())
dic = map_book(k)
dic_s_list = sorted(dic, key=lambda element: dic[element], reverse=True)

# Draw Chart by Using Matplotlib

d = {}
for i in range(5):
    d.update({dic_s_list[i]: dic[dic_s_list[i]]})

d2 = {}
for i in range(5):
    d2.update({dic_s_list[i]: dic[dic_s_list[i]]/dic[dic_s_list[0]]})

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

plt.bar(range(len(d)), d.values(), align="center")
plt.xticks(range(len(d)), list(d.keys()))

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

plt.bar(range(len(d2)), d2.values(), align="center")
plt.xticks(range(len(d2)), list(d2.keys()))

plt.show()

print("Processing finish! Check the double windows please!")
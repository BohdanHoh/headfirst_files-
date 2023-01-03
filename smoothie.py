smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']

favorite = smoothies[2]

print(favorite)

smoothies[3] = 'tropical'

smoothies[1] = 'blueberry'

print(smoothies)

for smoothie in smoothies:
    output = 'We serve ' + smoothie
    print(output)

length = len(smoothies)
for i in range(length):
    print('Smoothie #', i, smoothies[i])

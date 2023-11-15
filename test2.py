import time

a = '<a href="https://www.bybit.com/uk-UA/invite?ref=X12KX3">Привет</a>  <a href="https://google.com">.</a>   <a href="https://www.bybit.com/uk-UA/invite?rewrsdsdf">Привет</a>'

a = a.replace('</a>', '')
print(a, '\n\n\n')

while a.count('<a href') != 0:

    print(a.count('<a href'), a.find('<a href="'), a[a.find('<a href="')+9:].find('>')+8)

    link = a[a.find('<a href="')+9:a[a.find('<a href="')+9:].find('>')+8+a.find('<a href="')]

    if 'https://google' in link:
        a = a.replace(f'<a href="{link}">', f'')
    else:
        a = a.replace(f'<a href="{link}">', f'({link}) ')

    print(link, a)
    time.sleep(1)

print(a)
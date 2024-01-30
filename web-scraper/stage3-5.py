#scraper.py
'''
    import requests

    r = requests.get(input())

    html_file = open('source.html', 'wb')

    if r:
        html_file.write(r.content)
        print('Content saved.')
    else:
        print(f'The URL returned {r.status_code}!')

    html_file.close()
'''

#source.html
'''
<html>
<head>
  <title>warming up</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="calc.jpg"><br>
<font color="gold">
<p>Hint: try to change the URL address.
</body>
</html>
'''
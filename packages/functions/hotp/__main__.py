import os
import pyotp
import datetime

def main(event, context):
  headers = event.get("http", {}).get("headers", {})
  x_forwarded_for = headers.get("x-forwarded-for")
  msg= event.get("msg", {})
  key1= os.environ.get('key1')

  year, week, day= datetime.datetime.now().isocalendar()

  hotp=  pyotp.HOTP(key1, digits=8)
  #code=  hotp.at(week)
  check= hotp.verify(msg, week)

  return {
    "headers": { "Content-Type": "text/plain" },
    "body": f"{x_forwarded_for} {week} {msg} {check}\n"
  }

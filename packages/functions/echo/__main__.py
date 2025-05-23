import os

def main(event, context):
  headers = event.get("http", {}).get("headers", {})
  x_forwarded_for = headers.get("x-forwarded-for")
  msg= event.get("msg", {})
  key1= os.environ.get('key1')

  print (x_forwarded_for)
  print (msg)

  return {
      "headers": { "Content-Type": "text/plain" },
      "body": f"ip: {x_forwarded_for}\n"\
              f"Msg: {msg}\n"\
              f"key1: {key1}\n"
  }

#  return {
#    "body": {
#      "ip": x_forwarded_for,
#      "msg": msg,
#      "key1": key1
#    }
#  }

#  return {
#    "body": {
#      "event": event,
#      "ip": x_forwarded_for,
#      "context": {
#        "activationId": context.activation_id,
#        "apiHost": context.api_host,
#        "apiKey": context.api_key,
#        "deadline": context.deadline,
#        "functionName": context.function_name,
#        "functionVersion": context.function_version,
#        "namespace": context.namespace,
#        "requestId": context.request_id,
#      },
#    },
#  }

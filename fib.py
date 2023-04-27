import os
from flask import Flask,request,jsonify

def fibonacci(n):
    n-=1
    a=[1]*(n+1)
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]


app=Flask(__name__)
@app.route('/fib')
def get_fibonacci():
    try:
        n=request.args.get('n',type=int)
        result=fibonacci(n)
        response={'result':result}
        return jsonify(response),200
    except:
        response={
            "status":400,
            "message":"Bad request."
            }
        return  jsonify(response),400
if __name__=='__main__':
    app.run(host='0.0.0.0',port='7777',debug=False)
    


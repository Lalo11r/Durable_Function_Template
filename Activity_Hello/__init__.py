import logging as lg

def main(requestbody) -> dict:
    lg.info(f"Python HTTP trigger function processed a request. Request body: {requestbody}")
    try:
        return {"response": f"Hello {requestbody['name']}"}
    except KeyError:
        return {"error": "Please pass a name in the request body"}
    except Exception as e:
        return {"error": str(e)}
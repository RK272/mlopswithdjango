import mlflow

def addition(x,y):
    z = x+y
    
    return z

if __name__ == "__main__":
    x,y=3,5
    with mlflow.start_run():
       
        z = addition(x, y)
        mlflow.log_param("x", x)
        mlflow.log_param("y", y)
        mlflow.log_metric("z", z)
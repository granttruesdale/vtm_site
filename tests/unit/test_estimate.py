import app

def test_estimate_route(app, client):
    with app.test_client() as test_client:
        new_estimate = {"radius":"180", "height":"360"}
        res = test_client.post('/estimate',data=new_estimate)
        assert b"141,300.00" in res.data
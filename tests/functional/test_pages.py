def test_index(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data
        assert b"Welcome to VTM!" in res.data
        assert b"Image Source" in res.data

def test_about(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data
        assert b"Mauris a est mauris" in res.data 

def test_estimate(app, client):
    """
    GIVEN a flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"VTM Estimator" in res.data
        assert b"Radius (in inches):" in res.data 
        assert b"Height (in inches):" in res.data